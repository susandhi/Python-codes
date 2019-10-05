from tkinter import Tk, Frame, Label, Button, Entry, messagebox
import pandas as pd

special_symbol_list = ['!','@','#','$','%','&','*']

root = Tk()
root.title("")

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

def add_user_SignIn_details():
	email = Entry.get(E11)
	password = Entry.get(E21)
	flag = 0
	flag2 = 0
	flag3 = 0
	df = pd.read_csv("User_credentials.csv")
	email_list = df['Email-ID'].values
	for each_email in email_list:
		if email == each_email:
			messagebox.showerror('Error','Email already registered!!!')
			flag = 1
	if flag == 0:
		for each_alphabet in email:
			if each_alphabet == '@':
				flag2 = 1
		if email[-4:] == '.com' and flag2 == 1:
			if len(password) > 7:
				if password.islower() == False and password.isupper() == False and password.isdigit() == False and password.isalpha() == False:
					for each_special_symbol in special_symbol_list:
						if each_special_symbol in password:
							flag3 = 1
					
			if flag3 == 1:
				df2 = pd.DataFrame({'Email-ID':[email], 'Password':[password]})
				df = df.append(df2, ignore_index = True)
				df.to_csv('User_credentials.csv', index = False)
				messagebox.showinfo('Info','SignIn Successful!!!')
			else:
				messagebox.showerror('Error','Password doesn\'t match password complexity requirements!!!\n\n1. Password must be minimum 8 characters long\n2. Password must contain atleast one uppercase letter, one lowercase letter and one digit\n3. Password must contain one of the following special character (!,@,#,$,%,&,*)')					

def user_login():
	global E1, E2
	L1 = Label(sub_frame, justify="left", text="Email-ID:", fg = 'magenta', width = 10).grid(row = 1, column = 1, padx = 0, pady = 5)
	E1 = Entry(sub_frame, bd =5,width=30)
	E1.grid(row=1,column=2, padx = 5, pady = 10)
	L2 = Label(sub_frame, justify="left", text="Password:", fg = 'magenta', width = 10).grid(row = 2, column = 1, padx = 0, pady = 5)
	E2 = Entry(sub_frame, show = '*' ,bd =5,width=30)
	E2.grid(row=2,column=2, padx = 5, pady = 10)
	Button(sub_frame, text ="Login", fg = 'orange', relief = "raised", command = verify_credientials, bd =5, width = 20).grid(row = 3, column = 2, padx = 0, pady = 10)

def user_signIn():
	global E11, E21
	L11 = Label(sub_frame, justify="left", text="Email-ID:", fg = 'brown', width = 10).grid(row = 1, column = 1, padx = 0, pady = 5)
	E11 = Entry(sub_frame, bd =5,width=30)
	E11.grid(row=1,column=2, padx = 5, pady = 10)
	L21 = Label(sub_frame, justify="left", text="Password:", fg = 'brown', width = 10).grid(row = 2, column = 1, padx = 0, pady = 5)
	E21 = Entry(sub_frame, show = '*' ,bd =5,width=30)
	E21.grid(row=2,column=2, padx = 5, pady = 10)
	Button(sub_frame, text ="SignIn", fg = 'green', relief = "raised", command = add_user_SignIn_details, bd =5, width = 20).grid(row = 3, column = 2, padx = 0, pady = 10)

main_frame = Frame(root, pady =15, padx=15)
main_frame.pack(expand=True, fill="both")
sub_frame = Frame(root, pady =15, padx=15)
sub_frame.pack(expand=True, fill="both")

Button(main_frame, text ="New User", fg = 'red', relief = "flat", command = user_signIn, bd =5, width = 17).grid(row = 1, column = 1, padx = 5, pady = 0)
Button(main_frame, text ="Old User", fg = 'blue', relief = "flat", command = user_login, bd =5, width = 17).grid(row = 1, column = 2, padx = 5, pady = 0)

root.mainloop()
