"""
Restaurant Bill Calculator

Ask for:

Customer name
Food bill
GST (18%)

Calculate:

GST amount
Final bill

If the bill is above ₹1000:

Give a 10% discount.
"""

# Here is the solution.

# Ask for customer name
customer_name = input("Enter customer name: ")

# Ask for food bill
food_bill = float(input("Enter food bill: "))

# Calculate GST amount
gst_amount = food_bill * 0.18

# Calculate final bill
final_bill = food_bill + gst_amount

# Check if the bill is above ₹1000
if final_bill > 1000:
    # Apply 10% discount
    discount = final_bill * 0.10
    final_bill -= discount  # final_bill = final_bill - discount


    print("Customer name:", customer_name)
    print("Food bill:", food_bill)
    print("GST amount:", gst_amount)
    print("Discount:", discount)
    print("Total bill:", final_bill)
    print("Final bill with discount: ₹", round(final_bill, 2)) 
    # round(number, 2) keeps only 2 digits after the decimal point.

else:
     print("Customer name:", customer_name)
     print("Food bill:", food_bill)
     print("GST amount:", gst_amount)
     print("Total bill:", final_bill)
     print("Final bill: ₹", round(final_bill, 2))
     # round(number, 2) keeps only 2 digits after the decimal point.
    