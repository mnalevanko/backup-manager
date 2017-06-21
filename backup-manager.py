# this defines a BackupManager class that glues together all other pieces 
# performing scan of dir and subdirs + criteria checking + backup if necessary, with the values from settings.conf

from scanner import *
from criteria import *
from backup import *
import sys
import os

#myDir = "/Users/davecohen/Documents/DEC/Programming/-PYTHON/__get__lessons"
#backupDir = "/Users/davecohen/MEGA/Backups-Mega/backup-test"

myDir = "/home/gg/python/"
backupDir = '/home/gg/tmp/'

# #how do I initialize and use Extension filter? I think I need to make a new instance of the class, but the parameters depend on the output of Scan(), correct?
# myFilter = ExtensionFilter().filter((filename, folderName), backupDir, 'txt')
#
# for filename, folderName in Scan(myDir):
#     if filename in myFilter(): #see issue above
#         Backup(os.path.join(filename, foldername), backupDir)

if __name__ == "__main__":
    files = ExtensionFilter(Scan(myDir), ('.py', '.txt')).results
    for file, path in files:
        Backup(os.path.join(path, file), backupDir)