"""
        *** For Better experience and Run without Any error install and use Python Official Compiler and go to CMD/Commend Prompt/Powershell/Any command terminal and run this commend ***
        *** Make sure you run this commend on ISA folder ***
            Command >>> pip install -r requirements.txt
"""

# built in framework or module 
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import datetime
import subprocess

# External framework or module 
from PIL import Image, ImageTk
from stegano import lsb
import customtkinter

# set the display
root=Tk()
root.title("Image Security & Analysis (ISA)")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

# define global variable 
global userIn, passIn, imgx,imgy, frame,frame2, mailIn, logoimg

# text for about us page 
global aboutusText
aboutusText = """

Welcome to our app, your all-in-one solution for advanced image security and analysis. Our app offers a comprehensive suite of tools designed to enhance the privacy, integrity, and investigative capabilities of your images.


Features:

Image Encryption and Decryption: Secure your images with state-of-the-art encryption algorithms, ensuring that only authorized users can access your sensitive visual data. Easily decrypt your images when needed with our user-friendly interface.

Image Steganography: Conceal information within images through our robust steganography tools. Embed secret messages or data seamlessly within your pictures, maintaining their original appearance and ensuring discreet communication.

Photo Forensics: Investigate and analyze images with our powerful forensic tools. Detect alterations, verify authenticity, and uncover hidden details to support your investigative needs.


*Here are some guidence for our application to help you use this application more smoothly and comfortably.*

On Startup:
After you sign up an account or login to your existing account you will get into the main page [Image Security & Analysis] of the application. On this page you will get the options to use our various services.
Such as:
        1. Image Encrypt/Decrypt
        2. Image Steganography
        3. Digital Photo Forensics

Choose any of the options above to access that particular service.
Once you choosen a service option it will take you on that service page.

1. Image Encrypt/Decrypt Page:
In this page you get the service to encrypt an image or decrypt a previously encrypted image.

To Encrypt:
    First you need to upload an image that you want to encrypt. When encrypting an image it will ask you to put a secret key. Provide a secret key that consists 2 numbers. After that press the button "Encrypt/Decrypt" which will complete the service and show you a successful message.

To Decrypt:
    Simply upload the previously encrypted image and provide the secret key that was used for encryption. After that, press the "Encrypt/Decrypt" button to decrypt the image. After completion it will show you a successfull note.

2. Image Steganography Page:
In this page you get the service to hide texts in an image known as "Image steganography". Steganography is the technique of hiding data within an ordinary, nonsecret file or message to avoid detection; the hidden data is then extracted at its destination.
To do it, upload an image that you want to use to hide in some texts and write down the texts you want to hide in it in the text box at right side. After that put a secret key which will help to regain the hidden text from the image.
Press the "Hide Data" option and then it will show you a "Save Image" option. Finally press the Save image option and the image will be saved with the hidden text in ISA Image storage. After that it will show you Saved successful message.
Moreover, if there is any image selected in the Image Steganography service which is already has hidden data in it, simply put the secret key that was given before to hide data in it and press the "Show Data" option. It will show you the hidden data in the image.

*Note: Every image from image steganography service will be saved into ISA "Saved file" folder. Evrytime someone want to see the hidden data in a image they have to choose the image from ISA "Saved file" folder and use the correct secret key*

3. Digital Photo Forensic Page:
Photo forensic allows you to scan devices such as computers or mobile devices and obtain photo evidence for analysis.
To do the research, upload the image that you want to scan and get information of the image. After that you will get the option "Get Data". Press the "Get Data" option and it will show you various information that it get from the device.
There is a "Save Data" option which will save the data it get from the scan in a text file. After that it will show you Saved successful message.

*Note: The saved text file will be saved in "Saved file" folder of ISA*


Our app is designed with user privacy and security at its core, providing you with reliable and efficient tools for all your image processing requirements. Whether you're protecting personal photos, conducting covert communication, or performing detailed forensic analysis, our app is here to support your needs.

"""

