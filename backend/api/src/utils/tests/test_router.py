import unittest
from unittest.mock import patch, MagicMock
from src.utils.view import View
from src.utils.router import Router
from src.utils.enum import HttpMethod, HttpStatus
from src.utils.event import ApiGatewayEvent
from src.utils.response import ErrorResponse


class TestRouter(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_event = {
            "pathParameters": {"proxy": View.route},
            "httpMethod": HttpMethod.GET.value,
        }
        self.Views = [View]

    @patch("src.utils.view.View.get")
    def test_correct_path_and_method(self, mock_get: MagicMock):
        event = ApiGatewayEvent(self.raw_event)
        router = Router(event, self.Views)
        router.route()

        mock_get.assert_called_once()

    def test_correct_path_but_wrong_method(self):
        self.raw_event["httpMethod"] = HttpMethod.PUT.value
        event = ApiGatewayEvent(self.raw_event)
        router = Router(event, self.Views)
        response = router.route()

        self.assertIsInstance(response, ErrorResponse)

    def test_wrong_path(self):
        self.raw_event["pathParameters"]["proxy"] = "/wrong"
        event = ApiGatewayEvent(self.raw_event)
        router = Router(event, self.Views)
        response = router.route()

        self.assertIsInstance(response, ErrorResponse)

    @patch("src.utils.view.View.get")
    def test_runtime_error(self, mock_get: MagicMock):
        error_msg = "A runtime error"
        mock_get.side_effect = RuntimeError(error_msg)

        event = ApiGatewayEvent(self.raw_event)
        router = Router(event, self.Views)
        response = router.route()

        self.assertIsInstance(response, ErrorResponse)
        self.assertIn(error_msg, response.body.get("error"))

    @patch("src.utils.view.View.get")
    def test_runtime_error_serialization(self, mock_get: MagicMock):
        error_msg = "A runtime error"
        mock_get.side_effect = RuntimeError(error_msg)

        event = ApiGatewayEvent(self.raw_event)
        router = Router(event, self.Views)
        response = router.route()

        self.assertDictEqual(
            response.to_dict(),
            {
                "statusCode": HttpStatus.INTERNAL_SERVER_ERROR.value,
                "body": {"error": str(mock_get.side_effect)},
                "headers": {
                    "Content-Type": "application/json",
                },
            },
        )


if __name__ == "__main__":
    unittest.main()
