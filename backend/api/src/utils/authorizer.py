def lambda_handler(raw_event, context) -> dict:
    return {
        "isAuthorized": False,
        "context": {"email": "marcosraul94@gamil.com"},
    }
