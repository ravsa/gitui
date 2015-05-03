from subprocess import *
import sys
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
root=None
def process():
	child='curl '+'-u '+"'"+username+"'"+':'+"'"+passwd+"'"+' https://api.github.com/user/repos '+'-d '+'"'+'{'+'\\"name\\"'+':'+'\\"'+reponame+'\\"'+'}'+'"'
	cho=call(child,shell=True,stderr=PIPE)
	if cho is not 0:
		print "Error in communication"
	
def init():
	global root,helv
	root.geometry('800x500')
	helv=tkFont.Font(family='helvetica',size=15)
def dest():
	bg.destroy()
def sepretor(i,j):
	tk.Label(root,text='').grid(row=i,column=j)
def entryBox():

	global userbox,passbox,repobox,root,helv
	title=tk.Label(root,text='Creating a New Repository',font=tkFont.Font(family='helvetica',size=22))
	title.grid(rowspan=2,stick='e',row=0,column=1)
	usrname=tk.Label(root,text='Username: ',font=helv)
	usrname.grid(rowspan=2,row=2,column=1)
	passlab=tk.Label(root,text='Password: ',font=helv)
	passlab.grid(rowspan=2,row=4,column=1)
	repolab=tk.Label(root,text='Repository: ',font=helv)
	repolab.grid(rowspan=2,row=6,column=1)
	userbox=tk.Entry(root,width=30,font=tkFont.Font(family='helvetica',size=13))
	userbox.grid(rowspan=2,row=2,column=2)
	passbox=tk.Entry(root,width=30,font=tkFont.Font(family='helvetica',size=13),show='*')
	passbox.grid(rowspan=2,row=4,column=2)
	repobox=tk.Entry(root,width=30,font=tkFont.Font(family='helvetica',size=13))
	repobox.grid(rowspan=2,row=6,column=2)
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
root=tk.Tk()
init()
start=tk.PhotoImage(file='images/logo.gif')
bg=tk.Label(root,image=start)
bg.place(x=0,y=0,relwidth=1,relheight=1)
bg.after(150,dest)
root.after(150,entryBox)
sepretor(8,1)
sepretor(9,1)
submit=tk.Button(root,text='SUBMIT',command=getValues)
submit.grid(row=10,column=1,stick='e'+'s')
reset=tk.Button(root,text='RESET',command=reset)
reset.grid(row=10,column=2,stick='w'+'s')
root.mainloop()

