import Tkinter as tk
import tilone as tl
import tkMessageBox as tb
import sys,subprocess,os
root,branch,noncommit,committed,statlab,stat,delete=None,None,'','',None,None,''
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
	stat.set("""[STATUS]\n\n<BRANCH>:%s \n<NON-COMMITTED>: %s\n<COMMITTED>: %s\n<DELETED>: %s"""%(branch,noncommit,committed,delete))	
def creat_repo():
	er=os.system('python tilone.py')
	if er is not 0:
		tb.showerror("","Python tilone.py module not found")
def main():
	global root,statlab,stat
	root=tk.Tk()
	root.geometry('700x500')
	logo=tk.PhotoImage(file='images/load.gif')
	tl.sepretor(0,0)
	tk.Label(root,image=logo).grid(column=1)
	tl.sepretor(1,0)
	stat=tk.StringVar()
	stat.set('')	
	gitstatus('')
	statlab=tk.Label(root,textvariable=stat,width=36,height=20,relief='raised')
	statlab.grid(rowspan=3,columnspan=3)
	statlab.bind('<Enter>',gitstatus)
	root.mainloop()
main()
