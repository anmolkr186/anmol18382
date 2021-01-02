import csv 
import requests 
import xml.etree.ElementTree as ET 
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["stackoverflowdb"]

print("Conversion started....")

"""
Parameters :
col_name - Name of the collection for the database
file_name - XML file to parse
This function converts deletes the already existing collection
and makes a new one based on the xml present in the same directory.
"""

def make_collection(col_name, file_name):
	#if collection already existing in the database, then delete it
	if(col_name in mydb.list_collection_names()):
		 col = mydb[col_name]
		 col.drop()

	aa = str(col_name)
	col_name = mydb[aa]
	tree = ET.parse(file_name)
	root = tree.getroot()
	count = 0

	#
	for row in root:
		x = col_name.insert_one(row.attrib)
		count+=1
	print(aa + " collection done, Extracted " + str(count) + " datapoints")

# Function calls for the five XMLs present in the same directory

make_collection("tag_col", "stackoverflow.com\Tags.xml")
make_collection("user_col", "stackoverflow.com\\Users.xml")
make_collection("votes_col", "stackoverflow.com\\Votes.xml")
make_collection("votes_col", "stackoverflow.com\\Badges.xml")
make_collection("votes_col", "stackoverflow.com\\Posts.xml")

print("Done!")


	