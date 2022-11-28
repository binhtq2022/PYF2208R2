from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
from tkinter.filedialog import asksaveasfile


class Account:
	def __init__(self, username, password):
		self.username = username
		self.password = password
class Material:
	def __init__(self, code, name, quantity, unit, location):
		self.material_code = code
		self.material_name = name
		self.material_stock = quantity
		self.material_unit = unit
		self.material_location = location

list_account = []
list_material = []

with open('user.csv', 'r') as f:
	reader = csv.reader(f)
	for acc in reader:
		if acc != []:
			print(acc)
			list_account.append(Account(acc[0], acc[1]))
	f.close()
with open('data.csv', 'r') as f:
	reader = csv.reader(f)
	data = [item for item in reader]
	for i in range(1, len(data)):
		list_material.append(Material(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]))
	f.close()

login_wd = Tk()
login_wd.title("Login")
login_wd.geometry('900x400')
login_wd.configure(bg = '#fff')
login_wd.resizable(False,False)


def signin_click():
	userName = user.get()
	pw = password.get()
	exist = False
	for acc in list_account:
		if userName == acc.username and pw == acc.password:
			main_window()
			exist = True
			break	
	if not exist:
		messagebox.showerror("Invalid", "User or Password is not correct")


# Sign Up frame*********************************

def sign_up_btn_click():
	signUp = Toplevel(login_wd)
	signUp.title("Register")
	signUp.geometry('360x300')
	signUp.configure(bg = 'white')
	signUp.resizable(False,False)


	def Register_btn_click():
		userName = user.get()
		pw = password.get()
		confrim_pw = confrim_password.get()

		if pw != confrim_pw:
			messagebox.showerror("Mistake", "Password does not match!")
			signUp.focus_force()
		elif pw == confrim_pw and userName != '' and userName != "Username":
			with open('user.csv', 'a', newline = '') as f:
				writer = csv.writer(f)
				writer.writerow([userName,pw])
				f.close()

			list_account.append(Account(userName, pw))
			
			messagebox.showinfo("Register", "Register successfuly!")
			signUp.destroy()
		elif userName == 'Username':
			messagebox.showerror("Mistake", "Please input User Name!")
			signUp.focus_force()


	Label(signUp, text = "Register Form", bg = 'white', fg = "#57a1f8", font = ("Tahoma", 20, 'bold')).place(x = 80, y = 10)
	#--------------------------------------
	def on_enter(e):
		user.delete(0, 'end')
	def on_leave(e):
		name = user.get()
		if name == '':
			user.insert(0, 'Username')
	user = Entry(signUp, width = 25, fg = 'black', border = 0, bg = "white", font = ('Tahoma', 9))
	user.place(x = 30, y = 80)
	user.insert(0, 'Username')
	Frame(signUp, width = 295, height = 2, bg = 'black').place(x = 25, y = 102)
	user.bind('<FocusIn>', on_enter)
	user.bind('<FocusOut>', on_leave)
	#-------------------------------------
	def on_enter(e):
		password.delete(0, 'end')
		password.config(show = '*')
	def on_leave(e):
		code = password.get()
		if code == '':
			password.insert(0, 'Password')
			password.config(show = '')

	password = Entry(signUp, width = 25, fg = 'black', border = 0, bg = "white", font = ('Tahoma', 9))
	password.place(x = 30, y = 130)
	password.insert(0, 'Password')
	Frame(signUp, width = 295, height = 2, bg = 'black').place(x = 25, y = 150)
	password.bind('<FocusIn>', on_enter)
	password.bind('<FocusOut>', on_leave)
	#---------------------------------------
	def on_enter(e):
		confrim_password.delete(0, 'end')
		confrim_password.config(show = '*')
	def on_leave(e):
		code = confrim_password.get()
		if code == '':
			confrim_password.insert(0, 'Confrim Password')
			confrim_password.config(show = '')

	confrim_password = Entry(signUp, width = 25, fg = 'black', border = 0, bg = "white", font = ('Tahoma', 9))
	confrim_password.place(x = 30, y = 180)
	confrim_password.insert(0, 'Confrim Password')
	Frame(signUp, width = 295, height = 2, bg = 'black').place(x = 25, y = 200)
	confrim_password.bind('<FocusIn>', on_enter)
	confrim_password.bind('<FocusOut>', on_leave)

	Register_btn = Button(signUp, width = 39, pady = 7, text = 'Register', bg = "#57a1f8", fg = 'white', border = 0, font = ('Tahoma', 10, 'bold'), command = Register_btn_click)
	Register_btn.place(x = 25, y = 235)
	
	
	
	signUp.mainloop()
	



