account_balance = float(input())
risk_percentage = float(input())
stop_loss = float(input())

#standard lot --> 1 pip = 10$
#mini lot --> 1 pip = 1$
#micro lot --> 1 pip = 0.1$

risk_amount = account_balance * (risk_percentage / 100)
lot_size = risk_amount / (stop_loss * 10)

if stop_loss <= 0:
    print("Invalid Stop Loss!")

elif risk_percentage > 10:
    print("Risk Too High!")

elif lot_size < 0.01:
    print("Lot Size Too Small!")

print(f"Lot Size: {lot_size} lots")

