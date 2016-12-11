import arcpy
import os
import sys


#Added Extra Field to 2006 Attribute Table to Calculate Duplicate Fires
#Named Field "DUPS"

#Used following python script to calculate duplicates
dup_dict={}
def dups(x):
    dup_dict[x]=dup_dict.setdefault(x,-1)+1
    return dup_dict[x]

#Enter into Python Window to find days in 2006 that had fifty or more fires
#This code saves me from individually going through every single date
#In every single year and building the query to show me individual repeated dates
#And physically counting all the duplicates for all ten years
#Using this data to find hotspots
#Set for days with fifty+ fires

cursor_location=arcpy.da.SearchCursor("2006",["DUPS","JDATE"]) #Change year accordingly
test=(49.0, 2006005) #Tests for days that had fifty or more fire and shows the Julian date as an identifier
fifty=[] #Empty list to put for loop results into
#Must find first Julian Date from attribute table to use here in order for it to work
for row in cursor_location:
    if row>test:
        fifty.append(row)

#Make function that gets rid of the days that are printed multiple times
        #Due to having more than one number over 49

def rid_dupes(x):
    uniques=set()
    for i in x:
        if not uniques.intersection(i):
            yield i
            uniques.update(i)


#List the days with 50+ fires to use to run hot spot tool
list(rid_dupes(fifty))

#Will have to do same tests for every year
