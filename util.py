
import sys
import os

DEFAULT_DIR = 'output/'


def get_target_file_from_argv1():
    if len(sys.argv) != 2:
        print("Please provide the file name.")
        exit()
    return sys.argv[1]


def mkdir_is_not_exist():
    if not os.path.exists(DEFAULT_DIR):
        os.mkdir(DEFAULT_DIR)
