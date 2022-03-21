try:
    L = [x for x in range(10)]
    f = open('numbers.txt', 'w')
    for x in L:
        f.write(x)
except FileNotFoundError:
    print('File was not found')
except:
    print('This is some other error')
finally:
    print('The file has been closed')
    f.close()