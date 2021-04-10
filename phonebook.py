import sqlite3
conn = sqlite3.connect("phonebook.sqlite")
cur = conn.cursor()

print('''
----------------------------------------------------------
                PYTHON PHONEBOOK
----------------------------------------------------------''')

def create_db():
    cur.execute('''
    CREATE TABLE contacts (
        "key" INTEGER UNIQUE,
        "name" TEXT NOT NULL,
        "phone" TEXT NOT NULL,
        "email" TEXT,
        "dob" TEXT
        PRIMARY KEY("key" AUTOINCREMENT)
    )
    ''')

def menu():
    print("\nMAIN MENU\n")
    print("1.Find Contact\n2.Add Contact\n3.All Contacts\n4.Exit")
    choice = input("Select Code: ")
    if choice == "1":
        find_contact()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        cnt_lst = cur.execute('SELECT * FROM contacts')
        view_contact(cnt_lst)
    elif choice == "4":
        quit()
    else:
        print("Wrong input. Try again.")
        menu()

def find_contact():
    print("\nFIND CONTACT\n")
    print("Find contact by:\n1.Name\n2.Number\n3.Email\n4.DOB")
    choice = input("Select Code: ")
    if choice == "1":
        query = input("Enter name to find contact: ")
        cur.execute('SELECT * FROM contacts WHERE name = ?', (query,))
        view_contact(cur.fetchall())
    elif choice == "2":
        query = input("Enter phone number to find contact: ")
        cur.execute('SELECT * FROM contacts WHERE phone = ?', (query,))
        view_contact(cur.fetchall())
    elif choice == "3":
        query = input("Enter email to find contact: ")
        cur.execute('SELECT * FROM contacts WHERE email = ?', (query,))
        view_contact(cur.fetchall())
    elif choice == "4":
        query = input("Enter DOB to find contact: ")
        cur.execute('SELECT * FROM contacts WHERE dob = ?', (query,))
        view_contact(cur.fetchall())
    else:
        print("\nWrong input. Try again.")
        find_contact()

def add_contact():
    print("\nADD CONTACT\n")
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email: ")
    dob = input("Enter contact DOB: ")
    cur.execute('INSERT INTO contacts (name, phone, email, dob) VALUES (?, ?, ?, ?)', (name, phone, email, dob))
    print("\nContact added successfully.\n")
    cur.execute('SELECT * FROM contacts ORDER BY key DESC LIMIT 1')
    view_contact(cur.fetchall())

def view_contact(cnt_lst, all=False):
    print("{:^20}   {:^20}   {:^20}   {:^20}".format("Name", "Phone", "Email", "DOB"))
    print("{:^20}   {:^20}   {:^20}   {:^20}".format("-------", "-------", "-------", "-------"))
    if all == False:
        for cnt in cnt_lst:
            print("{:^20}   {:^20}   {:^20}   {:^20}".format(cnt[1], cnt[2], cnt[3], cnt[4]))
        choice = input("\n1.Update contact\n2.Delete contact\n3.Main menu\n4.Exit\nEnter code:")
        if choice == "1":
            if len(cnt_lst) == 1:
                update_contact(cnt_lst[0])
            else:
                choice = int(input("Select the contact to be updated (1/2/3): "))
                update_contact(cnt_lst[choice-1])
        elif choice == "2":
            if len(cnt_lst) == 1:
                delete_contact(cnt_lst[0])
            else:
                choice = int(input("Select the contact to be deleted (1/2/3): "))
                delete_contact(cnt_lst[choice-1])
        elif choice == "3":
            menu()
        elif choice == "4":
            quit()
        else:
            print("Wrong input. Going back to main menu.")
            menu()
    if all == True:
        choice = input("\n1.Main menu\n2.Exit\nEnter code:")
        if choice == "1":
            menu()
        elif choice == "2":
            quit()
        else:
            print("Wrong input. Going back to main menu.")
            menu()

def update_contact(cnt_lst):
    print("UPDATE CONTACT\n1.Name   2.Phone   3.Email   4.DOB   5.Back\n")
    choice = input("Select the field to be updated: ")
    if choice == "1":
        new_data = input("Enter new name: ")
        cur.execute('UPDATE contacts SET name = ? WHERE key = ?', (new_data, cnt_lst[0]))
        conn.commit()
        print("Contact updated successfully.")
    elif choice == "2":
        new_data = int(input("Enter new phone number: "))
        cur.execute('UPDATE contacts SET phone = ? WHERE key = ?', (new_data, cnt_lst[0]))
        conn.commit()
        print("Contact updated successfully.")
        menu()
    elif choice == "3":
        new_data = input("Enter new email: ")
        cur.execute('UPDATE contacts SET email = ? WHERE key = ?', (new_data, cnt_lst[0]))
        conn.commit()
        print("Contact updated successfully.")
        menu()
    elif choice == "4":
        new_data = input("Enter  new DOB: ")
        cur.execute('UPDATE contacts SET dob = ? WHERE key = ?', (new_data, cnt_lst[0]))
        conn.commit()
        menu()
        print("Contact updated successfully.")
    elif choice == "5":
        menu()
    else:
        print("Wrong input. Try again.")

def delete_contact(cnt_lst):
    print("Deleting contact")
    cur.execute('DELETE FROM "contacts" WHERE key = ?', (cnt_lst[0], ))
    conn.commit()
    print("Contact deleted successfully.")
    menu()

def quit():
    print("Exiting program...")
    print("Thank for using Python Phonebook.")
    conn.close()

menu()