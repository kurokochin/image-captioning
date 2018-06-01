from os import listdir

from os.path import isfile, join
# filenames = [f for f in listdir('../captions-indonesia') if isfile(join('../captions-indonesia', f))]
# list.sort(filenames)

# with open('data/captions-indonesia.txt', 'w') as outfile:
#     for fname in filenames:
#         print(fname)
#         with open('../captions-indonesia/' + fname) as infile:
#             for line in infile:
#                 outfile.write(line)

with open('data/captions-indonesia.txt', 'w') as outfile:
    for i in range(0,414500, 500):
        with open('./captions-indonesia/captions-indonesia-' + str(i) + '-' + str(i+499) + '.txt') as infile:
            for line in infile:
                outfile.write(line)