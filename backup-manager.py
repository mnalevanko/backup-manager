# this defines a BackupManager class that glues together all other pieces 
# performing scan of dir and subdirs + criteria checking + backup if necessary, with the values from settings.conf

from scanner import *
from criteria import *
from backup import *
import sys
import os

myDir = "/Users/davecohen/Documents/DEC/Programming/-PYTHON/__get__lessons"
backupDir = "/Users/davecohen/MEGA/Backups-Mega/backup-test"
myFilter = ExtensionFilter().filter(filename, folderName, 'txt')

for filename, folderName in Scan(myDir):
    if filename in myFilter():
        Backup(os.path.join(filename, folderName), backupDir)
