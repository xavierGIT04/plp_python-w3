
# question 1
def  calculate_discount(price, discount_percent=0):
    if(discount_percent > 20):
        return (price * discount_percent/100)
    else:
        return  price

# question 2

result = calculate_discount(145, 30)#with discount
print(f"price after discount : {result}")

other_result = calculate_discount(145)#without discount
print(f" price : {other_result}")
