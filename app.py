import tkinter as tk
import random

app = tk.Tk()
app.title("App")
app.geometry("300x200")

reqapp = tk.Toplevel()
reqapp.title("Requirements")
reqapp.geometry("300x200")
reqapp.withdraw()

feedapp = tk.Toplevel()
feedapp.title("Feedback")
feedapp.geometry("300x200")
feedapp.withdraw()

# kullanıcı 1 (artık gerek yok :D)

# fun = "User"
# fup = "12345"

user = tk.Label(text="Username:")
user.place(x=10, y=10)

user = tk.Label(text="Password:")
user.place(x=13, y=43)

userintf = tk.StringVar()
userlogin = tk.Entry(textvariable=userintf)
userlogin.place(x=80, y=8)

userints = tk.StringVar()
userlogin = tk.Entry(textvariable=userints, show="*")
userlogin.place(x=80, y=41)

coinbox = tk.Label(font="Verdana 20 bold", text="-")
coinbox.place(x=187, y=73)

coin = tk.Label(font="Verdana 18 bold")

cointxt = tk.Label(text="-", font="Verdana 20 bold", fg="White")
cointxt.place(x=40, y=70)

status = tk.Label(font="Verdana 9", text="Status:")
status.place(x=29, y=66)

usernamecharerror = tk.Label(font="Verdana 10 bold", text="Username must contain at least 5 characters!")
passwordcharerror = tk.Label(font="Verdana 10 bold", text="Password must contain at least 8 characters!")
usernamenumleterror = tk.Label(font="Verdana 10 bold", text="Username can only contain numbers and letters.")
passworduppercaseerror = tk.Label(font="Verdana 10 bold", text="Password must contain at least one uppercase letter.")

# req = tk.Label(font="Verdana 9 bold", text="""The values don't meet the
# requirements.""")

ispasswordhidden = True


def togglepasswordvisibility():
    global ispasswordhidden
    if ispasswordhidden:
        userlogin.config(show="")
        pastogb.config(text="‿", width=1)
        ispasswordhidden = False
    else:
        userlogin.config(show="*")
        pastogb.config(text="𓁼", width=1)
        ispasswordhidden = True


def feedentsend():
    userentry = feedent.get("1.0", tk.END)
    print("Your feedback:\n-", userentry)
    feedent.delete("1.0", tk.END)


def coinhide():
    coin.place_forget()


def feedentclear():
    feedent.delete("1.0", tk.END)


def feedentsmaller():
    feedent.config(width=29)
    feedbacksmallerbutton.place_forget()


def feedentlarger():
    feedent.config(width=40)
    feedbacksmallerbutton.place(x=205, y=85)


def cointxthide():
    cointxt.config(font="Verdana 20 bold", text="-", fg="white")
    cointxt.place(x=40, y=70)


def hidereq():
    reqapp.withdraw()


def hidefeed():
    feedapp.withdraw()


reqapp.protocol("WM_DELETE_WINDOW", hidereq)
feedapp.protocol("WM_DELETE_WINDOW", hidefeed)


def reqc():
    reqapp.deiconify()


def feedc():
    feedapp.deiconify()


# def hide():
#     req.place_forget()

def usernamecharerrorhide():
    usernamecharerror.place_forget()


def passwordcharerrorhide():
    passwordcharerror.place_forget()


def usernamenumleterrorhide():
    usernamenumleterror.place_forget()


def passworduppercaseerrorhide():
    passworduppercaseerror.place_forget()


