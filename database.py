try:
    import psycopg2
except psycopg2.DatabaseError:
    print("AN ERROR OCCOURRED WHILE IMPORTING PSYCOPG2") #TO HELP YOU DEBUG

def conexão():
    try:
        # CONEXÃO 
        global con, cur
        con = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="blackgarden")
        cur = con.cursor()
        print("Conexão realizada!")
    except:
        print("Não foi possível realizar a conexão")

