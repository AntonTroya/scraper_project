Проект: мониторинг рынка аренды квартир в Санкт-Петербурге (BN.ru)

Непрерывного скрапинга данных с BN.ru для анализа динамики цен и предложений на рынке аренды жилья в Санкт-Петербурге.


Структура проекта:

 scraper:
  - config.py – настройки (URL, селекторы, задержки)
  - cian_scraper.py – основной класс скрапера
  - parser.py – функции парсинга HTML
  - __init__.py - модуль импорта


 flows:
- prefect_flow.py – основной flow мониторинга
- deployment.py – создание деплоя с расписанием
- __init__.py - модуль импорта
- data/raw/ – сырая БД SQLite
- data/processed/ – агрегированные данные
- notebooks – Jupyter ноутбук для анализа
- artifacts – графики и отчеты

--

Инструкции по запуску проекта




1. CHROMEDRIVER
   - Убедитесь, что установлен браузер Google Chrome.
   - Скачайте ChromeDriver под вашу версию Chrome с https://chromedriver.chromium.org/
   - Поместите chromedriver.exe (или chromedriver) в папку, которая есть в переменной PATH,
     либо укажите полный путь в файле scraper/config.py в переменной CHROME_DRIVER_PATH.

* При запуске: cian_scraper.py совершается поиск на соответствие актуальной версии и ее установку, устанавливать CHROMEDRIVER не нужно. 

2. ПРОВЕРКА СКРАПЕРА
   - Выполните (CMD): python -m scraper.cian_scraper (пример:C:\Users\Anton_Troya\Python_projects\scraper_project>python -m scraper.cian_scraper)
   - Должны появиться сообщения о сборе данных. В папке data/raw/ создастся файл spb_rentals.db.

3. ЗАПУСК НЕПРЕРЫВНОГО МОНИТОРИНГА (PREFECT)
   - В отдельном терминале (с активированным venv) запустите сервер: prefect server start
   - В другом терминале создайте деплой: python flows/deployment.py
   - Запустите воркера: prefect worker start --pool default
   - Flow будет автоматически запускаться ежедневно в 9:00 по Москве.

4. РУЧНОЙ ЗАПУСК FLOW (БЕЗ РАСПИСАНИЯ)
   - Выполните: python flows/prefect_flow.py
   - Пример: C:\Users\Anton_Troya\Python_projects\scraper_project>python -m flows.prefect_flow


5. ПРОСМОТР РЕЗУЛЬТАТОВ
   - Сырая БД: data/raw/spb_rentals.db (можно открыть с помощью DB Browser for SQLite).
   - CSV с ежедневной статистикой: data/processed/daily_stats.csv. (не реализовано - файл создается, цена не извлекается)
   - Графики: artifacts/price_trend_spb.png и artifacts/listings_count_spb.png. (не реализовано)





1. CHROMEDRIVER
   - Убедитесь, что установлен браузер Google Chrome.
   - Скачайте ChromeDriver под вашу версию Chrome с https://chromedriver.chromium.org/
   - Поместите chromedriver.exe (или chromedriver) в папку, которая есть в переменной PATH,
     либо укажите полный путь в файле scraper/config.py в переменной CHROME_DRIVER_PATH.

* При запуске: cian_scraper.py совершается поиск на соответствие актуальной версии и ее установку. 

2. ПРОВЕРКА СКРАПЕРА
   - Выполните (CMD): python -m scraper.cian_scraper (пример:C:\Users\Anton_Troya\Python_projects\scraper_project>python -m scraper.cian_scraper)
   - Должны появиться сообщения о сборе данных. В папке data/raw/ создастся файл spb_rentals.db.

3. ЗАПУСК НЕПРЕРЫВНОГО МОНИТОРИНГА (PREFECT)
   - В отдельном терминале (с активированным venv) запустите сервер: prefect server start
   - В другом терминале создайте деплой: python flows/deployment.py
   - Запустите воркера: prefect worker start --pool default
   - Flow будет автоматически запускаться ежедневно в 9:00 по Москве.

4. РУЧНОЙ ЗАПУСК FLOW (БЕЗ РАСПИСАНИЯ)
   - Выполните: python flows/prefect_flow.py
   - Пример: C:\Users\Anton_Troya\Python_projects\scraper_project>python -m flows.prefect_flow


5. ПРОСМОТР РЕЗУЛЬТАТОВ
   - Сырая БД: data/raw/spb_rentals.db (можно открыть с помощью DB Browser for SQLite).
   - CSV с ежедневной статистикой: data/processed/daily_stats.csv. (не реализовано - файл создается, цена не извлекается)
   - Графики: artifacts/price_trend_spb.png и artifacts/listings_count_spb.png. (не реализовано)

