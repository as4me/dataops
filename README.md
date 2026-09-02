# Основы DataOps — итоговый проект

Репозиторий содержит **техническое задание** итогового проекта по дисциплине «Основы DataOps».

Студенты реализуют собственный проект по этому ТЗ в **отдельном** Git-репозитории.

---

## Документы

| Файл | Описание |
|------|----------|
| [docs/TZ.md](docs/TZ.md) | Полное техническое задание проекта |
| [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md) | Откуда брать данные: ссылки и инструкции |
| [docs/CHECKLIST.md](docs/CHECKLIST.md) | Чеклист готовности к сдаче |
| [docs/GRADING.md](docs/GRADING.md) | Критерии оценки (100 баллов) |

---

## Где взять данные

| Тип | Источник | Ссылка |
|-----|----------|--------|
| РСУБД (основной) | Olist → PostgreSQL | [Kaggle: brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| REST API | DummyJSON Products | [dummyjson.com/docs/products](https://dummyjson.com/docs/products) |
| Файлы CSV | Возвраты (сгенерировать из Olist) | см. [DATA_SOURCES.md](docs/DATA_SOURCES.md) |
| Доп. API | Open-Meteo (погода) | [open-meteo.com](https://open-meteo.com/) |

Подробные шаги загрузки — в [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md).

---

## Цель проекта

Спроектировать и реализовать **DataOps-платформу** для обработки и анализа данных интернет-магазина: от источников данных до аналитических витрин и мониторинга, с инженерным контуром Git → CI/CD → Testing → Deployment → Monitoring → Documentation.

## Жизненный цикл данных

```text
Источники → Загрузка → Хранение → Преобразование → Контроль качества → Публикация → Мониторинг → Аналитика
```

## Архитектура (концепт)

```text
Источники данных
       │
       ▼
   Ingestion
       │
       ▼
      RAW → STAGING → CORE → MART → BI / Analytics
```

DataOps-контур:

```text
Git → Pull Request → CI/CD (Code / Data / dbt Tests + Build) → Deployment → Monitoring
```

## Минимальные требования для зачёта

- минимум **3** типа источников данных;
- автоматизированный Data Pipeline + оркестрация;
- слои **RAW** и аналитический (**MART**);
- минимум **3** аналитические витрины;
- минимум **10** Data Quality Tests;
- Git, CI pipeline, базовый мониторинг;
- Data Lineage, README, итоговый аналитический результат.

Подробности — в [docs/TZ.md](docs/TZ.md).

## Рекомендуемый стек

| Обязательно | Рекомендуется |
|-------------|----------------|
| Git, Docker Compose, Python | ClickHouse, MinIO |
| PostgreSQL, Apache Airflow | Apache Superset, Grafana |
| dbt Core | Great Expectations / Soda, OpenMetadata / DataHub |

## Этапы работы

1. Архитектура и окружение  
2. Источники и Ingestion  
3. Pipeline и оркестрация  
4. Analytics as Code и Git  
5. CI/CD  
6. Data Quality  
7. Monitoring / Observability  
8. Metadata, Lineage, Documentation  
9. Интеграция и защита  

## Что сдавать

1. Git-репозиторий с исходным кодом  
2. Инструкция запуска (воспроизводимость)  
3. Архитектурная схема  
4. Работающий Data Pipeline + Airflow DAG (или аналог)  
5. dbt-проект (модели, зависимости, тесты)  
6. Data Quality (≥ 10 тестов)  
7. CI/CD  
8. Monitoring  
9. Dashboard / аналитические представления  
10. README  
11. Презентация  

## Важно

Оценивается не количество инструментов, а **системный DataOps-процесс**: как данные движутся, как ловятся ошибки, как изменения попадают в production, как воспроизводится система и откуда берётся аналитический показатель.

---

*Дисциплина: «Основы DataOps»*
