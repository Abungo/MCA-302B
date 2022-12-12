import os
import shutil

#Function to Create a folder
def makefolder(path1):
	if not os.path.exists(path1):
		os.makedirs(path1)
	else:
	   	shutil.rmtree(path1)
	   	os.makedirs(path1)

#Function to Search all the .py files
def get_py_files(base_dir):
    for entry in os.scandir(base_dir):
        if entry.is_file() and entry.name.endswith(".py"):
            yield entry.name,entry.path
        elif entry.is_dir():
            yield from get_py_files(entry.path)
            
 #Function to print Python Files
def print_py_files(dir):
	for x,y in get_py_files(dir):
		print(x)
		
#Function to Copy Python Files to a Folder
def copy_py_files():
	for x,y in get_py_files(cwd):
		try:
			shutil.copy2(y,path)
		except shutil.SameFileError:
			pass

#Main Program Starts Here
if __name__ == "__main__":
	cwd = os.getcwd()
	print("The Current Working Directory is:" ,cwd,"\n")
	path = cwd+"/python_progs/"
	
	#make python_progs folder
	makefolder(path)
	
	#printing the python files presend in cwd and subdirs
	print("All the Python Files are: ")
	print_py_files(cwd)
	
	#copy all .py files to python_progs folder
	copy_py_files()
	print("The .py Files in ",path,"are: ")
	print_py_files(path)
