#!/apps/sss/Anaconda3/5.0.0/bin/python
# -*- coding: utf-8 -*-

import shutil 
  
# use copyfile() 
# shutil.copyfile('example.txt','example2.txt')

file_path = 'example.txt'
line_to_read = 2

def append_after_line('example.txt', 'example2.txt', 10):
  with open('example.txt', 'r') as file1:
    contenttoappend = file1.read()
   with open('example2.txt', "a") as file2:
     lines = file2.readlines()
     start_line = min(10,len(lines) + 1)
     file2.write(contenttoappend)
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

