# Практика 2. Жизненный цикл данных

**Лекция:** [02-data-lifecycle.md](../lectures/02-data-lifecycle.md)  
**Время:** 90–120 мин  
**Цель:** спроектировать источники, слои и три контура pipeline для курсового проекта.

---

## Подготовка

- Аккаунт Kaggle (для Olist)  
- Прочитайте [DATA_SOURCES.md](../docs/DATA_SOURCES.md)  

---

## Задание A. Зафиксировать 3 источника (30 мин)

В `docs/sources.md` опишите:

| Источник | Тип | URL / путь | Что забираем | Частота | Техполя при загрузке |
|----------|-----|------------|--------------|---------|----------------------|
| Olist→Postgres | РСУБД | … | customers, orders, … | daily | ingestion_ts, source, batch_id |
| DummyJSON | API | … | … | … | … |
| Returns CSV | File | … | … | … | … |

Скачайте Olist **локально** (не коммитьте полный датасет). Положите sample 100–500 строк в `data/samples/`.

---

## Задание B. Схема слоёв (30 мин)

Нарисуйте архитектуру:

```text
Sources → Ingestion → RAW → STAGING → CORE → MART → BI
```

Для каждой сущности укажите имена таблиц (черновик):

- `raw_orders`, `stg_orders`, `fact_orders`, `mart_sales_daily`, …  

Минимум **3 mart** из ТЗ. Файл: `docs/architecture.md` (можно Mermaid).

---

## Задание C. Три pipeline (30 мин)

Опишите текстом:

1. **Production pipeline** — шаги daily run.  
2. **Development pipeline** — от ветки до merge.  
3. **Environment pipeline** — Dev / CI / Prod (что отличается).  

---

## Задание D. Docker Compose каркас (опционально, 30 мин)

Поднимите PostgreSQL:

```yaml
# docker-compose.yml (фрагмент)
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: dataops
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: shop
    ports:
      - "5432:5432"
```

- `.env` в gitignore, `.env.example` в git.  
- Загрузите sample customers/orders в схему `ops` (операционная БД).

---

## Критерии готовности

- [ ] 3 источника задокументированы  
- [ ] Sample данные локально  
- [ ] Схема слоёв + имена таблиц  
- [ ] Описаны Prod / Dev / Env pipelines  
- [ ] (Желательно) Postgres с sample  

## Связь с проектом

Это скелет разделов README: источники, архитектура, pipeline.
