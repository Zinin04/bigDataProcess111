# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zooLdlP-4jUMn_UUNuP1KtM6A4HLcVnI
"""

import random
n1= random.randint(1,100)
n2= random.randint(1,100)
while True:
    solution = n1+n2
    answer= eval(input('%d+%d='%(n1,n2)))
    if answer == solution:
        print ('Correct, ou are very good.')
        break
    else:
        print('Wrong, try again.')