# Start application Programme and open the login screen
def startAPP():
    # function for log info. entry
    def log_entry(c,d):
        # get date and time for entry the log
        x = datetime.datetime.now()
        date = x.strftime("%d-%m-%y")
        time = x.strftime("%H-%M-%S")
        # identify the category of Activity for log 
        match c:
            case 0:
                cat="Loged In"
            case 1:
                cat="Image Encrypt/Decrypt"
            case 2:
                cat="Image Steganography"
            case 3:
                cat="Digital Photo Forensic"
            case 4:
                cat="Change Password"
        # open log dataset for append new data
        fla = open("assets/datasets/log.txt", "a")
        # append new log
        Wdata = username+" | "+date+" | "+time+" | "+cat+" | "+d+"\n"
        fla.write(Wdata)
        fla.close()

    # setup main application logo
    image_icon = PhotoImage(file="assets/img/logo1.png")
    root.iconphoto(False, image_icon)
    # function for sign up screen
    def sign_up():
        # function for destroy signup screen and open the main login screen
        def destroy_signUP():
            imgy.destroy()
            frame2.destroy()
            startAPP()

        # function for check signup details validation
        def signup_check():  
            # get all info. from input 
            username = userIn.get()
            password = passIn.get()
            Cpassword = passInc.get()
            mail = mailIn.get()
            fullName = fname.get()
            # check input password length
            if len(password)<8:
                messagebox.showerror("Invelid", "Password must need to contain minimum 8 Character.")
            # check -> is password and confirm password same or not ?
            elif password==Cpassword:
                SIGNUP = True
                # open file db for check username
                file = open("assets/datasets/db.txt","r")
                f = file.readlines()
                for i in f:
                    # split the line for take each data in a list
                    data = i.split(" | ")
                    # if username already exit in db then show error
                    if username == data[1]:
                        messagebox.showerror("Invelid","This Username already Exits.")
                        SIGNUP = False
                file.close()

                # if signup true or username didn't exits in db then appen new data in db from input
                if SIGNUP:
                    file = open("assets/datasets/db.txt","a")
                    file.write("0"+" | "+username+" | "+password+" | "+fullName+" | "+mail+"\n")
                    file.close()
                    messagebox.showinfo("Signup", "Sucessfully Signup")
                    # startAPP()
                    destroy_signUP()
            else:
                messagebox.showerror("Invelid", "Both Password should match.")

        # set side image for signup page   
        global imgS
        imgx.destroy()
        frame.destroy()
        imgS = PhotoImage(file='assets/img/signup.png')
        imgy = Label(root, image=imgS, bg="white")
        imgy.place(x=25,y=50)

        # setup a frame for input area
        frame2 = Frame(root, width=350, height=350, bg='white')
        frame2.place(x=480, y=70)
        # set a heading text for signup area
        heading = Label(frame2, text="Sign-up", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=110, y=0)

        # functions for input area values
        def on_enter(e):
            userIn.delete(0, 'end')
        def on_leave(e):
            name = userIn.get()
            if name == '':
                userIn.insert(0, 'Username')
        # set username Input area
        userIn = Entry(frame2, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
        userIn.place(x=30, y=60)
        userIn.insert(0, 'Username')
        userIn.bind('<FocusIn>', on_enter)
        userIn.bind('<FocusOut>', on_leave)
        Frame(frame2,width=295,height=2,bg='black').place(x=25, y=87)

        # set Full name Input area
        def on_enter(e):
            fname.delete(0, 'end')
        def on_leave(e):
            name = fname.get()
            if name == '':
                fname.insert(0, 'Full Name')
        fname = Entry(frame2, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
        fname.place(x=30, y=100)
        fname.insert(0, 'Full Name')
        fname.bind('<FocusIn>', on_enter)
        fname.bind('<FocusOut>', on_leave)
        Frame(frame2,width=295,height=2,bg='black').place(x=25, y=127)

        # set mail Input area
        def on_enter(e):
            mailIn.delete(0, 'end')
        def on_leave(e):
            name = mailIn.get()
            if name == '':
                mailIn.insert(0, 'Email')
        mailIn = Entry(frame2, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
        mailIn.place(x=30, y=140)
        mailIn.insert(0, 'Email')
        mailIn.bind('<FocusIn>', on_enter)
        mailIn.bind('<FocusOut>', on_leave)
        Frame(frame2,width=295,height=2,bg='black').place(x=25, y=167)
        
        # set password Input area
        def on_enter(e):
            passIn.delete(0, 'end')
        def on_leave(e):
            Pdata = passIn.get()
            if Pdata == '':
                passIn.insert(0, 'Password')
        passIn = Entry(frame2, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
        passIn.place(x=30, y=180)
        passIn.insert(0, 'Password')
        passIn.bind('<FocusIn>', on_enter)
        passIn.bind('<FocusOut>', on_leave)
        Frame(frame2,width=295,height=2,bg='black').place(x=25, y=207)
        
        # set Confirm password Input area
        def on_enter(e):
            passInc.delete(0, 'end')
        def on_leave(e):
            Pdata = passInc.get()
            if Pdata == '':
                passInc.insert(0, 'Confirm Password')
        passInc = Entry(frame2, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
        passInc.place(x=30, y=220)
        passInc.insert(0, 'Confirm Password')
        passInc.bind('<FocusIn>', on_enter)
        passInc.bind('<FocusOut>', on_leave)
        Frame(frame2,width=295,height=2,bg='black').place(x=25, y=247)
        
        # setup button for sign up
        Button(frame2, width=39, pady=7, text='Sign-up', bg='#57a1f8', cursor='hand2', fg='white', border=0, command=signup_check).place(x=35, y=274)
        
        # create login option in signup page
        label = Label(frame2, text="Already have an Account?", fg='black', bg="white", font=('Microsoft YaHei UI Light', 9))
        label.place(x=76, y=320)
        sign_up = Button(frame2, width=6, text='Login', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=destroy_signUP)
        sign_up.place(x=224, y=320)

    global  fname,umail,username, password

    # function for check login validity
    def login_check():  
        global  fname,umail,username, password
        LOGIN = False
        # get input data from login page
        username = userIn.get()
        password = passIn.get()
        RmBtn = agreement.get()
        # open file for read and check input data validity
        file = open("assets/datasets/db.txt","r")
        f = file.readlines()
        for i in f:
            # spilit every data from every line
            data = i.split(" | ")
            # check username
            if username == data[1]:
                # check password is correct or not 
                if password == data[2]:
                    LOGIN = True
                    # set full name and email if username and password both correct
                    fname = data[3]
                    umail = data[4]

                    # entry log
                    log_entry(0,"Loged In")
                    # check remember me button checked or not 
                    if RmBtn == "1":
                        # read all data
                        fur = open("assets/datasets/db.txt", "r")
                        furd = fur.readlines()
                        fur.close()
                        fuw = open("assets/datasets/db.txt", "w")
                        for i in furd:
                            ni = i.split(" | ")
                            if ni[1] == username:
                                # set first value 1 for the specific username next time it will login automatically 
                                ni[0] = "1"
                                # join and write the new data
                                fuw.write((" | ".join(ni)))
                            else:
                                fuw.write(i)
                        fuw.close()
                    # if login credential correct the open the home page
                    homePage()
        file.close()
        if not LOGIN:
            # show error if input the wrong credential
            messagebox.showerror("Invalid", "Invalid Combination")

    # function for home page
    def homePage():
        # destroy the login page
        imgx.destroy()
        frame.destroy()
        # create 2 navbar one for home page and other one for all service page
        navs = Frame(root, width=950, height=50, bg='white')
        navs.place(x=0, y=0)
        navh = Frame(root, width=600, height=50, bg='white')
        navh.place(x=0, y=0)

        # function for About Page
        def aboutPage():
            # destroy the home page
            service_frame.destroy()
            navh.destroy()
            # create a new frame for about  page
            about_frame = Frame(root, width=930, height=460, bg='white').place(x=-3, y=50)
            # hide the about page button from navbar
            Frame(root, width=47, height=47, bg='white').place(x=808,y=1)
            # set heading for about page
            Label(about_frame, text="About Us", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold')).place(x=390,y=60)
            
            # set frame for all text area
            SIn_frame = Frame(about_frame, width=825, height= 370, bg="white")
            SIn_frame.place(x=50, y=120)
            # set the details text 
            textArea = Text(SIn_frame, font="Robote 12", bg="white", fg="black",borderwidth=0,bd=0, wrap=WORD)
            textArea.place(x=0, y=0, width=805, height=363)
            # set a scroll bar for Scrolling
            scrollbar1 = Scrollbar(SIn_frame)
            scrollbar1.place(x=805,y=0,height=367)
            scrollbar1.configure(command=textArea.yview)
            textArea.configure(yscrollcommand=scrollbar1.set)
            # insert the details data in text area
            textArea.insert(END, aboutusText)
            textArea.configure(state=DISABLED)

        # function for user Info. page
        def userPage():
            # function for logout 
            def logout():
                fur = open("assets/datasets/db.txt", "r")
                furd = fur.readlines()
                fur.close()
                # open dataset for changes 
                fuw = open("assets/datasets/db.txt", "w")
                for i in furd:
                    ni = i.split(" | ")
                    if ni[1] == username:
                        # if username got in file then set the first value 0 for not login automatically next time 
                        ni[0] = "0"
                        # join and write new data
                        fuw.write((" | ".join(ni)))
                    else:
                        fuw.write(i)
                fuw.close()
                # after logout display the login screen 
                startAPP()

            # function for change the present password
            def changePassword():
                # function for change password confirmation 
                def changePasswordC():
                    # get input data for change password
                    OP = passIn.get()
                    NP = npassIn.get()
                    CNP = passInc.get()
                    
                    # check old password and new password
                    if (OP == password) and (NP == CNP):
                        # check password length
                        if len(NP)<8:
                            messagebox.showerror("Invelid", "Password must need to contain minimum 8 Character.")
                        else:
                            fur = open("assets/datasets/db.txt", "r")
                            furd = fur.readlines()
                            fur.close()
                            # if everything correct then change the dataset
                            fuw = open("assets/datasets/db.txt", "w")
                            for i in furd:
                                ni = i.split(" | ")
                                # find the username
                                if ni[1] == username:
                                    # set password as new password
                                    ni[2] = NP
                                    # join and write new data
                                    fuw.write((" | ".join(ni)))
                                else:
                                    fuw.write(i)
                            fuw.close()
                            # entry the log info.
                            log_entry(4,"Changed Password")
                            # show a sucess message
                            messagebox.showinfo("Sucess", "Sucessfully Password Changed")
                            # after changes the password display the user info screen
                            userPage()

                    else:
                        messagebox.showerror("Invelid", "Invelid Password Entry.")

                # hide the old button
                Frame(user_frame, width=240, height=70, bg='white').place(x=35,y=338)

                # take input for old password
                def on_enter(e):
                    passIn.delete(0, 'end')
                def on_leave(e):
                    Pdata = passIn.get()
                    if Pdata == '':
                        passIn.insert(0, 'Old Password')
                passIn = Entry(user_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
                passIn.place(x=38, y=340)
                passIn.insert(0, 'Old Password')
                passIn.bind('<FocusIn>', on_enter)
                passIn.bind('<FocusOut>', on_leave)
                Frame(user_frame,width=295,height=2,bg='black').place(x=38, y=367)

                # take input for new password
                def on_enter(e):
                    npassIn.delete(0, 'end')
                def on_leave(e):
                    Pdata = npassIn.get()
                    if Pdata == '':
                        npassIn.insert(0, 'New Password')
                npassIn = Entry(user_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
                npassIn.place(x=38, y=380)
                npassIn.insert(0, 'New Password')
                npassIn.bind('<FocusIn>', on_enter)
                npassIn.bind('<FocusOut>', on_leave)
                Frame(user_frame,width=295,height=2,bg='black').place(x=38, y=407)
                
                # take input for new confirm password
                def on_enter(e):
                    passInc.delete(0, 'end')
                def on_leave(e):
                    Pdata = passInc.get()
                    if Pdata == '':
                        passInc.insert(0, 'New Confirm Password')
                passInc = Entry(user_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
                passInc.place(x=38, y=420)
                passInc.insert(0, 'New Confirm Password')
                passInc.bind('<FocusIn>', on_enter)
                passInc.bind('<FocusOut>', on_leave)
                Frame(user_frame,width=295,height=2,bg='black').place(x=38, y=447)
                Button(user_frame, width=25, text='Change Password', border=0, bg='#57a1f8', cursor='hand2', fg='white', font=('Microsoft YaHei UI Light', 10), command=changePasswordC).place(x=80, y=460)

            # destroy the home page after go user page
            service_frame.destroy()
            navh.destroy()

            # create frame for user page
            user_frame = Frame(root, width=930, height=460, bg='white').place(x=-3, y=50)
            # set the heading
            Label(user_frame, text="User", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold')).place(x=100,y=70)
            # set the logout button on the navbar
            global logoutIcon
            logoutIcon = PhotoImage(file='assets/img/logout_icon.png')
            logout_btn = Button(navs, image=logoutIcon, command=logout, borderwidth=0, bg="white")
            logout_btn.place(x=870,y=3)

            # user details section, display all user info
            global userIcon2
            userIcon2 = PhotoImage(file='assets/img/usericon2.png')
            Label(user_frame, image=userIcon2, borderwidth=0, bg="white").place(x=87,y=130)
            Label(user_frame, text=("Username  : "+username), fg='black', bg='white', font=('Microsoft YaHei UI Light',10,'bold')).place(x=50,y=240)
            Label(user_frame, text=("Full Name  : "+fname), fg='black', bg='white', font=('Microsoft YaHei UI Light',10,'bold')).place(x=50,y=265)
            Label(user_frame, text=("Email        : "+umail), fg='black', bg='white', font=('Microsoft YaHei UI Light',10,'bold')).place(x=50,y=290)
            # set button for change password
            Button(user_frame, width=25, text='Change Password', border=0, bg='#57a1f8', cursor='hand2', fg='white', font=('Microsoft YaHei UI Light', 10), command=changePassword).place(x=38, y=340)

            # user history section
            Label(user_frame, text="User History : ", fg='black', bg='white', font=('Microsoft YaHei UI Light',13,'bold')).place(x=380,y=115)
            # frame for show user history
            SIn_frame = Frame(user_frame, width=480, height= 300, bg="white", borderwidth=1, bd=3, relief=GROOVE)
            SIn_frame.place(x=380, y=150)
            textArea = Text(SIn_frame, font="Robote 12", bg="white", fg="black", relief=GROOVE, wrap=WORD)
            textArea.place(x=0, y=0, width=460, height=293)
            # set scrollbar
            scrollbar1 = Scrollbar(SIn_frame)
            scrollbar1.place(x=460,y=0,height=297)
            scrollbar1.configure(command=textArea.yview)
            textArea.configure(yscrollcommand=scrollbar1.set)
            # set separator for make look like a table
            Frame(SIn_frame ,width=2,height=295,bg='#666666').place(x=75, y=0)
            Frame(SIn_frame ,width=2,height=295,bg='#666666').place(x=145, y=0)
            Frame(SIn_frame ,width=2,height=295,bg='#666666').place(x=313, y=0)

            # open the log file for get history data
            fulr = open("assets/datasets/log.txt", "r")
            fuld = fulr.readlines()
            fulr.close()
            # set head row of history table
            Sdata = " Date          Time         Category                          Details\n"+("_"*50)+"\n"
            textArea.insert(END,Sdata)
            for line in fuld:
                # check all data start with the present username
                if line.startswith(username+" | "):
                    data = line.split(" | ")
                    # set space after all category to make a good align
                    space = 25-len(data[3])
                    match data[3]:
                        case "Loged In":
                            space = 28
                        case "Image Encrypt/Decrypt":
                            space = 4
                        case "Image Steganography":
                            space = 5
                        case "Digital Photo Forensic":
                            space = 4
                        case "Change Password":
                            space = 10
                    # if the detail length is bigger then 17 then resize it 
                    if len(data[4])>17:
                        data[4] = data[4][:7]+"..."+data[4][-5:]
                    # add the colomn in  histroy table
                    Sdata = " "+data[1]+"  "+data[2]+"  "+data[3]+(" "*space)+data[4]
                    textArea.insert(END,Sdata)
                    # insert row separator
                    textArea.insert(END,("-"*90)+"\n")
            textArea.configure(state=DISABLED)

    # navbers
        # set logo in home navbar
        global imgl1
        imgl1 = PhotoImage(file='assets/img/logo1.png')
        logoimg = Label(navh, image=imgl1, bg="white", height=45, width=45)
        logoimg.place(x=25)
        heading = Label(navh, text="Image Security & Analysis", fg='black', bg='white', font=('Microsoft YaHei UI Light',20,'bold'))
        heading.place(x=80, y=3)
        # set logo in other navbar
        Label(navs, image=imgl1, bg="white", height=45, width=45).place(x=395)
        Label(navs, text="ISA", fg='black', bg='white', font=('Microsoft YaHei UI Light',20,'bold')).place(x=460, y=3)
        # set about page button on navbar
        global aboutimg
        aboutimg = PhotoImage(file='assets/img/about.png')
        about_btn = Button(navs, image=aboutimg, command=aboutPage, borderwidth=0, bg="white")
        about_btn.place(x=810,y=3)
        # set user page button on navbar
        global userIcon
        userIcon = PhotoImage(file='assets/img/usericon.png')
        user_btn = Button(navs, image=userIcon, command=userPage, borderwidth=0, bg="white")
        user_btn.place(x=870,y=3)
        # set back button for other page navbar
        global backIcon
        backIcon = PhotoImage(file='assets/img/back_icon.png')
        backIcon_btn = Button(navs, image=backIcon, command=homePage, borderwidth=0, bg="white")
        backIcon_btn.place(x=20,y=3)
        # create navabar separator
        Frame(navs,width=950,height=2,bg='black').place(x=0, y=48)
        Frame(navh,width=950,height=2,bg='black').place(x=0, y=48)

        # function for service page 1 
        def service1_page():
            # function for input image
            def inputImage():
                # function for file Encrypt or decrypt
                def File_EnDe():
                    # get secrect key from input  
                    key = keyIn.get()
                    try:
                        # check key is a number or not if not the show error
                        if len(key) != 4:
                            ccc=int("Check")
                        key2 = key[:2]
                        key2 = int(key2)
                        key3 = key[-2:]
                        key3 = int(key3)
                        key = int(key)
                        # open the image in read binary mode for encrypt/decrypt
                        fi = open(fileS1_name, 'rb')
                        images1 = fi.read()
                        fi.close()

                        # check image is already encrypted or not 
                        by1 = images1.split(bytearray("Encrypted", "utf-8"))
                        
                        # if already encrypted then decrypt it 
                        if images1 != by1[0]:
                            # check secrect key validity
                            newByte3 = str(key2)
                            newByte4 = str(key3)
                            newByte3 = bytearray(newByte3, "utf-8")
                            newByte4 = bytearray(newByte4, "utf-8")
                            newByteCheck = newByte3+newByte4
                            if by1[-1] == newByteCheck:
                                images1 = by1[0]
                                images1 = bytearray(images1)
                                # change image byte data and decrypt it with key 
                                for index, values in enumerate(images1):
                                    images1[index]=values^key2
                                # store and replace the decrypted file 
                                fi1 = open(fileS1_name, 'wb')
                                fi1.write(images1)
                                fi1.close()
                                # entry the log info
                                log_entry(1,fileS1_name2)
                                # show success message
                                messagebox.showinfo("Sucess", "File Decrypted Sucessfully")
                            else:
                                # show error if wrong key input for decrypt
                                messagebox.showerror("Invalid", "Invalid Key")
                        else:
                            # if file is not ecrypted already then encrypt it 
                            images1 = bytearray(images1)
                            # change image byte data and encrypt it with key 
                            for index, values in enumerate(images1):
                                images1[index]=values^key2
                            # store and replace the encrypted file 
                            fi1 = open(fileS1_name, 'wb')
                            newByte1 = "Encrypted"+str(key2)
                            newByte2 = str(key3)
                            newByte1 = bytearray(newByte1, "utf-8")
                            newByte2 = bytearray(newByte2, "utf-8")
                            fi1.write(images1+newByte1+newByte2)
                            fi1.close()
                            # entry the log 
                            log_entry(1,fileS1_name2)
                            messagebox.showinfo("Sucess", "File Encrypted Sucessfully")
                    except Exception as e:
                        # show error if key is not a number or int 
                        messagebox.showerror("Invalid", "Invalid Key, key Must need to be a 4 digit Number")
                
                # input image section
                # set file type for input 
                ftt = (("All File","*.*"),
                        ("PNG file","*.png"),
                        ("JPG File","*.jpg"))
                # input the image
                fileS1 = filedialog.askopenfile(mode="r",initialdir=os.getcwd(), title='Select Image File', filetype=ftt)
                if fileS1 is not None:
                    fileS1_name = fileS1.name
                    # split the file name and resize it for display
                    fileS1_name2 = fileS1_name.split("/")
                    if len(fileS1_name2[-1])<15:
                        fileS1_name2 = fileS1_name2[-1]
                    else:
                        fileS1_name2 = fileS1_name2[-1][:6]+"...."+fileS1_name2[-1][-6:]
                    # display the file name after input the image 
                    Label(service1_frame, text=("File Name\t: "+fileS1_name2), fg='black', bg='white', font=('Microsoft YaHei UI Light',10,'bold')).place(x=596, y=240)

                    # take secret key as input 
                    def on_enter(e):
                        keyIn.delete(0, 'end')
                    def on_leave(e):
                        name = keyIn.get()
                        if name == '':
                            keyIn.insert(0, 'Secret Key')
                    keyIn = Entry(service1_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
                    keyIn.place(x=596, y=277)
                    keyIn.insert(0, 'Secret Key')
                    keyIn.bind('<FocusIn>', on_enter)
                    keyIn.bind('<FocusOut>', on_leave)
                    Frame(service1_frame,width=220,height=2,bg='black').place(x=594, y=305)
                    # Button for encrypt or decrypt
                    Button(service1_frame, width=29, pady=7, text='Encrypt/Decrypt', bg='#57a1f8', cursor='hand2', fg='white', border=0, command=File_EnDe).place(x=600, y=320)

        # service 1 page section 
            # destroy the home page
            service_frame.destroy()
            navh.destroy()
            # set new frame for service 1 page
            service1_frame = Frame(root, width=930, height=460, bg='white').place(x=-3, y=50)
            # set heading
            Label(service1_frame, text="Image Encrypt/Decrypt", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold')).place(x=290, y=65)
            Label(service1_frame, text="Hide your Image for your Safety", fg='black', bg='white', font=('Microsoft YaHei UI Light',10,'bold')).place(x=345, y=110)
            # set a side image for service 1 page
            global imgs1
            imgs1 = PhotoImage(file='assets/img/BgS1.png')
            bgimgs1 = Label(root, image=imgs1, bg="white", height=267, width=400).place(x=50,y=160)
            # set a button for take image as input 
            Button(service1_frame, width=29, pady=7, text='Upload File', bg='#57a1f8', cursor='hand2', fg='white', border=0, command=inputImage).place(x=600, y=320)
            # set a note for user to understand that which type of data he/she need to input
            tls11 = "*Note --> Insert a Image, Picture, Photo File \nwith \nExtention jpg, jpeg, png etc..\nor \nA Encrypted File for Decrypt*"
            Label(service1_frame, text=tls11, bg="white", fg="Black").place(x=587, y=370)

        # function for service 2 page
        def service2_page():
            # function for take input and display it 
            def input_image():
                lbl = Label(service2_frame,bg="black")
                lbl.place(x=100, y=150)
                # input file type
                ftt = (("All File","*.*"),
                        ("PNG file","*.png"),
                        ("JPG File","*.jpg"))
                # take image as input 
                global filename
                filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetype=ftt)
                # resize the input image and display it 
                img=Image.open(filename)
                img = img.resize((200,250))
                img=ImageTk.PhotoImage(img)
                lbl.configure(image=img)
                lbl.image=img

            # function for hide data in image 
            def hideData():
                # function for save hidden data image
                def saveEnImage():
                    # get date and time for rename file with it 
                    x = datetime.datetime.now()
                    ffName = filename.split("/")
                    ffName = ffName[-1].split(".")
                    # save the image
                    saveFileName ="saved file/" + ffName[0]+ "-" + x.strftime("%d%m%y%H%M%S") + ".png"
                    secret.save(saveFileName)
                    ms2 = os.getcwd()
                    ms2 = "File Saved to\n"+ms2+"\\saved file\\"
                    messagebox.showinfo("Save File", ms2)
                    service2_page()

                # get secrect key and message from input 
                key = keyIn.get()
                message = textArea.get(1.0,END)
                try:
                    # test the file
                    fileOK = False
                    fileTest = filename+"ISA"
                    fileOK = True
                except Exception:
                    messagebox.showerror("Invalid", "Insert a Image First")
                
                if fileOK:
                    global secret
                    try:
                        # check that image already have any secrect message
                        clear_message = lsb.reveal(filename)
                        checkPastHide = clear_message.split("|#@#|")
                        if checkPastHide[-1]==key:
                            # if already have any message then check the key
                            message = message + "|#@#|" + key
                            # hide the new message
                            secret = lsb.hide(str(filename), message)
                            fff2 = filename.split("/")
                            # entry the log
                            log_entry(2,fff2[-1])
                            # set button for save image
                            Button(service2_frame, width=12, text='Save Image', border=0, bg='#57a1f8', cursor='hand2', fg='white', font=('Microsoft YaHei UI Light', 14), command=saveEnImage).place(x=330, y=250)
                        else:
                            # show error if key invalid
                            messagebox.showerror("Invalid", "Invalid key")
                    except Exception:
                        # set new message if the image haven't any past message
                        message = message + "|#@#|" + key
                        secret = lsb.hide(str(filename), message)
                        fff2 = filename.split("/")
                        log_entry(2,fff2[-1])
                        # set button for save image
                        Button(service2_frame, width=12, text='Save Image', border=0, bg='#57a1f8', cursor='hand2', fg='white', font=('Microsoft YaHei UI Light', 14), command=saveEnImage).place(x=330, y=250)

            # function for show data from image 
            def showData():
                # get key from input 
                key = keyIn.get()
                try:
                    # test the file 
                    fileTest = filename+"ISA"
                    # reveal the secret message
                    clear_message = lsb.reveal(filename)
                    cml = clear_message.split("|#@#|")
                    # check the key validity
                    if key == cml[-1]:
                        clear_message = cml[0]
                        textArea.delete(1.0, END)
                        fff2 = filename.split("/")
                        # entry the log
                        log_entry(2,fff2[-1])
                        # display the hidden message
                        textArea.insert(END, clear_message)
                    else:
                        messagebox.showerror("Invalid", "Invalid Key")
                except Exception:
                    messagebox.showerror("Invalid", "This image don't have any hidden data.")

        # service 2 section
            # destroy the home page
            service_frame.destroy()
            navh.destroy()
            # set new frame for service 2 
            service2_frame = Frame(root, width=930, height=460, bg='white').place(x=-3, y=50)
            # set a clikable frame for input image
            InImg_frame = Frame(service2_frame, width=200, height= 245, bg="#858689").place(x=100, y=150)
            InImg_btn = Button(InImg_frame, width=28, height= 16, text='Select Image from Device', border=0, cursor='hand2', fg='white', bg="#858689", command=input_image)
            InImg_btn.place(x=100, y=150)
            # set heading
            Label(service2_frame, text="Image Steganography", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold')).place(x=310, y=65)
            Label(service2_frame, text="Hide you Message in the Image", fg='black', bg='white', font=('Microsoft YaHei UI Light',10,'bold')).place(x=365, y=110)
            # set input area for secret message
            SIn_frame = Frame(service2_frame, width=330, height= 250, bg="white", borderwidth=1, bd=3, relief=GROOVE)
            SIn_frame.place(x=500, y=150)
            textArea = Text(SIn_frame, font="Robote 12", bg="white", fg="black", relief=GROOVE, wrap=WORD)
            textArea.place(x=0, y=0, width=310, height=243)
            # set scrollbar
            scrollbar1 = Scrollbar(SIn_frame)
            scrollbar1.place(x=310,y=0,height=247)
            scrollbar1.configure(command=textArea.yview)
            textArea.configure(yscrollcommand=scrollbar1.set)
            # display note for user
            tls21 = "*Note --> Insert a Image, Picture, Photo File \nwith \nExtention jpg, jpeg, png etc..*"
            Label(service2_frame, text=tls21, bg="white", fg="Black").place(x=85, y=420)

            # set input for secrect key
            def on_enter(e):
                keyIn.delete(0, 'end')
            def on_leave(e):
                name = keyIn.get()
                if name == '':
                    keyIn.insert(0, 'Secret Key')
            keyIn = Entry(service2_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
            keyIn.place(x=510, y=403)
            keyIn.insert(0, 'Secret Key')
            keyIn.bind('<FocusIn>', on_enter)
            keyIn.bind('<FocusOut>', on_leave)
            Frame(service2_frame,width=295,height=2,bg='black').place(x=510, y=430)
            # set 2 button for hide and show secret message from image
            Button(service2_frame, width=12, text='Hide Data', border=0, bg='#57a1f8', cursor='hand2', fg='white', font=('Microsoft YaHei UI Light', 14), command=hideData).place(x=510, y=440)
            Button(service2_frame, width=12, text='Show Data', border=0, bg='#57a1f8', cursor='hand2', fg='white', font=('Microsoft YaHei UI Light', 14), command=showData).place(x=685, y=440)
        
        # function for service 3 page
        def service3_page():
            # function for input image
            def input_image():
                # function for get image data
                def getDataImg():
                    # function for save image data
                    def saveDataImg():
                        # set filename for save info.
                        x = datetime.datetime.now()
                        ffName = filename2.split("/")
                        ffName = ffName[-1].split(".")
                        saveFileName ="saved file/" + ffName[0]+ "-" + x.strftime("%d%m%y%H%M%S") + ".txt"
                        # write all data on new file 
                        NFILE = open(saveFileName, "w")
                        NFILE.write("ISA\n\n")
                        for line in output:
                            line = line.decode('ascii').strip()
                            if line.startswith("ExifTool"):
                                continue
                            NFILE.write(line+"\n")
                        NFILE.close()
                        ms3 = os.getcwd()
                        ms3 = "File Saved to\n"+ms3+"\\saved file\\"
                        messagebox.showinfo("Save File", ms3)

                    # user-defined variables
                    exifTool        = "assets/tools/exiftool.exe"
                    filePath        = filename2
                    # run exifTool on one of the files found
                    exifOut = subprocess.Popen( [ exifTool, filePath ],
                                                stdout = subprocess.PIPE, 
                                                stderr = subprocess.STDOUT)
                    # get all the lines of output of command and display it
                    output = exifOut.stdout.readlines()
                    textArea.configure(state=NORMAL)
                    textArea.delete(1.0, END)
                    for line in output:
                        line = line.decode('ascii').strip()
                        if line.startswith("ExifTool"):
                            continue
                        # replace all extra space
                        line = line.replace("  ","")
                        # insert data on display
                        textArea.insert(END, line+"\n")
                        textArea.insert(END, ("-"*90)+"\n")
                    fff2 = filePath.split("/")
                    # entry the log
                    log_entry(3,fff2[-1])
                    textArea.configure(state=DISABLED)
                    # set button for save all data
                    Button(service3_frame, width=28, pady=7, text='Save Data', bg='#57a1f8', cursor='hand2', fg='white', border=0, command=saveDataImg).place(x=657, y=458)

            # input image section
                lbl = Label(service3_frame,bg="black")
                lbl.place(x=70, y=150)
                ftt = (("All File","*.*"),
                        ("PNG file","*.png"),
                        ("JPG File","*.jpg"))
                # get input image
                filename2 = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetype=ftt)
                img=Image.open(filename2)
                # resize the image and display it 
                img = img.resize((200,200))
                img=ImageTk.PhotoImage(img)
                lbl.configure(image=img)
                lbl.image=img
                # set a button for get data
                Frame(service3_frame, width=250, height=150, bg="white").place(x=53, y=368)
                Button(service3_frame, width=28, pady=7, text='Get Data', bg='#57a1f8', cursor='hand2', fg='white', border=0, command=getDataImg).place(x=71, y=370)
                # set note for user 
                tls31 = "*Note --> You will get Data that \nis Embedded with your Photo. \nNot possible to get any Information\n outside of this.*"
                tls31 = Label(service3_frame, text=tls31, bg="white", fg="Black").place(x=73, y=410)

        # service 3 section
            # destroy the home page
            service_frame.destroy()
            navh.destroy()
            # set new frame for service 3 page
            service3_frame = Frame(root, width=930, height=460, bg="white").place(x=-3, y=50)
            # set heading
            Label(service3_frame, text="Digital Photo Forensic", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold')).place(x=290, y=65)
            Label(service3_frame, text="Find Clue in a Photo for your Investigation", fg='black', bg='white', font=('Microsoft YaHei UI Light',10,'bold')).place(x=305, y=110)
            # button for input image
            InImg_btn = Button(service3_frame, width=28, height= 13, text='Select Image from Device', border=0, cursor='hand2', fg='white', bg="#858689", command=input_image).place(x=70, y=150)
            tls31 = "*Note --> Insert a Image, Picture, Photo File \nwith \nExtention jpg, jpeg, png etc..*"
            tls31 = Label(service3_frame, text=tls31, bg="white", fg="Black").place(x=55, y=370)
            # set textarea for display app data from image
            SIn_frame = Frame(service3_frame, width=480, height= 300, bg="white", borderwidth=1, bd=3, relief=GROOVE)
            SIn_frame.place(x=380, y=150)
            textArea = Text(SIn_frame, font="Robote 12", bg="white", fg="black", relief=GROOVE, wrap=WORD)
            textArea.place(x=0, y=0, width=460, height=293)
            scrollbar1 = Scrollbar(SIn_frame)
            scrollbar1.place(x=460,y=0,height=297)
            scrollbar1.configure(command=textArea.yview)
            textArea.configure(yscrollcommand=scrollbar1.set)
            textArea.delete(1.0, END)
            # insert predata
            textArea.insert(END, "\n\n\n\n\n\n\n\tInsert your Image First & Press on Get Data")
            textArea.configure(state=DISABLED)
            
    # home page section
        # set frame for home page
        service_frame = Frame(root, width=930, height=460, bg='white')
        service_frame.place(x=-3, y=50)
        # set background image
        global service_bg
        service_bg = PhotoImage(file='assets/img/service_bg.png')
        SBG = Label(service_frame, image=service_bg, bg="white", borderwidth=0).place(x=0, y=0)
        # set service-1 frame and button 
        global service1_img
        service1_img = PhotoImage(file='assets/img/service1.png')
        service1_btn = Button(service_frame, image=service1_img, command=service1_page, borderwidth=0, bg="#3737af")
        service1_btn.place(x=50,y=50)
        service1_title = Label(service_frame, text="Image\nEncrypt/Decrypt", fg='white', bg='#3c46dc', font=('Microsoft YaHei UI Light',8,'bold'))
        service1_title.place(x=60, y=175)
        # set service-2 frame and button 
        global service2_img
        service2_img = PhotoImage(file='assets/img/service2.png')
        service2_btn = Button(service_frame, image=service2_img, command=service2_page, borderwidth=0, bg="#3737af")
        service2_btn.place(x=220,y=50)
        service2_title = Label(service_frame, text="Image\nSteganography", fg='white', bg='#353dc4', font=('Microsoft YaHei UI Light',8,'bold'))
        service2_title.place(x=232, y=175)
        # set service-3 frame and button 
        global service3_img
        service3_img = PhotoImage(file='assets/img/service3.png')
        service3_btn = Button(service_frame, image=service3_img, command=service3_page, borderwidth=0, bg="#3737af")
        service3_btn.place(x=50,y=230)
        service3_title = Label(service_frame, text="Digital Photo\nForensics", fg='white', bg='#3239bb', font=('Microsoft YaHei UI Light',8,'bold'))
        service3_title.place(x=70, y=355)
        
# login area
    # set new frame for login page
    Mainframe = Frame(root, width=950, height=550, bg='white')
    Mainframe.place(x=-5, y=-5)
    # set side image in loginpage
    img = PhotoImage(file='assets/img/loginX1.png')
    imgx = Label(root, image=img, bg="white", height=350, width=350)
    imgx.place(x=50,y=50)
    # set frame for take inputs
    frame = Frame(root, width=350, height=350, bg='white')
    frame.place(x=480, y=70)
    # set heading
    heading = Label(frame, text="Login", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=125, y=5)

    # set username input area
    def on_enter(e):
        userIn.delete(0, 'end')
    def on_leave(e):
        name = userIn.get()
        if name == '':
            userIn.insert(0, 'Username')
    userIn = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
    userIn.place(x=30, y=80)
    userIn.insert(0, 'Username')
    userIn.bind('<FocusIn>', on_enter)
    userIn.bind('<FocusOut>', on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25, y=107)
    
    # set password input area
    def on_enter(e):
        passIn.delete(0, 'end')
    def on_leave(e):
        Pdata = passIn.get()
        if Pdata == '':
            passIn.insert(0, 'Password')
    passIn = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
    passIn.place(x=30, y=150)
    passIn.insert(0, 'Password')
    passIn.bind('<FocusIn>', on_enter)
    passIn.bind('<FocusOut>', on_leave)
    Frame(frame,width=295,height=2,bg='black').place(x=25, y=177)
    
    # set remember me option for user to login aoutomatically next time 
    agreement = StringVar()
    # set checkbutton
    ckbtn = Checkbutton(frame,
                text='Remember me',
                bg="white",
                variable=agreement,
                onvalue='1',
                offvalue='0')
    ckbtn.deselect()
    ckbtn.place(x=25, y=190)
    # button for login
    Button(frame, width=39, pady=7, text='Login', bg='#57a1f8', cursor='hand2', fg='white', border=0, command=login_check).place(x=35, y=224)
    # set option for sign up
    label = Label(frame, text="Don't have an Account?", fg='black', bg="white", font=('Microsoft YaHei UI Light', 9))
    label.place(x=76, y=270)
    sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign_up)
    sign_up.place(x=215, y=270)

    # check already login status
    flcr=open("assets/datasets/db.txt", "r")
    flcd = flcr.readlines()
    flcr.close()
    for i in flcd:
        if i.startswith("1"):
            i = i.split(" | ")
            username = i[1]
            password = i[2]
            fname = i[3]
            umail = i[4]
            # if anyone login already the redirect to home page
            homePage()

    # Run and Display this application
    root.mainloop()
    
    
# Start this Application
startAPP()



"""
======================================
    Developed by 
  Md. Mosotfa Mahin
github: https://github.com/mostofaahmed101
======================================
"""