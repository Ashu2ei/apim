import logging, traceback, os
from logging.handlers import RotatingFileHandler

# def init_logging_handler():
#     log_level, format, datefmt = logging.INFO, '%(asctime)s - %(levelname)s - %(message)s', '%d-%b-%Y %H:%M:%S %p'

#     logger = logging.getLogger(__name__)
#     logger.setLevel(log_level)
#     logger.addHandler(file_handler)

#     if AppConstants.Environment.IS_DEV_ENV:
#         # Set the stream_handler to print the logs in terminal
#         stream_handler = logging.StreamHandler()

#         # Set the log level and format
#         stream_handler.setLevel(logging.DEBUG)
#         stream_handler.setFormatter(logging.Formatter(format, datefmt=datefmt))

#         logger.addHandler(stream_handler)

#     return logger

# logger = init_logging_handler()