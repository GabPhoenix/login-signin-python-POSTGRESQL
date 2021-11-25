import teste1 as t1
import sys
import tkinter as tk
import database as db
import psycopg2

class Main:
    def __init__(self):
        self.setup_ui = t1.UISigninLogin()

        #DATA BASE CONNECTION CALL 
        db.conexão()
        

if __name__ == "__main__":
    app = Main()
    tk.mainloop()
    sys.exit(0)