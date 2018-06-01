from os import listdir

from os.path import isfile, join
filenames = [f for f in listdir('../captions-indonesia') if isfile(join('../captions-indonesia', f))]
list.sort(filenames)
with open('data/captions300000.txt', 'w') as outfile:
    for fname in filenames:
        print(fname)
        with open('../captions-indonesia/' + fname) as infile:
            for line in infile:
                outfile.write(line)