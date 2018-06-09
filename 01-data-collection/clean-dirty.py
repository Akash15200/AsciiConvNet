import os

dirty = """
47
48
50
68
70-86
98
120
121
123-129
143-145
155
178
""".splitlines()

for elem in dirty:
    files = []
    if '-' not in elem:
        files.append(elem + '.png')
    else:
        start, end = elem.split('-')
        for file in range(int(start), int(end) + 1):
            files.append(str(file) + '.png')

    for file in files:
        try:
            os.remove('dataset/' + file)
            print('Deleted file:', file)
        except:
            pass
