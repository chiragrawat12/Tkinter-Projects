from tkinter import *

root = Tk()

root.geometry("480x360")

def submitentry():
    if name.get() and emailid.get() and phone.get():    
        with open("My_First_Small_Projet/form.txt","a") as file:
            file.write("Name = "+name.get() + "\nEmail Id = " + emailid.get()+ "\nPhone No. = "+
            phone.get() + "\n\n")

username = Label(root, text = "Name:" )
useremail = Label(root, text = "Email Id:" )
phoneno = Label(root, text = "Phone No.:" )
username.grid()
useremail.grid(row =1)
phoneno.grid(row =2)


name = StringVar()
emailid = StringVar()
phone = StringVar()


nameentry = Entry(root, textvariable= name)
emailidentry = Entry(root, textvariable = emailid)
phonentry = Entry(root, textvariable = phone)

nameentry.grid(row= 0,column=1)
emailidentry.grid(row =1,column=1)
phonentry.grid(row = 2, column =1)

submit = Button(root,text = "Submit" , command = submitentry)
submit.grid(column = 1)

root.mainloop()