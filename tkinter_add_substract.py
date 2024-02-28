from tkinter import*

currentsum=0

def addition():
   global currentsum # New
   currentsum+=float(e1.get()) # Fix
   #e1.insert(INSERT,str(currentsum))
   l2['text'] = str(currentsum) # Change

def subtraction():
   global currentsum # New
   currentsum=currentsum-float(e1.get())
   #e1.insert(INSERT,str(currentsum))
   l2['text'] = str(currentsum) # Change

def reset():
   global currentsum # New
   currentsum=0
   #e1.insert(INSERT,str(currentsum))
   l2['text'] = str(currentsum) # Change
window=Tk()

l1=Label(window,text="current sum:")
l1.grid(row=0, column=0)
l2=Label(window,text=str(currentsum))
l2.grid(row=0,column=1)

e1=Entry(window)
e1.grid(row=1,column=0)


b1=Button(window,text="ADD(+)",command=addition)
b2=Button(window,text="SUBTRACT(-)",command=subtraction)
b3=Button(window,text="RESET",command=reset)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)

window.mainloop()