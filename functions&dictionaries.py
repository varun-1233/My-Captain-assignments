# -*- coding: utf-8 -*-
"""Functions&Dictionaries

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PdEGVdgSLb1SHYxx2HOUWQvjrqqTM-vI
"""

def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print(most_frequent('mississipi'))