from tkinter import *
import tkinter.messagebox
import sqlite3

#class for front-end user interface
class Food:
    def __init__(self,root):

        #create database object
        f=Database()
        f.conn()
        self.root=root
        self.root.title("Resturent Management System")
        self.root.geometry('1325x690') 
        self.root.config(bg="powderblue")
        #_________create variables_____________
        fId=StringVar()
        fName=StringVar()
        fPrice=StringVar()
        fQuantity=StringVar()
        tableNo=StringVar()

        def close():
          print("Close")
          close=tkinter.messagebox.askyesno("Resturent Management System","Want to close system...???")
          if close>0:
            root.destroy()
            print("Food close method close")
            return
#_______________function for clear the values
        def clear():
          print("Reset the values")
          self.labelentryfId.delete(0,END)
          self.labelentryfName.delete(0,END)
          self.labelentryfPrice.delete(0,END)
          self.labelentryfQuantity.delete(0,END)
          self.labelentrytableNo.delete(0,END)
          print("Reset the values\n")
#_________________function for insert the values__
        def insert():
          if (len(fId.get())!=0):
            f.insert(fId.get(),fName.get(),fPrice.get(),fQuantity.get(),tableNo.get())
            foodlist.delete(0,END)
            foodlist.insert(END,fId.get(),fName.get(),fPrice.get(),fQuantity.get(),tableNo.get()) 
            showfoodlist() #calling foodlist after inserting  
          else:
            tkinter.messagebox.askyesno("Resturent Management System","Enter foods item..!!?")
#______show food list_________________
        def showfoodlist():
          foodlist.delete(0,END)
          for row in f.view():
            foodlist.insert(END,row,str ( ""))
          print("Showing the list of foods")

#___________food records from scroll bar_______________
        def foodrec(event):
          global fd
          select=foodlist.curselection()[0]
          fd=foodlist.get(select)
          self.labelentryfId.delete(0,END)
          self.labelentryfId.insert(END,fd[0])
          self.labelentryfName.delete(0,END)
          self.labelentryfName.insert(END,fd[1])
          self.labelentryfPrice.delete(0,END)
          self.labelentryfPrice.insert(END,fd[2])
          self.labelentryfQuantity.delete(0,END)
          self.labelentryfQuantity.insert(END,fd[3])
          self.labelentrytableNo.delete(0,END)
          self.labelentrytableNo.insert(END,fd[4])
          print("Food record method finish")

#_________delete record function______________
        def delete():
          if(len(fId.get())!=0):
            f.delete(fd[0])
            clear()
            showfoodlist
            print("Record deleted")

#______________search method_________
        def search():
          print("database search ")
          foodlist.delete(0,END)
          for row in f.search(fId.get(),fName.get(),fPrice.get(),fQuantity.get(),tableNo.get()):
            foodlist.insert(END,row,str(""))

