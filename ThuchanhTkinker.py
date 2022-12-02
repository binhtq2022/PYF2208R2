from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Ingredient Management System")
window.geometry("340x130")
window.resizable(width = False, height = False)

list_ingredient = []


class Ingredient:
	def __init__(self, name, quantity):
		self.name = name
		self.quantity = quantity


def add_btn_click():
	list_ingredient.append(Ingredient(name_entry.get(), int(quantity_entry.get())))
	print([item.name for item in list_ingredient])
	messagebox.showinfo("Ingredient", name_entry.get() + " added sucessfully")

def reset_btn_click():
	quantity_entry.delete(0, "end")
	name_entry.delete(0, "end")

def search_btn_click():
	search_name = search_entry.get()
	exist = False
	for item in list_ingredient:
		if item.name == search_name:
			exist = True
			messagebox.showinfo("Ingredient",f"Quantity of {search_name} is {item.quantity}")
			break
	if(exist == False):
		messagebox.showinfo("Ingredient",f"{search_name} does not exist")
		
def delete_btn_click():
	delete_name = search_entry.get()
	exist = False
	for item in list_ingredient:
		if item.name == search_name:
			exist = True
			messagebox.showinfo("Ingredient",f"Quantity of {search_name} is {item.quantity}")
			break
	if(exist == False):
		messagebox.showinfo("Ingredient",f"{search_name} does not exist")


name_lbl = Label(window, text = "Name:")
name_lbl.place(x = 10, y = 5)

quantity_lbl = Label(window, text = "Quantity:")
quantity_lbl.place(x = 10, y = 25)

name_entry = Entry(window, width = 39)
name_entry.place(x = 90, y = 5)

quantity_entry = Entry(window, width = 39)
quantity_entry.place(x = 90, y = 25)

add_btn = Button(window, text = "Add", height  = 1, width = 8, command = add_btn_click)
add_btn.place(x = 10, y = 55)


delete_btn = Button(window, text = "Delete", height = 1, width = 12)
delete_btn.place(x = 105, y = 55)

reset_btn = Button(window, text = "Reset", height = 1, width = 12, command = reset_btn_click)
reset_btn.place(x = 230, y = 55)

search_btn = Button(window, text = "Search", height = 1, width = 12, command = search_btn_click)
search_btn.place(x = 230, y = 95)

search_entry = Entry(window, width = 35)
search_entry.place(x = 10, y = 98)

window.mainloop()


