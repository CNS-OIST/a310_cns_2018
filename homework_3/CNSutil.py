"""
CNSutil.py

A collection of utility functions for A310 Computational Neuroscience Course.

written by Sungho Hong, Computational Neuroscience Unit, OIST, Japan
January 2018
"""

__version__ = 0.1

import numpy as np

def check_type(reclist):
    """checks type of reclist."""
    if type(reclist)==list:
        return 'list of ' + check_type(reclist[0])
    else:
        if 'to_python' in dir(reclist):
            return 'hvector'
        else:
            raise TypeError('Unknown type to convert')

            
def convert_to_array(reclist):
    """converts reclist to an numpy array."""
    tp = check_type(reclist)
    if tp=='list of hvector':
        return np.array([convert_to_array(x) for x in reclist]).T
    elif tp=='hvector':
        return np.array(reclist.to_python())
    else:
        raise TypeError('Unknown type to convert')

        
def savetxt(fname, reclist):
    """saves reclist in a text file, fname"""
    np.savetxt(fname, convert_to_array(reclist))
    print('Data saved in', fname)

    