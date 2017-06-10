# this searches for files that meet certain criteria (does not decide the criteria)

from os import walk

def Scan(dir):
    """
    Given the path to a directory, it will return an iterable containing tuples (filename, subpath)
    :param dir: path to the directory to scan
    :return: 
    """
    for folderName, subfolders, filenames in walk(dir):
        for filename in filenames:
            yield (filename, folderName)
