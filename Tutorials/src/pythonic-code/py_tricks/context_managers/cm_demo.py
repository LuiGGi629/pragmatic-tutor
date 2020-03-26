# with open('sample.txt', 'w') as f:
#     f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()


with open_file('test.txt', 'w') as f:
    f.write('ale ale ale ale ale ale ale ale ale ale ale ale')

print(f.closed)


class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# with OpenFile('test.txt', 'w') as f:
#     f.write('Testing')
#
# print(f.closed)
