# backup.py
'''
This takes care of the actual copying of the files.
'''

# QUESTION - SHOULD I CHECK THAT THE FILE IS NOT BEING OVER-WRITTEN?
# Not for now, let's keep it simple and add stuff as we go.


import sys, os, shutil
from os import path as p


def Backup(from_path, to_path):
    """
    Backups a file.
    from_path :str
    to_path :str
    """
    from_path, to_path = p.expanduser(from_path), p.expanduser(to_path)
    try:
        if not p.isfile(from_path):
            raise ValueError(from_path + " does not seem to point to a file.")
        if not p.isdir(to_path):
            raise ValueError("Directory not found: " + path2)
    except ValueError as e:
        print(e)

    shutil.copy(from_path, to_path)
