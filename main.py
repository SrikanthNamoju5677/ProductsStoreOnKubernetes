#!/apps/sss/Anaconda3/5.0.0/bin/python
# -*- coding: utf-8 -*-

import shutil 
  
# use copyfile() 
# shutil.copyfile('example.txt','example2.txt')

file_path = 'example.txt'
line_to_read = 2
specified2_linenumber = 10

with open('example.txt', 'r') as file1:
  lines = file1.readlines()
with open('example2.txt', "w") as file2:
   file2.writelines(lines[:specified2_linenumber])
with open('example.txt', "r") as appendfile:
   file2.write(appendfile.read())
   file2.writelines(lines[specified2_linenumber])
   file1.close()
   file2.close()


# with open(file_path, 'r') as file:
#   lines = file.readlines()
#   data = file.read(line_to_read)

# if 1 <= line_to_read <= len(lines):
#   desired_line = lines[line_to_read - 1].strip()
#   variable = desired_line[80:86]
#   print(variable)
#   data2 = desired_line.replace(variable, "replaced")
#   print(data2)
#   with open(file_path, 'w') as file:
#     file.write(data2)
#   print("Text replaced")
#   # lines = file.writelines(line.replace('variable', '7777777'))
# else:
#   print("invalid line")

