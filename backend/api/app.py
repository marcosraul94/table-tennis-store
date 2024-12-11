from src.utils.router import Router
from src.utils.event import ApiGatewayEvent
from src.utils.response import ErrorResponse


def lambda_handler(raw_event, context) -> dict:
    print(raw_event)
    print("--------------")
    print(context)

    event = ApiGatewayEvent(raw_event)

    try:
        response = Router(event).route()
    except Exception as err:
        response = ErrorResponse(err)

    return response.to_json()
