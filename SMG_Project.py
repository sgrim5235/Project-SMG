import arcpy


#Added Extra Field to 2006-2016 Attribute Tables to Calculate Duplicate Fires
#Named Field "DUPS" before running any scripts

#Use following python script to calculate duplicates in
#new "DUPS" field in Field Calculator window
dup_dict={}
def dups(x):
    """Takes a field from the attribute table and

    in order to add values to the new field "DUPS"

    showing how many times an element from the chosen

    field are duplicated. Returns results into "DUPS" field.

    """
    dup_dict[x]=dup_dict.setdefault(x,-1)+1
    return dup_dict[x]


#Change working directory to location of this file
#Enter following scripts into python window of ArcMap in order
    #to find days of every year that had more than fifty fires on said day.
    #Will need to do this code for each individual year
    #To find appropriate Julian date, open the year's attribute table
    #And note what the first Julian date is (may need to sort field ascending


fifty=[]
testrow=(49.0, #insert first julian date from attribute table)
cursor_location=arcpy.da.SearchCursor(#layer ie "2006",["DUPS", "JDATE"])
for row in cursor_location:
    if row>testrow:
        fifty.append(row)

#Using the above script appropriately will yield a list (fifty) of
    #All the Julian Dates of that year that have "DUPS" numbers greater
    #Than 49.0 and also print their significant Julian Date


def rid_dupes(x):
    """Takes list and returns the same list without tuples that have

    elements that are repeated due to occasional Julian Dates that

    have 51, 52, 53 etc fires being printed in said list more than once

    """
    uniques=set()
    for i in x:
        if not uniques.intersection(i):
            yield i
            uniques.update(i)


#List the days with more than 50 fires to use to run hot spot tool
def fifty_plus_days(listname):
    return(list(rid_dupes(listname)))



