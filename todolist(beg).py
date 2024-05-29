import tkinter as tk
from tkinter import ttk



def tab1task():
    data = entry1.get()
    if data.strip():
        with open("datas.txt","a") as file:
            print("/n" + data)
            listbox1.insert(tk.END,data)
            entry1.delete(0, tk.END)


def tab2task():
    data1 = text1.get("1.0", tk.END)

    if data1.strip() :
        with open("datass.txt","a") as file:
            print('/n' + data1)
            listbox2.insert(tk.END,data1)
            text1.delete("1.0", tk.END)


window = tk.Tk()
window.geometry("720x720")
Notebook = ttk.Notebook(window)
Tab1 = ttk.Frame(Notebook)
Tab2 = ttk.Frame(Notebook)

Notebook.add(Tab1,text="TODOLIST")
Notebook.add(Tab2,text="NOTES")
Notebook.pack(expand=True,fill="both")

entry1 = tk.Entry(Tab1,
                font=("Raleway",17),
                bg="WHITE",
                fg="red"
              
)
entry1.pack()






tk.Button(Tab1,
                    text="ADD",  command=tab1task,
).pack(side="top"),


listbox1 = tk.Listbox(Tab1,height=80,width=100,bg="BLACK",fg="red",font=("time new roman",15))
listbox1.pack(padx=5,pady=5)


menubar = tk.Menu(Tab1,)
filemenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit", command=window.quit) 
window.config(menu=menubar)


helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Share")
helpmenu.add_command(label="Report")
helpmenu.add_command(label="Problem")
menubar.add_cascade(label="Help", menu=helpmenu)
window.config(menu=menubar)



entry2 = tk.Entry(Tab2,font=("Raleway",17),
                bg="white",
                fg="red").pack()


tk.Button(Tab2,
                    text="ADD NOTE",  command=tab2task,
).pack(side="top"),


text1 = tk.Text(Tab2,
                font=("Raleway",15),
                bg="white",
                fg="red",
                height=15,
                width=50).pack()




listbox2 = tk.Listbox(Tab2,height=8,width=30,bg="BLACK",fg="red",font=("time new roman",10))
listbox2.pack(padx=5,pady=5)

                










window.mainloop()





