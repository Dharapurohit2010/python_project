############Part1#############
custName = "Mary smith wants"
itemDesc = "to purchase a Shirt"
message= custName + " " + itemDesc
print(message)

###########Part2################
quantity=3
tax=20.5
price=500.20
message = custName +" " + "to purchase" + " " +str(quantity)+" " +"shirt"
print(message)
total=price*quantity*tax
print("Total cost with tax is: ", total)
###########Part3################
out_of_stock= False
if quantity>1:
    print("Total cost"+"s" +" "+"with tax is: " , total)
if out_of_stock == True:
    print("Item is unavailable")
else:
    print(message)
    print(total)

############Part4**********#####
cloths=["Shirt","Skirt","pazama","Dress"]
print(len(cloths))
print(cloths[3])

