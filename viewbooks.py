from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "rash.1234"
mydatabase="db"

con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"


def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font = ('Courier',15))

    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    Label(labelFrame, text='Bid',bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text='Title',bg='black',fg='white').place(relx=0.20,rely=0.1)
    Label(labelFrame, text='Author',bg='black',fg='white').place(relx=0.40,rely=0.1)
    Label(labelFrame, text='Status',bg='black',fg='white').place(relx=0.60,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()


        for i in cur:
            Label(labelFrame,text=i[0] ,bg='black', fg='white').place(relx=0.07,rely=y)
            Label(labelFrame,text=i[1] ,bg='black', fg='white').place(relx=0.20,rely=y)
            Label(labelFrame,text=i[2] ,bg='black', fg='white').place(relx=0.40,rely=y)
            Label(labelFrame,text=i[3] ,bg='black', fg='white').place(relx=0.60,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch entries from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
