from src.utils.view import View
from src.views.user import UserView
from src.views.product import ProductView
from src.utils.router import Router
from src.utils.event import ApiGatewayEvent


def lambda_handler(raw_event, context, views: list[View]) -> dict:
    import json

    print(json.dumps(raw_event, sort_keys=True, indent=4))

    event = ApiGatewayEvent(raw_event)
    response = Router(event, views).route()

    return response.serialize()


def protected_routes_handler(raw_event, context) -> dict:
    return lambda_handler(raw_event, context, [UserView])


def unprotected_routes_handler(raw_event, context) -> dict:
    return lambda_handler(raw_event, context, [ProductView])
