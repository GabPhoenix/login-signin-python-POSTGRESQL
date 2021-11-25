try:
    import tkinter as tk #Import module tkinter (from python version above 2.0)
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk #Import module Tkinter (from python version bellow 3.0)

#DATABASE POSTGRESQL
import tkinter
import database as db
import psycopg2

class UISigninLogin:
    def __init__(self):
        self.login()

    def login(self):
        self.back = tk.Tk()
        self.back.geometry("300x450+500+100")
        self.back.configure(background="#2F2F2F")
        self.back.resizable(False, False)

        self.labell = tk.Label(self.back)
        self.labell.place(x=10, y=50, width=280, height=60)
        self.labell.configure(
            background="#2F2F2F",
            foreground="#FFF",
            font="-family {Seoge UI} -size 40 -weight bold",
            text="Login"
        )

        self.lb_name = tk.Label(self.back)
        self.lb_name.place(x=10, y=125, width=120, height=40)
        self.lb_name.configure(
            background="#2F2F2F",
            foreground="#FFF",
            font="-family {Seoge UI} -size 17 -weight bold",
            text="Username:"
        )

        self.entry_nome_login = tk.Entry(self.back)
        self.entry_nome_login.place(x=10, y=180, width=280, height=40)
        self.entry_nome_login.configure(
            background="#FFF",
            foreground="#000",
            font="-family {Seoge UI} -size 17 -weight bold",
        )

        self.lb_pw = tk.Label(self.back)
        self.lb_pw.place(x=10, y=225, width=120, height=40)
        self.lb_pw.configure(
            background="#2F2F2F",
            foreground="#FFF",
            font="-family {Seoge UI} -size 17 -weight bold",
            text="Password:"
        )

        self.entry_pw_login = tk.Entry(self.back)
        self.entry_pw_login.place(x=10, y=270, width=280, height=40)
        self.entry_pw_login.configure(
            background="#FFF",
            foreground="#000",
            font="-family {Seoge UI} -size 17 -weight bold",
            show="•"
        )

        self.btn_login = tk.Button(self.back)
        self.btn_login.place(x=30, y=335, width=240, height=40)
        self.btn_login.configure(
            background="#FFF",
            foreground="#2F2F2F",
            font="-family {Seoge UI} -size 17 -weight bold",
            text="Login",
            activeforeground="#FFF",
            activebackground="#2F2F2F",
            cursor="hand2",
            relief="flat",
            command=self.command_login
        )

        self.btn_call_login = tk.Button(self.back)
        self.btn_call_login.place(x=30, y=385, width=240, height=40)
        self.btn_call_login.configure(
            background="#2F2F2F",
            foreground="#FFF",
            font="-family {Seoge UI} -size 10 -weight bold",
            text="Havent an account? Sign up here",
            activeforeground="#FFF",
            activebackground="#2F2F2F",
            cursor="hand2",
            relief="flat",
            command=self.switch_lg_sg
        )

    def switch_lg_sg(self):
        self.signin()    


    def command_login(self):
        # VERIFICATION IF ENTRIES FIELDS AREN'T NULL
        if self.entry_nome_login.get() != "" and self.entry_pw_login.get() != "": 
            try:
                us = str(self.entry_nome_login.get()) #PICK VALUE FROM USERNAME
                pw = str(self.entry_pw_login.get()) #PICK VALUE FROM PASSWORD
                # SQL COMMAND TO ACESS DATABASE AND READ username AND userpassword FIELDS
                db.cur.execute("SELECT userpassword FROM funcionarios WHERE username = '{}'".format(us))
                password = db.cur.fetchall() # GET PASSWORD
                # VERIFICATION IF PASSOWRD FIELD INFORMATION IS EQUALS TO PASSWORD FIELD FROM DATABASE
                if pw == password[0][0]: #CLEAR PASSOWORD "WITHOUT [()]"
                    # IF TRUE IT WILL CALLS MAIN WINDOW AND CLOSE LOGIN WINDOW
                    self.back.destroy() 
                    self.main_window()
                    db.cur.close() # CLOSE CURSOR
                    db.con.close() # CLOSE CONNECTION
                else:
                    # MESSAGEBOX 
                    # INCORRECT PASSWORD
                    messagebox.showerror(title="ERROR", message="INCORRECT PASSWORD \n Please, try again!")
                    return False
            except psycopg2.DatabaseError:
                # ERROR IN DATABASE CONECTION
                return False
            except:
                # INCORRECT USERNAME
                messagebox.showerror(title="ERROR", message="INCORRECT Username \n Please, try again!")
                return False
        else:
            return False


    def signin(self):
        self.back.destroy()
        self.backsg = tk.Tk()
        self.backsg.geometry("300x450+500+100")
        self.backsg.configure(background="#2F2F2F")
        self.backsg.resizable(False, False)

        self.labell = tk.Label(self.backsg)
        self.labell.place(x=10, y=50, width=280, height=60)
        self.labell.configure(
            background="#2F2F2F",
            foreground="#FFF",
            font="-family {Seoge UI} -size 40 -weight bold",
            text="Sign in"
        )

        self.lb_name = tk.Label(self.backsg)
        self.lb_name.place(x=10, y=125, width=120, height=40)
        self.lb_name.configure(
            background="#2F2F2F",
            foreground="#FFF",
            font="-family {Seoge UI} -size 17 -weight bold",
            text="Username:"
        )

        self.entry_nome_sgn = tk.Entry(self.backsg)
        self.entry_nome_sgn.place(x=10, y=180, width=280, height=40)
        self.entry_nome_sgn.configure(
            background="#FFF",
            foreground="#000",
            font="-family {Seoge UI} -size 17 -weight bold",
        )

        self.lb_pw = tk.Label(self.backsg)
        self.lb_pw.place(x=10, y=225, width=120, height=40)
        self.lb_pw.configure(
            background="#2F2F2F",
            foreground="#FFF",
            font="-family {Seoge UI} -size 17 -weight bold",
            text="Password:"
        )

        self.entry_pw_sgn = tk.Entry(self.backsg)
        self.entry_pw_sgn.place(x=10, y=270, width=280, height=40)
        self.entry_pw_sgn.configure(
            background="#FFF",
            foreground="#000",
            font="-family {Seoge UI} -size 17 -weight bold",
            show="•"
        )

        self.btn_sgn = tk.Button(self.backsg)
        self.btn_sgn.place(x=30, y=335, width=240, height=40)
        self.btn_sgn.configure(
            background="#FFF",
            foreground="#2F2F2F",
            font="-family {Seoge UI} -size 17 -weight bold",
            text="Sign in",
            activeforeground="#FFF",
            activebackground="#2F2F2F",
            cursor="hand2",
            relief="flat",
            command=self.command_signin
        )

        self.btn_call_sgn = tk.Button(self.backsg)
        self.btn_call_sgn.place(x=30, y=385, width=240, height=40)
        self.btn_call_sgn.configure(
            background="#2F2F2F",
            foreground="#FFF",
            font="-family {Seoge UI} -size 10 -weight bold",
            text="Have an account? Login here",
            activeforeground="#FFF",
            activebackground="#2F2F2F",
            cursor="hand2",
            relief="flat",
            command= self.switch_sg_lg
        )


    def switch_sg_lg(self):
        self.backsg.destroy()
        self.login()


    # SIGN IN FUNCIOTION (CALLS SQL)
    def command_signin(self):
        # VERIFICATION IF ENTRIES FIELDS AREN'T NULL
        if self.entry_nome_sgn.get() != "" and self.entry_pw_sgn.get() != "": 
            us = str(self.entry_nome_sgn.get()) #PICK VALUE FROM USERNAME
            pw = str(self.entry_pw_sgn.get()) #PICK VALUE FROM PASSWORD 
            try:
                # EXECUTE COMMAND TO INSERT VALUES INTO TABLE (FUNCIONARIOS)
                db.cur.execute("INSERT INTO funcionarios (personid, username, userpassword) VALUES (default, %s, %s)", (us, pw))
                db.con.commit() # COMMIT UPDATE
                messagebox.showinfo(title="SING-IN", message="COMPLETED SIGN-IG! \n Please Login now!")
                self.backsg.destroy()
                self.login()
            except psycopg2.DatabaseError: 
                # ERROR IN DATABASE CONECTION
                return False
        else:
            # MESSAGE ERROR
            # IT WILL CALLED TO DON'T LET FILL NULL FIELDS IN DATABASE
            messagebox.showerror(title="ERROR", message="PEASE, FILL THE FIELDS!")
            return False

    #MAIN WINDOW
    def main_window(self):
        self.main_back = tk.Tk()
        self.main_back.geometry("1000x600+50+50")
        self.main_back.configure(background="#000")