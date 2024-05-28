import tkinter as tk
from tkinter import IntVar

def options():
    print("Bread:", bread_var.get())
    print("Pastries:", pastries_var.get())
    print("Cakes:", cakes_var.get())
    print("Vanilla:", vanilla_var.get())
    print("Chocolate:", chocolate_var.get())
    print("Blackforest:", blackforest_var.get())
    print("Cream:", cream_var.get())

list_order = []
def inpuut():

    pass



def orders():
    
    if bread_var.get() == 1:
        print("You ordered bread")
    if pastries_var.get() == 2:
        print("You ordered pastries")
    if cakes_var.get() == 3:
        print("You ordered cakes")
    if vanilla_var.get() == 4:
        print("You ordered vanilla")
    if chocolate_var.get() == 5:
        print("You ordered chocolate")
    if blackforest_var.get() == 6:
        print("You ordered blackforest")
    if cream_var.get() == 7:
        print("You ordered cream")

def option1():
    name = entry_box1.get()
    print(f"Your name is {name}")
    phone = entry_box2.get()
    print(f"Your phone number is {phone}")
    address = entry_box3.get()
    print(f"Your phone number is {address}")



def payment_final():
    final = fo.get()
    print(f"Payment : {payment_options[final]}")



window = tk.Tk()
window.geometry("340x340")
window.title("Eveready")

icon = tk.PhotoImage(file="file_path/bakerylogo.png")
photo1 = tk.PhotoImage(file="file_path/baerypics3.png")
photo2 = tk.PhotoImage(file="file_path/bread.png")

label1 = tk.Label(window,
                  text="WELCOME TO EVEREADY BAKERY",
                  font=("Times New Roman", 14),
                  fg="green",
                  bg="#D2B48C",
                  bd=10,
                  image=photo1,
                  compound="bottom"
)


photo2 = tk.PhotoImage(file="file_path/bread.png")
label1.pack()


label3 = tk.Label(window,
                  text = ("Please fill in the information"),
                  font = ("times new roman",12))
label3.pack(anchor="center")
label4 = tk.Label(window,
                  text = ("Fullname"),
                  font = ("times new roman",12))
label4.pack(anchor="center")
entry_box1 = tk.Entry(window,
                    font = ("times new roman",13),
                    
                   
)   

entry_box1.pack()
label5 = tk.Label(window,
                  text = ("Phone NO"),
                  font = ("times new roman",12))
label5.pack(anchor="center")
entry_box2 = tk.Entry(window,
                    font = ("times new roman",13),
                    
                   
)   

entry_box2.pack()
label6 = tk.Label(window,
                  text = ("Address"),
                  font = ("times new roman",12))
label6.pack(anchor="center")

entry_box3 = tk.Entry(window,
                    font = ("times new roman",13),
                    
                   
)   

entry_box3.pack()
submit_button1 = tk.Button(window,
                        text = "Submit",
                        font = ("times new roman",10),
                        fg = "green",
                        pady=5,
                        command = option1)

submit_button1.pack(anchor="center")

# Define separate IntVar instances for each checkbox
label2 = tk.Label(window,
                  text="Here is the Menu",
                  font=("Times New Roman", 15)
)
label2.pack(anchor="w")
bread_var = tk.IntVar()
pastries_var = tk.IntVar()
cakes_var = tk.IntVar()
vanilla_var = tk.IntVar()
chocolate_var = tk.IntVar()
blackforest_var = tk.IntVar()
cream_var = tk.IntVar()


check_button1 = tk.Checkbutton(window, text="Bread", variable=bread_var,command=orders, onvalue=1, offvalue=0, bg="#D2B48C")
check_button2 = tk.Checkbutton(window, text="Pastries", variable=pastries_var,command=orders, onvalue=2, offvalue=0, bg="#D2B48C")
check_button3 = tk.Checkbutton(window, text="Cakes", variable=cakes_var,command=orders, onvalue=3, offvalue=0, bg="#D2B48C")
check_button4 = tk.Checkbutton(window, text="Vanilla", variable=vanilla_var,command=orders, onvalue=4, offvalue=0, bg="#D2B48C")
check_button5 = tk.Checkbutton(window, text="Chocolate", variable=chocolate_var,command=orders, onvalue=5, offvalue=0, bg="#D2B48C")
check_button6 = tk.Checkbutton(window, text="Blackforest", variable=blackforest_var,command=orders, onvalue=6, offvalue=0, bg="#D2B48C")
check_button7 = tk.Checkbutton(window, text="Cream", variable=cream_var, onvalue=7,command=orders, offvalue=0, bg="#D2B48C")

check_button1.pack(anchor="w")
check_button2.pack(anchor="w")
check_button3.pack(anchor="w")
check_button4.pack(anchor="w")
check_button5.pack(anchor="w")
check_button6.pack(anchor="w")
check_button7.pack(anchor="w")
payment_options = ["Cash", "Card", "Online payment"]


fo = IntVar()

for index in range(len(payment_options)):
    radio_button = tk.Radiobutton(window,
                                  text=payment_options[index],
                                  font=("times new roman", 15),
                                  variable=fo,
                                  value=index,
                                  command = payment_final
                                  )
    radio_button.pack(side="right",pady=5)
label7 = tk.Label(window,
                  text="Please select the payment option: ",
                  font=("Times New Roman", 15)
)       
label7.pack(side="right")


window.iconphoto(True, icon)

window.mainloop()
