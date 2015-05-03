from Tkinter import *
def menter(event):
	button=event.widget
	button.config(text="click me")
def mexit(event):
	button=event.widget
	button.config(text='logon')
def main():
	global root
	root=Tk()
	b=Label(root,text='logo')
	b.bind("<Enter>",menter)
	b.bind("<Leave>",mexit)
	b.pack()
	root.mainloop()
main()

