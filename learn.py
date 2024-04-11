#!/usr/bin/env python3
import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

"""
Setting up a configuration for the logging with logging.basicConfig
The logged info is directed to a file called test.log
The logging Level is set to Debug. P.S The default log
level is set to Warning, and the level must be in capital letters
The third argument is used for setting the format of the log
asctime is the time of the log, levelname is the log level,
message is the message to be logged, lineno shows the line
at which each logging was made
"""
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s:%(lineno)d')



def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 20
num_2 = 10

"""
creating a new logger instead of the default root logger
setting the level for the new logger to INFO
creating a file handler for the new logger
adding the file handler to the new logger
creating a log formatter for the new logger
adding the formatter to the file handler
"""
new_logger = logging.getLogger(__name__)
new_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('new_test.log')
new_logger.addHandler(file_handler)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s:%(lineno)d')
file_handler.setFormatter(formatter)


"""using the new logger"""
add_result = add(num_1, num_2)
new_logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
new_logger.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
new_logger.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
new_logger.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))

""" logging tests for the default root logger
add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
"""