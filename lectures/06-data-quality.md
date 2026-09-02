# Глава 6. Data Quality и автоматическое тестирование

## Цели главы

- Знать измерения качества данных  
- Уметь проектировать автоматические тесты  
- Познакомиться с dbt Tests, GE, Soda  
- Понять Data Contracts и shift-left  

---

## 6.1. Что такое качество данных

**Качество данных** — степень пригодности данных для конкретной цели (отчёт, ML, операция).

Качество **относительно потребителя**: «достаточно хорошо для дашборда продаж» ≠ «достаточно для кредитного скоринга».

Плохое качество проявляется как:

- неверные KPI;  
- потеря доверия к платформе;  
- ручные сверки;  
- инциденты и откаты.  

DataOps встраивает проверки в pipeline, а не оставляет «на глаз аналитика».

---

## 6.2. Accuracy

**Accuracy** — соответствие реальности / эталону.

Примеры:

- сумма платежей совпадает с суммой заказа (в пределах правил);  
- курс валюты из официального источника;  
- адрес геокодирован верно.  

Проверяют сверками (reconciliation), бизнес-правилами, spot-check с источником.

---

## 6.3. Completeness

**Completeness** — полнота обязательных атрибутов и записей.

Примеры тестов:

- `order_id IS NOT NULL`;  
- доля NULL в `email` < порога;  
- все дни месяца присутствуют в daily mart.  

Неполнота часто приходит из API (поля опциональны) или частичного ingestion.

---

## 6.4. Freshness

**Freshness** — насколько данные актуальны.

Примеры:

- max(`order_purchase_timestamp`) не старше N часов;  
- файл `returns_YYYY_MM_DD.csv` за вчера появился до 06:00;  
- watermark ingestion не отстаёт от SLA.  

Нарушение freshness — классический аварийный сценарий курса.

---

## 6.5. Validity

**Validity** — значение допустимо по формату и домену.

Примеры:

- `quantity > 0`;  
- `price >= 0`;  
- `status IN ('delivered','shipped',...)`;  
- дата в разумном диапазоне.  

---

## 6.6. Uniqueness

**Uniqueness** — ключи уникальны там, где должны.

Примеры:

- один `order_id` в `dim`/`fact` зерне;  
- нет дублей после повторного ingestion.  

Связано напрямую с **идемпотентностью** загрузок.

---

## 6.7. Unit / Integration / Data Tests

| Тип | Что проверяет | Пример |
|-----|---------------|--------|
| **Unit** | Функция / кусок кода | Парсер CSV, расчёт AOV |
| **Integration** | Связка компонентов | Airflow task → таблица RAW |
| **Data tests** | Содержимое таблиц | not_null, relationships |

Все три нужны: зелёные unit при красных data tests = логика кода ок, данные — нет.

---

## 6.8. dbt Tests / Great Expectations / Soda

### dbt Tests

- generic: `unique`, `not_null`, `accepted_values`, `relationships`;  
- singular: SQL-файл с assert’ом;  
- легко живут рядом с моделями.  

### Great Expectations (GX)

- expectation suites;  
- богатые профили и документы data docs;  
- гибко вне dbt.  

### Soda

- checks как код (SodaCL);  
- удобен для мониторинга DQ в проде.  

В курсе достаточно **≥10 тестов** (часто на dbt); GX/Soda — плюс.

---

## 6.9. Data Contracts

**Data Contract** — соглашение между производителем и потребителем данных:

- схема (поля, типы);  
- семантика;  
- SLA свежести;  
- качество (пороги);  
- владелец.  

Контракт делает breaking change **явным**: сначала версия контракта, потом код.

Пример: витрина `mart_sales_daily` обещает поля `date`, `revenue`, `orders_count` к 08:00 ежедневно.

---

## 6.10. Shift-left testing

**Shift-left** — перенос проверок «влево» по жизненному циклу:

```text
Идея → PR/CI → Staging → Prod run → Потребитель
         ↑ тестируем здесь, а не только здесь ↑
```

Практики:

- тесты в PR;  
- schema checks на ingestion;  
- не публиковать mart при fail DQ (gate);  
- синтетические «плохие» фикстуры в CI.  

Чем раньше пойман orphan `customer_id`, тем дешевле инцидент.

---

## Минимальный набор для проекта (пример)

1. `orders.order_id` not_null + unique  
2. `customers.customer_id` unique  
3. `orders.customer_id` → `customers`  
4. `order_items.price >= 0`  
5. `order_items.quantity > 0`  
6. `payments.payment_value >= 0`  
7. `returns.refund_amount >= 0`  
8. `return_date >= order_date`  
9. freshness RAW / returns files  
10. accepted_values для `order_status`  

Покрыть несколько измерений, не десять одинаковых not_null.

---

## Ключевые выводы

1. Качество многомерно: accuracy, completeness, freshness, validity, uniqueness…  
2. Тесты автоматизируются и становятся gate пайплайна.  
3. Контракты фиксируют ожидания на границах.  
4. Shift-left снижает стоимость дефектов.  

---

## Вопросы для самопроверки

1. Чем freshness отличается от completeness?  
2. Почему uniqueness связана с идемпотентностью?  
3. Когда выбрать singular dbt test вместо generic?  
4. Что должно быть в data contract витрины?  
5. Как продемонстрировать срабатывание DQ на orphan FK?
