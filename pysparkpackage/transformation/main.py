import argparse
from pysparkpackage.helper.components.read_file import read_file_helper

def read_infor():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path', dest='path')
    parser.add_argument('-t', '--type', help='File type', dest='file_type')
    args = parser.parse_args()

    return args

def main():
    args = read_infor()
    data = read_file_helper.read_file(args.path, args.file_type)

    data.show()