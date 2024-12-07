def users(event, context):
    print(event)
    print('--------------')
    print(context)

    return {
        "statusCode": 200,  # HTTP status code
        "body": '{"message": "hello my friend again"}',  # The body should be a JSON string
        "headers": {
            "Content-Type": "application/json"  # Optional headers, but often necessary
        }
    }
