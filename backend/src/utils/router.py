from src.utils.view import View
from src.views.user import UserView
from src.utils.enum import HttpStatus
from src.utils.response import Response, ErrorResponse
from src.utils.event import ApiGatewayEvent

Views = [UserView]


class Router:
    def __init__(
        self, event: ApiGatewayEvent, Views: list[View] = Views
    ) -> None:
        self.__event = event
        self.__Views = Views

    def route(self) -> Response:
        http_method = self.__event.http_method.value
        route = self.__event.route

        for View_ in self.__Views:
            if View_.route == route:
                view = View_(self.__event)

                if hasattr(view, http_method):
                    view_method = getattr(view, http_method)

                    return view_method(self.__event)

                return ErrorResponse(
                    error=f"Unsupported http method {http_method} from route {route}",
                    status=HttpStatus.NOT_FOUND,
                )

        return ErrorResponse(
            error=f"Route {route} not found!",
            status=HttpStatus.NOT_FOUND,
        )
