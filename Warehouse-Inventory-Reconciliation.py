n = int(input("Enter number of products: "))

for i in range(n):
    name = input("\nProduct name: ")
    opening = int(input("Opening stock: "))
    incoming = int(input("Incoming quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    actual = int(input("Actual closing stock: "))
    target = int(input("Target stock level: "))

    expected = opening + incoming - dispatched
    difference = actual - expected

    print("\nProduct:", name)
    print("Expected stock:", expected)
    print("Actual stock:", actual)

    if difference == 0:
        print("Status: No Discrepancy")
    elif difference < 0:
        print("Status: Shortage", -difference)
    else:
        print("Status: Surplus", difference)

    print("Replenishment quantity:", max(0, target - actual))

print("\nInventory reconciliation completed.")