import os
import csv
#cwd = os.getcwd()
#print("My current working directory is: {} ".format(cwd))

file_to_save = os.path.join('analysis','election_analysis.txt')
with open(file_to_save, 'w') as txt_file:
    txt_file.write('Hello World')
    