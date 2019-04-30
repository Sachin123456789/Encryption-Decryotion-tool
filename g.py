from tkinter import *

from tkinter import filedialog

import webbrowser

import os





"""  

    

 *****Developer Info ****

 Name :    Sachin Nema

 Email :    ssachinnema98@gmail.com

 contact :  9074695402

 Date :     7/4/2019





"""







# Start of Program





# Designing window for registration

def register():

    global register_screen

    register_screen = Toplevel(main_screen)

    register_screen.title("Register")

    register_screen.geometry("300x250")



    global username

    global password

    global username_entry

    global password_entry

    username = StringVar()

    password = StringVar()



    Label(register_screen, text="Please enter details below", bg="blue").pack()

    Label(register_screen, text="").pack()

    username_lable = Label(register_screen, text="Username * ")

    username_lable.pack()

    username_entry = Entry(register_screen, textvariable=username)

    username_entry.pack()

    password_lable = Label(register_screen, text="Password * ")

    password_lable.pack()

    password_entry = Entry(register_screen, textvariable=password, show='*')

    password_entry.pack()

    Label(register_screen, text="").pack()

    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()





# Designing window for login

def login():

    global login_screen

    login_screen = Toplevel(main_screen)

    login_screen.title("Login")

    login_screen.geometry("300x250")

    Label(login_screen, text="Please enter details below to login").pack()

    Label(login_screen, text="").pack()



    global username_verify

    global password_verify



    username_verify = StringVar()

    password_verify = StringVar()



    global username_login_entry

    global password_login_entry



    Label(login_screen, text="Username * ").pack()

    username_login_entry = Entry(login_screen, textvariable=username_verify)

    username_login_entry.pack()

    Label(login_screen, text="").pack()

    Label(login_screen, text="Password * ").pack()

    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')

    password_login_entry.pack()

    Label(login_screen, text="").pack()

    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()





# Implementing event on register button

def register_user():

    username_info = username.get()

    password_info = password.get()



    file = open(username_info, "w")

    file.write(username_info + "\n")

    file.write(password_info)

    file.close()



    username_entry.delete(0, END)

    password_entry.delete(0, END)



    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()





# Implementing event on login button

def login_verify():

    username1 = username_verify.get()

    password1 = password_verify.get()

    username_login_entry.delete(0, END)

    password_login_entry.delete(0, END)



    list_of_files = os.listdir()

    if username1 in list_of_files:

        file1 = open(username1, "r")

        verify = file1.read().splitlines()

        if password1 in verify:

            login_sucess()



        else:

            password_not_recognised()



    else:

        user_not_found()





# Designing popup for login success

def login_sucess():

    global login_success_screen

    login_success_screen = Toplevel(login_screen)

    login_success_screen.title("Success")

    login_success_screen.geometry("150x100")

    Label(login_success_screen, text="Login Success").pack()

    Button(login_success_screen, text="OK", command=delete_login_success).pack()

    root = Tk()

    root.configure(background="white")



    #Function to select a file



    def openfile():

        global path

        path = filedialog.askopenfilename()





    # Function to Encrypt

    def encrypt():

        openfile()

        global ext

        ext = path.split('.')

        ext = str(ext[1])

        f = open(path, 'rb')

        image = f.read()

        f.close()



        image = bytearray(image)



        key = 100



        for i, v in enumerate(image):

            image[i] = v ^ key



        f = open('encrypted.' + ext , 'wb')

        f.write(image)

        f.close()

        encpopup()



    # Function to Deccrypt

    def decrypt():

        openfile()

        ext = path.split('.')

        ext = str(ext[1])

        f = open('encrypted.' + ext, 'rb')

        image = f.read()

        f.close()



        image = bytearray(image)



        key = 100



        for i, v in enumerate(image):

            image[i] = v ^ key



        f = open('deccrypted.' + ext, 'wb')

        f.write(image)

        f.close()

        decpopup()



    # setting title for the window

    root.title("    Envryption Decryption Tool   ")





    # creating a text label

    Label(root, text="Data Encryption/Decryption tool", font=("times new roman", 20), fg="white", bg="maroon", height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)





    # creating top button

    Button(root, text="About", font=("times new roman", 20), bg="#0D47A1", fg='white', command=about).grid(row=3,columnspan=2,sticky=N + E + W + S,padx=5,pady=5)







    # creating first button

    Button(root, text="Encrypt", font=("times new roman", 20), bg="#0D47A1", fg='white', command=encrypt).grid(row=4,columnspan=2,sticky=W + E + N + S,padx=5,pady=5)







    # creating second button

    Button(root, text="Decrypt", font=("times new roman", 20), bg="#0D47A1", fg='white', command=decrypt).grid(row=5,columnspan=2,sticky=N + E + W + S,padx=5,pady=5)



    # creating bottom button

    Button(root, text="Developer", font=("times new roman", 20), bg="#0D47A1", fg='white', command=developer).grid(row=6,columnspan=2,sticky=N + E + W + S,padx=5,pady=5)



    # creating a text label

    Label(root, text="Developed by Sachin Nema \xa9 2019", font=("times new roman", 20), fg="white", bg="black", height=2).grid(row=7, rowspan=2, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)











# Designing popup for login invalid password



def password_not_recognised():

    global password_not_recog_screen

    password_not_recog_screen = Toplevel(login_screen)

    password_not_recog_screen.title("Success")

    password_not_recog_screen.geometry("150x100")

    Label(password_not_recog_screen, text="Invalid Password ").pack()

    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()





# Designing popup for user not found



def user_not_found():

    global decsuccess

    decsuccess = Toplevel(login_screen)

    decsuccess.title("Success")

    decsuccess.geometry("150x100")

    Label(decsuccess, text="User Not Found").pack()

    Button(decsuccess, text="OK", command=delete_user_not_found_screen).pack()





# Designing popup for Encryption Success



def encpopup():

    global decsuccess

    decsuccess = Toplevel(login_screen)

    decsuccess.title("Success")

    decsuccess.geometry("200x100")

    Label(decsuccess, text="File Encrypted Successfully").pack()

    Button(decsuccess, text="OK", command=delete_encpopup).pack()



# Designing popup for Deccryption Success



def decpopup():

    global decsuccess

    decsuccess = Toplevel(login_screen)

    decsuccess.title("Success")

    decsuccess.geometry("200x100")

    Label(decsuccess, text="File Decrypted Successfully").pack()

    Button(decsuccess, text="OK", command=delete_decpopup).pack()





# script to open about section



def about():

    webbrowser.open('a.html')



# script to open github link



def developer():

    webbrowser.open('https://github.com/Sachin123456789/Encryption-Decryotion-tool/find/master')



# Deleting popups



def delete_login_success():

    login_success_screen.destroy()





def delete_password_not_recognised():

    password_not_recog_screen.destroy()





def delete_user_not_found_screen():

    decsuccess.destroy()





def delete_encpopup():

    decsuccess.destroy()



def delete_decpopup():

    decsuccess.destroy()





# Designing Main(first) window



def main_account_screen():

    global main_screen

    main_screen = Tk()

    main_screen.geometry("300x250")

    main_screen.title("Account Login")

    Label(text="Select Your Choice", bg="orange", width="300", height="2", font=("Calibri", 13)).pack()

    Label(text="").pack()

    Button(text="Login", height="2", width="30", command=login).pack()

    Label(text="").pack()

    Button(text="Register", height="2", width="30", command=register).pack()



    main_screen.mainloop()





main_account_screen()



# End of Program
