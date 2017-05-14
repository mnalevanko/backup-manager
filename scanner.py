# this searches for files that meet certain criteria (does not decide the criteria)

from os import walk

def Scan(dir):
    """
    Given the path to a directory, it will return an iterable containing tuples (filename, subpath)
    :param dir: path to the directory to scan
    :return: 
    """
    filelist = []
    for folderName, subfolders, filenames in walk(dir):
#         print('The current folder is ' + folderName)
        for subfolder in subfolders:
            pass
#             print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            filelist.append((filename, folderName))
    return filelist

#test Scan
for data in Scan(dir):
    print(data)
