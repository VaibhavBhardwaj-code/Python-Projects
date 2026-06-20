name = []
amount = []

name.append("Rahul")
amount.append(500)

name.append("Vaibhav")
amount.append(501)

name.append("Krish")
amount.append(5000)

total = sum(amount)
total_doner = len(name)

 
high = max(amount)
ind = amount.index(high)

print("="*15,"Donation Tracker","="*15,"\n")

for i in range(len(name)):
    print(f"Donor: {name[i]:<20} | Amount: ₹{amount[i]}")

print()
print("="*48)

print("Total Donor: ", total_doner)
print(f"Total Collection: ₹{total}",)
print(f"Top Donor: {name[ind]} (₹{high})")