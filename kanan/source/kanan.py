#!/usr/bin/python
#Modules to check arguments and pick random strings
import sys, random

#Variables
n = len(sys.argv)
kanan_art = """
       / \\__
      (    @\\___
      /         O
     /   (_____/
    /_____/     U
"""

#Amount of arguments
if n == 3:
	if sys.argv[1] == "-r":
		file = sys.argv[2]
		try:
			#Open file and close after in read mode
			with open(file, 'r') as openFile:
				#Assign contents of openFile to printFile
				printFile = openFile.read()
				#Print contents of printFile
				print(printFile.strip())
	
		#If FileNotFoundError is raised
		except FileNotFoundError:
			print(file + " was not found. Double check you have the correct file/path.")
	
		#If another error is raised
		except Exception as otherError:
			print("An error occured: " + otherError + ".")

	else:
		print("Oops")

if n == 2:
	if sys.argv[1] == "-s":
		#List of speeched for Kanan to say
		kananSpeeches = ["My best job was being a musician, but eventually I found I wasn’t noteworthy.", "You see people every single day that you'll never see again.", "You may have once made a decision that saved your life without knowing it.", "In every Olympic event, they should have an average person compete so we can have a point of reference and appreciate the athletes more.", "The number of people older than you never goes up.", "One day, you'll be someone's ancestor.", "Why is it called a boxing ring if it's a square?", "Why is it lipstick if it doesn't stick your lips together?"]
		print(kanan_art)
		print("\nKanan says: ", random.choice(kananSpeeches)) 
