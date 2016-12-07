import arcpy

#Added Extra Field to 2006 Attribute Table to Calculate Duplicate Fires
#Named Field "DUPS"

#Used following python script to calculate duplicates
dup_dict={}
def dups(x):
    dup_dict[x]=dup_dict.setdefault(x,-1)+1
    return dup_dict[x]

#Enter into Python Window to find days in 2006 that had thirty or more fires
#Using this data to find hotspots
cursor_location=arcpy.da.SearchCursor("2006","DUPS")
test=(29.0,) #Tests for days that had thirty or more fires, in tuple format because
#that is how the rows are printed for some reason...haven't figured that out
for row in cursor_location:
    if row>test:
        print row

#Need to find a way to print row identifier as well, like the Julian Date
#Will have to do same test for every year
#Also need to add the DUPS field to 2006-2016
