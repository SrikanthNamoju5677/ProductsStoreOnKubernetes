#!/apps/sss/Anaconda3/5.0.0/bin/python
# -*- coding: utf-8 -*-

import shutil 
  
# use copyfile() 
# shutil.copyfile('example.txt','example2.txt')

file_path = 'example.txt'
line_number_tomodify = 3
newcontent = 'file got changed'

with open(file_path, 'r') as file:
  lines = file.readlines()

if 1 <= line_number_tomodify <= len(lines):
  lines[line_number_tomodify - 1] = newcontent + '\n'

with open(file_path, 'r') as file:
  lines = file.writelines(lines)
