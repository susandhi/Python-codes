from tkinter import Tk, Frame, Label, Button, Entry, messagebox
import pandas as pd

root = Tk()
root.title("User Login")

def verify_credientials():
	email = Entry.get(E1)
	password = Entry.get(E2)
	flag = 0
	if email == "":
		messagebox.showerror('Error','Email not entered!!!')
		flag = 1
	if password == "":
		messagebox.showerror('Error','Password not entered!!!')
		flag = 1
	if flag == 0:
		df = pd.read_csv("User_credentials.csv")
		email_list = df['Email-ID'].values
		password_list = df['Password'].values
		flag2 = 0
		for index in range(len(email_list)):
			if email_list[index] == email:
				flag2 = 1
				break
		if flag2 == 1:
			if password_list[index] == password:
				messagebox.showinfo('Info','Login Successful!!!')
			else:
				messagebox.showerror('Error','Wrong Credentials!!!')
		else:
			messagebox.showerror('Error','User not registered!!!')
					
main = Frame(root, bg = 'sky blue', pady =15, padx=15)
main.pack(expand=True, fill="both")

L1 = Label(main, justify="left", text="Email-ID:", bg = 'sky blue', width = 10).grid(row = 1, column = 1, padx = 0, pady = 5)
E1 = Entry(main, bd =5,width=30)
E1.grid(row=1,column=2, padx = 0, pady = 10)
L2 = Label(main, justify="left", text="Password:", bg = 'sky blue', width = 10).grid(row = 2, column = 1, padx = 0, pady = 5)
E2 = Entry(main, bd =5,width=30)
E2.grid(row=2,column=2, padx = 0, pady = 10)
Button(main, text ="OK", bg = "white", relief = "raised", command = verify_credientials, bd =5, width = 20).grid(row = 3, column = 2, padx = 0, pady = 10)

root.mainloop()
