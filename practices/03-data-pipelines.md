# Практика 3. Data Pipelines и оркестрация

**Лекция:** [03-data-pipelines.md](../lectures/03-data-pipelines.md)  
**Время:** 2–3 часа  
**Цель:** сделать идемпотентную загрузку и DAG с зависимостями.

---

## Подготовка

- Python 3.10+  
- Postgres из практики 2  
- (Желательно) Airflow в Docker  

---

## Задание A. Idempotent ingestion (45–60 мин)

Напишите скрипт `ingestion/load_returns.py`:

1. Читает `data/returns/incoming/returns_YYYY_MM_DD.csv`.  
2. Пишет в `raw.raw_returns` с полями:
   - все колонки файла;
   - `ingestion_timestamp`, `source_system='returns_csv'`, `batch_id`.  
3. Повторный запуск **не плодит дубли** (delete+insert за batch_id / merge по `return_id`+`batch_id`).

Проверка:

```bash
python ingestion/load_returns.py --date 2026-09-01
python ingestion/load_returns.py --date 2026-09-01   # снова
# row count не вырос x2
```

Дополнительно: загрузчик DummyJSON → `raw.raw_inventory`.

---

## Задание B. Сгенерировать returns (30 мин)

Скрипт `scripts/generate_returns.py`:

- берёт sample order_items;  
- 2–5% строк → возвраты;  
- раскладывает по дневным CSV;  
- `return_date >= order_date`, `refund_amount <= price`.  

---

## Задание C. DAG (45–60 мин)

Файл `airflow/dags/ecommerce_daily.py` (или аналог):

```text
load_ops_snapshot → load_api_inventory → load_returns
        → raw_quality_check → dbt_run → dbt_test → end
```

Обязательно продемонстрировать:

- зависимости;  
- `retries=2`;  
- `execution_timeout`;  
- логирование row_count (хотя бы print/XCom).  

Если Airflow ещё тяжёл — тот же граф через `Makefile` / bash с `set -e` + документ «как перенесём в Airflow».

---

## Задание D. Сбой и retry (20 мин)

Сломайте путь к CSV → покажите fail task → почините → успешный rerun без дублей. Скрин/лог в отчёт.

---

## Критерии готовности

- [ ] Идемпотентная загрузка returns (и желательно API)  
- [ ] Генератор CSV  
- [ ] DAG / оркестрация с retry и timeout  
- [ ] Демо повторного запуска и восстановления после ошибки  

## Связь с проектом

Закрывает разделы ТЗ: Ingestion, RAW, Оркестрация, Idempotency.