#______________update method_____________
        def update():
           if(len(fId.get())!=0):
            print("fd[0]",fd[f])
            f.delete(fd[0])
           if(len(fId.get())!=0):
              f.insert(fId.get(),fName.get(),fPrice.get(),fQuantity.get(),tableNo.get())
              foodlist.delete(0,END)
              foodlist.insert(END,(fId.get(),fName.get(),fPrice.get(),fQuantity.get(),tableNo.get()))







        '''________Frame____________'''
        mainFrame=Frame(self.root,bg='lightblue')
        mainFrame.grid()
        headFrame=Frame(mainFrame,bd=1,padx=300,pady=10,bg='YellowGreen',relief=RIDGE)
        headFrame.pack(side=TOP)
        self.Ititle=Label(headFrame,font=('arial',40,'bold'),fg='black',text='Resturent Management System')
        self.Ititle.grid()
        bottomFrame=Frame(mainFrame,bd=3,padx=50,pady=30,width=1390,height=80,bg='YellowGreen',relief=RIDGE)
        bottomFrame.pack(side=BOTTOM)

        bodyFrame=Frame(mainFrame,bd=2,padx=50,pady=30,width=1390,height=500,relief=RIDGE,bg="white")
        bodyFrame.pack(side=BOTTOM)

        leftFrame=LabelFrame(bodyFrame,width=800,height=500,padx=50,pady=30,text="Food Item Details : ",font=('arial',15,'bold'),relief=RIDGE,bg='LightGray')
        leftFrame.pack(side=LEFT)

        rightFrame=LabelFrame(bodyFrame,width=300,height=380,text="Food Item Details : ",font=('arial',15,'bold'),relief=RIDGE,bg='LightGray')
        rightFrame.pack(side=RIGHT)

        #___________widgets___________

        #__________label_________1
        self.labelfId=Label(leftFrame,font=('arial',12,'bold'),text='Food Id',padx=2,bg='white',fg='green')
        self.labelfId.grid(row=0,column=0,sticky=W)
        #___________entry_______
        self.labelentryfId=Entry(leftFrame,font=('arial',20,'bold'),textvariable=fId,width=40)
        self.labelentryfId.grid(row=0,column=1,sticky=W)
         #__________label_________2
        self.labelfName=Label(leftFrame,font=('arial',12,'bold'),text='Food Name',padx=2,bg='white',fg='green')
        self.labelfName.grid(row=1,column=0,sticky=W)
        #___________entry_______
        self.labelentryfName=Entry(leftFrame,font=('arial',20,'bold'),textvariable=fName,width=40)
        self.labelentryfName.grid(row=1,column=1,sticky=W)
          #__________label_________3
        self.labelfPrice=Label(leftFrame,font=('arial',12,'bold'),text='Food Price',padx=2,bg='white',fg='green')
        self.labelfPrice.grid(row=2,column=0,sticky=W)
        #___________entry_______
        self.labelentryfPrice=Entry(leftFrame,font=('arial',20,'bold'),textvariable=fPrice,width=40)
        self.labelentryfPrice.grid(row=2,column=1,sticky=W)
         #__________label_________4
        self.labelfQuantity=Label(leftFrame,font=('arial',12,'bold'),text='Food Quantity',padx=2,bg='white',fg='green')
        self.labelfQuantity.grid(row=3,column=0,sticky=W)
        #___________entry_______
        self.labelentryfQuantity=Entry(leftFrame,font=('arial',20,'bold'),textvariable=fQuantity,width=40)
        self.labelentryfQuantity.grid(row=3,column=1,sticky=W)
        #__________label_________5
        self.labeltableNo=Label(leftFrame,font=('arial',12,'bold'),text='Table No',padx=2,bg='white',fg='green')
        self.labeltableNo.grid(row=4,column=0,sticky=W)
        #___________entry_______
        self.labelentrytableNo=Entry(leftFrame,font=('arial',20,'bold'),textvariable=tableNo,width=40)
        self.labelentrytableNo.grid(row=4,column=1,sticky=W)
        #___________scroll bar right frame___________
        scroll=Scrollbar(rightFrame)
        scroll.grid(row=0,column=1,sticky='ns')
        foodlist=Listbox(rightFrame,width=30,height=15,font=('arial',12,'bold'),yscrollcommand=scroll.set)

        #_____called function of food record
        foodlist.bind('<<ListboxSelect>>',foodrec)
        foodlist.grid(row=0,column=0,padx=8)
        scroll.config(command=foodlist.yview)
        
        #______________________buttons__________________
        self.button=Button(bottomFrame,text='Save',font=('arial',12,'bold'),width=9,height=2,bd=3,command=insert)
        self.button.grid(row=0,column=0)
        self.button=Button(bottomFrame,text='Reset',font=('arial',12,'bold'),width=9,height=2,bd=3,command=clear)
        self.button.grid(row=0,column=1)
        self.button=Button(bottomFrame,text='Delete',font=('arial',12,'bold'),width=9,height=2,bd=3,command=delete)
        self.button.grid(row=0,column=2)
        self.button=Button(bottomFrame,text='Search',font=('arial',12,'bold'),width=9,height=2,bd=3,command=search)
        self.button.grid(row=0,column=3)
        self.button=Button(bottomFrame,text='View',font=('arial',12,'bold'),width=9,height=2,bd=3,command= showfoodlist)
        self.button.grid(row=0,column=4)
        self.button=Button(bottomFrame,text='Update',font=('arial',12,'bold'),width=9,height=2,bd=3,command=update)
        self.button.grid(row=0,column=5)
        self.button=Button(bottomFrame,text='Close',font=('arial',12,'bold'),width=9,height=2,bd=3,command=close)
        self.button.grid(row=0,column=6)


        #____________Database______________


class Database():
    def conn(self):
      print("Database Connection created")
      con=sqlite3.connect("resturent.db")
      cur=con.cursor()
      query="create table if not exists resturent (fId integer primary key,fName text,fPrice text,fQuantity text,tableNo text)"
      cur.execute(query)
      con.commit()
      con.close()
      print("Database Connection Finished")
    
    def insert(self,fId,fName,fPrice,fQuantity,tableNo):
      print("Database Insert Method")
      con=sqlite3.connect("resturent.db")
      cur=con.cursor()
      query="insert into resturent values (?,?,?,?,?)"
      cur.execute(query,(fId,fName,fPrice,fQuantity,tableNo))
      con.commit()
      con.close()
      print("Database Insert method done \n")
    def view(self):
      print("Show method called")
      con=sqlite3.connect("resturent.db")
      cur=con.cursor()
      query="select * from resturent"
      cur.execute(query)
      rows=cur.fetchall()
      con.close()
      print("View method done")
      return rows
    
    def delete(self,fId):
      print("Delete method called")
      con=sqlite3.connect("resturent.db")
      cur=con.cursor()
      cur.execute("delete from resturent where fId=?",(fId,))
      con.commit()
      con.close()
      print(fId,"deleted from database\n")
    
    def search(self,fId="",fName="",fPrice="",fQuantity="",tableNo=""):
      print("Search method called")
      con=sqlite3.connect("resturent.db")
      cur=con.cursor()
      cur.execute("select * from resturent where fId=? or fName=? or fPrice=? or fQuantity=? or tableNo=?",(fId,fName,fPrice,fQuantity,tableNo))
      row=cur.fetchall()
      con.close()
      print(fId,"Search method done")
      return row

    def update(self,fId="",fName="",fPrice="",fQuantity="",tableNo=""):
      print("Update method called")
      con=sqlite3.connect("resturent.db")
      cur=con.cursor()
      cur.execute("update  resturent set fId=? or fName=? or fPrice=? or fQuantity=? or tableNo=? where fId=?",(fId,fName,fPrice,fQuantity,tableNo) )
      con.commit()
      con.close()
      print(fId,"Updated")






if __name__ =='__main__':
    root=Tk()
    app=Food(root)
    root.mainloop()
