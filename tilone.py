from subprocess import *
import time
import tkFont
import Tkinter as tk
username=''
passwd=''
reponame=''
userbox=None
passbox=None
repobox=None
root=None
helv=None
reset=None
root,status=None,None
def process():
	global status

	if username is '':
		status.set("Username field is empty")
	elif passwd is '':
		status.set("Password field is empty")
	elif reponame is '':
		status.set("Reponame field is empty")
	else:
		status.set("Processing")
		child='curl '+'-u '+"'"+username+"'"+':'+"'"+passwd+"'"+' https://api.github.com/user/repos '+'-d '+'"'+'{'+'\\"name\\"'+':'+'\\"'+reponame+'\\"'+'}'+'"'
		cho,chr=Popen(child,shell=True,stdout=PIPE).communicate()
		if len(cho)<2:
			status.set("connection error")
		elif len(cho)<110 and len(cho)>80:
			status.set("username & password not matched !")
		elif len(cho)<400 and len(cho)>160:
			status.set("repository already exists")
		elif len(cho)>2900:
			status.set("repository created Successfully!\n url:https://github.com/{}/{}.git".format(username,reponame))
def init():
	global root,helv
	root.geometry('800x400')
	helv=tkFont.Font(family='helvetica',size=15)
def dest():
	bg.destroy()
def sepretor(i,j):
	tk.Label(root,text='').grid(row=i,column=j)
def entryBox():

	global userbox,passbox,repobox,root,helv
	
	title=tk.Label(root,text='Creating a New Repository',font=tkFont.Font(family='helvetica',size=22))
	title.grid(rowspan=2,stick='e',row=0,column=2)
	usrname=tk.Label(root,text='Username: ',font=helv)
	usrname.grid(rowspan=2,row=2,column=2)
	passlab=tk.Label(root,text='Password: ',font=helv)
	passlab.grid(rowspan=2,row=4,column=2)
	repolab=tk.Label(root,text='Repository: ',font=helv)
	repolab.grid(rowspan=2,row=6,column=2)
	userbox=tk.Entry(root,width=30,font=tkFont.Font(family='helvetica',size=13))
	userbox.grid(rowspan=2,row=2,column=3,stick='w')
	passbox=tk.Entry(root,width=30,font=tkFont.Font(family='helvetica',size=13),show='*')
	passbox.grid(rowspan=2,row=4,column=3)
	repobox=tk.Entry(root,width=30,font=tkFont.Font(family='helvetica',size=13))
	repobox.grid(rowspan=2,row=6,column=3)
def getValues():
	global username,userbox,reponame,repobox,passbox,passwd
	passwd=passbox.get()
	username=userbox.get()
	reponame=repobox.get()
	print username,passwd,reponame
	process()
def reset():
	global userbox,passbox,repobox
	passbox.delete(0,'end')
	repobox.delete(0,'end')
	userbox.delete(0,'end')
	status.set("")
def main():
	global root,status,reset
	root=tk.Tk()
	init()
	logo=tk.PhotoImage(file='images/load.gif')
	tk.Label(root,image=logo).grid(rowspan=3,columnspan=2,row=0,column=0,stick='e')
	entryBox()
	sepretor(8,1)
	sepretor(9,1)
	submit=tk.Button(root,text='SUBMIT',command=getValues,bg='darkgrey')
	submit.grid(row=10,column=2,stick='e'+'s')
	reset=tk.Button(root,text='RESET',command=reset,bg='darkgrey')
	reset.grid(row=10,column=3,stick='w'+'s')
	sepretor(11,1)
	status=tk.StringVar()
	status.set('')
	statlab=tk.Label(root,textvariable=status).grid(rowspan=5,columnspan=3,row=12,column=0)
	root.mainloop()
if __name__=="__main__":
	main()
