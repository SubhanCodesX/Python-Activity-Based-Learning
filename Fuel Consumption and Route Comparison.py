n = int(input("Enter number of routes: "))
price = float(input("Enter fuel price per litre: "))
lowest, best = float('inf'), ""

if n <= 0 or price <= 0:
    print("Invalid input")
else:
    for i in range(n):
        name = input("Route name: ")
        d = float(input("Distance (km): "))
        m = float(input("Mileage (km/litre): "))

        if d <= 0 or m <= 0:
            print("Invalid route details")
            continue

        fuel = d / m
        cost = fuel * price
        print("Route:", name, "| Fuel:", round(fuel, 2),
              "litres | Cost: Rs.", round(cost, 2))

        if cost < lowest:
            lowest, best = cost, name

    if best:
        print("Lowest-cost route:", best)
        print("Lowest fuel cost: Rs.", round(lowest, 2))