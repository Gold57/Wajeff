from tkinter import*
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost', password='@Mosemuthoni57', user='Mosenje', db='wajeff')
    if conn.is_connected():
        print("connection established....\n")
except Error as e:
    print("could not make a connection")

def printer():
    try:
        cursor = conn.cursor()
        query = """
        select name from food;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        for m in result:
            m = str(m)
            m = m.replace("('", "")
            m = m.replace("',)", "")
            food_list.insert(END, m)
    except Error as err:
        print(f"Error: '{err}'")

def printer2():
    try:
        cursor = conn.cursor()
        query = """
        select quantity from food;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        for m in result:
            m = str(m)
            m = m.replace("(", "")
            m = m.replace(",)", "")
            price_list.insert(END, m)
    except Error as err:
        print(f"Error: '{err}'")
def submitter():
    cursor = conn.cursor()
    selected = food_list.curselection()
    selc = food_list.get(selected)
    insertstmt =(
    " insert into orders (detail, num) values(%s, %s) "
    )
    data = (selc,1)
    try:
        cursor.execute(insertstmt, data)
        print("success")
        print(selc)
    except Error as err:
        print(f"Error: '{err}'")

def reducer():
    cursor = conn.cursor()
    selected = food_list.curselection()
    selc = food_list.get(selected)
    try:
        query = "SELECT quantity FROM food WHERE name = ?"
        v = (query, (selc,))
        v = str(v)
        v = v.replace("?', ('", "")
        v = v.replace("?', ('", "")
        print(v)
        cursor.execute(v)
        result = cursor.fetchall()
        result = str(result)
        print(result)
        print("Query successfull..")
    except Error as err:
        print(f"Error: '{err}'")


root =Tk()
root.title('DataFrame')
root.geometry("570x500")
#list for the foods stuff
food_list = Listbox(root, selectmode=SINGLE,relief=FLAT, activestyle=DOTBOX , cursor='hand2',bg='purple', highlightcolor= 'orange', fg='white', font= ('Georgia', 15), height=7, width=12, selectbackground='gray', selectforeground='black')
food_list.grid(padx=2, pady=25)

price_list = Listbox(root, selectmode=SINGLE,relief=FLAT, activestyle=DOTBOX , cursor='hand2',bg='purple', highlightcolor= 'orange', fg='white', font= ('Georgia', 15), height=7, width=12, selectbackground='gray', selectforeground='black')
price_list.place(relx=0.25, rely=0.05)

printer()
printer2()

label1 = Label(root, text="FOOD MENU", fg='white', bg='purple')
label1.place(relx=0.0, rely=0.0)

label2 = Label(root, text="Quantity", fg='white', bg='purple')
label2.place(relx=0.3, rely=0.0)

submit = Button(root, text="SUBMIT", fg="blue", command=reducer)
submit.place(relx=0.4, rely=0.63)

mainloop()