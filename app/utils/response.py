# # # # # # # # # # # # # # # # # # # # #
# Name: Error/Response Handler          #
# Version : 1.0                         #
# Author : Dinar Hamid                  #
# # # # # # # # # # # # # # # # # # # # #
from flask import jsonify, make_response

class InvalidExtensionException(Exception):

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class InvalidMethodsException(Exception):

    def __init__(self, message: str, route: str | None = None) -> None:
        self.message = message
        super().__init__(self.message)


class MakeJsonError:

    def __init__(self, array: list[str | int | dict[str, str | int]] | dict[str, int | str], 
                       message: str, 
                       status_code: int) -> tuple[dict[str, int | str | list], int]:
        return make_response(
            jsonify({
                'errors' : array,
                'message' : message,
                'status_code' : status_code
            })
        ), status_code

class MakeJsonSuccess:

    def __init__(self, array: list[str | int | dict[str, str | int]] | dict[str, int | str],
                       message: str,
                       status_code: int) -> tuple[dict[str, int | str | list], int]:
        return make_response(
            jsonify({
                'data' : array,
                'message' : message,
                'status_code' : status_code
            })
        ), status_code