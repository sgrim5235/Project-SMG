# Project-SMG
GISC3200K Final Project

Please view in "RAW" format to view appropriately.

The attached Python file includes codes to simplify the narrowing of data in ArcMap for a specific issue.
In an ArcMap document, I needed to identify certain elements within 11 different attribute tables that each have thousands
among thousands of elements.
Though, simply using the "Select by Attributes" option would work, it would take an endless amount of time.
This is because within each attribute table, I needed to identify which elements from a certain field were repeated.
For example, every attribute table has a field that includes the date of the year that that element was identifited/reported.
I wanted to identifty which of those days were repeated, and how many times.
Using "Select by Attributes" would work, yes, but obviously would take an excessively amount of time due to the fact that I was analyzing
11 year with thousands of elements within each year.
Instead, I created an new field on each year's table called "DUPS" - type: integer.
In the Field Calculator, I needed a python code that would count the Dates from the Julian Date field of the table and print in the DUPS field how many times that Date was repeated. So, if a date only showed up once, it would print 0. Twice, it would print 1. Three times, 2. So on, and so forth. I created a function called "dups" and used it in the code block of the Field Calculator.
Once the "DUPS" field was filled, I needed to then identify which elements that were duplicated were duplicated more than 50 times.
Using the "Select by Attribute" field could again work to identify these elements, but I wanted the results in a list on the screen that I could read off of while using "Select by Attribute" later, without exporting these elements into a new layer or table (would take up useless memory).
I then created a python script that would identify the elements of the year I was working on that had more than 50 duplicates and put them into a list.
Before using the following script for each year, I changed the working directory to where my python file was located so that I could import the module in order to use the function I defined after the following script.
  fifty=[]
  testrow=(49.0, insert first Julian date in attribute table)
  cursor_location=arcpy.da.SearchCursor("insert year analyzing",["DUPS", "Name of Julian Date field ie JDATE or JULIAN"]
  for row in cursor_location:
    if row>testrow:
      fifty.append(row)
      
After having used the above script for a year, I needed to narrow the list once more to get rid of the Julian dates that were inserted to the "fifty" list more than once due to having 51, 52, 53 etc duplicates on said day.
In order to do so, I defined a function that would give me the tuples one time instead of multiple times. The function is "rid_dupes".
I imported the function from my module before attempting to run it, obviously. This only needs to be done one time.
After this function is run, I needed to print my final list. In order to do so, I created a function called "fifty_plus_days".
Running this function prints me my final list of Julian Dates that I need to refer to in order to use the "Select by Attributes" tool to select the dates from the year I'm on.

Repeat this process for each year.
I used this process to find days of each year that had more than 50 wildfires on said day in order to use the Hot Spot analysis tool to identify clusters. Doing days that had more than 50 fires instead of using every single day that had a fire each year narrows the data, making it easier to understand and visualize.
