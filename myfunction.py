# -*- coding: utf-8 -*-
"""MyFunction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TbU7zwyN2UQ2BS9LBYKg_n1OfUfCQnsn
"""

def my_star_func(x):
  import numpy as np
  for i in list(np.arange(1,x+1)):
    print("*"*i)