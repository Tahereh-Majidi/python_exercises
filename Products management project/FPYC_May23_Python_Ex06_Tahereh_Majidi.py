products=[] #String
prices=[] # int
# adding, deleting, editing, detail and searching 

while True:
    user=input("Products management---> Select one option(add/delete/edit/ detail/search/display):  ")
    if user=="add":
            number=int(input("Enter your number of product: "))
            for i in range(number):
                product=input("Enter your product product:    ")
                if product not in products:
                        price=int(input("Enter your price:   "))  
                        products.append(product)
                        prices.append(price)
                        print("your  product product and price  have been successfuly added \n")
                else:
                        print(f"{product}: Exist  \n")  
    elif user=="display":
          for i,n in enumerate(products):
             print(f"product_{i+1}: {n}---->{prices[i]}")

    elif user=="delete":
         names=input("Enter your product to remove: ")
         names=names.split()
         for p in names:
            i=products.index(p)
            products.pop(i)
            prices.pop(i)
                 
    elif  user=="edit":
       
            new_product=input("Enter your new product product to edit:    ") #p1, p2 , p3
            new_product=new_product.split()
            for p in new_product:
                i=products.index(p) 
                prices[i]= int(input(f"new price of {p}: "))
              
         
    elif  user=="detail":
          total_number=len(products)
          print(f"The total number of products are : {total_number}")

          sum_prices=sum(prices)
          average_price=sum_prices/total_number
          print(f"The average price of products is: {average_price}")

          max_price = max(prices)
          max_indices = [ i for i, x in enumerate(prices) if x == max_price]
          for i in max_indices:
            print(f" The most expensive product is:  {products[i]}")


          min_price = min(prices)
          min_indices = [ i for i, x in enumerate(prices) if x == min_price]
          for i in min_indices:
             print(f" The cheapest product is:  {products[i]}")



    elif user=="search":
        name=input("product to search:  ")
        for i, t in enumerate(products):
            if name in t:
                print(f" {t}---->{prices[i]}")
    elif user=="":
         pass

    elif user=="exit":
        break
    else:
            print(f"{user}: command not found!")