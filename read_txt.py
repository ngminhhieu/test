import glob
import os
import re


path = './lan_lan_2/'
for label_path in glob.glob(os.path.join(path,"*.txt")):
    # Read in the file
    with open(label_path, 'r') as file :
        lines = file.readlines()
        new_lines = ''
        for line in lines:
            if re.match('0', line):
                new_lines += (re.sub('0', '1', line, 1))
            elif re.match('1', line):
                new_lines += re.sub('1', '0', line, 1)
            elif re.match('2', line):
                new_lines += re.sub('2', '4', line, 1)
            elif re.match('3', line):
                new_lines += re.sub('3', '5', line, 1)
            elif re.match('4', line):
                new_lines += re.sub('4', '3', line, 1)
            elif re.match('5', line):
                new_lines += re.sub('5', '2', line, 1)
    with open(label_path, 'w') as file :
        file.write(new_lines)