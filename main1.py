#!/apps/sss/Anaconda3/5.0.0/bin/python
# -*- coding: utf-8 -*-

import shutil 
  
# use copyfile() 
# shutil.copyfile('example.txt','example2.txt')

release_notes = 'example.txt'
release_history = 'example2.txt'
release_template = 'example1.txt'
line_to_read = 2
line_to_write = 7
specific_line_number = 14


output_file = open(release_history, 'r')
lines = output_file.readlines()
input_file = open(release_notes, "r")
content_to_append = input_file.read()

output_file = open(release_history, 'r')
output_file.writelines(lines[:specific_line_number])
output_file.write(content_to_append)
output_file.writelines(lines[specific_line_number:])
output_file.close()


with open(release_notes, 'r') as file1:
  lines = file1.readlines()
  desired_line = lines[line_to_read - 1].strip()
  updateversion = desired_line[80:86]
  print(updateversion)
with open(release_history, 'r') as file2:
    line = file2.readlines()  
  

if 1 <= line_to_write <= len(line):
    desired_lines = line[line_to_write - 1].strip()
    existversion = desired_lines[42:48]
    print(existversion)
    data2 = desired_lines.replace(existversion, updateversion)
else:
  print("invalid line")

with open(release_history, 'r') as file:
  contents = file.read()
  contents = contents.replace(variable,updateversion)

with open(release_history, "w") as file:
  file.write(contents)
  file.close()
  
# use copyfile() 
shutil.copyfile(release_template,release_notes)  
