print("                    CONTACT BOOK                    ")
contact_book={}


while True:
    
    print("1. Add Contact             2. View Contact List")
    print("3. Update Contact          4. Delete Contact")
    print("5. Exit\n")

    print("               Choose Option               ")
    user=input()
    if user=="1":
        print("\n     Add Contact     ")
        name=input("Name: ")
        p_number=int(input("Enter Number: "))
        email=input("Enter Email: ")
        address=input("Enter Address: ")
        contact_book[name]={"Number":p_number,"Email":email,"Address":address} 
        print("\n                    SAVED SUCCESSFULLY                   \n")
    
    
    elif user=="2":
        print("\n     View Contact List     ")
        if contact_book:
            for name, details in contact_book.items():
                print("\n-----------------------------")
                print(f"Name : {name}")
                print(f"Number : {details['Number']}")
                print(f"Email : {details['Email']}")
                print(f"Address : {details['Address']}")
   
                print("-----------------------------\n")
        else:
            print("Contact Not found\n")
                
        
        
    elif user=="3":
        print("\n     Update Contact     ")
        name=input("Name : ")
        if name in contact_book:
            p_number=int(input("Number : "))
            email=input("Email : ")
            address=input("Address : ")            
            contact_book[name]={"Number":p_number,"Email":email,"Address":address}
            print(f"\n{name}\n                    UPDATED SUCCESSFULLY                   \n")
        else:
            print("\n          Contact Not Found!         \n")
      
    elif user=="4":
        name=input("Name: ")
        if name in contact_book:
            del contact_book[name]
            print("                    DELETED SUCCESSFULLY                   \n")
        else:
            print("          Contact Not Found          \n")
        
        
    elif user=="5":
         print("------------------------\n          Exit          \n------------------------")
         break
    else:
        print("          Invalid Choice         \n        Please Enter Choice \n   -----------------------------\n")
              