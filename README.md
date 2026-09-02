# Основы DataOps

Материалы дисциплины **«Основы DataOps»**: лекции и итоговое проектное задание.

Студенты читают лекции здесь и реализуют практический проект в **отдельном** Git-репозитории по ТЗ.

---

## Лекции

Полная программа: [lectures/README.md](lectures/README.md)

| # | Тема |
|---|------|
| 1 | [Введение в DataOps](lectures/01-introduction-to-dataops.md) |
| 2 | [Жизненный цикл данных и DataOps-процесс](lectures/02-data-lifecycle.md) |
| 3 | [Data Pipelines и оркестрация](lectures/03-data-pipelines.md) |
| 4 | [Data as Code и управление версиями](lectures/04-data-as-code.md) |
| 5 | [CI/CD в DataOps](lectures/05-cicd.md) |
| 6 | [Data Quality и автоматическое тестирование](lectures/06-data-quality.md) |
| 7 | [Мониторинг и Data Observability](lectures/07-observability.md) |
| 8 | [Metadata, Data Lineage и Governance](lectures/08-metadata-governance.md) |
| 9 | [Построение DataOps в организации](lectures/09-organization.md) |

---

## Итоговый проект

| Файл | Описание |
|------|----------|
| [docs/TZ.md](docs/TZ.md) | Полное техническое задание |
| [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md) | Откуда брать данные |
| [docs/CHECKLIST.md](docs/CHECKLIST.md) | Чеклист сдачи |
| [docs/GRADING.md](docs/GRADING.md) | Критерии оценки (100 баллов) |

### Где взять данные

| Тип | Источник | Ссылка |
|-----|----------|--------|
| РСУБД | Olist → PostgreSQL | [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| REST API | DummyJSON | [dummyjson.com/products](https://dummyjson.com/docs/products) |
| CSV | Возвраты (генерация) | [DATA_SOURCES.md](docs/DATA_SOURCES.md) |
| Доп. | Open-Meteo | [open-meteo.com](https://open-meteo.com/) |

### Цель проекта

DataOps-платформа для интернет-магазина:

```text
Источники → Ingestion → RAW → STAGING → CORE → MART → BI
+ Git + CI/CD + Tests + DQ + Monitoring + Lineage + Docs
```

### Минимум для зачёта

- ≥3 типа источников, автоматизированный pipeline + оркестрация  
- RAW + MART (≥3 витрины), ≥10 Data Quality Tests  
- Git, CI, мониторинг, lineage, README, аналитический результат  

Подробности — в [docs/TZ.md](docs/TZ.md).

### Связь лекций и этапов проекта

| Этап проекта | Главы |
|--------------|-------|
| Архитектура и окружение | 1–2 |
| Ingestion и Pipeline | 2–3 |
| Analytics as Code и Git | 4 |
| CI/CD | 5 |
| Data Quality | 6 |
| Monitoring | 7 |
| Metadata, Lineage, Docs | 8 |
| Защита | 9 |

---

*Дисциплина: «Основы DataOps»*
