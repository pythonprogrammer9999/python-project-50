import argparse


def get_gendiff():
    parser = argparse.ArgumentParser()
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(args)
    exit()

get_gendiff()