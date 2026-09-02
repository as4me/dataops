# Практика 5. CI/CD

**Лекция:** [05-cicd.md](../lectures/05-cicd.md)  
**Время:** 2 часа  
**Цель:** автоматические проверки на Pull Request.

---

## Задание A. GitHub Actions workflow (60 мин)

Файл `.github/workflows/ci.yml` (или GitLab CI):

Минимальный pipeline на `pull_request`:

```text
lint/tests (Python) → dbt deps → dbt parse/compile → dbt test (если есть CI DB)
```

Пример каркаса:

```yaml
name: ci
on:
  pull_request:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest -q || true   # замените на реальные тесты
      - run: pip install dbt-postgres  # или ваш адаптер
      - run: dbt parse --project-dir dbt
```

Доведите до **реального fail** при ошибке (не глотайте ошибки через `|| true` в финале).

---

## Задание B. Намеренно сломать CI (20 мин)

1. В ветке внесите синтаксическую ошибку в dbt-модель.  
2. Откройте PR → дождитесь Failed.  
3. Скрин статуса.  
4. Почините → CI зелёный → merge.

---

## Задание C. Окружения (30 мин)

В `docs/environments.md`:

| Env | Как поднять | Данные | Деплой |
|-----|-------------|--------|--------|
| Dev | docker compose | sample | вручную |
| CI | GitHub runner | sample/sqlite/postgres service | авто |
| Prod | … | полные | после merge |

Опишите, **что** деплоится при merge в `main` (DAG-файлы, dbt).

---

## Задание D. Rollback plan (20 мин)

Опишите в `docs/runbooks/rollback.md`:

- как откатить плохой SQL (revert);  
- как пересчитать mart за день;  
- кого оповещать.  

---

## Критерии готовности

- [ ] CI запускается на PR  
- [ ] Показан Failed и последующий Success  
- [ ] Описаны Dev/CI/Prod  
- [ ] Есть rollback runbook  

## Связь с проектом

Раздел ТЗ «CI/CD»; branch protection желателен.
