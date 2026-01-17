insert_price = input('insert:') #投入金額を受け取る

product_price = input('product:') #商品金額を受け取る

change = int(insert_price) - int(product_price) #おつりを計算
print("change:", change)

