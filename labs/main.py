# No starter code provided — write the full function yourself.
# Function name: split_bill
# Parameters: bill_amount, tip_percent, people
# Must return: each person's share, rounded to 2 decimal places

def split_bill(bill_amount, tip_percent,people):

    tip_amount = bill_amount*(tip_percent/100)
    ground_total = bill_amount + tip_amount
    person_share = ground_total/people

    return round(person_share,2)

print(split_bill(100,10,2))
print(split_bill(60,20,3))
print(split_bill(50,0,1))