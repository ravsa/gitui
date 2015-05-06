import Tkinter as tk
import tilone as tl
import tkFont as tf
import tkMessageBox as tb
import sys,subprocess,os
root,branch,noncommit,committed,statlab,stat,delete=None,None,'','',None,None,''
frame1,frame2,frame3,commit=None,None,None,None
username,passwd,reponame='','',''
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
def check():
	global username,passwd
	def warn(strng):
		tb.showerror('error',strng)
	if username is '':
		warn("username field is empty")
		return 1
	if passwd is '':
		warn('password field is empty')
		return 1
	return 0
def create_repo():
	er=os.system('python tilone.py')
	if er is not 0:
		tb.showerror("","Python tilone.py module not found")
def cmt():
	global commit
	new=tk.Tk()			
	gk=tk.Text(new,width=35,height=10)
	gk.pack()
	def com():
		commit=gk.get(0.0,'end')
		commit='git '+'commit -m '+'"'+commit[:-1]+'"'
		err=os.system(commit)
		if err:
			tb.showinfo('success','Successfully commited !')
		else:
			tb.showerror('failed','Failed to commit!')
	tk.Button(new,text='  DONE  ',command=com).pack()
def add():
	os.system('git add *')
	gitstatus('')
def inpOpt():
	global frame2,frame3,username,passwd,reponame
	tk.Label(frame2,text='username',height=3,font=tf.Font(family='halvetica',size=15)).grid(rowspan=2,row=0,column=0)
	tk.Label(frame2,text="password",height=3,font=tf.Font(family='halvetica',size=15)).grid(rowspan=2,row=2,column=0)
	tk.Label(frame2,text="Repositoy",height=3,font=tf.Font(family='halvetica',size=15)).grid(rowspan=2,row=4,column=0)
	use=tk.Entry(frame2)
	use.grid(row=0,column=1,stick='s')
	pwd=tk.Entry(frame2)
	pwd.grid(row=2,column=1,stick='s')
	renme=tk.Entry(frame2,foreground='darkgreen')
	renme.grid(row=4,column=1,stick='s')
	renme.insert(0,tl.currentDir())
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='NewRepo',command=create_repo,width=10,height=2).grid(row=0,column=0,stick='n')
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='  Add  ',command=add,width=10,height=2).grid(row=1,column=0,stick='n')
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='Commit',command=cmt,width=10,height=2).grid(row=2,column=0,stick='n')
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='Push',command=cmt,width=10,height=2).grid(row=3,column=0,stick='n')
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='Pull',command=cmt,width=10,height=2).grid(row=4,column=0,stick='n')
def action():
	pass		
def main():
	global root,statlab,stat,frame1,frame2,frame3
	root=tk.Tk()
	root.geometry('1000x700')
	frame1=tk.Frame(root,width=300,height=800)
	frame1.grid(row=0,column=0)
	tk.Frame(root,width=50,height=600).grid(row=0,column=1)
	frame2=tk.Frame(root,width=350,height=800)
	frame2.grid(row=0,column=2)
	tk.Frame(root,width=50,height=600).grid(row=0,column=3)
	frame3=tk.Frame(root,width=250,height=700)
	frame3.grid(row=0,column=4)
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
