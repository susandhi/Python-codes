from tkinter import Tk, Frame, Label, Button, Entry, messagebox
import pandas as pd

root = Tk()
root.title("User SignIn")

special_symbol_list = ['!','@','#','$','%','&','*']

def verify_credientials():
	email = Entry.get(E1)
	password = Entry.get(E2)
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
				print(email)
				print(password)
				df2 = pd.DataFrame({'Email-ID':[email], 'Password':[password]})
				df = df.append(df2, ignore_index = True)
				df.to_csv('User_credentials.csv', index = False)
				messagebox.showinfo('Info','SignIn Successful!!!')
			else:
				messagebox.showerror('Error','Password doesn\'t match password complexity requirements!!!\n\n1. Password must be minimum 8 characters long\n2. Password must contain atleast one uppercase letter, one lowercase letter and one digit\n3. Password must contain one of the following special character (!,@,#,$,%,&,*)')
			
		
					
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
