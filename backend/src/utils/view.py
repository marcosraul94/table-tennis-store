class View:
    @staticmethod
    def get() -> dict:
        raise NotImplementedError

    @staticmethod
    def post() -> dict:
        raise NotImplementedError

    @staticmethod
    def delete() -> dict:
        raise NotImplementedError

    @staticmethod
    def patch() -> dict:
        raise NotImplementedError