#Begin Main window form-------------------------------------------------------------------------------------------------------------------------
def main_window():
	def clear_entry():
		material_code_entry.delete(0, 'end')
		material_name_entry.delete(0, 'end')
		material_stock_entry.delete(0, 'end')
		material_unit_entry.delete(0, 'end')
		material_loc_entry.delete(0, 'end')

	def add_btn_click():
		list_code = [item.material_code for item in list_material]
		if material_code_entry.get() == '' or material_name_entry.get() == '' or material_stock_entry.get() == '' or material_unit_entry.get() == '' or material_loc_entry.get() == '':
			messagebox.showinfo('Mistake', 'Plase full fill data!')
		elif list_code.count(material_code_entry.get()) > 0:
			messagebox.showinfo('Mistake', 'MC code have existed')
		else:
			list_material.append(Material(material_code_entry.get(), material_name_entry.get(), material_stock_entry.get(), material_unit_entry.get(), material_loc_entry.get()))
			with open('data.csv', 'a', newline = '') as f:
				writer = csv.writer(f)
				writer.writerow([material_code_entry.get(), material_name_entry.get(), material_stock_entry.get(), material_unit_entry.get(), material_loc_entry.get()])
				f.close()
			material_code_entry.delete(0, 'end')
			material_name_entry.delete(0, 'end')
			material_stock_entry.delete(0, 'end')
			material_unit_entry.delete(0, 'end')
			material_loc_entry.delete(0, 'end')
			messagebox.showinfo('Material adding', 'Added successfuly!')

	def search_btn_click():
		condition  = search_condition_cb.get()
		exist = False
		for item in result_table.get_children():
					result_table.delete(item)
		if condition == "MC code":
			list_code = [item.material_code for item in list_material]
			if list_code.count(search_entry.get()) > 0:
				resutl_index = list_code.index(search_entry.get())
				list_d = [list_material[resutl_index].material_code,list_material[resutl_index].material_name, list_material[resutl_index].material_stock, list_material[resutl_index].material_unit, list_material[resutl_index].material_location]
				result_table.insert('', END, values = list_d)
		if condition == "Material name":
			list_name = [item.material_name for item in list_material]
			if list_name.count(search_entry.get()) > 0:
				for item in list_material:
					if item.material_name == search_entry.get():
						list_d = [item.material_code,item.material_name, item.material_stock, item.material_unit, item.material_location]
						result_table.insert('', END, values = list_d)
		if condition == "Location":
			list_location = [item.material_location for item in list_material]
			if list_location.count(search_entry.get()) > 0:
				for item in list_material:
					if item.material_location == search_entry.get():
						list_d = [item.material_code,item.material_name, item.material_stock, item.material_unit, item.material_location]
						result_table.insert('', END, values = list_d)

				
		
	def item_selected(event):
		for selected_item in result_table.selection():
			item = result_table.item(selected_item)
			record = item['values']
			clear_entry()
			material_code_entry.insert(0,record[0])
			material_name_entry.insert(0,record[1])
			material_stock_entry.insert(0,record[2])
			material_unit_entry.insert(0,record[3])
			material_loc_entry.insert(0,record[4])
			material_code_entry['state'] = DISABLED
			add_btn['state'] = DISABLED
			export_btn['state']  = NORMAL
			update_btn['state']  = NORMAL
			delete_btn['state'] = NORMAL

	
	def update_btn_click():
		for item in result_table.get_children():
			result_table.delete(item)
		for i in range (len(list_material)):
			if list_material[i].material_code == material_code_entry.get():
				messagebox.showinfo('Update',f'{material_code_entry.get()} updated successfuly!')
				list_material[i].material_name = material_name_entry.get()
				list_material[i].material_stock = material_stock_entry.get()
				list_material[i].material_unit = material_unit_entry.get()
				list_material[i].material_location = material_loc_entry.get()
				write_csv()
				reset_btn_click()
				search_btn_click()
				break
	def delete_btn_click():
		for item in result_table.get_children():
			result_table.delete(item)
		for i in range (len(list_material)):
			if list_material[i].material_code == material_code_entry.get():
				messagebox.showinfo('Delete',f'{material_code_entry.get()} deleteted successfuly!')
				list_material.pop(i)
				reset_btn_click()
				write_csv()
				search_btn_click()
				break

	def write_csv():
		with open('data.csv', 'w', newline = '') as f:
			writer = csv.writer(f)
			heading = ['MC code', 'Material name', 'Stock', 'Unit', 'Location']
			writer.writerow(heading)
			for item in list_material:
				writer.writerow([item.material_code, item.material_name, item.material_stock, item.material_unit, item.material_location])
			f.close()

	def reset_btn_click():
		add_btn['state'] = NORMAL
		export_btn['state']  = DISABLED
		update_btn['state']  = DISABLED
		delete_btn['state']  = DISABLED
		material_code_entry['state'] = NORMAL
		for item in result_table.get_children():
			result_table.delete(item)
		clear_entry()
		
	def export_btn_click():
		def export_btn_export_wd_click():
			if int(export_entry.get()) > stock:
				messagebox.showinfo('Mistake', 'Not enough material stock!')
				export_wd.focus_force()
			if int(export_entry.get()) <= stock:
				for i in range(len(list_material)):
					if list_material[i].material_code == material_code_entry.get():
						list_material[i].material_stock = str(int(list_material[i].material_stock) - int(export_entry.get()))
						messagebox.showinfo('Export', f"Remain stock {list_material[i].material_stock}")
						export_wd.destroy()
						reset_btn_click()
						if list_material[i].material_stock == "0":
							list_material.pop(i)
			print([item.material_stock for item in list_material])
			write_csv()				
			search_btn_click()		
						
						
		for i in range(len(list_material)):
			if list_material[i].material_code == material_code_entry.get():
				stock = int(list_material[i].material_stock)
				unit = list_material[i].material_unit
				
		export_wd = Toplevel(login_wd)
		export_wd.geometry('240x125')
		export_wd.title('Export')
		export_wd.resizable(False,False)
		Label(export_wd, text = "MC code", fg = "black", font = ('Tahoma', 9, 'bold')).place(x = 10, y = 10)
		Label(export_wd, text = "Stock", fg = "black", font = ('Tahoma', 9, 'bold')).place(x = 10, y = 35)
		code_entry = Entry(export_wd, border = 1)
		code_entry.place(x = 80, y = 10, width = 150)
		code_entry.insert(0,material_code_entry.get())
		code_entry['state'] = DISABLED
		stock_entry = Entry(export_wd, border = 1)
		stock_entry.place(x = 80, y = 35, width = 150)
		stock_entry.insert(0,f"{stock} {unit}")
		stock_entry['state'] = DISABLED
		
		export_entry = Entry(export_wd, border = 1)
		export_entry.place(x = 80, y = 70, width = 150)
		Label(export_wd, text = "Export", fg = "black", font = ('Tahoma', 9, 'bold')).place(x = 10, y = 70)
		
		export_btn = Button(export_wd, text = "Export", width = 8, bg = '#ddec00', fg = 'white', border = 0, font = ('Tahoma', 9, 'bold'), command = export_btn_export_wd_click)
		export_btn.place(x = 90, y = 100)
		export_wd.mainloop()

	def export_file_btn_click():
		
		f = asksaveasfile(initialfile = 'Export Data.csv', 
			defaultextension=".csv",filetypes=[("Comma-separated values","*.csv")])
		if f:
			with open(f.name, 'w', newline = '') as w:
				writer = csv.writer(w)
				heading = ['MC code', 'Material name', 'Stock', 'Unit', 'Location']
				writer.writerow(heading)
				for item in list_material:
					writer.writerow([item.material_code, item.material_name, item.material_stock, item.material_unit, item.material_location])
			w.close()
			messagebox.showinfo("Export file", "Exported file successfuly!")
		
			

	login_wd.title("Raw Material Inventory")
	login_wd.geometry('900x230')
	main_fm = Frame(login_wd, width = 900, height = 430, bg = "#f5f5f5")
	main_fm.place(x = 0, y = 0)

	info_fm = LabelFrame(login_wd, text = "  Information  ", width = 320, height = 210, bg = "#f2b1f9", bd = 2, relief = RIDGE, font = ('Tahoma', 9, 'bold'))
	info_fm.place(x = 10, y = 10)

	Label(info_fm, text = "MC code", fg = "black", bg = '#f2b1f9', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 10)
	material_code_entry = Entry(info_fm, border = 1)
	material_code_entry.place(x = 110, y = 10, width = 200)

	Label(info_fm, text = "Material Name", fg = "black", bg = '#f2b1f9', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 40)
	material_name_entry = Entry(info_fm, border = 1)
	material_name_entry.place(x = 110, y = 40, width = 200)

	Label(info_fm, text = "Stock", fg = "black", bg = '#f2b1f9', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 70)
	material_stock_entry = Entry(info_fm, border = 1)
	material_stock_entry.place(x = 110, y = 70, width = 200)

	Label(info_fm, text = "Unit", fg = "black", bg = '#f2b1f9', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 100)
	material_unit_entry = Entry(info_fm, border = 1)
	material_unit_entry.place(x = 110, y = 100, width = 200)

	Label(info_fm, text = "Location", fg = "black", bg = '#f2b1f9', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 130)
	material_loc_entry = Entry(info_fm, border = 1)
	material_loc_entry.place(x = 110, y = 130, width = 200)

	add_btn = Button(info_fm, text = "Add", width = 8, bg = '#25eb9b', fg = 'white', border = 0, font = ('Tahoma', 9, 'bold'), command = add_btn_click)
	add_btn.place(x = 10, y = 165)

	update_btn = Button(info_fm, text = "Update", width = 8, bg = '#d99245', fg = 'white', border = 0, font = ('Tahoma', 9, 'bold'), command = update_btn_click)
	update_btn.place(x = 85, y = 165)
	update_btn['state']  = DISABLED

	export_btn = Button(info_fm, text = "Export", width = 8, bg = '#ddec00', fg = 'white', border = 0, font = ('Tahoma', 9, 'bold'),command = export_btn_click)
	export_btn.place(x = 240, y = 165)
	export_btn['state']  = DISABLED
	
	delete_btn = Button(info_fm, text = "Delete", width = 8, bg = 'red', fg = 'white', border = 0, font = ('Tahoma', 9, 'bold'),command = delete_btn_click)
	delete_btn.place(x = 162, y = 165)
	delete_btn['state']  = DISABLED

	search_fm = LabelFrame(login_wd, text = "  Search  ", width = 540, height = 210, bg = "#a4f6bf", bd = 2, relief = RIDGE, font = ('Tahoma', 9, 'bold'))
	search_fm.place(x = 350, y = 10)

	search_btn = Button(search_fm, text = "Search", width = 10, bg = '#57a1f8', fg = 'white', border = 0, font = ('Tahoma', 9, 'bold'), command = search_btn_click)
	search_btn.place(x = 10, y = 40)

	reset_btn = Button(search_fm, text = "Reset", width = 10, bg = 'red', fg = 'white', border = 0, font = ('Tahoma', 9, 'bold'), command = reset_btn_click)
	reset_btn.place(x = 120, y = 40)

	search_entry = Entry(search_fm,border = 1)
	search_entry.place(x = 10, y = 10, width = 200)

	export_file_btn = Button(search_fm, text = "Export All To Excel", width = 15, bg = '#57a1f8', fg = 'white', border = 0, font = ('Tahoma', 9, 'bold'), command = export_file_btn_click)
	export_file_btn.place(x = 300, y = 50)

	Label(search_fm, text = "Search by: ", fg = "black", bg = '#a4f6bf', font = ('Tahoma', 9, 'bold')).place(x = 240, y = 10)
	search_condition_cb = ttk.Combobox(search_fm, width = 20, state= "readonly")
	search_condition_cb['values'] = ('MC code', 'Material name', 'Location')
	search_condition_cb.place(x = 320, y = 10)
	search_condition_cb.current(0)


	#-------------------------------

	table_fm = LabelFrame(search_fm, text = "  Result  ", bg = "#a4f6bf", bd = 2, relief = RIDGE, font = ('Tahoma', 9, 'bold'))
	table_fm.place(x = 0, y = 70, width = 535, height = 121)

	scroll_y = Scrollbar(table_fm,orient = VERTICAL)
	result_table = ttk.Treeview(table_fm, columns = ('code', 'name', 'stock','unit', 'location'), yscrollcommand = scroll_y.set)
	scroll_y.pack(side = RIGHT, fill = Y)
	scroll_y.config(command = result_table.yview)

	result_table.heading("code", text = "MC code")
	result_table.heading("name", text = "Material name")
	result_table.heading("stock", text = "Stock")
	result_table.heading("unit", text = "Unit")
	result_table.heading("location", text = "Location")
	result_table['show'] = 'headings'
	result_table.column('code', width = 100)
	result_table.column('name', width = 210)
	result_table.column('stock', width = 60)
	result_table.column('unit', width = 60)
	result_table.column('location', width = 100)	
	result_table.bind('<<TreeviewSelect>>', item_selected)	
	result_table.pack()
	








