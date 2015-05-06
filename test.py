#!/usr/bin/python
import Tkinter as tk
import pexpect 
import tilone as tl
import tkFont as tf
import pexpect
import tkMessageBox as tb
import sys,subprocess,os
root,branch,noncommit,committed,statlab,stat,delete=None,None,'','',None,None,''
frame1,frame2,frame3,commit=None,None,None,None
use,pwd,renme=None,None,None
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
	global username,passwd,reponame,use,pwd,renme
	passwd=pwd.get()
	username=use.get()   
	reponame=renme.get() 	
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
	done=None
	new=tk.Tk()			
	gk=tk.Text(new,width=35,height=10)
	gk.pack()
	def com():
		commit=gk.get(0.0,'end')
		commit='git '+'commit -m '+'"'+commit[:-1]+'"'
		err=os.system(commit)
		if err==0:
			tb.showinfo('success','Successfully commited !')
			new.destroy()
		else:
			tb.showerror('failed','Failed to commit!')
			new.destroy()
	done=tk.Button(new,text='  DONE  ',command=com)
	done.pack()
def push():
	global username,passwd,reponame
	but=None
	branchDef='master'
	if check():
		pass
	else:
		new=tk.Tk()
		new.geometry('200x60')
		la=tk.Label(new,text="Branch*->",width=23,foreground='darkgreen')
		la.pack()
		gk=tk.Entry(new,width=25,fg='darkblue')
		gk.pack()
		gk.insert(0,branchDef)
		def don():
			branchDef=gk.get()
			gk.destroy()
			la.destroy()
			but.destroy()
			
			tk.Label(new,text='Processing...',).pack()
			cmd='git remote add origin https://github.com/'+username+'/'+reponame+'.git' 
			
			
			git='git push -u origin '+branchDef
			child=pexpect.spawn(git)
			child.expect("Username")
			child.sendline(username)
			child.expect("Password")
			child.sendline(passwd)
			child.expect("Delta")
			new.destroy()
			tb.showinfo('',"repository successfully updated on remote server")
		but=tk.Button(new,text='DONE',width=23,bg='black',fg='white',command=don)
		but.pack()	
def init():
	ask=tb.askquestion('','Is it first time')	
	if ask == 'yes':
		main=tk.Tk()
		tk.Label(main,text='username').pack()
		name=tk.Entry(main)
		name.pack()
		tk.Label(main,text='  E-mail ').pack()
		email=tk.Entry(main)
		email.pack()
		def apak():
			nm=name.get()
			el=email.get()
			nm='git config --global user.name '+'"'+nm+'"'
			el='git config --global user.email '+'"'+el+'"'
			os.system(nm)
			os.system(el)
			os.system('git init')
			main.destroy()
		tk.Button(main,text='DONE',command=apak).pack()
	else:
		os.system('git init')
		i=tb.showinfo('','Initialized')
def add():
	os.system('git add *')
	gitstatus('')
def inpOpt():
	global frame2,frame3,use,pwd,renme
	tk.Label(frame2,text='username',height=3,font=tf.Font(family='halvetica',size=15)).grid(rowspan=2,row=0,column=0)
	tk.Label(frame2,text="password",height=3,font=tf.Font(family='halvetica',size=15)).grid(rowspan=2,row=2,column=0)
	tk.Label(frame2,text="Repositoy",height=3,font=tf.Font(family='halvetica',size=15)).grid(rowspan=2,row=4,column=0)
	use=tk.Entry(frame2)
	use.grid(row=0,column=1,stick='s')
	pwd=tk.Entry(frame2,show='*')
	pwd.grid(row=2,column=1,stick='s')
	renme=tk.Entry(frame2,foreground='darkgreen')
	renme.grid(row=4,column=1,stick='s')
	renme.insert(0,tl.currentDir())
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='Init',command=init,width=10,height=2).grid(row=0,column=0,stick='n')

	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='NewRepo',command=create_repo,width=10,height=2).grid(row=1,column=0,stick='n')
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='  Add  ',command=add,width=10,height=2).grid(row=2,column=0,stick='n')
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='Commit',command=cmt,width=10,height=2).grid(row=3,column=0,stick='n')
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='Push',command=push,width=10,height=2).grid(row=4,column=0,stick='n')
	tk.Button(frame3,foreground='white',activebackground='blue',bg='black',text='Pull',width=10,height=2).grid(row=5,column=0,stick='n')
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
	add=subprocess.Popen('echo ~',shell=True,stdout=subprocess.PIPE).communicate()[0]
	add=add[:-1]+'/.gitui/images/load.gif'
	try:
		logo=tk.PhotoImage(file='images/load.gif')
	except Exception,e:
		logo=tk.PhotoImage(file=add)

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
