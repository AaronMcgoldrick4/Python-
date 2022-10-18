d
ef openfile():

    #Variables
    f = open("database.txt", "a")
    productID = input("What is the product ID? ")
    productname = input("What is the product name? ")
    productprice = float(input("What is the product price exl VAT? "))
    productpriceVAT = float(productprice * 1.20)
    productprice = str(productprice)
    productpriceVAT = str(productpriceVAT)
    productlocation = ("")
#writing to file
    f.write(" | ProductID: ")
    f.write(productID)
    f.write(" | Name: ")
    f.write(productname)
    f.write(" | Product price: £")
    f.write(productprice)
    f.write(" | Product price inc VAT: £")
    f.write(productpriceVAT)
    f.write("\n")
#menu creation

def searchcontents():
    f = open("database.txt", "r")
    choice = input("How do you want to search for the product: 1: Product ID or 2: Product name? ")
    if choice == "1":
        productID = input("Enter Product ID: ")
        with open("database.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.find(productID) != -1:
                    print(line)
                else:
                    print("Item not found in database")     
    elif choice == "2":
        productname = str(input("what is the product name? "))
        with open("database.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.find(productname) != -1:
                    print(line)
                else:
                    print("Item could not be found!")
                          
    else:
        print("This is not valid ")
        searchcontents()
#allows user to search for product

def menu():
    choice = input("1) View dataset\n2) Add new product\n3) Search product\n")
    print(choice)

    if choice == "1":
        f = open("datasbase.txt", "r")
        contents = f.read()
        print(contents)

    elif choice == "2":
        openfile()

    elif choice == "3":
        searchcontents()
    elif choice == "4":
        print("
        


menu()
    
