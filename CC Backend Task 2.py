#ADMIN Password is Admin123
item_list_id_name={1151:"Acer Aspire 3 Laptop",1152:'Lenovo IdeaPad Slim 1',1153:'Dell 15 (2021) Ryzen 3-3250U',1251:'Samsung Galaxy M53 5G',1252:'Redmi A1',1253:'OnePlus Nord 2T 5G',1351:'SanDisk Cruzer Blade 32GB',1352:'HP v236w USB 2.0 64GB',1353:'SanDisk Ultra Flair 128GB',2151:'Masala',2152:'Salted',2153:'Cream and onion',2251:'50-50',2252:'Monaco',2253:'Milkbikies',2351:'Dairy milk',2352:'5 star',2353:'Kit Kat',3151:'Pentonic',3152:'Goldex',3153:'Claro gel',3251:'Doms',3252:'Apsara',3253:'Nataraj',3351:'Apsara',3352:'Doms',3353:'Funblast',4151:'Dettol',4152:'Nivea',4153:'Cinthanol',4251:'3 Boxes',4351:'Joy',4352:'Vaseline',4353:'Nivea',5151:'3 Buckets(Ratan Plastics)',5152:'Cello',5153:'Nayasa',5251:'Kuber pack of 4',5252:'Milton Pack of 3',5253:'Doveaz pack of 1',5351:'Kuber pack of 3',5352:'Signoware single',5353:'Nakonda'}
item_list_id_price={1151:33990,1152:31017,1153:33714,1251:24999,1252:6199,1253:28999,1351:299,1352:468,1353:959,2151:20,2152:20,2153:20,2251:15,2252:20,2253:10,2351:50,2352:20,2353:20,3151:5,3152:7,3153:5,3251:5,3252:5,3253:3,3351:7,3352:5,3353:10,4151:80,4152:65,4153:50,4251:300,4351:180,4352:240,4353:370,5151:1052,5152:300,5153:700,5251:199,5252:230,5253:180,5351:359,5352:260,5353:80}
item_list_id_discount={1151:0.02,1152:0.02,1153:0.02,1251:0.02,1252:0.02,1253:0.02,1351:0.02,1352:0.02,1353:0.02,2151:0.01,2152:0.01,2153:0.01,2251:0.01,2252:0.01,2253:0.01,2351:0.01,2352:0.01,2353:0.01,3151:0.005,3152:0.005,3153:0.005,3251:0.005,3252:0.005,3253:0.005,3351:0.005,3352:0.005,3353:0.005,4151:0.04,4152:0.04,4153:0.04,4251:0.04,4351:0.04,4352:0.04,4353:0.04,5151:0.05,5152:0.05,5153:0.05,5251:0.05,5252:0.05,5253:0.05,5351:0.05,5352:0.05,5353:0.05}
item_list_name_id = dict(zip(item_list_id_name.values(), item_list_id_name.keys()))
a=0
b=0
from datetime import datetime
class akshay:
    def __init__(self,electronics,food,stationery,toiletries,plastics):
        self.electronics=electronics
        self.food=food
        self.stationery=stationery
        self.toiletries=toiletries
        self.plastics=plastics
        self.takenitem=dict()
        self.item_name=dict()

    def display(self):
        c2=int(input('Enter \n1 for Electronics\n2 for Food items\n3 for Stationery\n4 for Toiletries\n5 for Plastics\n'))
        n=1
        if c2==1:
            for item in self.electronics:
                print('{}: {}'.format(n, item))
                n=n+1
        elif c2==2:
            for item in self.food:
                print('{}: {}'.format(n, item))
                n=n+1
        elif c2==3:
            for item in self.stationery:
                print('{}: {}'.format(n, item))
                n=n+1
        elif c2==4:
            for item in self.toiletries:
                print('{}: {}'.format(n, item))
                n=n+1
        elif c2==5:
            for item in self.plastics:
                print('{}: {}'.format(n, item))
                n=n+1
        else:
            print("Wrong input!Please try again")
            exit()

    def addtocart(self):
        add=int(input(print("Enter 1 if you want to add by ID number\n2 if you want to add by item name")))
        if add==1:
            id=int(input("Enter ID of the product: "))
            quantity=int(input("Enter the quantity of product "))
            self.takenitem.update({id: quantity})
            self.item_name.update({item_list_id_name.get(id): quantity})
        elif add==2:
            product_name=input("Enter product name ")
            quantity = int(input("Enter the quantity of product "))
            self.item_name.update({product_name: quantity})
            self.takenitem.update({item_list_name_id.get(product_name): quantity})
        print("Item added to cart!!")

    def displaydiscount(self):
        print("The discount on Electronic items is 2% of each item\nThe discount on Food items is 1% of each item\nThe discount on Stationery items is 0.5% of each item")
        print("The discount on Toiletries is 4% of each item\nThe discount on Plastic items is 5% of each item\nSpecial discounts: ")
        print("1 If total amount is between Rs 1000 and Rs 2000 then a discount of 1% on total\n2 If total amount is between Rs 2000 and Rs 3000 then a discount of 2% on total")
        print("3 If total amount is between Rs 3000 and Rs 5000 then a discount of 5% on total\n4 If total amount is above 5000 then a discount of 10% on total")

    def delete_item(self):
        delete=int(input("Enter the ID of the product you want to remove from the cart "))
        self.takenitem.pop(delete)
        self.item_name.pop(item_list_id_name.get(delete))
        print("Item removed from cart ")

    def displaybill(self,id4,names,bhavan,roomno):
        print ("Item Name"+" "*5+"Quantity"+" "*4+"Item total"+" "*4+"Amount saved ")
        for attribute, value in self.item_name.items():
            temp_id=item_list_name_id.get(attribute)
            print('{} : {}'.format(attribute, value)+" : "+str((item_list_id_price.get(temp_id)*self.item_name.get(attribute)))+" : "+str((item_list_id_discount.get(temp_id)*(item_list_id_price.get(temp_id))*(self.takenitem.get(temp_id)))))
        print("\n")
        total=0
        total2=0
        for item in self.takenitem.keys():
            total=total+((item_list_id_price.get(item))*(self.takenitem.get(item)))-(item_list_id_discount.get(item)*(item_list_id_price.get(item))*(self.takenitem.get(item)))
            total2 = total2 + ((item_list_id_price.get(item)) * (self.takenitem.get(item)))
        if (1000<=total<=2000):
            total=total-(0.01*total)
            print(f"Congratulations you saved Rs {0.01*total+(total2-total)}!!")
        if (2000<total<=3000):
            total=total-(0.02*total)
            print(f"Congratulations you saved Rs {0.02*total+(total2-total)}!!")
        if (3000<total<=5000):
            total=total-(0.05*total)
            print(f"Congratulations you saved Rs {0.05*total+(total2-total)}!!")
        if (5000<total):
            total=total-(0.1*total)
            print(f"Congratulations you saved Rs {(0.1*total)+(total2-total)}!!")
        print(f"\nYour Total amount to be paid is Rs {total+(0.18*total)}")
        print("\nThe tax incurred is:\n"+" "*21+f"9% SGST {0.09*total}\n"+" "*21+f"9% CGST {0.09*total}"+"\n\n")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("Date and time =", dt_string)
        if a==1:
            print("Login type : By ID")
            print(f"Thank you for shopping with us {id4}")
        elif a==2:
            print("Login type : By Name")
            print(f"Thank you for shopping with us {names}")
        elif a==3:
            print("Login type : By Bhavan and Room number")
            print("Thank you for shopping with us")
        feedback = input("Please give us feedback of your experience at our store ")
        pay=int(input(print("Enter\n1 if you want money to be deducted from swd account\n2 if you want to pay in cash\n3 if you want to pay through UPI\n")))
        if pay==1 and a==1:
            pass
        elif pay==1:
            id5=input("Enter your ID ")
        elif pay==2:
            print(f"Please pay Rs {total+(0.18*total)} at the counter ")
        elif pay==3:
            print("Please scan the QR displayed on the counter ")
        else:
            print("Wrong input!Please try again")
            exit()
        print("Thank you for your valuable feedback!\nDo visit again!!")
        exit()

