import Tkinter as tk
import tilone as tl
import tkFont as tf
import tkMessageBox as tb
import sys,subprocess,os
root,branch,noncommit,committed,statlab,stat,delete=None,None,'','',None,None,''
frame1,frame2=None,None

def gitstatus(event):
	global noncommit,committed,stat,delete,branch
	noncommit,committed,delete,branch='','','',''
	sta=subprocess.Popen(['git','status'],stdout=subprocess.PIPE).communicate()[0]
	flag=0
	branch=subprocess.Popen(['git','branch'],stdout=subprocess.PIPE).communicate()[0]
	for i in sta.split('\n'):
		if 'committed:' in i:
			flag=1
		if flag==1 and 'modified:' in i:
			committed=committed+'\n'+i
		if  'not staged for commit' in i:
			flag=2
		if flag==2 and 'modified:' in i:
			noncommit=noncommit+'\n'+i
		if 'deleted:' in i:
			delete=delete+'\n'+i
	stat.set("""[STATUS]\n\n<BRANCH>:%s\n<NOT 2B COMMITTED>: %s\n<2B COMMITTED>: %s\n<DELETED>: %s"""%(branch,noncommit,committed,delete))	
def creat_repo():
	er=os.system('python tilone.py')
	if er is not 0:
		tb.showerror("","Python tilone.py module not found")
def inpOpt():
	global frame2
	tk.Label(frame2,text='username',height=4,font=tf.Font(family='halvetica',size=15)).grid(rowspan=2,row=0,column=0)
	tk.Label(frame2,text="password",height=4,font=tf.Font(family='halvetica',size=15)).grid(rowspan=2,row=2,column=0)
	tk.Label(frame2,text="Repositoy",height=4,font=tf.Font(family='halvetica',size=15)).grid(rowspan=2,row=4,column=0)
	#tl.username=tk.Entery
def main():
	global root,statlab,stat,frame1,frame2
	root=tk.Tk()
	root.geometry('1000x700')
	frame1=tk.Frame(root,width=400,height=800)
	frame1.grid(row=0,column=0)
	tk.Frame(root,width=50,height=600).grid(row=0,column=1)
	frame2=tk.Frame(root,width=400,height=800)
	frame2.grid(row=0,column=2)
	logo=tk.PhotoImage(file='images/load.gif')
	tk.Label(frame1,image=logo).grid(column=1,stick='n')
	stat=tk.StringVar()
	stat.set('')	
	gitstatus('')
	tk.Label(frame1,text='').grid(column=0)
	tk.Label(frame1,text='').grid(column=0)
	tk.Label(frame1,text='').grid(column=0)
	tk.Label(frame1,text='').grid(column=0)
	statlab=tk.Label(frame1,textvariable=stat,width=36,height=20,relief='raised')
	statlab.grid(rowspan=4,columnspan=4,stick='w')
	statlab.bind('<Enter>',gitstatus)
	inpOpt()	
	root.mainloop()
main()
