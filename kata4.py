#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      isingh
#
# Created:     06/11/2013
# Copyright:   (c) isingh 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re
def first(file,f,s,r, regex):
    """
    file is the file name, |f - s| is the value, r is position returned, regex
    is the regular expression match filter for the lines of file
    """
    with open(file,'r') as infile:
        tempSpread=1000
        for line in infile:
                if re.search(regex,line):
                    myList = line.split()
                    if abs(int(myList[f][0:2]) - int(myList[s][0:2])) < tempSpread:
                        tempSpread = abs(int(myList[f][0:2]) - int(myList[s][0:2]))
                        output = myList[r]
        print output

regex=r'(^\s+[0-9])'
first('C:\Users\isingh\Documents\kata\weather.dat',1,2,0,regex)
first(r'C:\Users\isingh\Documents\kata\football.dat',6,8,1,regex)

