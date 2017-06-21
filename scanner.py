# this searches for files that meet certain criteria (does not decide the criteria)

from os import walk

### DON'T USE dir as a variable/argument name, or you'll override the builtin function dir() in the local namespace !!

def Scan(directory):
    """
    Given the path to a directory, it will return an iterable containing tuples (filename, subpath)
    :param dir: path to the directory to scan
    :return: 
    """
    filelist = []
    for folderName, subfolders, filenames in walk(directory):
        #print('The current folder is ' + folderName)
        for filename in filenames:
            filelist.append((filename, folderName))
    ### This could also be made into a generator, let's maybe talk about it next lesson?
    return filelist

# ### LET'S TALK ABOUT HOW TO DO TESTS NEXT TIME :)
# #test Scan
# for data in Scan(directory):
#     for folderName, subfolders, filenames in walk(directory):
# #         print('The current folder is ' + folderName)
#         for subfolder in subfolders:
#             pass
# #             print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#         for filename in filenames:
#             filelist.append((filename, folderName))
#     return filelist
#
# #test Scan
# for data in Scan(my_dir):
#     print(data)
