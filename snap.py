#!/usr/bin/python2.7
# -- coding: utf-8 --
# directory snapshot program
import os
import pickle
import pprint
import difflib
prompt = "> "
os.system('clear')
print "="*60
print "   This is program to create snapshot of a directory.  "
print "   The snapshot is a collection of all the files and   "
print "   directory at a given instance of time. A Snapshot   "
print "   is compared with another snapshot of the same dir-  "
print "   ctory to see what changes have occured. "
print "="*60
print "Type 1 to create snapshot of a directory"
print "Type 2 to view snapshots"
print "Type 3 to comapre snapshots"
print "Type 4 to exit"
inputx = raw_input(prompt)

#inputx = '2'
#while inputx != "1" or inputx != "2" or inputx != "3" or inputx != "4" or inputx != "5" :
#	print "type correct input"
#	inputx = raw_input(prompt)

if inputx == '1':
	print "creating snapshot of a directory"
	print "Type the name of the directory of which the snapshot is to be created"
	directory = raw_input(prompt)
	print "%r" % directory
	directory_list = []
	file_list = []
	for root,dirs,files in os.walk(directory):
		directory_list = directory_list + dirs
		file_list = file_list + files
	#print directory_list
	#print file_list

	print "type the name of the snapshot"
	snap_name = raw_input(prompt)
	print "the snapshot name is ", snap_name
	output = open(snap_name, 'wb')

	pickle.dump(directory_list, output, -1)
	pickle.dump(file_list, output, -1)

	output.close()

	output = open(snap_name, 'rb')
	data = pickle.load(output)
	data2 = pickle.load(output)

	pprint.pprint(data)
	pprint.pprint(data2)

	output.close()

elif inputx == '2':
	print "type the name of the directory in which the snapshots are kept"
	print "default directory is current directory"
	
	directory = raw_input(prompt)
	
	extension = '.snp'
	snaplist = []
	filelist = os.listdir(os.curdir)
	for item in filelist:
		if item.find(extension) != -1:
			snaplist.append(item)
	print '''
	Snapshot list:
	===============================================
	'''
	pprint.pprint(snaplist)
	raw_input("Press [Enter] to continue...")

elif inputx == '3':
	print "comparing snapshots of the directory"
	print "type the name of the first snapshot"
	snap1 = raw_input(prompt)
	print "type the name of the second snapshot"
	snap2 = raw_input(prompt)
	snap1obj = open(snap1,'rb')
	snap2obj = open(snap2,'rb')
	dirs1 = pickle.load(snap1obj)
	files1 = pickle.load(snap1obj)
	dirs2 = pickle.load(snap2obj)
	files2 = pickle.load(snap2obj)
	compared_dirs = list(difflib.unified_diff(dirs1,dirs2))
	compared_files = list(difflib.unified_diff(files1,files2))
	added_dirs = []
	removed_dirs = []
	added_files = []
	removed_files = []
	for result in compared_files:
		if result.find("\n") == -1:
			if result.startswith("+"):
				resultadd = result.strip("+")
				added_files.append(resultadd)
			elif result.startswith("-"):
				resultsubtract = result.strip("-")
				removed_files.append(resultsubtract)
	
	for result in compared_dirs:
		if result.find("\n") == -1:
			if result.startswith("+"):
				resultadd = result.strip("+")
				added_dirs.append(resultadd)
			elif result.startswith("-"):
				resultsubtract = result.strip("-")
				removed_dirs.append(resultsubtract)

	print "\n\nAdded Directories "
	pprint.pprint(added_dirs)
	print "\n\nAdded Files "
	pprint.pprint(added_files)
	print "\n\nRemoved Directories "
	pprint.pprint(removed_dirs)
	print "\n\nRemoved Files "
	pprint.pprint(removed_files)

	snap1obj.close()
	snap2obj.close()
		


elif inputx == '4':
	print "exiting"	
else :
	print "type correct number"



	
