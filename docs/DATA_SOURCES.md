# Откуда брать данные

В проекте нужны **минимум 3 типа источников**. Ниже — рекомендованные источники со ссылками и краткой инструкцией.

---

## 1. Операционная БД (PostgreSQL) ← датасет Olist

Это основной набор данных интернет-магазина. Сначала скачиваете CSV с Kaggle, загружаете в PostgreSQL и дальше считаете PostgreSQL **операционной системой** магазина.

### Ссылка

- **Kaggle:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- Прямой путь к файлам: [Data Explorer](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data)

### Файлы в датасете

| Файл | Сущность |
|------|----------|
| `olist_customers_dataset.csv` | клиенты |
| `olist_orders_dataset.csv` | заказы |
| `olist_order_items_dataset.csv` | позиции заказов |
| `olist_products_dataset.csv` | товары |
| `olist_sellers_dataset.csv` | продавцы |
| `olist_order_payments_dataset.csv` | платежи |
| `olist_order_reviews_dataset.csv` | отзывы |
| `olist_geolocation_dataset.csv` | геолокация |

### Как скачать

**Вариант A — вручную**

1. Зарегистрируйтесь на [Kaggle](https://www.kaggle.com/).
2. Откройте страницу датасета.
3. Нажмите **Download**.
4. Распакуйте архив в каталог проекта, например `data/olist/` (этот каталог обычно в `.gitignore`).

**Вариант B — Kaggle API**

```bash
# нужен файл credentials: ~/.kaggle/kaggle.json
pip install kaggle
kaggle datasets download -d olistbr/brazilian-ecommerce -p data/olist --unzip
```

### Что сделать дальше

Загрузите таблицы в PostgreSQL (скрипт загрузки — часть вашего проекта). После этого ingestion из «операционной системы» идёт уже из PostgreSQL, а не напрямую из CSV.

> Не коммитьте полный датасет (~100+ MB) в Git. В README опишите, откуда скачать и как загрузить.

---

## 2. REST API — DummyJSON

Внешний HTTP-источник для товаров / остатков / цен / рейтингов.

### Ссылки

| Что | URL |
|-----|-----|
| Документация | https://dummyjson.com/docs |
| Товары (список) | https://dummyjson.com/products |
| Один товар | https://dummyjson.com/products/1 |
| С лимитом | https://dummyjson.com/products?limit=100 |

### Пример запроса

```bash
curl -s "https://dummyjson.com/products?limit=30" | head
```

### Какие поля использовать

Из ответа API можно взять, например:

- `id` → `product_id`
- `price`
- `stock`
- `rating`
- `availabilityStatus` / статус наличия
- `title`, `category` (по необходимости)

Загрузка должна выполняться **программно** (Python `requests` / `httpx`), а не вручную через браузер.

---

## 3. Файловый источник — CSV с возвратами

Отдельный периодический файловый поток (имитация выгрузки из внешней системы возвратов).

В исходном Olist **нет готовой таблицы возвратов** — её нужно **сгенерировать** на основе заказов / order_items.

### Рекомендуемый формат файлов

```text
data/returns/incoming/
  returns_2026_09_01.csv
  returns_2026_09_02.csv
  returns_2026_09_03.csv
```

### Схема файла

```text
return_id,order_id,product_id,return_date,return_reason,refund_amount
```

### Как получить данные

1. Возьмите выборку из `olist_orders_dataset.csv` + `olist_order_items_dataset.csv`.
2. Скриптом сгенерируйте «возвраты» (например, 1–5% заказов):
   - `return_date` ≥ даты заказа;
   - `refund_amount` ≤ суммы позиции / заказа;
   - разумные `return_reason` (`damaged`, `wrong_item`, `not_as_described`, …).
3. Разложите записи по дневным файлам `returns_YYYY_MM_DD.csv`.

В репозитории можно хранить:

- небольшой **sample** (несколько файлов) для демо;
- скрипт генерации полного набора.

Это же удобно для сценария **Freshness**: убрать файл за день и показать срабатывание контроля.

---

## 4. Дополнительно (не обязательно) — Open-Meteo

Погода как внешний фактор для расширенной аналитики.

### Ссылки

| Что | URL |
|-----|-----|
| Сайт / docs | https://open-meteo.com/ |
| API docs | https://open-meteo.com/en/docs |
| Пример (São Paulo) | `https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&daily=temperature_2m_max,precipitation_sum&timezone=America%2FSao_Paulo` |

API бесплатный, ключ обычно не требуется для базовых запросов. Можно сопоставить погоду с датами заказов / доставок (по городу или координатам из geolocation).

---

## Сводная таблица

| # | Тип источника | Откуда взять | Обязательно? |
|---|---------------|--------------|--------------|
| 1 | РСУБД (после загрузки Olist) | [Kaggle Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) → PostgreSQL | Да |
| 2 | REST API | [DummyJSON Products](https://dummyjson.com/docs/products) | Да |
| 3 | Файлы CSV | Сгенерировать returns из Olist | Да |
| 4 | Внешний API | [Open-Meteo](https://open-meteo.com/) | Нет (доп. баллы) |

---

## Рекомендуемая раскладка в репозитории студента

```text
data/
├── olist/                 # скачанные CSV Olist (gitignore)
├── returns/
│   └── incoming/          # дневные returns_*.csv
└── samples/               # маленькие примеры для README/CI (можно в Git)
```

В `.gitignore` обычно игнорируют полные дампы и крупные CSV, оставляя samples и скрипты загрузки.
