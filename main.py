import sys

import mysql.connector as sql
                                                                                                                             #connecting sql to python
conn = sql.connect(host='Harshils-MacBook-Pro.local', user='root', passwd='Ganesh@2019', database='Rent_a_Car')
if conn.is_connected():
    print("Successfully Connected")
c1 = conn.cursor()

print("******************************************************")
print("*                                                    *")
print("*******************   WELCOME   **********************")
print("*                                                    *")
print("******************************************************")


class CAR_RENTAL:

    def home(self):                                                             #homepage options

        print("1. Employee Login")
        print("2. Registrtion(Employee)")
        print("3. Details Of Vehicle")
        print("4. About XYZ rent a car")
        print("5. Contact Details")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if (choice == 1):
            self.login()
            self.emp_login()

        if (choice == 2):
            self.login()
            self.new_eid()

        if (choice == 3):
            self.login()
            self.vehicles()

        if (choice == 4):
            self.about()

        if (choice == 5):
            self.contact()

        if (choice == 6):
            self.exit()

        else:
            print("Please select a Valid Input(1-6).")
            print("--------------------Thankyou--------------------------")
            self.home()

    def login(self):

        password = input("Enter Password to Proceed: ")
        if (password == "harshil"):
            print("Access Granted")
        else:
            print("Access Denied")
            self.login()

    def approval(self):

        x = input("Are you sure you want to proceed? (y/n)")
        if (x == "y"):
            print("Mission Successful")

        else:
            print("Mission Failed")
            self.home()

    def emp_login(self):

        print("1. Create New Customer ID")
        print("2. Update Customer Info")
        print("3. Delete Customer Info")
        print("4. Update Employee Info")
        print("5. Delete Employee Info")
        print("6. View Employee list")
        print("7. View Customer list")
        print("8. Back")

        choice1 = int(input("Enter your choice: "))

        if (choice1 == 1):
            self.login()
            self.new_cid()

        if (choice1 == 2):
            self.login()
            self.update_cid()

        if (choice1 == 3):
            self.login()
            self.del_cid()

        if (choice1 == 4):
            self.login()
            self.update_eid()

        if (choice1 == 5):
            self.login()
            self.del_eid()

        if (choice1 == 6):
            self.login()
            self.emp_table()

        if (choice1 == 7):
            self.login()
            self.cus_table()

        if (choice1 == 8):
            self.home()

        else:
            print("Wrong Input")

            self.home()

    def new_cid(self):

        Cus_ID = int(input("Enter Customer ID: "))
        Cus_Name = input("Enter Customer Name: ")
        C_Address = input("Enter Customer Address: ")
        C_Number = input("Enter Customer Contact: ")
        C_Gender = input("Enter Customer Gender: ")
        Support_Emp_ID = input("Enter ID of Support Staff: ")

        print("\n")
        print("C_ID:", C_ID1)
        print("C_NAME:", C_NAME1)
        print("C_ADDRESS:", C_ADDRESS1)
        print("C_CONTACT:", C_CONTACT1)
        print("C_GENDER:", C_GENDER1)
        print("SUPPORT_E_ID:", SUPPORT_E_ID1)
        print("\n")

        self.approval()

        c1.execute("INSERT INTO CUSTOMERS VALUES(%s, %s, %s, %s, %s, %s)",
                   (Cus_ID, C_Name, C_Address, C_Number, C_Gender, Support_Emp_ID))
        conn.commit()

        print("Customer Info Successfully Added!")
        print("\n")
        print("What do you want to do?")
        print("1. Create another customer ID")
        print("2. Back")
        print("\n")

        c = int(input("Enter your choice: "))

        if (c == 1):
            print("\t\t------------------------------------------------------\t\t")
            self.new_cid()

        if (c == 2):
            print("------------------------------------------------------")
            self.emp_login()

    def update_cid(self): #customer id updation

        Cus_ID= int(input("Enter the ID of Customer to be updated: "))

        c1.execute("SELECT * FROM CUSTOMERS WHERE Cus_ID=" + str(Cus_ID))
        customer = c1.fetchall()
        for row in customer:
            print(row)

        print("What do you want to update?")
        print("\n")
        print("1. Name")
        print("2. Address")
        print("3. Contact")
        print("4. Gender")
        print("5. Support Employee ID")
        print("6. All of the above")
        print("7. Go back")

        ch = int(input("Enter Your Choice: "))

        if (ch == 1):

            C_Name = input("Enter Updated Customer Name: ")
            print("\n")
            print("Updated Cus_Name:", C_Name)
            print("\n")

            self.approval()

            p1 = "UPDATE CUSTOMERS SET Cus_Name=%s WHERE Cus_ID=%s"
            p2 = (C_Name, Cus_ID)
            c1.execute(p1, p2)
            conn.commit()

            print("Customer Info Updated Successfully!")
            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_cid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch == 2):

            Cus_Address = input("Enter Updated Customer Address: ")
            print("\n")
            print("Updated Cus_ADDRESS:", Cus_Address)
            print("\n")

            self.approval()

            q1 = "UPDATE CUSTOMERS SET Cus_Address=%s WHERE Cus_ID=%s"
            q2 = (Cus_Address, Cus_ID)
            c1.execute(q1, q2)
            conn.commit()

            print("Customer Info Updated Successfully!")
            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_cid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch == 3):

            Cus_Number = input("Enter Updated Customer Contact: ")
            print("\n")
            print("Updated Cus_Number:", Cus_Number)
            print("\n")

            self.approval()

            r1 = "UPDATE CUSTOMERS SET Cus_Number=%s WHERE Cus_ID=%s"
            r2 = (Cus_Number, Cus_ID)
            c1.execute(r1, r2)
            conn.commit()

            print("Customer Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_cid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch == 4):

            Cus_Gender = input("Enter Updated Customer Gender: ")
            print("\n")
            print("Updated Cus_Gender:", Cus_Gender)
            print("\n")

            self.approval()

            s1 = "UPDATE CUSTOMERS SET Cus_Gender=%s WHERE Cus_ID=%s"
            s2 = (C_Gender, Cus_ID)
            c1.execute(s1, s2)
            conn.commit()

            print("Customer Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_cid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch == 5):

            Support_Emp_ID = input("Enter Updated ID of Support Staff: ")
            print("\n")
            print("Updated SUPPORT_Emp_ID:", Support_Emp_ID)
            print("\n")

            self.approval()

            t1 = "UPDATE CUSTOMERS SET Support_Emp_ID=%s WHERE Cus_ID=%s"
            t2 = (Support_Emp_ID, Cus_ID1)
            c1.execute(t1, t2)
            conn.commit()

            print("Customer Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_cid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch == 6):

            Cus_Name = input("Enter Updated Customer Name: ")
            Cus_Address = input("Enter Updated Customer Address: ")
            Cus_Number = input("Enter Updated Customer Contact: ")
            Cus_Gender = input("Enter Updated Customer Gender: ")
            Support_Emp_ID= input("Enter Updated ID of Support Staff: ")

            print("\n")
            print("Customer ID to be updated:", Cus_ID)
            print("Updated C_NAME:", Cus_Name)
            print("Updated C_ADDRESS:", Cus_Address)
            print("Updated C_CONTACT:", Cus_Number)
            print("Updated C_GENDER:", Cus_Gender)
            print("Updated SUPPORT_E_ID:", Support_Emp_ID)
            print("\n")

            self.approval()

            p1 = "UPDATE CUSTOMERS SET Cus_Name=%s WHERE Cus_ID=%s"
            p2 = (Cus_Name, Cus_ID)
            c1.execute(p1, p2)
            q1 = "UPDATE CUSTOMERS SET Cus_Address=%s WHERE Cus_ID=%s"
            q2 = (Cus_Address, Cus_ID)
            c1.execute(q1, q2)
            r1 = "UPDATE CUSTOMERS SET Cus_Number=%s WHERE Cus_ID=%s"
            r2 = (Cus_Number, Cus_ID)
            c1.execute(r1, r2)
            s1 = "UPDATE CUSTOMERS SET C_Gender=%s WHERE Cus_ID=%s"
            s2 = (Cus_Gender, Cus_ID)
            c1.execute(s1, s2)
            t1 = "UPDATE CUSTOMERS SET Support_Emp_ID=%s WHERE Cus_ID=%s"
            t2 = (Support_Emp_ID, Cus_ID)
            c1.execute(t1, t2)

            conn.commit()

            print("Customer Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_cid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch == 7):
            self.emp_login()

        else:
            print("Wrong Input")
            self.update_cid()

    def del_cid(self):

        delete = int(input("Enter Customer ID to be deleted: "))

        c1.execute("SELECT * FROM CUSTOMERS WHERE Cus_ID=" + str(delete))

        employee = c1.fetchall()
        for row in employee:
            print(row)

        self.approval()

        c1.execute("DELETE FROM CUSTOMERS WHERE Cus_ID=" + str(delete))
        conn.commit()

        print("Customer Info Deleted Successfully!")

        print("\n")
        print("What do you want to do?")
        print("1. Delete another one")
        print("2. Back")

        c2 = int(input("Enter your choice: "))

        if (c2 == 1):
            print("------------------------------------------------------")
            self.del_cid()

        if (c2 == 2):
            print("------------------------------------------------------")
            self.emp_login()

    def update_eid(self):

        E_ID1 = int(input("Enter Employee ID to be updated: "))

        c1.execute("SELECT * FROM EMPLOYEES WHERE Emp_ID=" + str(E_ID1))
        customer = c1.fetchall()
        for row in customer:
            print(row)

        print("What do you want to update?")
        print("\n")
        print("1. Name")
        print("2. Address")
        print("3. Contact")
        print("4. Gender")
        print("5. Username")
        print("6. Password")
        print("7. All of the above")
        print("8. Go back")

        ch1 = int(input("Enter your choice: "))

        if (ch1 == 1):

            Emp_Name = input("Enter Updated Employee Name: ")
            print("\n")
            print("Updated E_NAME:", Emp_Name)
            print("\n")

            self.approval()

            a1 = "UPDATE EMPLOYEES SET Emp_Name=%s WHERE Emp_ID=%s"
            a2 = (Emp_Name, Emp_ID)
            c1.execute(a1, a2)
            conn.commit()

            print("Employee Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("\t\t------------------------------------------------------\t\t")
                self.update_eid()

            if (c2 == 2):
                print("\t\t------------------------------------------------------\t\t")
                self.emp_login()

        if (ch1 == 2):

            Emp_Address = input("Enter Updated Employee Address: ")
            print("\n")
            print("Updated E_ADDRESS:", Emp_Address)
            print("\n")

            self.approval()

            b1 = "UPDATE EMPLOYEES SET Emp_Address=%s WHERE Emp_ID=%s"
            b2 = (Emp_Address, Emp_ID)
            c1.execute(b1, b2)
            conn.commit()

            print("Employee Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_eid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch1 == 3):

            Emp_Contact = input("Enter Updated Employee Contact: ")
            print("\n")
            print("Updated Emp_Contact:", Emp_Contact)
            print("\n")

            self.approval()

            d1 = "UPDATE EMPLOYEES SET Emp_Contact=%sWHERE Emp_ID=%s"
            d2 = (Emp_Contact, Emp_ID)
            c1.execute(d1, d2)
            conn.commit()

            print("Employee Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_eid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch1 == 4):

            Emp_Gender = input("Enter Updated Employee Gender: ")
            print("\n")
            print("Updated Emp_Gender:", Emp_Gender)
            print("\n")

            self.approval()

            e1 = "UPDATE EMPLOYEES SET Emp_Gender=%sWHERE Emp_ID=%s"
            e2 = (Emp_Gender, Emp_ID)
            c1.execute(e1, e2)
            conn.commit()

            print("Employee Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("\t\t------------------------------------------------------\t\t")
                self.update_eid()

            if (c2 == 2):
                print("\t\t------------------------------------------------------\t\t")
                self.emp_login()

        if (ch1 == 5):

            USERNAME1 = input("Enter Updated Username: ")
            print("\n")
            print("Updated USERNAME:", USERNAME1)
            print("\n")

            self.approval()

            f1 = "UPDATE EMPLOYEES SET USERNAME=%s WHERE Emp_ID=%s"
            f2 = (USERNAME1, Emp_ID)
            c1.execute(f1, f2)
            conn.commit()

            print("Employee Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_eid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch1 == 6):

            PASSWORD1 = input("Enter Updated Password: ")
            print("\n")
            print("Updated PASSWORD:", PASSWORD1)
            print("\n")

            self.approval()

            g1 = "UPDATE EMPLOYEES SET PASSWORD=%sWHERE Emp_ID=%s"
            g2 = (PASSWORD1, Emp_ID)
            c1.execute(g1, g2)
            conn.commit()

            print("Employee Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_eid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch1 == 7):

            Emp_Name = input("Enter Updated Employee Name: ")
            Emo_Address = input("Enter Updated Employee Address: ")
            Emp_Contact = input("Enter Updated Employee Contact: ")
            Emp_Gender = input("Enter Updated Employee Gender: ")
            USERNAME1 = input("Enter Updated Username: ")
            PASSWORD1 = input("Enter Updated Password: ")

            print("\n")
            print("Employee ID to be updated:", Emp_ID)
            print("Updated E_NAME:", Emp_Name)
            print("Updated E_ADDRESS:", Emp_Address)
            print("Updated E_CONTACT:", Emp_Contact)
            print("Updated E_GENDER:", Emp_Gender)
            print("Updated USERNAME:", USERNAME1)
            print("Updated PASSWORD:", PASSWORD1)
            print("\n")

            self.approval()

            a1 = "UPDATE EMPLOYEES SET Emp_Name=%s WHERE Emp_ID=%s"
            a2 = (Emp_Name, Emp_ID)
            c1.execute(a1, a2)
            b1 = "UPDATE EMPLOYEES SET Emp_Address=%s WHERE Emp_ID=%s"
            b2 = (Emp_Address, Emp_ID)
            c1.execute(b1, b2)
            d1 = "UPDATE EMPLOYEES SET Emp_Contact=%sWHERE Emp_ID=%s"
            d2 = (Emp_Contact, Emp_ID)
            c1.execute(d1, d2)
            e1 = "UPDATE EMPLOYEES SET Emp_Gender=%sWHERE Emp_ID=%s"
            e2 = (Emp_Gender, Emp_ID)
            c1.execute(e1, e2)
            f1 = "UPDATE EMPLOYEES SET USERNAME=%s WHERE Emp_ID=%s"
            f2 = (USERNAME1, Emp_ID1)
            c1.execute(f1, f2)
            g1 = "UPDATE EMPLOYEES SET PASSWORD=%sWHERE Emp_ID=%s"
            g2 = (PASSWORD1, E_ID1)
            c1.execute(g1, g2)

            conn.commit()

            print("Employee Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_eid()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.emp_login()

        if (ch1 == 8):
            self.emp_login()

        else:
            print("Wrong Input")
            self.update_eid()

    def del_eid(self):

        ID = int(input("Enter the Emp_ID to be deleted: "))

        c1.execute("SELECT * FROM EMPLOYEES WHERE Emp_ID=" + str(ID))
        employee = c1.fetchall()
        for row in employee:
            print(row)

        self.approval()

        c1.execute("DELETE FROM EMPLOYEES WHERE Emp_ID=" + str(ID))
        conn.commit()

        print("Employee Info Deleted Successfully!")

        print("\n")
        print("What do you want to do?")
        print("1. Delete another one")
        print("2. Back")

        c2 = int(input("Enter your choice: "))

        if (c2 == 1):
            print("------------------------------------------------------")
            self.del_eid()

        if (c2 == 2):
            print("------------------------------------------------------")
            self.emp_login()

    def emp_table(self):

        c1.execute("SELECT * FROM EMPLOYEES")
        e_table = c1.fetchall()
        for e_row in e_table:
            print(e_row)

        print("------------------------------------------------------")

        self.emp_login()

    def cus_table(self):

        c1.execute("SELECT * FROM CUSTOMERS")
        c_table = c1.fetchall()
        for c_row in c_table:
            print(c_row)

        print("------------------------------------------------------")

        self.emp_login()

    def new_eid(self):

        Emp_ID = int(input("Enter Employee ID: "))
        Emp_Name = input("Enter Employee Name: ")
        Emp_Address= input("Enter Employee Address: ")
        Emp_Contact = input("Enter Employee Contact: ")
        Emp_Gender = input("Enter Employee Gender: ")
        USERNAME = input("Enter Username: ")
        PASSWORD = input("Enter Password: ")

        print("\n")
        print("E_ID:", Emp_ID)
        print("E_NAME:", Emp_Name)
        print("E_ADDRESS:", Emp_Address)
        print("E_CONTACT:", Emp_Contact)
        print("E_GENDER:", Emp_Gender)
        print("USERNAME:", USERNAME)
        print("Password:", PASSWORD)
        print("\n")

        self.approval()

        c1.execute("INSERT INTO EMPLOYEES VALUES(%s, %s, %s, %s, %s, %s, %s)",
                   (Emp_ID, Emp_Name, Emp_Address, Emp_Contact, Emp_Gender, USERNAME, PASSWORD))
        conn.commit()

        print("Employee Info Successfully Added!")
        print("\n")
        print("What do you want to do?")
        print("1. Create another employee ID")
        print("2. Back")
        print("\n")

        c = int(input("Enter your choice: "))

        if (c == 1):
            print("------------------------------------------------------")
            self.new_eid()

        if (c == 2):
            print("------------------------------------------------------")
            self.home()

    def vehicles(self):

        print("1. View Vehicle Details")
        print("2. View Rental Details")
        print("3. Add vehicle info")
        print("4. Update vehicle info")
        print("5. Delete vehicle info")
        print("6. Add Rental Detail")
        print("7. Approximate Rent Calculator")
        print("8. Back")

        choice3 = int(input("Enter your choice: "))

        if (choice3 == 1):
            self.veh_table()

        if (choice3 == 2):
            self.veh_log()

        if (choice3 == 3):
            self.add_vehicle()

        if (choice3 == 4):
            self.update_vehicle()

        if (choice3 == 5):
            self.del_vehicle()

        if (choice3 == 6):
            self.add_vehiclelog()

        if (choice3 == 7):
            self.calculator()

        if (choice3 == 8):
            print("------------------------------------------------------")
            self.home()

        else:
            print("Wrong Input")
            print("------------------------------------------------------")
            self.vehicles()

    def veh_table(self):

        self.login()

        c1.execute("SELECT * FROM VEHICLES")
        v_table = c1.fetchall()
        for v_row in v_table:
            print(v_row)

        print("------------------------------------------------------")

        self.vehicles()

    def veh_log(self):

        self.login()

        c1.execute("SELECT * FROM VEHICLE_LOG")
        log_table = c1.fetchall()
        for log_row in log_table:
            print(log_row)

        print("------------------------------------------------------")

        self.vehicles()

    def add_vehicle(self):

        self.login()

        Vehicle_NO = input("Enter Vehicle Number: ")
        Model = input("Enter Vehicle Model: ")
        Driver = input("Enter Driver's Name: ")
        Capacity = input("Enter Vehicle Capacity: ")
        Manufacture_Year = input("Enter Vehicle's Year of Manufacture: ")
        Price_per_Day = input("Enter Vehicle's price/day: ")

        print("\n")
        print("V_NO:", Vehicle_NO)
        print("Model:", Model)
        print("Driver:", Driver)
        print("Capacity:", Capacity)
        print("Manufacture_Year:", Manufacture_Year)
        print("Price_per_Day:", Price_per_Day)
        print("\n")

        self.approval()

        c1.execute("INSERT INTO VEHICLES VALUES(%s, %s, %s, %s, %s, %s)",
                   (Vehicle_NO, Model, Driver, Capacity, Manufacture_Year, Price_per_Day))
        conn.commit()

        print("Vehicle Info Added Successfully!")

        print("\n")
        print("What do you want to do?")
        print("1. Add another one")
        print("2. Back")

        c2 = int(input("Enter your choice: "))

        if (c2 == 1):
            print("------------------------------------------------------")
            self.add_vehicle()

        if (c2 == 2):
            print("------------------------------------------------------")
            self.vehicles()

    def update_vehicle(self):

        self.login()

        Vehicle_NO = input("Enter the Vehicle Number to update its info in single quotations(' '): ")

        c1.execute("SELECT * FROM VEHICLES WHERE Vehicle_NO=" + str(Vehicle_NO))
        vehicle = c1.fetchall()
        for row in vehicle:
            print(row)

        Vehicle_NO1 = input("Enter the Vehicle Number above without (' '): ")

        print("What do you want to update?")
        print("\n")
        print("1. Model")
        print("2. Driver")
        print("3. Capacity")
        print("4. Year of Manufacture")
        print("5. Price/Day")
        print("6. All of the above")
        print("7. Go back")

        ch2 = int(input("Enter your choice: "))

        if (ch2 == 1):

            Model = input("Enter Updated Vehicle Model: ")
            print("\n")
            print("Updated Model:", Model)
            print("\n")

            self.approval()

            a3 = "UPDATE VEHICLES SET Model=%s WHERE Vehicle_NO=%s"
            a4 = (Model, Vehicle_NO1)
            c1.execute(a3, a4)
            conn.commit()

            print("Vehicle Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_vehicle()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.vehicles()

        if (ch2 == 2):

            Driver4 = input("Enter Updated Driver's Name: ")
            print("\n")
            print("Updated Driver:", Driver4)
            print("\n")

            self.approval()

            b3 = "UPDATE VEHICLES SET Driver=%s WHERE V_NO=%s"
            b4 = (Driver4, Vehicle_NO1)
            c1.execute(b3, b4)
            conn.commit()

            print("Vehicle Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_vehicle()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.vehicles()

        if (ch2 == 3):

            Capacity4 = input("Enter Updated Vehicle Capacity: ")
            print("\n")
            print("Updated Capacity:", Capacity4)
            print("\n")

            self.approval()

            d3 = "UPDATE VEHICLES SET Capacity=%sWHERE Vehicle_NO=%s"
            d4 = (Capacity4, Vehicle_NO1)
            c1.execute(d3, d4)
            conn.commit()

            print("Vehicle Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_vehicle()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.vehicles()

        if (ch2 == 4):

            Manufacture_Year4 = input("Enter Updated Vehicle's Year of Manufacture: ")
            print("\n")
            print("Updated Manufacture_Year:", Manufacture_Year4)
            print("\n")

            self.approval()

            e3 = "UPDATE VEHICLES SET Manufacture_Year=%sWHERE Vehicle_NO=%s"
            e4 = (Manufacture_Year4, V_NOx)
            c1.execute(e3, e4)
            conn.commit()

            print("Vehicle Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_vehicle()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.vehicles()

        if (ch2 == 5):

            Price_per_Day4 = input("Enter Updated Vehicle's Price/Day: ")
            print("\n")
            print("Updated Price_per_Day:", Price_per_Day4)
            print("\n")

            self.approval()

            f3 = "UPDATE VEHICLES SET Price_per_Day=%s WHERE Vehicle_NO=%s"
            f4 = (Price_per_Day4, Vehicle_NO1)
            c1.execute(f3, f4)
            conn.commit()

            print("Vehicle Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_vehicle()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.vehicles()

        if (ch2 == 6):

            Model = input("Enter Updated Vehicle Model: ")
            Driver4 = input("Enter Updated Driver's Name: ")
            Capacity4 = input("Enter Updated Vehicle Capacity: ")
            Manufacture_Year4 = input("Enter Updated Vehicle's Year of Manufacture: ")
            Price_per_Day4 = input("Enter Updated Vehicle's Price/Day: ")

            print("\n")
            print("Vehicle Number to be updated:", Vehicle_NO1)
            print("Updated Model:", Model)
            print("Updated Driver:", Driver4)
            print("Updated Capacity:", Capacity4)
            print("Updated Manufacture_Year:", Manufacture_Year4)
            print("Updated Price_per_Day:", Price_per_Day4)
            print("\n")

            self.approval()

            a3 = "UPDATE VEHICLES SET Model=%s WHERE V_NO=%s"
            a4 = (Model, Vehicle_NO1)
            c1.execute(a3, a4)
            b3 = "UPDATE VEHICLES SET Driver=%s WHERE V_NO=%s"
            b4 = (Driver4, Vehicle_NO1)
            c1.execute(b3, b4)
            d3 = "UPDATE VEHICLES SET Capacity=%sWHERE V_NO=%s"
            d4 = (Capacity4, Vehicle_NO1)
            c1.execute(d3, d4)
            e3 = "UPDATE VEHICLES SET Manufacture_Year=%sWHERE V_NO=%s"
            e4 = (Manufacture_Year4, Vehicle_NO1)
            c1.execute(e3, e4)
            f3 = "UPDATE VEHICLES SET Price_per_Day=%s WHERE V_NO=%s"
            f4 = (Price_per_Day4, Vehicle_NO1)
            c1.execute(f3, f4)

            conn.commit()

            print("Vehicle Info Updated Successfully!")

            print("\n")
            print("What do you want to do?")
            print("1. Update again/further")
            print("2. Back")

            c2 = int(input("Enter your choice: "))

            if (c2 == 1):
                print("------------------------------------------------------")
                self.update_vehicle()

            if (c2 == 2):
                print("------------------------------------------------------")
                self.vehicles()

        if (ch2 == 7):
            print("------------------------------------------------------")
            self.vehicles()

        else:
            print("Wrong Input")
            print("------------------------------------------------------")
            self.update_vehicle()

    def del_vehicle(self):

        self.login()

        NO = input("Enter the Vehicle_NO to be deleted in single quotations(' '): ")

        c1.execute("SELECT * FROM VEHICLES WHERE Vehicle_NO=" + str(NO))
        vehicle = c1.fetchall()
        for row in vehicle:
            print(row)

        self.approval()

        c1.execute("DELETE FROM VEHICLES WHERE Vehicle_NO=" + str(NO))
        conn.commit()

        print("Vehicle Info Deleted Successfully!")

        print("\n")
        print("What do you want to do?")
        print("1. Delete another one")
        print("2. Back")

        c2 = int(input("Enter your choice: "))

        if (c2 == 1):
            print("------------------------------------------------------")
            self.del_vehicle()

        if (c2 == 2):
            print("------------------------------------------------------")
            self.vehicles()

    def new_vehiclelog(self):

        self.login()

        Vehicle_NO6 = input("Enter Vehicle Number: ")
        Model6 = input("Enter Vehicle Model: ")
        Date_of_Rental6 = input("Enter Date of Rental: ")
        Date_of_Return6 = input("Enter Date of Return: ")
        Total_Days6 = input("Enter Total days: ")
        Cus_ID6 = input("Enter Customer ID: ")
        Total_Fare6 = input("Enter the Total Fare: ")

        print("\n")
        print("V_NO:", Vehicle_NO6)
        print("Model:", Model6)
        print("Date_of_Rental:", Date_of_Rental6)
        print("Date_of_Return:", Date_of_Return6)
        print("Total_Days:", Total_Days6)
        print("C_ID:", C_ID6)
        print("Total_Fare:", Total_Fare6)
        print("\n")

        self.approval()

        c1.execute("INSERT INTO VEHICLE_LOG VALUES(%s, %s, %s, %s, %s, %s, %s)",
                   (Vehicle_NO6, Model6, Date_of_Rental, Date_of_Return6, Total_Days, Cus_ID6, Total_Fare6))
        conn.commit()

        print("Rental Info Added Successfully!")

        print("\n")
        print("What do you want to do?")
        print("1. Add another one")
        print("2. Back")

        c2 = int(input("Enter your choice: "))

        if (c2 == 1):
            print("------------------------------------------------------")
            self.new_vehiclelog()

        if (c2 == 2):
            print("------------------------------------------------------")
            self.vehicles()

    def calculator(self):

        self.login()

        ppd = int(input("Enter the price/day for you selected vehicle: "))
        td = int(input("Enter the total period of your rental in days: "))
        tf = ppd * td
        print("Your approximate cost for renting the car of your choice is", tf)

        print("\n")
        print("What do you want to do?")
        print("1. Calculate again")
        print("2. Back")

        c2 = int(input("Enter your choice: "))

        if (c2 == 1):
            print("------------------------------------------------------")
            self.calculator()

        if (c2 == 2):
            print("------------------------------------------------------")
            self.vehicles()

    def about(self):
        with open("About.txt") as f1:
            about = f1.read()

        print("\n")
        print(about)
        print("\n")

        print("------------------------------------------------------")

        self.home()

    def contact(self):

        with open("Contact.txt") as f2:
            contact = f2.read()

        print("\n")
        print(contact)
        print("\n")

        print("------------------------------------------------------")

        self.home()

    def exit(self):

        z = input("Are you sure you want exit? (y/n)")
        if (z == "y"):
            print("Exit Successful")
            print("------------------------------------------------------")
            sys.exit()

        else:
            print("Exit Failed")
            print("------------------------------------------------------")
            self.home()


var = CAR_RENTAL()
var.home()
var.login()
var.approval()
var.emp_login()
var.new_cid()
var.update_cid()
var.del_cid()
var.update_eid()
var.del_eid()
var.emp_table()
var.cus_table()
var.new_eid()
var.vehicles()
var.veh_table()
var.veh_log()
var.add_vehicle()
var.update_vehicle()
var.del_vehicle()
var.new_vehiclelog()
var.calculator()
var.about()
var.contact()
var.exit()
