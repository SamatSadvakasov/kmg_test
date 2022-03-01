import os
import datetime as dt
import argparse
from parsing.parse import parsing_folder
from database.db import initialize_database, \
    drop_database


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Parser application for KMG Engineering')
    parser.add_argument('-i', '--init', action='store_true',
                        help='Initialize database')
    parser.add_argument('--drop_database', action='store_true',
                        help='Drop database')
    parser.add_argument('-d', '--directory', type=str,
                        help='Path to directory')
    return parser.parse_args()


if __name__ == "__main__":
    try:
        args = get_arguments()
        if args.init:
            initialize_database()
            print("Database successfully created")
            exit(0)
        if args.drop_database:
            drop_database()
            print("Database successfully dropped")
            exit(0)
        elif args.directory:
            if os.path.exists(args.directory):
                start = dt.datetime.now()
                res = parsing_folder(args.directory)
                end = dt.datetime.now()
                print('Time ', end - start)
                print("Directory successfully parsed")
            else:
                print(args.directory, 'directory is not exists')
            exit(0)
        else:
            print("No file or directory for parsing")
    except KeyboardInterrupt:
        print("Canceled ...")
        exit(0)
