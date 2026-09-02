# Практика 7. Monitoring и Observability

**Лекция:** [07-observability.md](../lectures/07-observability.md)  
**Время:** 2 часа  
**Цель:** измерить здоровье пайплайна, задать SLA/SLO и поймать аномалию объёма.

---

## Задание A. Журнал загрузок (45 мин)

Таблица `meta.ingestion_log` (или файл метрик):

| Поле | Смысл |
|------|--------|
| pipeline_name | имя DAG |
| task_name | шаг |
| started_at / finished_at | длительность |
| status | success/failed |
| row_count | обработано строк |
| batch_id | партия |
| source_system | источник |
| error_message | если fail |

Пишите запись из ingestion-скриптов и/или Airflow callback.

Простой дашборд: SQL-запросы или Grafana/Metabase/Superset на этой таблице.

---

## Задание B. SLA и SLO (20 мин)

В `docs/slo.md`:

```text
SLA: данные за предыдущий день (mart_sales_daily) готовы к 08:00 Europe/Moscow.
SLO: ≥ 99% ежедневных запусков ecommerce_daily успешны за календарный месяц.
SLI: share of successful DAG runs; freshness_hours of mart_sales_daily.
```

Добавьте ещё 1–2 метрики: test pass rate, MTTR (хотя бы как определение).

---

## Задание C. Volume anomaly (30 мин)

1. Запомните baseline `row_count` для orders/returns.  
2. Сделайте загрузку с искусственно обрезанным файлом (например, 1% строк).  
3. Правило: если `row_count < 0.2 * baseline` → fail или alert (лог + ненулевой exit code).  
4. Скрин/лог срабатывания.

---

## Задание D. Alerting (20 мин)

Минимум одно из:

- Airflow email/Slack webhook при failed DAG;  
- скрипт, пишущий `ALERT: ...` в лог и файл `monitoring/last_alert.txt`;  
- Grafana alert (если подняли).  

Опишите severity: P1 (SLA mart) vs P3 (warning volume).

---

## Критерии готовности

- [ ] Лог/метрики run + row_count  
- [ ] Документированы SLA, SLO, SLI  
- [ ] Демо volume anomaly  
- [ ] Есть механизм алерта  

## Связь с проектом

ТЗ §18–19 Observability / SLA.
