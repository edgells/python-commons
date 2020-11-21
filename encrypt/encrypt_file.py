import time
import os
from encrypt import transposition as transpt


def test():
    input_file_name = 'test_input.txt'
    output_file_name = 'test_output.txt'
    key = 10
    mode = 'encrypt'

    if not os.path.exists(input_file_name):
        with open(input_file_name, 'w'):
            pass

    if not os.path.exists(output_file_name):
        with open(input_file_name, 'w'):
            pass

