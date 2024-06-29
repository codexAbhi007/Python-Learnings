#! TO run this file correctly do `code -r 46_context_managers` in terminal

import os 
from contextlib import contextmanager


##without context manager we have to manually switch directories and do our work and again change back
# cwd = str(os.getcwd())
# os.chdir('sample_dir_1')
# print(os.listdir())
# os.chdir(cwd)



# os.chdir('sample_dir_2')
# print(os.listdir())
# os.chdir(cwd)
# print(os.getcwd())


##With context manager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield #the thing we yeild goes to with as variable 
    finally:
        os.chdir(cwd)

with change_dir('sample_dir_1'):
    print(os.listdir())

with change_dir('sample_dir_2'):
    print(os.listdir())

print(os.getcwd())