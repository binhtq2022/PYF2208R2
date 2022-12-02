from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename


class Account:
	def __init__(self, username, password):
		self.username = username
		self.password = password
class Material:
	def __init__(self, code, name, quantity, unit, location):
		self.material_code = code
		self.material_name = name
		self.material_stock = int(quantity)
		self.material_unit = unit
		self.material_location = location

list_account = []
list_material = []
list_img_file = []

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
		img_path_entry['state'] = NORMAL
		img_path_entry.delete(0, 'end')
		img_path_entry['state'] = DISABLED
		
		


	def add_btn_click():
		list_code = [item.material_code for item in list_material]
		if material_code_entry.get() == '' or material_name_entry.get() == '' or material_stock_entry.get() == '' or material_unit_entry.get() == '' or material_loc_entry.get() == '' or img_path_entry.get() == "":
			messagebox.showinfo('Mistake', 'Plase full fill data!')
		elif list_code.count(material_code_entry.get()) > 0:
			messagebox.showinfo('Mistake', 'MC code have existed')
		else:
			list_material.append(Material(material_code_entry.get(), material_name_entry.get(), material_stock_entry.get(), material_unit_entry.get(), material_loc_entry.get()))
			with open('data.csv', 'a', newline = '') as f:
				writer = csv.writer(f)
				writer.writerow([material_code_entry.get(), material_name_entry.get(), material_stock_entry.get(), material_unit_entry.get(), material_loc_entry.get()])
				f.close()


			path = img_path_entry.get()
			img1 = Image.open(path)
			img1 = img1.resize((295,155))

			file_name = "./IMG_DATA/"+material_code_entry.get()+".png"

			img1.save(file_name)
	
			messagebox.showinfo('Material adding', 'Added successfuly!')
			img_path_entry['state'] = NORMAL
			img_path_entry.delete(0,'end')
			img_path_entry['state'] = DISABLED
			reset_btn_click()

	def search_btn_click():
		condition  = search_condition_cb.get()
		exist = False
		for item in result_table.get_children():
					result_table.delete(item)
		text = search_entry.get()
		if text == "":
			return
		elif text == "*":
			for item in list_material:
				list_d = [item.material_code,item.material_name, item.material_stock, item.material_unit, item.material_location]
				result_table.insert('', END, values = list_d)
		elif text[-1] == "*":
			text = text.replace("*","")
			for item in list_material:
				exist = False
				if condition == "MC code" and item.material_code.find(text) != -1:
					exist = True
				elif condition == "Material name" and item.material_name.find(text) != -1:
					exist = True
				elif condition == "Location" and item.material_location.find(text) != -1:
					exist = True	
				if exist:
					list_d = [item.material_code,item.material_name, item.material_stock, item.material_unit, item.material_location]
					result_table.insert('', END, values = list_d)

		elif condition == "MC code":
			list_code = [item.material_code for item in list_material]
			if list_code.count(text) > 0:
				resutl_index = list_code.index(text)
				list_d = [list_material[resutl_index].material_code,list_material[resutl_index].material_name, list_material[resutl_index].material_stock, list_material[resutl_index].material_unit, list_material[resutl_index].material_location]
				result_table.insert('', END, values = list_d)
		elif condition == "Material name":
			list_name = [item.material_name for item in list_material]
			if list_name.count(text) > 0:
				for item in list_material:
					if item.material_name == text:
						list_d = [item.material_code,item.material_name, item.material_stock, item.material_unit, item.material_location]
						result_table.insert('', END, values = list_d)
		elif condition == "Location":
			list_location = [item.material_location for item in list_material]
			if list_location.count(text) > 0:
				for item in list_material:
					if item.material_location == text:
						list_d = [item.material_code,item.material_name, item.material_stock, item.material_unit, item.material_location]
						result_table.insert('', END, values = list_d)

				
		
	def item_selected(event):
		for selected_item in result_table.selection():
			material_code_entry['state'] = NORMAL
			item = result_table.item(selected_item)
			record = item['values']
			clear_entry()
			material_code_entry.insert(0,record[0])

			material_name_entry.insert(0,record[1])
			material_stock_entry.insert(0,record[2])
			material_unit_entry.insert(0,record[3])
			material_loc_entry.insert(0,record[4])
			material_code_entry['state'] = DISABLED
			add_btn.place_forget()
			export_btn.place(x = 40, y = 195)
			update_btn.place(x = 130, y = 195)
			delete_btn.place(x = 220, y = 195)
			img_show.configure(image="")
			img_show.image=""
			path = "./IMG_DATA/"+ record[0]+".png"
			try:
				img1 = Image.open(path)
				img1 = img1.resize((295,155))
				img = ImageTk.PhotoImage(img1)
				img_show.configure(image=img)
				img_show.image=img
				img_path_entry['state'] = NORMAL
				img_path_entry.delete(0, 'end')
				img_path_entry.insert(0,path)
				img_path_entry['state'] = DISABLED
			except:
				img_path_entry['state'] = NORMAL
				img_path_entry.delete(0, 'end')
				img_path_entry.insert(0,"Not found the image")
				img_path_entry['state'] = DISABLED
			
			
	
	def update_btn_click():
		
		for item in result_table.get_children():
			result_table.delete(item)
		for i in range (len(list_material)):
			if list_material[i].material_code == material_code_entry.get():
				list_material[i].material_name = material_name_entry.get()
				list_material[i].material_stock = material_stock_entry.get()
				list_material[i].material_unit = material_unit_entry.get()
				list_material[i].material_location = material_loc_entry.get()
				
				path = img_path_entry.get()
				print(path)
				img1 = Image.open(path)
				img1 = img1.resize((295,155))
				file_name = "./IMG_DATA/"+material_code_entry.get()+".png"
				
				write_csv()
				reset_btn_click()
				search_btn_click()
				
				

				img1.save(file_name)
				messagebox.showinfo('Update',f'{material_code_entry.get()} updated successfuly!')
				break
	def delete_btn_click():
		for item in result_table.get_children():
			result_table.delete(item)
		for i in range (len(list_material)):
			if list_material[i].material_code == material_code_entry.get():
				list_material.pop(i)
				reset_btn_click()
				write_csv()
				search_btn_click()
				messagebox.showinfo('Delete',f'{material_code_entry.get()} Deleteted successfuly!')
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
		add_btn.place(x = 140, y = 195)
		export_btn.place_forget()
		update_btn.place_forget()
		delete_btn.place_forget()
		material_code_entry['state'] = NORMAL	
		for item in result_table.get_children():
			result_table.delete(item)
		
		clear_entry()
		img_show.configure(image="")
		img_show.image=""
		
		
		
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
	def browser_path_btn_click():
		o = askopenfilename(filetypes = (('PNG','*.png')
										, ('JPEG', '*jpg, *.jpeg')
										, ('Bitmap file', '*.bmp')
										))
			
		if o:
			img_path_entry['state'] = NORMAL
			img_path_entry.delete(0,'end')
			img_path_entry.insert(0, o)
			img_path_entry['state'] = DISABLED
			path = str(o)
			img1 = Image.open(path)
			img1 = img1.resize((295,155))
			img = ImageTk.PhotoImage(img1)
			img_show.configure(image=img)
			img_show.image=img
			login_wd.mainloop()
		
				
	login_wd.title("Raw Material Inventory")
	login_wd.geometry('900x430')
	main_fm = Frame(login_wd, width = 900, height = 430, bg = "#f5f5f5")
	main_fm.place(x = 0, y = 0)

	info_fm = LabelFrame(login_wd, text = "  Information  ", width = 320, height = 410, bg = "#E3D5FF", bd = 2, relief = RIDGE, font = ('Tahoma', 9, 'bold'))
	info_fm.place(x = 10, y = 10)

	Label(info_fm, text = "MC code", fg = "#0000CC", bg = '#E3D5FF', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 10)
	material_code_entry = Entry(info_fm, border = 1)
	material_code_entry.place(x = 110, y = 10, width = 200)

	Label(info_fm, text = "Material Name", fg = "#0000CC", bg = '#E3D5FF', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 40)
	material_name_entry = Entry(info_fm, border = 1)
	material_name_entry.place(x = 110, y = 40, width = 200)

	Label(info_fm, text = "Stock", fg = "#0000CC", bg = '#E3D5FF', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 70)
	material_stock_entry = Entry(info_fm, border = 1)
	material_stock_entry.place(x = 110, y = 70, width = 200)

	Label(info_fm, text = "Unit", fg = "#0000CC", bg = '#E3D5FF', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 100)
	material_unit_entry = Entry(info_fm, border = 1)
	material_unit_entry.place(x = 110, y = 100, width = 200)

	Label(info_fm, text = "Location", fg = "#0000CC", bg = '#E3D5FF', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 130)
	material_loc_entry = Entry(info_fm, border = 1)
	material_loc_entry.place(x = 110, y = 130, width = 200)

	Label(info_fm, text = "Image", fg = "#0000CC", bg = '#E3D5FF', font = ('Tahoma', 9, 'bold')).place(x = 16, y = 160)
	img_path_entry = Entry(info_fm, border = 1)
	img_path_entry.place(x = 110, y = 160, width = 120)
	img_path_entry['state'] = DISABLED

	add_btn = Button(info_fm, text = "Add", width = 8, bg = '#336600', fg = 'white', border = 1, font = ('Tahoma', 9, 'bold'), command = add_btn_click)
	add_btn.place(x = 140, y = 195)

	update_btn = Button(info_fm, text = "Update", width = 8, bg = '#381EF6', fg = 'white', border = 1, font = ('Tahoma', 9, 'bold'), command = update_btn_click)
	update_btn.place(x = 85, y = 195)
	update_btn.place_forget()

	export_btn = Button(info_fm, text = "Export", width = 8, bg = '#381EF6', fg = 'white', border = 1, font = ('Tahoma', 9, 'bold'),command = export_btn_click)
	export_btn.place(x = 240, y = 195)
	export_btn.place_forget()
	
	delete_btn = Button(info_fm, text = "Delete", width = 8, bg = 'red', fg = 'white', border = 1, font = ('Tahoma', 9, 'bold'),command = delete_btn_click)
	delete_btn.place(x = 162, y = 195)
	delete_btn.place_forget()

	search_fm = LabelFrame(login_wd, text = "  Search  ", width = 540, height = 410, bg = "#a4f6bf", bd = 2, relief = RIDGE, font = ('Tahoma', 9, 'bold'))
	search_fm.place(x = 350, y = 10)

	search_btn = Button(search_fm, text = "Search", width = 10, bg = '#381EF6', fg = 'white', border = 1, font = ('Tahoma', 9, 'bold'), command = search_btn_click)
	search_btn.place(x = 10, y = 40)

	reset_btn = Button(search_fm, text = "Clear all", width = 10, bg = 'red', fg = 'white', border = 1, font = ('Tahoma', 9, 'bold'), command = reset_btn_click)
	reset_btn.place(x = 120, y = 40)

	search_entry = Entry(search_fm,border = 1)
	search_entry.place(x = 10, y = 10, width = 200)

	export_file_btn = Button(search_fm, text = "Export All To Excel", width = 15, bg = '#381EF6', fg = 'white', border = 1, font = ('Tahoma', 9, 'bold'), command = export_file_btn_click)
	export_file_btn.place(x = 400, y = 45)

	browser_path_btn = Button(info_fm, text = "Browser", width = 8, bg = '#FF9900', fg = 'white', border = 1, font = ('Tahoma', 9, 'bold'), command = browser_path_btn_click)
	browser_path_btn.place(x = 240, y = 160)

	img_show = Label(info_fm, image = None, border = 0, bg = "#E3D5FF")
	img_show.place(x = 10, y = 225)		

	Label(search_fm, text = "Search by: ", fg = "#0E02FE", bg = '#a4f6bf', font = ('Tahoma', 9, 'bold')).place(x = 240, y = 10)
	search_condition_cb = ttk.Combobox(search_fm, width = 20, state= "readonly")
	search_condition_cb['values'] = ('MC code', 'Material name', 'Location')
	search_condition_cb.place(x = 320, y = 10)
	search_condition_cb.current(0)


	#-------------------------------

	table_fm = LabelFrame(search_fm, text = "  Result  ", bg = "#a4f6bf", bd = 2, relief = RIDGE, font = ('Tahoma', 9, 'bold'))
	table_fm.place(x = 0, y = 70, width = 535, height = 321)

	scroll_y = Scrollbar(table_fm,orient = VERTICAL)
	result_table = ttk.Treeview(table_fm, columns = ('code', 'name', 'stock','unit', 'location'), height = 14, yscrollcommand = scroll_y.set)
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