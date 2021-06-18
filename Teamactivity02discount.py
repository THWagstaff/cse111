from datetime import datetime

current = datetime.now()

weekday = current.isoweekday()

#weekday = 4

subtotal = float(input("Please enter the subtotal: "))


if (weekday == 2 or weekday == 3) and subtotal >= 50:
  discount = subtotal * .1
  subtotal *=0.9
  print(f"Discount amount: ${discount:.2f}")
  tax = subtotal * .06
  print(f"Sales tax amount: ${tax:.2f}")
  subtotal *= 1.06
  print(f"You get a discount! Your new total is ${subtotal:.2f}")
elif (weekday == 2 or weekday == 3) and subtotal < 50:
  tax = subtotal * .06
  print(f"Sales tax amount: ${tax:.2f}")
  difference = 50 - subtotal
  subtotal *= 1.06
  print(f"Total: ${subtotal:.2f}")
  print(f"You do not qualify for the discount. Your total is ${subtotal:.2f} and you need ${difference} more to qualify.")
else:
  tax = subtotal * .06
  print(f"Sales tax amount: ${tax:.2f}")
    
  subtotal *= 1.06
  print(f"Total: ${subtotal:.2f}")
  
  print(f"You do not qualify for the discount. Your total is ${subtotal:.2f}")  


