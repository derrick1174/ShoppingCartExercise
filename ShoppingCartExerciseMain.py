import json

taxRate = 0.0825 #8.25% expressed as decimal
taxTotal = 0.0
subTotal = 0.0
addend = 0.0 #temp storage for calculating discounts

#opening JSON files
fileCart = open('cart.json') #shopping cart file
fileCoupon = open('coupons.json') #coupon file

#returns JSON objects as a dictionary
cartData = json.load(fileCart) 
couponData = json.load(fileCoupon)

#iterating through the JSON 'shopping cart' list to calculate requested features
for i in cartData:
    for j in couponData: #checks all coupons against each item's sku
        if i["sku"] == j["appliedSku"]: #found a coupon for this sku

            addend = round(i["price"] - j["discountPrice"], 2)
            if addend < 0: #final price of an item cannot be negative
                addend = 0.0
            subTotal += addend

            #check taxability
            if i["isTaxable"]:
                taxTotal += round(addend * taxRate, 2)
            
            break;
    else: #checks whether break was reached; if not, coupon was not found for this item
        subTotal += i["price"]

        #check taxability
        if i["isTaxable"]:
            taxTotal += round(i["price"] * taxRate, 2)


#output
print("Subtotal: " + format(subTotal, '.2f'))
print("Tax total: " + format(taxTotal, '.2f'))
grandTotal = subTotal + taxTotal
print("Grand total: "+ format(grandTotal, '.2f'))

  
#closing files
fileCart.close()
fileCoupon.close()