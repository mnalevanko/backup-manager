# the code actually doing the backup. This simply copies files around when told to

'''
write a function named Backup in backup.py that:
    given two paths it will copy the file from path1 into path2. You should check that path1 points to a file and that path2 is an existing directory. If any of those checks should fail, raise an exception.

kind of one - should I look more into os.path functions or is the len(source) ok for now?

don't worry about subdirs for now
just write a function that given 2 paths (file and dir) will copy the file into the dir
'''

# QUESTION - SHOULD I CHECK THAT THE FILE IS NOT BEING OVER-WRITTEN?


import sys, os, shutil
from os import path as p

class CustomException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

# path1 points to a file
path1 = '/Users/davecohen/Documents/DEC/-Inbox/Emails.txt'
# path2 is an existing directory
path2 = '/Users/davecohen/MEGA/Backups-Mega'

print('Checking path1 and path2.')

if not p.isfile(path1):
    raise CustomException("File not found: " + path1)
    
if not p.isdir(path2):
    raise CustomException("Directory not found: " + path2)
    
print('Files checked.')

print('Copying {} to {}'.format(path1, path2))

shutil.copy(path1, path2)

print('Successful!')
