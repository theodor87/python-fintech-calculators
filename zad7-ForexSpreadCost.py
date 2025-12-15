spread_in_pips = int(input())
lot_size = float(input())

spread_cost = spread_in_pips * lot_size * 10

if lot_size < 0.01:
    print("Lot size too small")

elif spread_in_pips <= 0:
    print("Invalid spread")

else:
    print(f"Spread cost: {spread_cost:.2f} USD")