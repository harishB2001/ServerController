import os
from datetime import datetime

def startMySQL():
	now = datetime.now()
	root.destroy()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	os.system('cmd /k "python startMySQL80.py"')
	print("Mysql server started  "+str(dt_string))
	exit()

def stopMySQL():
	now = datetime.now()
	root.destroy()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	os.system('cmd /k "python stopMySQL80.py"')
	print("Mysql server Stopped  "+str(dt_string))		
	exit()

def startMongoDB():
	now = datetime.now()
	root.destroy()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	os.system('cmd /k "python startMongoDB.py"')
	print("MongoDB server started  "+str(dt_string))
	exit()

def stopMongoDB():
	now = datetime.now()
	root.destroy()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	os.system('cmd /k "python stopMongoDB.py"')
	print("MongoDB server Stopped  "+str(dt_string))		
	exit()

from tkinter import *
root = Tk()
root.title("Server Controlle ")
root.geometry('200x50')

btn = Button(root, text = "Start MySQL" ,fg = "red", command=startMySQL)
btn.grid(column=1, row=1)


btn1 = Button(root, text = "Stop MySQL" ,fg = "red", command=stopMySQL)
btn1.grid(column=3, row=1)

btn3 = Button(root, text = "Start MongoDB" ,fg = "red", command=startMongoDB)
btn3.grid(column=1, row=2)


btn4 = Button(root, text = "Stop MongoDB" ,fg = "red", command=stopMongoDB)
btn4.grid(column=3, row=2)
root.mainloop()