def signc():
    usersigname = userintf.get()
    usersigpas = userints.get()

    usernamecharerrorhide()
    passwordcharerrorhide()
    passworduppercaseerrorhide()
    usernamenumleterrorhide()

    error_y = 100
    has_error = False

    if len(usersigname) < 5:
        print("Error: Username must contain at least 5 characters!")
        usernamecharerror.place(x=1, y=error_y)
        usernamecharerror.after(10000, usernamecharerrorhide)
        error_y += 15
        has_error = True
    if len(usersigpas) < 8:
        print("Error: Password must contain at least 8 characters!")
        passwordcharerror.place(x=1, y=error_y)
        passwordcharerror.after(10000, passwordcharerrorhide)
        error_y += 15
        has_error = True
    if not any(c.isupper() for c in usersigpas):
        print("Error: Password must contain at least one uppercase letter!")
        passworduppercaseerror.place(x=1, y=error_y)
        passworduppercaseerror.after(10000, passworduppercaseerrorhide)
        error_y += 15
        has_error = True
    if not usersigname.isalnum():
        print("Error: Username can only contain letters and numbers!")
        usernamenumleterror.place(x=1, y=error_y)
        usernamenumleterror.after(10000, usernamenumleterrorhide)
        error_y += 15
        has_error = True

    if has_error:
        return

    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                registered_username, _ = line.strip().split(",")
                if usersigname == registered_username:
                    print("This user already exists!")
                    return

        with open("data.txt", "a") as file:
            file.write(f"{usersigname},{usersigpas}\n")
        print("A user created an account successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def feedback():
    print("")


def loginc():
    use = userintf.get()
    pas = userints.get()

    try:
        with open("data.txt") as file:
            lines = file.readlines()
            for line in lines:
                registered_username, registered_password = line.strip().split(",")
                if use == registered_username and pas == registered_password:
                    print("Correct!")
                    coin.config(text="✓", fg="lime")
                    coin.place(x=185, y=73)
                    cointxt.config(font="Verdana 12 bold", text="Correct!", fg="lime")
                    cointxt.place(x=17, y=76)
                    cointxt.after(3333, cointxthide)
                    coin.after(3333, coinhide)

                    print(f"""Kullanıcı Adı: {use}
        Şifre: {pas}""")

                    inapp = tk.Toplevel()
                    inapp.title("App")
                    inapp.geometry("2000x1140")
                    inapp.withdraw()

                    def startinapp():
                        inapp.deiconify()

                    def stopnotnecappwork():
                        reqapp.withdraw()
                        feedapp.withdraw()
                        app.withdraw()

                    def quitinapp():
                        app.quit()

                    def logout():
                        app.deiconify()
                        inapp.withdraw()

                    app.after(5000, startinapp)
                    inapp.after(5001, stopnotnecappwork)

                    inapp.protocol("WM_DELETE_WINDOW", quitinapp)

                    randomcolor = ["white", "red", "green", "blue", "yellow", "cyan", "magenta", "orange", "purple"]
                    randomchosencolor = random.choice(randomcolor)

                    welcometext = tk.Label(inapp, font="Verdana 100 bold", text="WELCOME", fg=randomchosencolor)
                    welcometext.place(x=0, y=0)

                    def center_label():
                        # Pencerenin genişlik ve yükseklik değerlerini al
                        window_width = inapp.winfo_width()
                        window_height = inapp.winfo_height()

                        # Label'in genişlik ve yüksekliğini al
                        label_width = welcometext.winfo_reqwidth()
                        label_height = welcometext.winfo_reqheight()

                        # x ve y koordinatlarını hesapla
                        x = (window_width - label_width) / 2  # Pencerenin yatay merkez noktası
                        y = (window_height - label_height) / 2  # Pencerenin dikey merkez noktası

                        # Label'i yeni konumuna yerleştir
                        welcometext.place(x=x, y=y)

                    inapp.bind('<Configure>', lambda event: center_label())

                    logoutbutton = tk.Button(inapp, text="Log Out", command=logout)
                    logoutbutton.place(x=1332,y=1)

                    return

        print("Incorrect!")
        coin.config(text="✗", fg="red")
        coin.place(x=187, y=72)
        cointxt.config(font="Verdana 12 bold", text="Incorrect!", fg="red")
        cointxt.place(x=11, y=76)
        cointxt.after(3333, cointxthide)
        coin.after(3333, coinhide)

    except FileNotFoundError:
        print("There is no user registered with that username and password!")
        print("Please create another account.")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

    print(f"""Kullanıcı Adı: {use}
        Şifre: {pas}""")


def quitdef():
    app.quit()


userlb = tk.Button(text="Log In", command=loginc)
userlb.place(x=203, y=72)

usersb = tk.Button(text="Sign Up", command=signc)
usersb.place(x=103, y=72)

pastogb = tk.Button(text="𓁼", command=togglepasswordvisibility, width=1)
pastogb.place(x=230, y=40)

feedbackbutton = tk.Button(reqapp, text="Feedback", command=feedc)
feedbackbutton.place(x=1, y=169)

secondfeedbackbutton = tk.Button(text="   Feedback   ", command=feedc)
secondfeedbackbutton.place(x=180, y=169)

feedlabel = tk.Label(feedapp, text="Type your feedback in the blank.")
feedlabel.place(x=4, y=1)

feedent = tk.Text(feedapp, width=29, height=4)
feedent.place(x=1, y=25)

feedbacksendbutton = tk.Button(feedapp, text="Send", command=feedentsend)
feedbacksendbutton.place(x=3, y=85)

feedbackclearbutton = tk.Button(feedapp, text="Clear", command=feedentclear)
feedbackclearbutton.place(x=67, y=85)

feedbacklargerbutton = tk.Button(feedapp, text="Larger", command=feedentlarger)
feedbacklargerbutton.place(x=132, y=85)

feedbacksmallerbutton = tk.Button(feedapp, text="Smaller", command=feedentsmaller)

reqb = tk.Button(text="Requirements", command=reqc)
reqb.place(x=62, y=169)

userqb = tk.Button(text="Quit", command=quitdef)
userqb.place(x=2, y=169)

# requirements app'i

reqapl1 = tk.Label(reqapp, font="Verdana 10 bold", text="1 - Username must be at least 5 characters.")
reqapl1.place(x=2, y=3)
reqapl2 = tk.Label(reqapp, font="Verdana 10 bold", text="2 - Password must be at least 8 characters.")
reqapl2.place(x=2, y=18)
reqapl3 = tk.Label(reqapp, font="Verdana 10 bold", text="3 - Username can only contain numbers and letters.")
reqapl3.place(x=2, y=33)
reqapl4 = tk.Label(reqapp, font="Verdana 10 bold", text="4 - Password must contain at least one uppercase letter.")
reqapl4.place(x=2, y=48)

app.mainloop()

