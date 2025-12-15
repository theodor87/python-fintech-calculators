entry_price = float(input())
exit_price = float(input())
amount = float(input())


result = (exit_price - entry_price) * amount

if result > 0:
    print(f"Profit: {result:.2f} USD")

elif result < 0:
    print(f"Loss: {result:.2f} USD")

else:
    print("BreakEven")
