# Глава 2. Жизненный цикл данных и DataOps-процесс

## Цели главы

- Описать полный Data Lifecycle  
- Понять роли Ingestion, Storage, Transformation, Serving  
- Различить Production, Development и Environment pipelines  

---

## 2.1. Data Lifecycle

**Жизненный цикл данных** — путь от появления факта в источнике до потребления в решении (отчёт, API, ML).

Типовая цепочка:

```text
Create / Capture
      → Ingest
      → Store
      → Process / Transform
      → Serve / Share
      → Use / Analyze
      → Archive / Delete
```

В DataOps вокруг этой цепочки строятся: версии, тесты, мониторинг, доступ и документация.

Важно: у данных есть **срок жизни**. Не всё нужно хранить вечно; политики retention — часть зрелой платформы.

---

## 2.2. Источники данных

Источники различают по типу:

| Тип | Примеры | Особенности |
|-----|---------|-------------|
| Операционные БД | PostgreSQL, MySQL | CDC / batch-снимки, нагрузка на OLTP |
| Файлы | CSV, Parquet, JSON в S3/локально | Простота, риск «ручных» правок |
| API | REST, GraphQL | Пагинация, лимиты, нестабильность контракта |
| Потоки | Kafka, Kinesis | Низкая задержка, exactly-once сложнее |
| SaaS | CRM, реклама, платежи | Готовые коннекторы, rate limits |
| Внешние открытые | погода, справочники | Доп. контекст для аналитики |

В курсовом проекте: **PostgreSQL (Olist)** + **REST (DummyJSON)** + **CSV (returns)** — три разных типа.

Принцип: фиксировать `source_system`, время загрузки и объём — иначе observability невозможна.

---

## 2.3. Ingestion

**Ingestion** — доставка данных из источников в платформу (часто в RAW).

Требования хорошего ingestion:

- **Автоматизация** (по расписанию / по событию)  
- **Идемпотентность** (повторный запуск без дублей)  
- **Обработка ошибок** и retry  
- **Метаданные загрузки**: timestamp, batch_id, row_count  
- **Минимальная трансформация** (сохранить исходный вид в RAW)  

Антипаттерн: «почистить и агрегировать сразу при загрузке» — теряется возможность переиграть историю.

---

## 2.4. Хранение

Слои хранения (логическая модель):

```text
RAW      — как пришло из источника + техполя
STAGING  — очистка, типы, имена
CORE     — бизнес-модель (dim/fact)
MART     — витрины под потребителей
```

Физически это может быть один PostgreSQL, lakehouse, DWH или комбинация (например, объектное хранилище + warehouse).

Критерии выбора:

- объём и характер запросов (OLAP vs operational analytics);  
- стоимость хранения и compute;  
- требования к latency;  
- навыки команды.  

В учебном проекте достаточно PostgreSQL + dbt-слои — принцип важнее количества СУБД.

---

## 2.5. Transformation

**Transformation** — приведение данных к виду, пригодному для анализа.

Типичные операции:

- приведение типов и timezone;  
- дедупликация;  
- стандартизация кодов и справочников;  
- join’ы и построение фактов/измерений;  
- бизнес-метрики (revenue, AOV, return rate).  

В современном ELT тяжёлые трансформации делают **в хранилище** (SQL/dbt), а не в отдельном ETL-сервере.

Правило DataOps: логика трансформаций — **код в Git** (Analytics as Code), а не ручные правки в UI продовой БД.

---

## 2.6. Serving и потребление данных

**Serving** — предоставление данных потребителям:

- BI (Superset, Power BI, Tableau);  
- SQL-доступ для аналитиков;  
- API / reverse ETL в операционные системы;  
- feature store / датасеты для ML.  

Хороший serving:

- стабильные контракты витрин;  
- документация и lineage;  
- понятные SLA по свежести;  
- разграничение доступа (особенно к PII).  

Потребитель не должен знать «как устроен RAW» — он работает с **продуктом данных** (mart / data product).

---

## 2.7. Production Pipeline

**Production Pipeline** — то, что реально крутится в проде:

```text
Schedule / Trigger
  → Ingest sources
  → Load RAW
  → Transform (dbt run)
  → Test (dbt test / DQ)
  → Publish marts
  → Notify / metrics
```

Свойства prod-пайплайна:

- расписание и зависимости;  
- retry / timeout;  
- алерты при падении;  
- логи и метрики;  
- запрет «ручных hotfix» в обход Git.  

Успех дня = данные готовы к SLA (например, к 08:00).

---

## 2.8. Development Pipeline

**Development Pipeline** — как изменения попадают в прод:

```text
Idea → Branch → Develop locally / in dev env
  → PR → CI (lint, compile, tests)
  → Review → Merge
  → Deploy to prod (или автодеплой)
```

Отличия от production pipeline:

| | Production | Development |
|---|------------|-------------|
| Цель | Доставить данные | Доставить **изменение кода** |
| Триггер | Время / событие | Commit / PR |
| Риск | Плохие данные | Плохой код / схема |
| Защита | DQ + monitoring | CI + review |

Без development pipeline команда снова правит прод руками.

---

## 2.9. Environment Pipeline

**Environment Pipeline** — управление окружениями:

```text
Dev → Test / CI → Staging → Production
```

Задачи:

- одинаковая структура слоёв в каждом env;  
- разные credentials и объёмы данных (в dev — sample);  
- миграции схем согласованы между env;  
- промоут артефактов (образы, dbt-пакет, DAG) только через pipeline.  

**Infrastructure as Code** и Docker Compose в курсе — способ сделать окружения воспроизводимыми.

Антипаттерн: «на моей машине работает», а в CI/проде — другие версии Airflow/dbt/Postgres.

---

## Связь трёх pipeline

```text
Environment Pipeline  →  даёт одинаковые «рельсы»
Development Pipeline  →  безопасно меняет логику
Production Pipeline   →  ежедневно гоняет данные
```

DataOps работает, когда все три контура согласованы.

---

## Ключевые выводы

1. Lifecycle данных шире, чем ETL: от capture до archive.  
2. Разные типы источников требуют разных стратегий ingestion.  
3. Слои RAW→MART разделяют «как есть» и «для бизнеса».  
4. Prod / Dev / Env pipelines — три обязательных контура зрелого DataOps.  

---

## Вопросы для самопроверки

1. Зачем нужен RAW, если всё равно всё чистится в STAGING?  
2. Чем production pipeline отличается от development pipeline?  
3. Что должно происходить в CI до merge в main?  
4. Почему serving — отдельный этап, а не «просто SELECT из RAW»?  
5. Как environment pipeline снижает риск релизов?
