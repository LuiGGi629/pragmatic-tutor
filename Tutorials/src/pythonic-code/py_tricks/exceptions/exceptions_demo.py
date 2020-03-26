try:
    f = open('corruptfile.txt')
    # if f.name == 'corrupt_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally...')
