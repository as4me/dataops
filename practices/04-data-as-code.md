# Практика 4. Data as Code и Git

**Лекция:** [04-data-as-code.md](../lectures/04-data-as-code.md)  
**Время:** 2 часа  
**Цель:** перевести трансформации в Git и провести schema change через PR.

---

## Задание A. Инициализация dbt (45 мин)

В репозитории проекта:

```text
dbt/
  dbt_project.yml
  models/
    staging/
    core/
    marts/
  models/sources.yml
```

1. Опишите `source()` на RAW-таблицы.  
2. Сделайте `stg_orders.sql` с `ref`/`source`, переименованиями и типами.  
3. Добавьте `schema.yml` с `description` для модели и 2–3 колонок.

Команды:

```bash
dbt parse
dbt run --select stg_orders
```

---

## Задание B. Git-flow на учебной задаче (30 мин)

1. Создайте issue: «Add stg_orders».  
2. Ветка `feature/stg-orders`.  
3. Commits с понятными сообщениями.  
4. Pull Request в `main` (пока можно без CI — CI на практике 5).  
5. Review самому себе по чеклисту лекции 4.7 → merge.

В отчёте: ссылки на issue и PR.

---

## Задание C. Schema change drill (45 мин)

Смоделируйте переименование в RAW/source:

1. В sample/API замените поле `price` → `product_price` (или добавьте только новое).  
2. Убедитесь, что старый `stg`/ingestion падает или молча ломается.  
3. Исправьте код в отдельной ветке.  
4. PR с описанием: проблема → локализация → фикс.  
5. Прогон `dbt run` после merge.

Это репетиция аварийного сценария 3 из ТЗ.

---

## Задание D. `.env.example` и запрет секретов (15 мин)

- Добавьте `.gitignore` для `.env`, дампов, полного Olist.  
- Закоммитьте `.env.example` без паролей.  
- Проверьте `git log -p` / `git grep` — секретов нет.

---

## Критерии готовности

- [ ] dbt-проект с source + stg + descriptions  
- [ ] История: issue → branch → PR → merge  
- [ ] Проведён schema change через PR  
- [ ] Секреты не в Git  

## Связь с проектом

Analytics as Code, Git, сценарий Schema Change.
