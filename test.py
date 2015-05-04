import Tkinter as tk
import tilone as tl
import tkMessageBox as tb
import sys,subprocess,os
root,branch,noncommit,committed,statlab,stat,delete=None,None,'','',None,'',''
def gitstatus():
	global noncommit,committed,stat,delete,branch
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
	stat='BRANCH: %s \nNON-COMMITTED: %s\nCOMMITTED: %s\nDELETED: %s'%(branch,noncommit,committed,delete)
	print stat
def creat_repo():
	er=os.system('python tilone.py')
	if er is not 0:
		tb.showerror("","Python tilone.py module not found")
def main():
	global root,statlab
	root=tk.Tk()
	root.geometry('700x500')
	logo=tk.PhotoImage(file='images/load.gif')
	tk.Label(root,image=logo).grid(row=0)
	tl.sepretor(1,0)
	tk.Button(root,text='STATUS',command=creat_repo).grid(row=2)
	#statlab=StringVar()
		
	gitstatus()
	root.mainloop()
main()
