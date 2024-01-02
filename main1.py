#!/apps/sss/Anaconda3/5.0.0/bin/python
# -*- coding: utf-8 -*-

import shutil 
  
# use copyfile() 
# shutil.copyfile('example.txt','example2.txt')

file_path = 'example.txt'
line_to_read = 2
line_to_write = 1
specified2_linenumber = 10



# op = open('example2.txt', 'r')
# lines = op.readlines()
# print(lines)
# ip = open('example.txt', "r")
# content_to_append = ip.read()

# op = open('example2.txt', 'w')
# op.writelines(lines[:specified2_linenumber])
# # data = ip.writelines(lines[:specified2_linenumber])
# # print(data)
# # appendfile = open('example.txt', "r")
# # data2 = appendfile.read()
# # print(data2)
# op.write(content_to_append)
# op.writelines(lines[specified2_linenumber:])
# op.close()


with open(file_path, 'r') as file:
  lines = file.readlines()
  desired_line = lines[line_to_read - 1].strip()
  updateversion = desired_line[80:86]
  print(updateversion)

if 1 <= line_to_write <= len(lines):
  with open('example2.txt', 'r') as file:
  lines = file.readlines()
  desired_line = lines[line_to_read - 1].strip()
  variable = desired_line[42:48]
  print(variable)
  data2 = desired_line.replace(variable, updateversion)
  print(data2)
  print("Text replaced")
  # lines = file.writelines(line.replace('variable', '7777777'))
# else:
  print("invalid line")
  
  
