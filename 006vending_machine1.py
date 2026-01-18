insert_price = input('insert:') #投入金額を受け取る

product_price = input('product:') #商品金額を受け取る

change = int(insert_price) - int(product_price) #おつりを計算

print("change:", change)

"""5行目のintは、「文字列（テキスト）として受け取った数字」を「計算できる整数」に変換するためのものです。=>型変換（キャスト）

- input()の戻り値は必ず文字列です（例："100"）。このままだと数値の引き算ができません。
- そこで int(insert_price) は "100" → 100 のように整数へ変換します。
- 同様に int(product_price) も整数へ変換し、100 - 80 のように引き算できるようにしています。"""

