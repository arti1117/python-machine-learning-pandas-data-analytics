#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:58:48 2020

@author: arti
"""

import pandas as pd
import numpy as np

student1 = pd.Series({'Korean': np.nan, 'English':80, 'Math':90})
student2 = pd.Series({'Korean':80, 'Math':90})

print(student1); print('--')
print(student2); print('--')

addition = student1.add(student2, fill_value=0) 
subtraction = student1.sub(student2, fill_value=0)
multiplication = student1.mul(student2, fill_value=1)
division = student1.div(student2, fill_value=1)

result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index=['Addition', 'Subtraction', 'Multiplication', 'Division'])

print(result)