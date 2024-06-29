from contextlib import contextmanager


@contextmanager
def open_file(file,mode):
    try:
        f = open(file,mode)
        yield f
    finally:
        f.close()


with open_file(r'46_context_managers\files\sample2.txt','w') as f:
    f.write('HELLO WORLD !')

print(f.closed)