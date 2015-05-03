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
frame,frame1,frame2,frame3=None,None,None,None
#child='curl '+'-u '+"'"+sys.argv[1]+"'"+':'+"'"+sys.argv[2]+"'"+' https://api.github.com/user/repos '+'-d '+'"'+'{'+'\\"name\\"'+':'+'\\"'+sys.argv[3]+'\\"'+'}'+'"'
#cho=call(child,shell=True,stderr=PIPE)
#if cho:
#	print "Error in communication"
def init():
	global root,helv
	root.geometry('800x500')
	helv=tkFont.Font(family='helvetica',size=15)
def dest():
	bg.destroy()
def entryBox():

	global userbox,passbox,repobox,root,helv
	frame=tk.Frame(root,width=300,height=150)
	frame.pack(side='top')
	title=tk.Label(frame,text='Creating a New Repository',font=tkFont.Font(family='helvetica',size=22))
	title.pack()
	seprator=tk.Label(frame,text='',height=2)
	seprator.pack()
	frame1=tk.Frame(frame,width=150,height=80)
	frame1.pack(side='left')
	usrname=tk.Label(frame1,text='Username: ',font=helv)
	usrname.pack()
	passlab=tk.Label(frame1,text='Password: ',font=helv)
	passlab.pack()
	repolab=tk.Label(frame1,text='Repository: ',font=helv)
	repolab.pack()
	frame2=tk.Frame(frame,width=150,height=80)
	frame2.pack()
	userbox=tk.Entry(frame2,width=30,font=tkFont.Font(family='helvetica',size=13))
	userbox.pack()
	passbox=tk.Entry(frame2,width=30,font=tkFont.Font(family='helvetica',size=13),show='*')
	passbox.pack()
	repobox=tk.Entry(frame2,width=30,font=tkFont.Font(family='helvetica',size=13))
	repobox.pack()
def getValues():
	global username,userbox,reponame,repobox,passbox,passwd
	passwd=passbox.get()
	username=userbox.get()
	reponame=repobox.get()
	print username,passwd,reponame
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
bg.after(1500,dest)
root.after(1500,entryBox)
submit=tk.Button(root,text='SUBMIT',command=getValues)
submit.pack(side='left')
reset=tk.Button(root,text='RESET',command=reset)
reset.pack(side='right')
root.mainloop()

