import Tkinter as tk
import tilone as tl
import tkMessageBox as tb
import sys,subprocess
root,branch,noncommit,committed,statlab1,statlab2,branchlab=None,None,None,None,None,None,None
def gitstatus():
	global noncommit,committed
	sta=subprocess.Popen(['git','status'],stdout=subprocess.PIPE).communicate()[0]
	flag=0
	for i in sta.split('\n'):
		if 'up-to-date' in i:
			print list(i.split())[-1]
		if 'committed:' in i:
			flag=1
		if flag==1 and 'modified:' in i:
			committed=i
		if  'not staged for commit' in i:
			flag=2
		if flag==2 and 'modified:' in i:
			noncommit=i
def main():
	global root
	root=tk.Tk()
	root.geometry('700x500')
	logo=tk.PhotoImage(file='images/load.gif')
	tk.Label(root,image=logo).grid()
	tk.Label(root,text='STATUS').grid()
	tk
	gitstatus()
	root.mainloop()
main()
