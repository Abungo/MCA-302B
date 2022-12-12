import os
import smtplib
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

req_libs = ["os","smtplib","shutil","email"]
#Function to Create a folder
def makefolder(path1):
	if not os.path.exists(path1):
		os.makedirs(path1)
	else:
	   	shutil.rmtree(path1)
	   	os.makedirs(path1)
	   	
#Function to build zip file from directory
def makezip(path2):
	try:
		shutil.make_archive(path2,'zip',path2)
		print("\nSuccessfully Made the Zip File\n")
	except shutil.ExecError:
		print("Error Making the Zip File")
	
#Function to Search all the .py files
def get_py_files(base_dir):
    for entry in os.scandir(base_dir):
        if entry.is_file() and entry.name.endswith(".py"):
            yield entry.name,entry.path
        elif entry.is_dir():
            yield from get_py_files(entry.path)
            
 #Function to print Python Files
def print_py_files():
	for x,y in get_py_files(cwd):
		print(x)
		
#Function to Copy Python Files to a Folder
def copy_py_files():
	for x,y in get_py_files(cwd):
		try:
			shutil.copy2(y,path)
		except shutil.SameFileError:
			pass

#A function to send mail
def send_mail(r_address,s_address,key,message):
	try:
		# creates SMTP session
		s = smtplib.SMTP('smtp.gmail.com', 587)
		# start TLS for security
		s.starttls()
		s.login("abungococ@gmail.com", key)
		# sending the mail
		s.sendmail(s_address, r_address, message.as_string())
		# terminating the session
		print("Email Sent Successfully to:",r_address)
	except smtplib.SMTPException :
		print("Failed to Send Email")
	s.quit()
#a function to compose mail
def compose_mail(r_add,s_add,sub,body):
	#start of composing mail
	msg = MIMEMultipart()
	Body = MIMEText(body)
	msg['Subject'] = sub
	msg['From'] = s_add
	msg['To'] = r_add
	msg['CC'] = ''
	msg['BCC'] = ''
	msg.attach(Body)
	part = MIMEBase("application", "octet-stream")
	part.set_payload(open(cwd + "/python_progs.zip", "rb").read())
	encoders.encode_base64(part)
	part.add_header("Content-Disposition", "attachment; filename=python_progs.zip")
	msg.attach(part)
	#end of composing mail
	return  msg

#Main Program Starts Here
if __name__ == "__main__":
	print("The Required Libraries are :",req_libs)
	cwd = os.getcwd()
	print("The Current Working Directory is:" ,cwd,"\n")
	path = cwd+"/python_progs/"
	
	sender_add = "abungococ@gmail.com"
	passkey = "tfjqqflstddpwfvk"
	subject = "Subject of the Email"
	mail_body= "Body of the Email"
	
	#make python_progs folder
	makefolder(path)
	#printing the python files presend in cwd and subdirs
	print("All the Python Files are: ")
	print_py_files()
	#copy all .py files to python_progs folder
	copy_py_files()
	#make a python_progs.zip file from python_progs directory
	makezip(path)
	#getting email id from user
	receiver_add = input("Enter an email address: ")
	#sending the mail
	msg = compose_mail(receiver_add,sender_add,subject,mail_body)
	send_mail(receiver_add,sender_add,passkey,msg)
