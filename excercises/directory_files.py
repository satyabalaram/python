#!/usr/bin/python

import os, sys, fnmatch

# Open a file
dirs = os.listdir("k:\\validat\\test_pool\\AndroidCTS_Main_2.1\\android-cts_nmr1\\testcases")  
#dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
     if fnmatch.fnmatch(file, '*.apk'):
        print file
   
