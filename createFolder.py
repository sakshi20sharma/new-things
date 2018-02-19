import os

def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
			print "success1"
	except OSError:
		print "error"

createFolder('./testFolder/')
print "final success"
