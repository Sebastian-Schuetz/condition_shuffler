# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:32:46 2021

@author: Sebastian
"""

from shuffler import getConditions


con = getConditions([-90, 0, 90, 180], [-4, 0, 4], 20)


# Example how it would be used. Here 12 conditions, meaning 20 trials á 12 runs

for i in range(20):
    for _c in con[:, i]:
        print(_c) # here we do the testing
    input("Press enter to start next trial")