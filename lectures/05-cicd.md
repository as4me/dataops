# Глава 5. CI/CD в DataOps

## Цели главы

- Понять CI и CD применительно к данным  
- Спроектировать pipeline проверок для PR  
- Различать окружения Dev/Test/Stage/Prod  
- Знать стратегии деплоя, миграций и rollback  

---

## 5.1. Continuous Integration

**CI** — автоматическая проверка каждого изменения (обычно на Pull Request).

Для data-проекта CI отвечает:

- код собирается / компилируется;  
- линтеры и unit-тесты проходят;  
- dbt compile / parse успешен;  
- (по возможности) data tests на sample/CI-БД.  

Цель: **сломать сборку до merge**, а не в проде в 03:00.

---

## 5.2. Continuous Delivery / Deployment

**Continuous Delivery** — изменения всегда в состоянии, готовом к выкладке (кнопка / approve).

**Continuous Deployment** — успешный main автоматически едет в prod.

В данных CD чаще осторожнее:

- автодеплой DAG/dbt в staging;  
- prod — по расписанию окна или после approve;  
- отдельные политики для schema migrations.  

---

## 5.3. CI/CD pipeline для данных

Типовой PR pipeline:

```text
Pull Request
  → checkout
  → setup Python / dbt
  → lint / unit tests (ingestion)
  → sqlfluff / sql checks (опционально)
  → dbt deps
  → dbt compile
  → dbt test (на CI database / sample)
  → build / package
  → status: success | failed
```

При критической ошибке — **Failed**, merge блокируется (branch protection).

Инструменты: GitHub Actions, GitLab CI, Jenkins и др.

---

## 5.4. Dev / Test / Stage / Prod

| Окружение | Назначение | Данные |
|-----------|------------|--------|
| **Dev** | Локальная разработка | Sample / синтетика |
| **Test / CI** | Автопроверки PR | Минимальный набор |
| **Staging** | Препрод, интеграция | Анонимизированная копия / subset |
| **Prod** | Боевые потребители | Полные данные |

Правила:

- одинаковые версии инструментов;  
- разные secrets;  
- промоут артефактов, а не «ручной копипаст SQL».  

---

## 5.5. Автоматические проверки

Уровни проверок:

1. **Синтаксис / compile** — dbt parse, Python import  
2. **Unit** — функции ingestion, макросы  
3. **Data tests** — not_null, unique, relationships, custom  
4. **Contract / schema** — ожидаемые колонки  
5. **Smoke** — пайплайн на sample отрабатывает end-to-end  

Чем левее пойман дефект (shift-left), тем дешевле фикс.

---

## 5.6. Deployment data pipelines

Что деплоится:

- Airflow DAG-файлы;  
- dbt-проект (или артефакт манифеста);  
- Docker-образы worker’ов;  
- конфиги (через secrets).  

Стратегии:

- sync репозитория в `dags/` folder;  
- Git-sync / CI copy on merge;  
- Helm/K8s deploy.  

После деплоя: мониторинг первого prod-run.

---

## 5.7. Schema migrations

Миграция схемы — отдельный риск:

1. Подготовить миграцию в коде.  
2. Прогнать на staging.  
3. Согласовать downtime / online strategy.  
4. Применить в prod в окне.  
5. Задеплоить код, совместимый со схемой.  
6. Иметь план отката.  

Совместимость версий кода и схемы критична: нельзя выкатить SQL с `product_price`, пока колонка ещё `price`.

---

## 5.8. Rollback

Откат при инциденте:

- **код**: revert commit / предыдущий образ DAG;  
- **данные**: восстановить из snapshot / пересчитать mart за период;  
- **схема**: down-migration (если безопасна).  

Rollback данных сложнее отката приложения: часть фактов уже успели потребить downstream.

Поэтому: feature flags / dark launch витрин, версионирование mart (`mart_v2`), постепенный switch.

---

## 5.9. dbt и CI/CD

dbt хорошо ложится на CI:

| Команда | Роль в CI |
|---------|-----------|
| `dbt parse` / `compile` | Быстрая проверка проекта |
| `dbt build` | run + test |
| `dbt test` | DQ как gate |
| `dbt docs generate` | Документация / lineage |

Практики:

- slim CI на изменённых моделях (`state:modified+`);  
- defer к prod-артефактам для экономии;  
- хранить `manifest.json` как артефакт.  

В курсе достаточно: compile + tests на PR.

---

## Ключевые выводы

1. CI ловит поломки до merge.  
2. CD доставляет изменения в окружения контролируемо.  
3. Окружения разделяют риск; артефакты продвигают, а не копируют руками.  
4. Schema change и rollback требуют отдельного плана.  
5. dbt — естественный центр тестового gate.  

---

## Вопросы для самопроверки

1. Чем Continuous Delivery отличается от Continuous Deployment?  
2. Какие шаги обязательны в CI для dbt-проекта?  
3. Почему staging нужен, если есть CI?  
4. Опишите порядок выкладки rename колонки.  
5. Что откатываете первым при падении prod после релиза: код или данные? Почему?
