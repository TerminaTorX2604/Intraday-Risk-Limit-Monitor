import pandas as pd

positions = pd.read_csv("positions.csv")

print("Intraday Risk Monitoring Report\n")

for _, row in positions.iterrows():

    trader = row["Trader"]
    instrument = row["Instrument"]
    position = row["Position"]
    limit = row["RiskLimit"]

    utilisation = (position / limit) * 100

    if position > limit:
        print(f"[ALERT] {trader}: {instrument} exceeds risk limit ({utilisation:.1f}%)")

    elif utilisation >= 90:
        print(f"[WARNING] {trader}: {instrument} approaching risk limit ({utilisation:.1f}%)")

    else:
        print(f"[OK] {trader}: {instrument} within limit ({utilisation:.1f}%)")
