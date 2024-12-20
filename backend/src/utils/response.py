from flask import jsonify
from src.utils.enum import HttpStatus
from src.utils.serialization import DictSerialization


class Response:
    def __init__(
        self,
        data: dict,
        status: HttpStatus = HttpStatus.OK,
    ):
        self.status = status
        self.data = data

    def to_json_response(self):
        serialized_data = DictSerialization.serialize(self.data)

        return jsonify(status=self.status.value, data=serialized_data), 200
