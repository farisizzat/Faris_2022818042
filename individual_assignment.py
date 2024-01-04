import tkinter as tk
import array
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="electric_device_registration"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()



# Function to handle the calculation and database saving
def SUBMIT():
    Student_name = Student_name_entry.get()
    Student_id_number = Student_id_number_entry.get()
    Student_room_number = Student_room_number_entry.get()
    Student_college = Student_college_combobox.get()
    Student_gender = Student_gender_combobox.get()
    Student_total_device = int(Student_total_device_entry.get())
    
    # Calculate the total price
    total_price = Student_total_device * 10
    
    # To print information on terminal
    print("id_student", Student_id_number)
    print("name", Student_name)
    print("room number", Student_room_number)
    print("college" , Student_college)
    print("gender" , Student_gender)
    print("Total Price = RM" , total_price)

    sql = "INSERT INTO registration_information (Student_name, Student_id_number, Student_room_number, Student_college, Student_gender, Student_total_device, total_price ) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (Student_name, Student_id_number, Student_room_number, Student_college, Student_gender, Student_total_device, total_price )
    mycursor.execute(sql, val)
    mydb.commit()
    
    # To Print back The output. It will happen in the function collect_data(). The f before the string indicates an f-string in Python. 
    output_Student.config(text=f"Total Price : RM{total_price}")

    
   
    
#create window
root = tk.Tk()
root.geometry("520x490")
root.title("student electric device registration"  )
root.configure (bg="#808080")

label = tk.Label(root, text='Electric Device registration', font=("Times New Romans",14, "bold"))
label.grid(column= 4, row=39 , pady=37)


#student_info

Student_name = tk.Label(root,text=("Name"))
Student_name.grid(row=3, column=3 )
Student_name_entry=tk.Entry(root)
Student_name_entry.grid(row=4, column=3)

Student_id_number = tk.Label(root,text=("id number"))
Student_id_number.grid(row=3, column=5)
Student_id_number_entry=tk.Entry(root)
Student_id_number_entry.grid(row=4, column=5)

Student_room_number = tk.Label(root,text=("room number"))
Student_room_number.grid(row=5, column=3)
Student_room_number_entry=tk.Entry(root)
Student_room_number_entry.grid(row=6, column=3)

Student_college = tk.Label(root,text=("college"))
Student_college.grid(row=5, column=5)
Student_college_combobox=ttk.Combobox(root , values= ["Melati" , "Malinja" , "Mawar"])
Student_college_combobox.grid(row=6, column=5)

Student_gender = tk.Label(root,text=("gender"))
Student_gender.grid(row=11, column=4)
Student_gender_combobox=ttk.Combobox (root, values= ["Men" , "Women"])
Student_gender_combobox.grid(row=12, column=4)

price_text=tk.Text(root, height=7 , width=16)
price_text.grid(row=20, column=4)

price_text.insert(tk.END, "Device Price:\n\n")
price_text.insert(tk.END, "One Electric\n Device:\n Price:RM10\n\n")


Student_total_device = tk.Label(root,text=("Total Device"))
Student_total_device.grid(row=23, column=4)
Student_total_device_entry=tk.Entry(root)
Student_total_device_entry.grid(row=24, column=4)

# Output Result
Student = tk.Label(root, text='Total', font=("Times New Romans",12))
Student.grid(row=25, column=4)
output_Student = tk.Label(root, text="")
output_Student.grid(row = 31, column = 4)

# Submit Button
create_table_button=tk.Button(root,text=("SUBMIT"), command=SUBMIT)
create_table_button.grid(row=27, column= 4)
root.mainloop()


    
