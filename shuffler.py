# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:33:00 2021

@author: Sebastian
"""

import numpy as np

def _generateConditionList(phases, frequencys):
    """
    

    Parameters
    ----------
    phases : list(int)
        Phases for the lucky loop.
    frequencys : list(int)
        Frequencys for the lucky loop.

    Returns
    -------
    conditions : list((int, int))
        List of tulples of all variants with (phase, frequency).

    """
    return [(p, f) for p in phases for f in frequencys]

def _generateConditionArray(conditionList, repeats):
    """
    

    Parameters
    ----------
    conditionList : list(tulple)
        List of the available conditions.
    repeats : int
        How often each condition will be tested.

    Returns
    -------
    np.array
        2D array with shape (len(conditionList), repeats) of tulples.

    """
    # generates the 2d array, by extending the list (*repeats) and creating
    # an array -> with dtype set to create an array of tulples
    # and then reshaping using fortan style index order!
    return np.array(conditionList*repeats, dtype=np.dtype("int, int")).reshape((len(conditionList), repeats), order='f')

def _permuteConditionArray(conArr):
    """
    Permutes the Condition Array, along the column

    Parameters
    ----------
    conArr : np.array
        2D array with shape (len(conditionList), repeats) of tulples.

    Returns
    -------
    con : np.array
        2D array with shape (len(conditionList), repeats) of tulples,
        permuted along the columns.

    """
    rng = np.random.default_rng()
    con = conArr.copy()
    for c in range(conArr.shape[1]):
        con[:, c] = rng.permutation(con[:, c])
    return con


def getConditions(phases, frequencys, repeats):
    """
    

    Parameters
    ----------
    phases : list(int)
        Phases for the lucky loop.
    frequencys : list(int)
        Frequencys for the lucky loop.
    repeats : int
        How often each condition will be tested.

    Returns
    -------
    np.array
        2D array with shape (len(phases) * len(frequencys), repeats) of tulples.
        Contains all the conditions, permuted along the columns.

    """
    _con_arr = _generateConditionArray(_generateConditionList(phases, frequencys), repeats)
    return _permuteConditionArray(_con_arr)
