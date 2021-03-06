class ApiError(Exception):
    status_code = 500
    message = None
    payload = None

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)

        self.message = message

        if status_code is not None:
            self.status_code = status_code

        self.payload = payload

    def serialize(self):
        result = dict(self.payload or ())
        result["message"] = self.message
        return result
