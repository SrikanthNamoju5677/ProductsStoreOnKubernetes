#!/apps/sss/Anaconda3/5.0.0/bin/python
# -*- coding: utf-8 -*-

import shutil, os

def append_after_line('example.txt','example2.txt', 10):
  with open('example.txt', 'r') as file1:
    contenttoappend = file1.read()
   with open('example2.txt', "a") as file2:
     lines = file2.readlines()
     start_line = min(10,len(lines) + 1)
     file2.write(contenttoappend)
