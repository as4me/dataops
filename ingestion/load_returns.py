import pandas as pd
import psycopg2
import argparse
import os
import sys

def load_returns(date_str):
    file_path = f"data/returns/incoming/returns_{date_str}.csv"
    batch_id = f"returns_{date_str}"
    
    if not os.path.exists(file_path):
        print(f"❌ ОШИБКА: Файл {file_path} не найден!")
        sys.exit(1) 

    print(f"--> Читаем файл {file_path}")
    df = pd.read_csv(file_path)

    conn = psycopg2.connect(
        host="localhost", port=5432, user="dataops", 
        password="BKN2501", dbname="shop" 
    )
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM raw.raw_returns WHERE batch_id = %s", (batch_id,))
        
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO raw.raw_returns 
                (return_id, order_id, return_date, return_reason, refund_amount, source_system, batch_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                row['return_id'], row['order_id'], row['return_date'], 
                row['return_reason'], row['refund_amount'], 
                'returns_csv', batch_id
            ))
        
        conn.commit()
        print(f"✅ Успех! Загружено {len(df)} строк. Batch ID: {batch_id}")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Ошибка при вставке: {e}")
        sys.exit(1)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Загрузка возвратов в RAW слой")
    parser.add_argument("--date", required=True, help="Дата файла в формате YYYY-MM-DD")
    args = parser.parse_args()
    
    load_returns(args.date)