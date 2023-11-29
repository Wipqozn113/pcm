import tkinter as tk
import db
my_w = tk.Tk()
#my_w.geometry("400x250")  # Size of the window 
ref=[] # to store the references 

dbhandler = db.DatabaseHandler()

def create_entry(add_button, save_button, number_of_inputs=1, name="", sheet=""):
    n = len(ref)
    for j in range(n, number_of_inputs+n):
        l1=tk.Label(my_w,text='Name: ',font=20,fg='blue')
        l1.grid(row=j,column=0,padx=3)
        e1 = tk.Entry(my_w, font=20,bg='lightyellow') 
        e1.insert(0, name)
        e1.grid(row=j, column=1,padx=10,pady=3) 

        l2=tk.Label(my_w,text='Sheet: ',font=20,fg='blue')
        l2.grid(row=j,column=2,padx=3)
        e2 = tk.Entry(my_w, font=20,bg='lightyellow') 
        e2.insert(0, sheet)
        e2.grid(row=j, column=3,padx=10,pady=3) 

        ref.append((e1, e2)) # store references     
    add_button.grid(row=j+1, column=0)
    save_button.grid(row=j+1, column=1)

def save_entries():
    for name, sheet in ref:
        dbhandler.CreatePlayer(name.get(), sheet.get())

save_button = tk.Button(my_w,text='Save', bg='lightgreen', command=lambda: save_entries(), font=18)
add=tk.Button(my_w,text='Add', bg='lightgreen', command=lambda: create_entry(add, save_button, 1), font=18)
players = dbhandler.GetPlayers()
for player in players:
    create_entry(add, save_button, 1, player.name, player.sheet)

create_entry(add, save_button, 1)
my_w.mainloop()  # Keep the window open