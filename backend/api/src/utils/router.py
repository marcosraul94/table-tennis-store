from src.utils.view import View
from src.utils.enum import HttpStatus
from src.utils.event import ApiGatewayEvent
from src.utils.response import Response, ErrorResponse


class Router:
    def __init__(self, event: ApiGatewayEvent, Views: list[View]) -> None:
        self.__event = event
        self.__Views = Views

    @property
    def __unsupported_route_response(self) -> ErrorResponse:
        return ErrorResponse(
            error=f"Route {self.__event.route} not found!",
            status=HttpStatus.NOT_FOUND,
            headers=self.__event.headers,
        )

    @property
    def __unsupported_method_response(self) -> ErrorResponse:
        return ErrorResponse(
            error=f"""
            Unsupported http method {self.__event.http_method.value}
            from route {self.__event.route}!
            """,
            status=HttpStatus.NOT_FOUND,
            headers=self.__event.headers,
        )

    def route(self) -> Response:
        for View_ in self.__Views:
            if View_.route == self.__event.route:
                view = View_(self.__event)

                if not hasattr(view, self.__event.http_method.value):
                    return self.__unsupported_method_response

                try:
                    view_method = getattr(view, self.__event.http_method.value)

                    return Response(
                        body=view_method(),
                        status=HttpStatus.OK,
                        headers=self.__event.headers,
                    )

                except NotImplementedError:
                    return self.__unsupported_method_response

                except Exception as runtime_error:
                    return ErrorResponse(
                        error=str(runtime_error),
                        status=HttpStatus.INTERNAL_SERVER_ERROR,
                        headers=self.__event.headers,
                    )

        return self.__unsupported_route_response
