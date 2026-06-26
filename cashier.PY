print("WELCOM TO THE CASHIER:") 
print()
print()
username="admin"
password=123
username=input("enter the username")
password=int(input("enter the password"))
print()
if username=="admin" and password==123:
    print("passed successfuly,welcom")

elif username!="admin" or password!=123:
    print("error!!!")
    exit()
else:
    exit()
print()
print("availeball products:")

print()

first_product="iphone 11 pro max:500$"
second_product="iphone 14 pro max:700$"
third_product="smart watch APPLE:200$"

print("product1:",first_product)
print("product2:",second_product)
print("product3:",third_product) 


print()
quantity1=int(input(" the quantity of 'iphone 11 pro max' "))
print()
quantity2=int(input(" the quantity of 'iphon 14 pro max' "))
print()
quantity3=int(input(" the quantity of 'smart watch APPLE' "))
print()
print()
subtotal=0
total_price1=0
total_price2=0
total_price3=0

total_price1=quantity1*500

total_price2=quantity2*700

total_price3=quantity3*200


subtotal=total_price1+total_price2+total_price3
print('total price is:' + str(subtotal) + '$')

if subtotal>10000:
    coupon=0.55
    print("coungratulation,you have a coupon 0.55%")
elif subtotal>6000:
    coupon=0.65
    print("coungratulation,you have a coupon 0.65%")
elif subtotal>3000:
    coupon=0.75
    print("coungratulation,you have a coupon 0.75%")
else:
    coupon=1
    print("no coupon available")
final_price=subtotal*coupon 
print("price after coupon:",str(final_price)+"$")

if subtotal==500:
    print("you earned 50 point!")
elif subtotal==700:
    print("you earned 70 point!")
elif subtotal==1000:
    print("you earned 100 point!")
elif subtotal>1000:
    print("you earned 150 point!")
print()    
print()
print("PRICE LISTE:")
print()

print("the total price befor coupon is",str(subtotal) + "$" )
print("__________________________________________")
print("the coupon is:",(coupon))
if subtotal>10000:
    coupon=0.55
    print("coungratulation,you have a coupon 0.55%")
elif subtotal>6000:
    coupon=0.65
    print("coungratulation,you have a coupon 0.65%")
elif subtotal>3000:
    coupon=0.75
    print("coungratulation,you have a coupon 0.75%")
else:
    coupon=1
    print("no coupon available")
final_price=subtotal*coupon 
print("___________________________________________")
print("the price after coupon:",str(subtotal*0.75)or str(subtotal*0.55)or str(subtotal*0.65)) 
print("___________________________________________")
print()
cash=0
creditCard=0
payment=input("how would you like to pay: cash or credit card?")
if payment=="cash":
    print("thank you sir.")
elif payment=="credit card":
    print("+5$ for livraison, thank you sir.")


    


