import sys
import shutil
import os


def recSearch(d):
    for f in os.scandir(d):
        if f.is_dir():
            if f.name == 'dv8' or f.name == 'csv':
                print(f.path)
                shutil.rmtree(f.path)


if __name__ == "__main__":
    for f in os.scandir():
        if f.is_dir():
            recSearch(f)
