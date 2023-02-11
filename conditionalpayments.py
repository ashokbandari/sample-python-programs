price=int(input('enter price'))
quantity=int(input('enter quantity'))
amount=price*quantity
if amount>1000:
   print("10% discount applicable")
   discount=amount*10/100
   amount=amount-discount
   print("amount payable:",amount)
else:
    print("discount not available")
    print("total amount payable:",amount)
