itemsAvailableDict = {}
shoppingDic = {}
#welcome user

userName= input("Please enter your name : ")
welcomeMessage = f"welcome to my store {userName}"

lenWCMsg = len(welcomeMessage)
print("*"*lenWCMsg)
print(welcomeMessage)
print("*"*lenWCMsg)

# read data from text file

my_file = open("available_grocery_items.txt")

file_line=my_file.readline()

itemsAvailable= my_file.readlines()
#print(itemsAvailable)
my_file.close()

#fetch items from list and add to a dictionary

print("******************Items Available in our Store ********************")

for item in itemsAvailable:
    item_name=item.split()[0]
    item_price=item.split()[1]
    print(f"{item_name}: {item_price}")
    
    itemsAvailableDict.update({item_name: float(item_price)})
print("*" * 20)
# print(itemsAvailableDict)

#propmt user to add items

proceedShopping=input("Do you wish to proceed (yes/no): ")
while proceedShopping.lower()=="yes":
    added_item=input("add an item: ")
    if added_item.title() in itemsAvailableDict:
        item_qty= int(input("Add quantity: ")) 
        shoppingDic.update({added_item:{
            "quantity":item_qty, "subtotal": 
                itemsAvailableDict[added_item.title()]*item_qty
        }})
        
        print(shoppingDic)
    else:
        print("unable to add unavailable item")
        proceedShopping=input("Do you wish to add more items (yes/no): ")

else:
    print("\n\n")
    print("***Bill Summary***")
    print("\n")
    print("Item Quantity Subtotal")
    total=0
    for key in shoppingDic:
        print (f"{key}       {shoppingDic[key]['quantity']}{shoppingDic[key]    ['subtotal']}")
        total=shoppingDic[key]['subtotal']+total
        print(f"Total: {total}")
    print("********Thank You*********")
    print("Hope to see you back soon ! ")
    
    

