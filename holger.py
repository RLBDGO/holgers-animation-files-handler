import sys
from os import listdir
from os.path import isfile, join
from shutil import copy

def main():
    
    DIR_PATH = str(sys.argv[2])


    files_in_dir = sorted([file.split('.')[0] for file in listdir(DIR_PATH)
                           if isfile(join(DIR_PATH, file))])

    index_changer = lambda file: file.replace(file.split('_')[-1], str(int(file[-1])+len(files_in_dir)))

    files_reversed = list(reversed(files_in_dir))
    
    for i in range(len(files_reversed)):
        copy(join(DIR_PATH, files_reversed[i]+'.txt'),
             join(DIR_PATH, index_changer(files_in_dir[i])+'.txt'))

        
if __name__ == '__main__':
    main()

