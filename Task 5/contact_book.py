import sys
import csv

contacts=[]
def main():
    load_contact()
    while True:
        #user interface
        print("++++++++++CONTACT APP+++++++++++")
        print()
        print("1.View ALL Contacts")
        print("2.Add New Contact")
        print("3.Search Contact")
        print("4.View Saved Contacts")
        print("5.Update Contact Details")
        print("6.Delete Contact")
        print("7.Exit Application")
        print()
        print("++++++++++++++++++++++++++++++++++")
        print()
        action=input("Enter an action example 1 to view contacts\n")
        if action=="1":
            view_contact_list()
            print()
        elif action=="2":
            try:
                add_contact() 
            except:
                print("Could not save new contact")   
        elif action=="3":
            #strip() removed whitespaces
            choice = input("Enter '1' to search by name or '2' to search by number").strip()
            if choice=="1":
                full_name=input("Enter contact name and surname.\t\n")
                try:
                 search_contact_by_name(full_name)
                except:
                    print("Insure you had name and surname separated by space")
            elif choice=="2":
                number=input("Enter contact number to search.\t\n")
                search_contact_by_number(number)
            else:
                print("Invalid input")
        elif action=="4":
            saved_contacts()
        elif action=="5":
            update_contact()
        elif action=="7":
            sys.exit()
            print("Application has been terminated.")
        elif action=="6":
            name = input("Enter the full name of the contact to delete below.\n")
            #checks if user entered name and surname
            try:
                delete_contact(name)
            except IndexError:
                print("Insure to add surname, name and surname should be separated by a space")

        else:
            print("Invalid input-Enter a number from 1 to 7")
def add_contact():
        #input
        name=input("Enter name of new contact below\n").title()
        sur_name=input("Enter surname of new contact below\n").title()
        full_name=name+" "+sur_name
        number=input("Enter number of new contact below\n")
        email=input("Enter email of new contact below\n")
        address=input("Enter address of the new contact below\n")
        #
        if validate_phone_number(number) and (full_name!="") and(email!="") and (address!=""):
            new_contact={"name":full_name,"number":number,"email":email,"address":address}
            contacts.append(new_contact)
            print("Contact Has been saved✔")
            store_contact()
        #2
        print()

def saved_contacts():
    print("===============SAVED CONTACTS=====================")
    print()
    for contact in contacts:
        status = contact['status']
        if status.strip()=="saved":
            print(f"{contact['name']}\t\t\t{contact['number']}")
    print()
    

def view_contact_list():
    print("+============================Contact List=========================")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    for contact in contacts:
        print(f"{contact['name']}\t\t{contact['number']}\t\t{contact['status']}")

def search_contact_by_number(number:str):
    
    print("++++++++++CONTACT INFO+++++++++++")
    print()
    found=False
    for contact in contacts:
        if number ==contact['number']:
            found=True
            print("Full name: ",contact['name'])
            print("Contact Number: ",contact['number'])
            print("Email address: ",contact['email'])
            print("Home address: ",contact['address'])
            break
        
    if not found:
        print(number,"does not exist in your contact")

def search_contact_by_name(name:str):
    print("++++++++++CONTACT INFO+++++++++++")
    print()
    #splits full name into name and surname
    splited = name.split(' ')
    first_name= splited[0]
    sur_name= splited[1]
    full_name=first_name.title()+' '+sur_name.title()
    #
    found=False
    for contact in contacts:
        if full_name ==contact['name']:
            found=True
            print("Full name: ",contact['name'])
            print("Contact Number: ",contact['number'])
            print("Email address: ",contact['email'])
            print("Home address: ",contact['address'])
            break
    #
    if not found:
        print(full_name,"does not exists")

    print()
    

def update_contact():
    print("===================")
    print("1. FUll Name")
    print("2. Contact Number")
    print("3. Email")
    print("4. Address")
    print("5. Status")
    print("======================")
    choice = input("What do you want to update?")
    number=input("Enter the number you want to update details of.\n")
    for contact in contacts:
        if number == contact['number']:
            if choice=="1":
                new_name=input("Enter New contact Full name\n").strip()
                if new_name!="":
                    contact['name']=new_name
            elif choice=="2":
                new_number=input("Enter the Updated contact number.\n").strip()
                if number!="" and len(new_number)==10:
                    contact['number']=new_number
            elif choice=="3":
                new_email=input("Enter Contact's new email.\n").strip()
                if new_email!="":
                    contact['email']=new_email
            elif choice=="4":
                new_add=input("Enter Contact's new updated address.\n").strip()
                if new_add!="":
                    contact['address']=new_add
            elif choice=="5":
                status=input("Would you like to save this contact? Y/N.\n").strip()
                if status!="" and status.upper()=="Y":
                    contact['status']="saved"
                elif status!="" and status.upper()=="N":
                    contact['status']="un-saved"
                else:
                    print("Invalid selection from update. ")
                    sys.exit()
            else:
                print("Invalid Option")
            print()
            print("UPDATED☑")
            break
    store_contact()
        
def delete_contact(name):
    splited = name.split(' ')
    first_name,surname = splited[0], splited[1]
    first_name.title()
    surname.title()
    full_name=first_name+" "+surname
    #removes  contact from list
    found=False
    for contact in contacts:
        if contact['name']==full_name:
            contacts.remove(contact)
            found =True
            print(f"{full_name} with {contact['number']} has been deleted")
            print()
            break
    #checks if contact was not found
    if not found:
        print(f"{full_name} does not exist in your contact")

    if found:
        store_contact()

def store_contact():
    #writes on csv
    with open("contacts.csv","w", newline="")as file:
        fieldnames=contacts[0].keys()#gets the keys of first dictionary in list
        line = csv.DictWriter(file,fieldnames=fieldnames)
        line.writeheader()#writes header on cvs
        line.writerows(contacts)#writes rows
    print()
    print("Contact Stored")
def load_contact():
    #loads contact from csv into dictionary and appends dictionary into list 
    try:#checks if file exists
        with open("contacts.csv","r")as file:
            lines=csv.DictReader(file)
            for line in lines:
                contacts.append(line)
        print("Contacts LOADED")
    except FileNotFoundError:
        print("Contacts were not found")

def validate_phone_number(number:str):
    if len(number)!=10:
        return False
    else:
        return True
if __name__=="__main__":
    main()