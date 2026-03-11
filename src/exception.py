import sys


class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):

        super().__init__(error_message)

        _, _, exc_tb = error_detail.exc_info()

        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
        else:
            file_name = "Unknown"
            line_number = "Unknown"

        self.error_message = f"""
        Error occurred in script: [{file_name}]
        Line number: [{line_number}]
        Error message: [{str(error_message)}]
        """

    def __str__(self):
        return self.error_message