price =50

while True:
    print("Amount Due: "+ str(price))
    user= int(input("insert Coin: "))
    
    if user == 25 or user == 10 or user == 5:
        price -= user
    else:
        print(None) 
    if user < price:
        continue
    if price == 0:
       break
    

       