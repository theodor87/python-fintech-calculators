direction = input()
entry_price = float(input())
exit_price = float(input())
lot_size = float(input())

#ako je BUY:

profit_long_position = (exit_price - entry_price) * lot_size * 100000

#ako je SELL:

profit_short_position = (entry_price - exit_price) * lot_size * 100000



if direction != "buy" and direction != "sell":
    print("Invalid Trade Direction!")

elif lot_size < 0.01:
    print("Lot Size Too Small!")

else:
    if direction == "buy":
        print(f"Profit: {profit_long_position:.2f} USD.")

    elif direction == "sell":
        print(f"Profit: {profit_short_position:.2f} USD.")
