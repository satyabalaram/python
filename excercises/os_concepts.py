import os
import multiprocessing
from os import listdir
from os.path import isfile, join
import getpass
import glob
import sys

dirpath = os.path.dirname(os.path.realpath(__file__))

print"Current File Name : ",os.path.realpath(__file__) # path name of the file currently executing
print(multiprocessing.cpu_count())  # no of CPUs using
files_list = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
print(files_list);
print (getpass.getuser())
print "obsolute file path", os.path.abspath('os_concepts.py')

    
#files sort by date

files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))

#find if system is big indian or little indian

if sys.byteorder == "little":
    print "\nLittle indian platform\n"
else:
    print "\nBig indian platform\n"

#check if a file path is a file or directory

path="os_concepts.py"  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )

# get size of a file
file_size = os.path.getsize("os_concepts.py")
print 'file size is:', file_size, 'bytes\n'

#extract filename from given path
print 'filename of given path',os.path.basename('c:\\naini\\python_scripts\\excercises\\os_concepts.py')
print 'directory where file is in', os.path.dirname('c:\\naini\\python_scripts\\excercises\\os_concepts.py')


