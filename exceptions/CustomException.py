import sys
from utils.CustomLogger import CustomLogger

logger = CustomLogger(module_name=__name__).get_logger()

class CustomException(Exception):
    """This Exception Class responsible to provide detailed error information."""
    def __init__(self, error_message, error_details = sys):
        super().__init__(error_message)
        self.error_details = error_details

        # Getting exception traceback info
        _, _, traceback = error_details.exc_info()

        # Getting the file name where error occured
        file_name = traceback.tb_frame.f_code.co_filename

        # formatting and displaying the error message in detail 
        self.error_message = (
            f"Error occured in Python script: '{file_name}'"
            f"at line number '{traceback.tb_lineno}'"
            f"with error message = '{str(error_message)}'"
        )

        logger.error(self.error_message)

    def __str__(self):
        """Return the formatted error message when exception is printed."""
        return self.error_message
    
