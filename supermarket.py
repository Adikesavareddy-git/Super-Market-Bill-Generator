from datetime import datetime

name = input("Enter your name:")
 
lists='''
rice   Rs 20/kg
sugar  Rs 30/kg
salt   Rs 20/Kg
oil    Rs 100/litre
paneer Rs 110/kg
maggi Rs 10/Each
milk  Rs 70/litre
Boost Rs 200/Kg
Colagate Rs 85/Each'''
print(lists)

#declaration
price=0
pricelist=[]
totalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':20,
       'sugar':30,
    'salt':20,'oil':100,'paneer':110,
    'maggi':10,'milk':70,'colgate':85,'boost':200}
option=int(input("for list of items press1:"))
if option ==1:
    print(lists)
for  i in range (len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit: "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity = int(input("Enter quantity:"))
        if item in items.keys():
            price= quantity *items[item]
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*0.05)
            finalamount =gst+totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("you entered wrong option")
    inp =input("Can I bill the items Yes or No:")
    if inp =='yes':
        pass
        if finalamount!=0:
            print(25*"=","Adi Supermarket",25*"=")
            print(28*"=","KADAPA")
            price("Name:",name,30*" ","Date:",datetime.now())
            price(75*"-")
            print("S.No",8*" ",'Item',8*" ",'Quantity',3*" ",'price')
        
            for i in range(len(pricelist)):
                print(i,8*" ",8*" ",ilist[i],3*" ",qlist[i],plist[i])
            print(75*"-")
            print(50*" ",'Total Amount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(50*" ","Thank you Visit Again")
            print(75*"-")