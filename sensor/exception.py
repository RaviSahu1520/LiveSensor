import sys
import os


def error_detail_message(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Corrected sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    return f"Error occurred in file: {filename}, at line: {exc_tb.tb_lineno}, and error is: {str(error)}"


class SensorException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_detail_message(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
