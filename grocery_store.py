itemsAvailableDict = {}
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
    
    itemsAvailableDict.update({item_name: item_price})
print("*" * 20)
# print(itemsAvailableDict)

#propmt user to add items

proceedShopping=input("Do you wish to proceed (yes/no): ")
if proceedShopping.lower()=="yes":
    add_item=input("add item: ")
else:
    print("We are sorry you dont want to purchase this time. Hope to see you back soon ! ")
    
    

