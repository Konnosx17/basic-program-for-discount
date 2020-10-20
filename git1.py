itm=raw_input("Item:")
price=input("Price:")
discount=(0.2 * price)
#0.2 is the decimal conversion for a 20% discount and can be easily changed
total=price-discount
print "This", itm ,"cost",int(total),"from",price
