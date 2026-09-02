# Практика 8. Metadata, Lineage и Governance

**Лекция:** [08-metadata-governance.md](../lectures/08-metadata-governance.md)  
**Время:** 90–120 мин  
**Цель:** задокументировать активы, построить lineage KPI и назначить ownership.

---

## Задание A. Lineage одного показателя (40 мин)

Выберите **Revenue** (или свой KPI).

1. Постройте цепочку от источника до mart (текст + схема).  
2. Сгенерируйте `dbt docs generate && dbt docs serve` (или экспортируйте граф зависимостей).  
3. В отчёте: скрин lineage + пояснение трансформаций на каждом слое.

Пример уровней:

```text
ops.orders → raw_orders → stg_orders → fact_orders → mart_sales_daily.revenue
```

Учтите payments/items, если revenue считается из них.

---

## Задание B. Data docs для витрин (30 мин)

Для каждой из 3 mart в `schema.yml`:

- `description` модели (бизнес-смысл);  
- описания ключевых колонок;  
- тег `mart` / `pii` при необходимости.  

Добавьте в README раздел «Модели данных» со ссылкой на dbt docs.

---

## Задание C. Catalog-lite: реестр активов (20 мин)

Таблица в `docs/data-catalog.md`:

| Актив | Слой | Владелец | SLA freshness | Потребители | PII |
|-------|------|----------|---------------|-------------|-----|
| mart_sales_daily | MART | … | 08:00 | BI sales | нет |
| raw_customers | RAW | … | … | staging | да/нет |

Минимум 8 активов.

---

## Задание D. Политика доступа (15 мин)

Коротко в `docs/access-policy.md`:

- кто читает RAW / MART;  
- запрет prod credentials в ноутбуках;  
- sample вместо полного PII в dev.  

---

## Критерии готовности

- [ ] Lineage KPI со скрином/схемой  
- [ ] Описания 3 mart в dbt  
- [ ] Реестр ≥8 активов с owner  
- [ ] Политика доступа  

## Связь с проектом

ТЗ §20–21 Lineage и Documentation; защита «откуда взялся показатель».