itemlist= akshay(['Laptop\n1151 Acer Aspire 3 Laptop--Rs 33,990\n1152 Lenovo IdeaPad Slim 1--Rs 31,017\n1153 Dell 15 (2021) Ryzen 3-3250U--Rs 33,714','Mobiles\n1251 Samsung Galaxy M53 5G--Rs 6,199\n1252 Redmi A1 Rs 6,199\n1253 OnePlus Nord 2T 5G Rs 28,999','Pendrives\n1351 SanDisk Cruzer Blade 32GB Rs 299\n1352 HP v236w USB 2.0 64GB Rs 468\n1353 SanDisk Ultra Flair 128GB Rs 959'],['Lays\n2151 Masala Rs 20\n2152 Salted Rs 20\n2153 Cream and onion Rs 20','Biscuits\n2251 50-50 Rs 15\n2252 Monaco Rs 20\n2253 Milkbikies Rs 10','Chocolates\n2351 Dairy milk Rs 50\n2352 5 star Rs 20\n2353 Kit Kat Rs 20'],['Pens\n3151 Pentonic Rs 5\n3152 Goldex Rs 7\n3153 Claro gel Rs 5','Pencils\n3251 Doms Rs 5\n3252 Apsara Rs 5\n3253 Nataraj Rs 3','Erasers\n3351 Apsara Rs 7\n3352 Doms Rs 5\n3353 Funblast Rs 10'],['Soaps\n4151 Dettol Rs 80\n4152 Nivea Rs 65\n4153 Cinthanol Rs 50','Tissues\n4251 3 Boxes Rs 300','Lotions\n4351 Joy Rs 180\n4352 Vaseline Rs 240\n4353 Nivea Rs 370'],['Plastic buckets\n5151 3 Buckets(Ratan Plastics) Rs 1052\n5152 Cello Rs 300\n5153 Nayasa Rs 700','Plastic mugs\n5251 Kuber pack of 4 Rs 199\n5252 Milton Pack of 3 Rs 230\n5253 Doveaz pack of 1 Rs 180','Plastic boxes\n5351 Kuber pack of 3 Rs 359\n5352 Signoware single Rs 260\n5353 Nakonda Rs 80'])
print("============Welcome to Akshay Stores============")
login=input("Enter the type of login- Student or Admin ")
if login=='Student':
    c1=int(input("Enter \n1 if  ID login \n2 if Name login \n3 if Room number login\n"))
    id3="Sample"
    name="Sample"
    room="Sample"
    room_no=0
    if c1==1:
        id3=input("Enter your id ")
        a=1
    elif c1==2:
        name=input(("Enter your name "))
        a=2
    elif c1==3:
        room=input(("Enter your Bhavan "))
        room_no=int(input("Enter your room number "))
        a=3
    else:
        print("Wrong input!Please try again")
        exit()
    while(True):
        choice=int(input("\nPlease select an option \n1 Display items\n2 Add item to cart\n3 Delete item from cart\n4 Display the discounts of the items\n5 Display final bill\n"))
        if choice==1:
            itemlist.display()
        elif choice==2:
            itemlist.addtocart()
        elif choice==5:
            itemlist.displaybill(id3,name,room,room_no)
        elif choice==3:
            itemlist.delete_item()
        elif choice==4:
            itemlist.displaydiscount()
        else:
            print("Wrong input!Please try again")
            exit()
elif login=='Admin':
    password=input("Enter the Admin password ")
    if password=="Admin123":
        while(True):
            admin=int(input(print("Select an option\n1 View the cost of each item\n2 View discounton each item\n3 Change the cost of any item\n4 Change the discount of any item\n5 Exit")))
            if admin==1:
                for attribute, value in item_list_id_price.items():
                    print('{} : {}'.format(attribute, value))
            elif admin==3:
                id1=int(input("Enter the ID of the product whose cost is to be changed "))
                new_cost=int(input("Enter the new cost "))
                item_list_id_price[id1]=new_cost
            elif admin == 4:
                id2 = int(input("Enter the ID of the product whose discount is to be changed "))
                new_discount = int(input("Enter the new discount in percentage "))
                item_list_id_price[id1] = new_discount/100
            elif admin==2:
                for attribute, value in item_list_id_discount.items():
                    print('{} : {}'.format(attribute, value))
            elif admin==5:
                exit()
            else:
                print("Wrong input!Please try again")
                exit()
    else:
        print("Wrong password!Please try again")
        exit()