import sqlite3
from tkinter import *
from tkinter import ttk
from unicodedata import numeric

root = Tk()
root.title("Management System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)
storeName = "Equipment valuation System"

photo1 = PhotoImage(file="sihle.png")
Label (root, image=photo1, bg="black") .grid(row=0, column=10, pady=20, padx=(20,20) )



def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


def insert( Laptops, Charges, Extentions, Routors):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    inventory(itemLaptops NUMERIC, itemCharges TEXT, itemExtentions NUMERIC, itemRouters NUMERIC)""")

    cursor.execute("INSERT INTO inventory VALUES ('" + str(Laptops) + "','" + str(Charges) + "','" + str(Extentions) + "','" + str(Routors) + "')")
    conn.commit()


def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemLaptops NUMERIC, itemCharges TEXT, itemExtentions NUMERIC, itemRouters NUMERIC)""")

    cursor.execute("DELETE FROM inventory WHERE itemId = '" + str(data) + "'")
    conn.commit()


def update(Laptops, Charges, Extentions, Routers):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemLaptops NUMERIC, itemCharges TEXT, itemExtentions NUMERIC, itemRouters NUMERIC)""")

    cursor.execute("UPDATE inventory SET itemLaptops = '" + str(Laptops) + "', itemCharges = '" + str(Charges) + "', itemExtentions = '" + str(Extentions) + "', itemRouters = '" + str(Routers) + "'")
    conn.commit()


def read():
    conn = sqlite3.connect("Equipment.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemName NUMERIC, itemD_O_B TEXT, itemStream NUMERIC, itemSex NUMERIC)""")

    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results


def insert_data():
    itemLaptops = str(entryLaptops.get())
    itemCharges = str(entryCharges.get())
    itemExtentions = str(entryExtentions.get())
    itemRouters = str(entryRouters.get())
    if itemLaptops == "" or itemLaptops == " ":
        print("Error Inserting Laptops")
    if itemCharges == "" or itemCharges == " ":
        print("Error Inserting Charges")
    if itemExtentions == "" or itemExtentions == " ":
        print("Error Inserting Extentions")
    if itemRouters == "" or itemRouters == " ":
        print("Error Inserting Routers")
    else:
        insert(str(itemLaptops), str(itemCharges), str(itemExtentions), str(itemRouters))

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=8, columnspan=4, rowspan=5, padx=10, pady=10)


def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=8, columnspan=4, rowspan=5, padx=10, pady=10)

def update_data():
    selected_item = my_tree.selection()[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(entryLaptops.get(), entryCharges.get(), entryExtentions.get(), entryRouters.get() ,update_name)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=8, columnspan=4, rowspan=5, padx=10, pady=10)


titleLabel = Label(root, text=storeName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

LaptopsLabel = Label(root, text="Laptops", font=('Arial bold', 15))
ChargersLabel = Label(root, text="Charges", font=('Arial bold', 15))
ExtentionsLabel = Label(root, text="Extentions", font=('Arial bold', 15))
RoutersLabel = Label(root, text="Routers", font=('Arial bold', 15))
LaptopsLabel.grid(row=1, column=0, padx=10, pady=10)
ChargersLabel.grid(row=2, column=0, padx=10, pady=10)
ExtentionsLabel.grid(row=3, column=0, padx=10, pady=10)
RoutersLabel.grid(row=4, column=0, padx=10, pady=10)

entryLaptops = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryCharges = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryExtentions = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryRouters = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryLaptops.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryCharges.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryExtentions.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryRouters.grid(row=4, column=1, columnspan=3, padx=5, pady=5)


buttonEnter = Button(
    root, text="Enter", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=insert_data)
buttonEnter.grid(row=7, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
buttonUpdate.grid(row=7, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=delete_data)
buttonDelete.grid(row=7, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("Laptops", "Charges", "Extentions", "Routers")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Laptops", anchor=W, width=100)
my_tree.column("Charges", anchor=W, width=200)
my_tree.column("Extentions", anchor=W, width=150)
my_tree.column("Routers", anchor=W, width=150)
my_tree.heading("Laptops", text="Laptops", anchor=W)
my_tree.heading("Charges", text="Charges", anchor=W)
my_tree.heading("Extentions", text="Extentions", anchor=W)
my_tree.heading("Routers", text="Routers", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="row")

my_tree.tag_configure('row', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=8, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()
