import sys ##give access to system level information 
from src.logger import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() ##exc_info() gives 3 things: What type of error,Error object ,Traceback (where error happened)We only want traceback, so:_ → ignore_ → ignore exc_tb → keep traceback_ is a Python way of saying “I don’t care about this value”
    file_name=exc_tb.tb_frame.f_code.co_filename ##“From the traceback, tell me which Python file caused the error.” exc_tb → error info tb_frame → the place where error occurred f_code → code details co_filename → file name
    error_message="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
    
class CustomException(Exception): ##Create my own error type based on Python’s Exception.
    def __init__(self,error_message,error_detail:sys): ##When this error happens, run this code
        super().__init__(error_message) ##Call the normal Python Exception first,constructor of parent class Exception
        self.error_message=error_message_detail(error_message,error_detail=error_detail) ##Create a detailed error message and store it inside this object

    def __str__(self):##without this function python prints the error as object not the error itself 
        return self.error_message ##When someone prints this error, show the detailed message
    