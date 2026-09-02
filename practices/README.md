# Практические занятия: Основы DataOps

Практики дополняют [лекции](../lectures/README.md). Выполняйте после соответствующей главы.

Итоговый проект: [docs/TZ.md](../docs/TZ.md) · Данные: [docs/DATA_SOURCES.md](../docs/DATA_SOURCES.md)

---

## Список практик

| # | Практика | Лекция | Файл |
|---|----------|--------|------|
| 1 | Проблемы «до DataOps» и карта принципов | [01](../lectures/01-introduction-to-dataops.md) | [01-intro-dataops.md](01-intro-dataops.md) |
| 2 | Источники → слои → три pipeline | [02](../lectures/02-data-lifecycle.md) | [02-data-lifecycle.md](02-data-lifecycle.md) |
| 3 | DAG, idempotent load, Airflow-скелет | [03](../lectures/03-data-pipelines.md) | [03-data-pipelines.md](03-data-pipelines.md) |
| 4 | Git-flow, Analytics as Code, schema change | [04](../lectures/04-data-as-code.md) | [04-data-as-code.md](04-data-as-code.md) |
| 5 | GitHub Actions CI для dbt/Python | [05](../lectures/05-cicd.md) | [05-cicd.md](05-cicd.md) |
| 6 | 10+ Data Quality tests | [06](../lectures/06-data-quality.md) | [06-data-quality.md](06-data-quality.md) |
| 7 | Метрики, SLA/SLO, алерты | [07](../lectures/07-observability.md) | [07-observability.md](07-observability.md) |
| 8 | Lineage, docs, ownership | [08](../lectures/08-metadata-governance.md) | [08-metadata-governance.md](08-metadata-governance.md) |
| 9 | Operating model и мини-внедрение | [09](../lectures/09-organization.md) | [09-organization.md](09-organization.md) |

---

## Как сдавать практики

1. Работайте в **своём** репозитории проекта (не в этом).  
2. К каждой практике — короткий отчёт: что сделали, скрин/лог, выводы (можно `practices/NN-report.md` у себя).  
3. Код и конфиги — через ветку + Pull Request.  
4. Практики 1–2 можно без полного Docker; с 3-й — желательно окружение проекта.

## Ожидаемый результат к концу курса

Набор артефактов из практик складывается в итоговый DataOps-проект: ingestion → dbt → CI → DQ → monitoring → lineage → docs.
