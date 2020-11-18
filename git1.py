itm=raw_input("Item:")
price=input("Price:")
discount=(0.2 * price)
#0.2 is the conversion for a 20% discount and can be easily changed by the divison of the discount with 100
total=price-discount
print "This", itm ,"cost",int(total),"from",price
