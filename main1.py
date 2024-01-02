#!/apps/sss/Anaconda3/5.0.0/bin/python
# -*- coding: utf-8 -*-

import shutil 
  
# use copyfile() 
# shutil.copyfile('example.txt','example2.txt')

file_path = 'example.txt'
line_to_read = 2
line_to_write = 7
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


with open(file_path, 'r') as file1:
  lines = file1.readlines()
  desired_line = lines[line_to_read - 1].strip()
  updateversion = desired_line[80:86]
  print(updateversion)
with open('example2.txt', 'r') as file2:
    line = file2.readlines()  
  

if 1 <= line_to_write <= len(line):
    desired_lines = line[line_to_write - 1].strip()
    variable = desired_lines[42:48]
    print(variable)
    data2 = desired_lines.replace(variable, updateversion)
    print(data2)
    print("Text replaced")
    # lines = file.writelines(line.replace('variable', '7777777'))
else:
  print("invalid line")

# filename = input("File: ")
# line_number = int(input("Line: "))
# text = input("Text: ")

# Call the replace_line() function to replace the text at the line number 
# 'line_number' in the file with the filename 'filename' with the replacement 
# text 'text'.
replace_line("example2.txt","7", data2)
  
def replace_line("example2.txt","7", data2):

# Open the file and read all the lines from the file into a list 'lines'
with open('example2.txt') as file:
  lines = file.readlines()

# if the line number is in the file, we can replace it successfully
if (7 <= len(lines)):
  
  # Replace the associated line in the list with the replacement text 
  # (followed by a newline \n to end the line), we need to use line_number - 1
  # as the index because lists are zero-indexed in Python.
  lines[line_number - 1] = data2 + "\n"
  
  # Open the file in 'writing mode' using the 2nd argument "w", this means 
  # that the file will be made blank, and any new text we write to the file 
  # will become the new file contents.
  with open('example2.txt', "w") as file:

    # Loop through the list of lines, write each of them to the file
    for line in lines:
      file.write(line)

# otherwise if the line number is past the length of the file, we can't 
# replace the line so output an error message instead
else:

  # Output the line number that was requested to be replaced and the number
  # of lines the file actually has to inform the user
  print("Line", 7, "not in file.")
  print("File has", len(lines), "lines.")

  
  
