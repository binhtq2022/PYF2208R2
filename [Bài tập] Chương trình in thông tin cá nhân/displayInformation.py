from tkinter import *
from tkinter import messagebox

class nhanVienSale:
    def __init__(self, id, name, address, sale):
        self.id = id
        self.name = name
        self.address = address
        self.sale = sale

list_nhanvien = []
        
def addNhanVien():
    list_nhanvien.append(nhanVienSale(en_id.get(), en_ten.get(), en_diachi.get(), en_doanhthu.get()))
    lst_danhsach.insert(END, list_nhanvien[len(list_nhanvien)-1].id + '   ' + list_nhanvien[len(list_nhanvien)-1].name + '   ' + list_nhanvien[len(list_nhanvien)-1].address + '   ' + list_nhanvien[len(list_nhanvien)-1].sale)
    
def repaidNhanVien():
    check = en_suaxoa.get()
    exit = False
    for i in range(len(list_nhanvien)):
        if list_nhanvien[i].id == check:
            if en_id.get() != '':
                list_nhanvien[i].id = en_id.get()
            if en_ten.get() != '':
                list_nhanvien[i].name = en_ten.get()
            if en_diachi.get() != '':
                list_nhanvien[i].address = en_diachi.get() 
            if en_doanhthu.get() != '':
                list_nhanvien[i].sale = en_doanhthu.get()
            lst_danhsach.delete(i)
            lst_danhsach.insert(i, str(list_nhanvien[i].id) + '   ' + list_nhanvien[i].name + '   ' + list_nhanvien[i].address + '   ' + str(list_nhanvien[i].sale))
            messagebox.showinfo('Thông báo', f'Giá trị mới là: {list_nhanvien[i].id}, {list_nhanvien[i].name}, {list_nhanvien[i].address}, {list_nhanvien[i].sale}')
            exit = True
            break
    if exit == False:
        messagebox.showinfo('Thông báo', f'Không tìm thấy nhân viên có ID {check}')

def deleteNhanVien():
    check = en_suaxoa.get()
    exit = False
    for i in range(len(list_nhanvien)):
        if list_nhanvien[i].id == check:
            del list_nhanvien[i]
            lst_danhsach.delete(i)
            messagebox.showinfo('Thông báo', f'Đã xóa thành công nhân viên có ID {check}')
            exit = True
            break
    if exit == False:
        messagebox.showinfo('Thông báo', f'Không tìm thấy nhân viên có ID {check}')

def resetEntry():
    en_id.delete(0, len(en_id.get()))
    en_ten.delete(0, len(en_ten.get()))
    en_diachi.delete(0, len(en_diachi.get()))
    en_doanhthu.delete(0, len(en_doanhthu.get()))
            
def locDoanhThu():
    lst_ketqua.delete(0, 20)
    for i in lst_diachi.curselection():
        sumsale = 0
        for j in list_nhanvien:
            if lst_diachi.get(i) == j.address:
                sumsale += int(j.sale)
        lst_ketqua.insert(END, lst_diachi.get(i) + '  ' + str(sumsale))

def locTrung():
    lst_diachi.delete(0, 100)
    list_nhanviencopy = list_nhanvien
    for i in range(len(list_nhanviencopy)):
        for j in range(len(list_nhanviencopy)-i-1):
            if list_nhanviencopy[len(list_nhanviencopy)-1].address == list_nhanviencopy[j].address:
                del list_nhanviencopy[len(list_nhanviencopy)-1]
                break
    for i in range(len(list_nhanviencopy)):
        lst_diachi.insert(i, list_nhanviencopy[i].address)
        
        
windown = Tk()
windown.title('Quản lý nhân viên bán hàng')
windown.configure(bg='light grey')

lb_tieude = Label(windown, text='CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN BÁN HÀNG', bg='green', fg='yellow', relief=RAISED, font='arial 25 bold', width=40, height=1)
lb_id = Label(windown, text='ID', bg='light grey', font='arial 15 bold underline')
lb_ten = Label(windown, text='HỌ VÀ TÊN', bg='light grey', font='arial 15 bold underline')
lb_diachi = Label(windown, text='ĐỊA CHỈ', bg='light grey', font='arial 15 bold underline')
lb_doanhthu = Label(windown, text='DOANH THU', bg='light grey', font='arial 15 bold underline')
lb_VND = Label(windown, text='VND', bg='light grey', font='arial 15 bold')
lb_danhsach = Label(windown, text='DANH SÁCH TỒN TẠI', bg='light grey', font='arial 15 bold')
lb_suaxoa = Label(windown, text='ID REPAI/DELETE', bg='light grey', font='arial 15 bold')
lb_locdiachi = Label(windown, text='LỰA CHỌN ĐỊA CHỈ', bg='light grey', font='arial 15 bold')
en_id = Entry(windown, relief=SUNKEN, width=20, font='arial 15')
en_ten = Entry(windown, relief=SUNKEN, width=20, font='arial 15')
en_diachi = Entry(windown, relief=SUNKEN, width=20, font='arial 15')
en_doanhthu = Entry(windown, relief=SUNKEN, width=20, font='arial 15', justify='right')
en_suaxoa = Entry(windown, relief=SUNKEN, width=20, font='arial 15', justify='right')
bt_add = Button(windown, relief=RAISED, bg='grey', text='ADD', width=6, font='arial 15 bold', command=addNhanVien)
bt_repaid = Button(windown, relief=RAISED, bg='grey', text='REPAID', width=6, font='arial 15 bold', command=repaidNhanVien)
bt_delete = Button(windown, relief=RAISED, bg='grey', text='DELETE', width=6, font='arial 15 bold', command=deleteNhanVien)
bt_reset = Button(windown, relief=RAISED, bg='grey', text='RESET', width=6, font='arial 15 bold', command=resetEntry)
bt_locdoanhthu = Button(windown, relief=RAISED, bg='red', text='LỌC DOANH THU', width=15, font='arial 15 bold', command=locDoanhThu)
lst_danhsach = Listbox(windown, selectmode=MULTIPLE, relief=SUNKEN, width=50, height=8)
lst_diachi = Listbox(windown, selectmode=MULTIPLE, relief=SUNKEN, width=50, height=8)
lst_ketqua = Listbox(windown, selectmode=MULTIPLE, relief=SUNKEN, width=50, height=8)
checkbt = Checkbutton(windown, text='Load địa chỉ', command=locTrung, onvalue = 1, offvalue = 0)

lb_tieude.place(x=250, y=20)
lb_id.place(x=70, y=100)
lb_ten.place(x=70, y=140)
lb_diachi.place(x=70, y=180)
lb_doanhthu.place(x=70, y=220)
lb_locdiachi.place(x=800, y=140)
en_id.place(x=230, y=100)
en_ten.place(x=230, y=140)
en_diachi.place(x=230, y=180)
en_doanhthu.place(x=230, y=220)
lb_VND.place(x=460, y=220)
bt_add.place(x=70, y=300)
bt_repaid.place(x=180, y=300)
bt_delete.place(x=290, y=300)
bt_reset.place(x=400, y=300)
lst_danhsach.place(x=70, y=500)
lst_ketqua.place(x=750, y=500)
lb_danhsach.place(x=110, y=450)
bt_locdoanhthu.place(x=800, y=450)
lb_suaxoa.place(x=130, y=360)
en_suaxoa.place(x=100, y=400)
lst_diachi.place(x=750, y=180)
checkbt.place(x=1100, y=235)

windown.mainloop()