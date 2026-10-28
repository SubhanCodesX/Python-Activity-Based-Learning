balance = 1000.00
transactions = []

while input("Continue? (yes/no): ").lower() == "yes":
    t = input("Transaction (withdrawal/deposit): ").lower()
    a = float(input("Enter amount: "))

    if a <= 0 or t not in ["withdrawal", "deposit"]:
        status = "Rejected"
        print("Invalid amount or transaction type.")
    elif t == "withdrawal" and a > balance:
        status = "Rejected"
        print("Insufficient balance.")
    else:
        balance += a if t == "deposit" else -a
        status = "Successful"
        print("Updated balance: ₹", balance)

    transactions.append((t, a, status))

print("\n--- ATM SUMMARY ---")
print("Initial balance: ₹1000.00")
print("Transaction history:", *transactions, sep="\n")
print("Final balance: ₹", balance)
print("Thank you for using the ATM!")