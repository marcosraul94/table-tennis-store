import unittest
from unittest.mock import patch
from src.utils.view import View
from src.utils.router import Router
from src.utils.enum import HttpMethod
from src.utils.event import ApiGatewayEvent
from src.utils.response import ErrorResponse


class TestRouter(unittest.TestCase):
    def setUp(self) -> None:
        self.raw_event = {
            "requestContext": {
                "http": {"path": View.route, "method": HttpMethod.GET.value}
            }
        }
        self.Views = [View]

    @patch("src.utils.view.View.get")
    def test_correct_path_and_method(self, mock_get):
        event = ApiGatewayEvent(self.raw_event)
        router = Router(event, self.Views)
        router.route()

        mock_get.assert_called_once()

    def test_correct_path_but_wrong_method(self):
        self.raw_event["requestContext"]["http"]["method"] = HttpMethod.PUT.value
        event = ApiGatewayEvent(self.raw_event)
        router = Router(event, self.Views)
        response = router.route()

        self.assertIsInstance(response, ErrorResponse)

    def test_wrong_path(self):
        self.raw_event["requestContext"]["http"]["path"] = "/wrong"
        event = ApiGatewayEvent(self.raw_event)
        router = Router(event, self.Views)
        response = router.route()

        self.assertIsInstance(response, ErrorResponse)


if __name__ == "__main__":
    unittest.main()
