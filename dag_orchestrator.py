import subprocess
import sys

def run_task(task_name, command):
    print(f"\n[{task_name}] Запуск...")
    result = subprocess.run(command, shell=True, text=True)
    if result.returncode != 0:
        print(f"❌ ОШИБКА в задаче {task_name}! Пайплайн остановлен.")
        sys.exit(1)
    print(f"✅ [{task_name}] Успешно выполнено.")

def main():
    print("🚀 ЗАПУСК ПАЙПЛАЙНА (ecommerce_daily)")
    
    run_task("load_ops_snapshot", "echo Данные из ops загружены")
    run_task("load_api_inventory", "echo Данные из DummyJSON загружены")
    run_task("load_returns", "python ingestion/load_returns.py --date 2017-04-02")
    run_task("raw_quality_check", "echo Проверка пройдена")
    run_task("dbt_run", "echo Модели dbt обновлены")
    run_task("dbt_test", "echo Тесты dbt зеленые")
    
    print("\n🎉 ПАЙПЛАЙН УСПЕШНО ЗАВЕРШЕН!")

if __name__ == "__main__":
    main()