#End Main window form---------------------------------------------------------------------------------------------------------------------------	

img = PhotoImage(file = 'logo.png')
Label(login_wd, image = img, border = 0, bg = "white").place(x = 10, y = 100)

login_fm = Frame(login_wd, width = 350, height = 350, bg = '#fff')
login_fm.place(x = 480, y = 70)

heading = Label(login_fm, text = 'Sign in', fg = '#57a1f8', bg = '#fff', font = ('Tahoma', 23, 'bold'))
heading.place(x = 100, y = 5)

#------------------
def on_enter(e):
	user.delete(0, 'end')
def on_leave(e):
	name = user.get()
	if name == '':
		user.insert(0, 'Username')
user = Entry(login_fm, width = 25, fg = 'black', border = 0, bg = "white", font = ('Tahoma', 9))
user.place(x = 30, y = 80)
user.insert(0, 'Username')
Frame(login_fm, width = 295, height = 2, bg = 'black').place(x = 25, y = 102)
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

#--------------------
def on_enter(e):
	password.delete(0, 'end')
	password.config(show = '*')
def on_leave(e):
	code = password.get()
	if code == '':
		password.insert(0, 'Password')
		password.config(show = '')

password = Entry(login_fm, width = 25, fg = 'black', border = 0, bg = "white", font = ('Tahoma', 9))
password.place(x = 30, y = 130)
password.insert(0, 'Password')
Frame(login_fm, width = 295, height = 2, bg = 'black').place(x = 25, y = 150)
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

#-------------------------
Sign_btn = Button(login_fm, width = 39, pady = 7, text = 'Sign in', bg = "#57a1f8", fg = 'white', border = 0, font = ('Tahoma', 10, 'bold'), command = signin_click)
Sign_btn.place(x = 25, y = 175)

Label(login_fm, text = "Don't have an account?", fg = 'black', bg = 'white', font = ('Tahoma', 9)).place(x = 100, y = 235)
sign_up_btn = Button(login_fm, text = "Register now", fg = '#57a1f8', border = 0, bg = 'white', cursor = 'hand2', command = sign_up_btn_click)
sign_up_btn.place(x = 240, y = 235)


login_wd.mainloop()