from tkinter import *
from database import Database
from tkinter import messagebox

class NLPApp:

  def __init__(self):

    self.dbo = Database()
    
    self.root = Tk()
    self.root.title("NLP-App")
    self.root.geometry("350x600")
    self.root.configure(bg="#B34C5B")

    self.login_gui()
    self.root.mainloop()

  def login_gui(self):

    self.clear()


    heading = Label(self.root , text='NLPApp' , bg='#B34C5B', fg='white')
    heading.pack( pady= (50 , 50))
    heading.configure(font=("verdana" , 24 , 'bold'))

    label1 = Label(self.root, text=" Enter Email" , bg= '#B34C5B' , fg= 'white')
    label1.pack(pady=(10, 10))

    self.email_input = Entry(self.root, width=40)
    self.email_input.pack(pady=(5, 10) , ipady=4)

    label2 = Label(self.root, text=" Enter Password" , bg= '#B34C5B' , fg= 'white')
    label2.pack(pady=(10, 10))

    self.pass_input = Entry(self.root, width=40 , show="*")
    self.pass_input.pack(pady=(5, 10) , ipady=4)

    login_btn = Button(self.root , text='Login Now' , width=20 ,height= 1 )
    login_btn.pack( pady=(20 , 10) )

    redirect_btn = Button(self.root , text='register now' , width=15 , command= self.register_gui)
    redirect_btn.pack( pady=(20 , 10) )

  def register_gui(self):
    self.clear()

    heading = Label(self.root , text='NLPApp' , bg='#B34C5B', fg='white')
    heading.pack( pady= (50 , 50))
    heading.configure(font=("verdana" , 24 , 'bold'))

    label0 = Label(self.root, text=" Enter name" , bg= '#B34C5B' , fg= 'white')
    label0.pack(pady=(10, 10))

    self.name_input = Entry(self.root, width=40)
    self.name_input.pack(pady=(5, 10) , ipady=4)

    label1 = Label(self.root, text=" Enter Email" , bg= '#B34C5B' , fg= 'white')
    label1.pack(pady=(10, 10))

    self.email_input = Entry(self.root, width=40)
    self.email_input.pack(pady=(5, 10) , ipady=4)

    label2 = Label(self.root, text=" Enter Password" , bg= '#B34C5B' , fg= 'white')
    label2.pack(pady=(10, 10))

    self.pass_input = Entry(self.root, width=40 , show="*")
    self.pass_input.pack(pady=(5, 10) , ipady=4)

    register_btn = Button(self.root , text='Register Now' , width=20 ,height= 1 )
    register_btn.pack( pady=(20 , 10) )

    redirect_btn = Button(self.root , text='Already a member' , width=15 , command= self.login_gui)
    redirect_btn.pack( pady=(20 , 10) )


  def clear(self):
    #clear the existing gui 
    for i in self.root.pack_slaves():
      print(i.destroy())
    
  def perform_registration(self):
    name = self.name_input.get()
    email = self.email_input.get()
    password = self.pass_input.get()

    response = self.dbo.add_data(name , email , password)

    if response:
      messagebox.showinfo('succes' , 'reg successful')

    else:
      messagebox.showerror('Error' ,'email exist ')

nlp = NLPApp()