#!/apps/sss/Anaconda3/5.0.0/bin/python
# -*- coding: utf-8 -*-

import shutil 
  
# use copyfile() 
# shutil.copyfile('example.txt','example2.txt')

file_path = 'example.txt'
line_to_read = 2


with open(file_path, 'r') as file:
  lines = file.readlines()

if 1 <= line_number_tomodify <= len(lines):
  desired_line = lines[line_to_read - 1].strip()
  variable = desired_line[5:15]
  print(variable)
else:
  print(invalid line )

