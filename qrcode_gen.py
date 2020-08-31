from tkinter import*
from tkinter import messagebox
import qrcode
import pyqrcode
import os
#
# https://pythonhosted.org/PyQRCode/_modules/pyqrcode/builder.html#QRCodeBuilder
#

#create window
window = Tk()

#generate QRCODE
def generator():
    if len(input_url.get()) != 0:
        global myQr
        #generates code from url  
        myQr = pyqrcode.QRCode(input_url.get(),error='H')
        #where the png will be saved
        dir = 'Desktop/qrcode'
        #if path does't exist create one
        if not os.path.isdir(dir): os.makedirs(dir)
        #save png to dir with the given file name
        myQr.png(os.path.join(dir, file_name.get()+".png"),scale=6)
        #display qrcode
        myQr.show()
        
    else:
        messagebox.showinfo("Invalid Input", "Please enter a URL")
       
window.title("QR Code Maker" )

label1 = Label(window, text = "", font = ("Arial",12))
label1.grid(row = 1, column = 0, sticky = 'nsew')

label2 = Label(window, text = "Enter URL", font = ("Arial",12))
label2.grid(row = 3, column = 0, sticky = 'nsew')

label3 = Label(window, text = "Enter File Name ", font = ("Arial",12))
label3.grid(row = 5, column = 0, sticky = 'nsew')

input_url = StringVar()
fileInput = Entry(window, textvariable = input_url, font = ("Arial",12))
fileInput.grid(row = 3, column = 1, sticky = 'nsew')

file_name = StringVar()
nameInput = Entry(window, textvariable = file_name, font = ("Arial",12), width =15)
nameInput.grid(row = 5, column = 1, sticky = 'nsew')

generate_button = Button(window, text = 'Generate', font = ("Arial",12), width = 15, command = generator)
generate_button.grid(row = 7, column = 1, sticky = 'nsew')

window.geometry("450x300")
window.mainloop()

