# Практика 6. Data Quality

**Лекция:** [06-data-quality.md](../lectures/06-data-quality.md)  
**Время:** 2–3 часа  
**Цель:** ≥10 автоматических тестов по разным измерениям качества + демо срабатывания.

---

## Задание A. Матрица тестов (20 мин)

Заполните до реализации:

| # | Тест | Измерение | Модель/таблица | Инструмент |
|---|------|-----------|----------------|------------|
| 1 | order_id not_null | Completeness | stg_orders | dbt |
| 2 | … | Uniqueness | … | … |
| … | | | | |

Покройте минимум: Completeness, Uniqueness, Referential Integrity, Validity, Freshness, Business Rules.

---

## Задание B. Реализация в dbt (60–90 мин)

В `schema.yml` / `tests/`:

**Примеры generic:**

```yaml
models:
  - name: stg_orders
    columns:
      - name: order_id
        tests: [not_null, unique]
      - name: customer_id
        tests:
          - relationships:
              to: ref('stg_customers')
              field: customer_id
```

**Singular / business rule** (`tests/assert_return_after_order.sql`):

```sql
select r.return_id
from {{ ref('stg_returns') }} r
join {{ ref('stg_orders') }} o on r.order_id = o.order_id
where r.return_date < o.order_date
```

**Freshness** — source freshness в `sources.yml` или свой тест на `max(ingestion_timestamp)`.

Запустите:

```bash
dbt test
```

---

## Задание C. Аварийный сценарий 1 — orphan FK (30 мин)

1. Вставьте в RAW/ops заказ с несуществующим `customer_id`.  
2. Прогоните pipeline / `dbt test`.  
3. Зафиксируйте: какой тест упал, статус DAG.  
4. Удалите брак или почините справочник → зелёный прогон.

---

## Задание D. Аварийный сценарий 2 — freshness (20 мин)

1. Не кладите CSV returns за «сегодня/вчера».  
2. Покажите срабатывание freshness-проверки или явный fail task `load_returns`.  
3. Добавьте файл → успешное восстановление.

---

## Критерии готовности

- [ ] ≥10 тестов  
- [ ] ≥5 разных измерений качества  
- [ ] Демо orphan FK  
- [ ] Демо freshness  

## Связь с проектом

ТЗ §17 Data Quality и §23 сценарии 1–2.
