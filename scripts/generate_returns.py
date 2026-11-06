import pandas as pd
import random
import os

INPUT_FILE = 'data/samples/orders_sample.csv'
OUTPUT_DIR = 'data/returns/incoming/'

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

returns = df.sample(frac=0.05).copy()

returns['return_id'] = ['RET_' + str(i) for i in range(len(returns))]
returns['return_reason'] = [random.choice(['damaged', 'wrong_item', 'not_as_described']) for _ in range(len(returns))]
returns['refund_amount'] = [round(random.uniform(10.0, 100.0), 2) for _ in range(len(returns))]

returns['order_date'] = pd.to_datetime(returns['order_purchase_timestamp'])
returns['return_date'] = returns['order_date'] + pd.to_timedelta([random.randint(1, 10) for _ in range(len(returns))], unit='D')

final_cols = ['return_id', 'order_id', 'return_date', 'return_reason', 'refund_amount']
returns = returns[final_cols]

for date, group in returns.groupby(returns['return_date'].dt.date):
    filename = f"{OUTPUT_DIR}returns_{date}.csv"
    group.to_csv(filename, index=False)
    print(f"Создан файл: {filename} (записей: {len(group)})")