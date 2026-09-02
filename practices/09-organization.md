# Практика 9. DataOps в организации + сборка проекта

**Лекция:** [09-organization.md](../lectures/09-organization.md)  
**Время:** 2–3 часа  
**Цель:** зафиксировать operating model и собрать end-to-end демо к защите.

---

## Задание A. Роли на учебном проекте (20 мин)

Даже если вы один — назначьте «шляпы»:

| Роль | Кто (вы / напарник) | Ответственность |
|------|---------------------|-----------------|
| Data Engineer | | pipelines, dbt |
| Analyst | | метрики, dashboard |
| Platform | | docker, CI |
| Data Owner (бизнес) | | определение Revenue / Return |

RACI для `mart_sales_daily` — в `docs/raci.md`.

---

## Задание B. Data Product passport (30 мин)

Паспорт витрины `docs/products/mart_sales_daily.md`:

- потребители и use cases;  
- контракт полей;  
- SLA/SLO;  
- DQ-тесты;  
- lineage (ссылка);  
- owner;  
- как запросить изменение (через issue/PR).  

---

## Задание C. Maturity self-assessment (20 мин)

Оцените проект по уровням 0–4 из лекции 9.9:

| Практика | Уровень сейчас | Что дотянуть до защиты |
|----------|----------------|------------------------|
| Git/PR | | |
| CI | | |
| DQ | | |
| Observability | | |
| Docs/Lineage | | |

---

## Задание D. End-to-end репетиция защиты (60–90 мин)

Прогоните и зафиксируйте доказательства:

1. `docker compose up` (или ваш запуск) → сервисы живы.  
2. Полный pipeline → mart обновлены.  
3. Dashboard: Revenue, Orders, AOV, Return Rate, Top Products…  
4. Три аварии (кратко повторить): DQ / freshness / schema.  
5. Показать PR + зелёный CI.  
6. Показать lineage Revenue.  

Чеклист: [docs/CHECKLIST.md](../docs/CHECKLIST.md).

Структура презентации (8–12 слайдов):

1. Проблема бизнеса  
2. Архитектура  
3. Источники  
4. Pipeline / DAG  
5. dbt-слои и витрины  
6. DQ и CI/CD  
7. Monitoring + SLA  
8. Lineage  
9. Аварийные сценарии  
10. Демо / итоги  

---

## Критерии готовности

- [ ] RACI и роли  
- [ ] Passport хотя бы одной витрины  
- [ ] Self-assessment зрелости  
- [ ] Полный прогон + черновик презентации  

## Связь с проектом

Финальная интеграция и защита (5 баллов + все разделы ТЗ).
