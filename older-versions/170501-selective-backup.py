# Adapted from Automate the Boring Stuff
'''
Selective Copy
Write a program that walks through a folder tree and searches for files 
with a certain file extension (such as .pdf or .jpg). Copy these files 
from whatever location they are in to a new folder.

Modifications
-The subfolders in the file directory are mirrored
-specified file types are copied
-Code names are used for file folders to be copied.
--Examples:
rootbackup / codename1 / filetype1 / file
rootbackup / codename2 / filetype2 / file
'''
import sys, os, shutil
from datetime import datetime as d
from os import path as p
from pathlib import Path

def today_backup_path(dirlist):
    '''dirlist is a list of files in the specified rootbackup directory. 
    returns a unique destination path (string) with a 01, 02, or etc suffix.
    '''
    todaydate = d.now().strftime("%y%m%d")
    for intsuffix in range(1,100):
        intsuffix = ('_{num:02d}'.format(num=intsuffix))
        todaybackup = ''.join(('backup', todaydate, intsuffix))
        if todaybackup in dirlist:
            continue
        else:
            break
            
    dest = p.join(rootbackup, todaybackup)
    return dest

def backup_files(codename, source, filetype, destination):
    '''name is a codename for the source folder. 
    source is a string of full path. 
    filetype is a string like 'txt' or 'md'. 
    destination is automatically created by today_backup_path function.
    '''
    for folderName, subfolders, filenames in os.walk(source):
    #     print('The current folder is ' + folderName)
    #     for subfolder in subfolders:
    #         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            if filename.endswith('.' + filetype)\
                and not filename.startswith('.'):
                new_source = p.join(folderName, filename)
                new_dest = p.join(destination, codename, filetype, folderName[len(source):])
                print('  Copying:', new_source)
                print('  to new folder:', new_dest)
                # toggle this line for testing
                shutil.copy(new_source, create_subfolder(new_dest))
    #     print('')
    
def create_subfolder(subfolder):
    '''subfolder path is created if it doesn't exist or left alone. subfolder path is returned.
    '''
    sub_path = Path(subfolder)
    if not sub_path.is_dir():
        os.makedirs(subfolder)
    return subfolder

rootbackup = ''
os.chdir(rootbackup)
dirlist = os.listdir('.')
#paths MUST end with /
sourcedict = {'Inbox': '.../-Inbox/', 'Programming':  '/.../Programming/'}
filetypelist = ('txt', 'md', 'html', 'py', 'js', 'csv')
destination = today_backup_path(dirlist)

# Backup 'filetype' files in 'source'
for name, source in sourcedict.items():
    for filetype in filetypelist:
        backup_files(name, source, filetype, destination)
