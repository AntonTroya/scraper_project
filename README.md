Проект: мониторинг рынка аренды квартир в Санкт-Петербурге (BN.ru)

Инструкции по запуску проекта




1. Установка

Через CMD установите зависимости: requirements.txt
pip install -r requirements.txt



 CHROMEDRIVER
   - Убедитесь, что установлен браузер Google Chrome.
   - Скачайте ChromeDriver под вашу версию Chrome с https://chromedriver.chromium.org/
   - Поместите chromedriver.exe (или chromedriver) в папку, которая есть в переменной PATH,
     либо укажите полный путь в файле scraper/config.py в переменной CHROME_DRIVER_PATH.

* При запуске: bn_scraper.py совершается поиск на соответствие актуальной версии и ее установку, устанавливать CHROMEDRIVER не нужно. 


2. Проверка скрапера
   - Выполните (CMD): python -m bn_scraper.py (пример:C:\Users\Anton_Troya\Python_projects\scraper_project>python -m bn_scraper.py)
   - Должны появиться сообщения о сборе данных. В папке data/raw/ создастся файл spb_rentals.db

3. Запуск непрерывного мониторинга (Prefect)
   - В отдельном терминале запустите сервер: prefect server start
   - В другом терминале создайте деплой: python flows/deployment.py
   - Запустите воркера: prefect worker start --pool default
   - Flow будет автоматически запускаться ежедневно в 9:00 по Москве.

4. Ручной запуск Flow (без расписания)
   - Выполните: python flows/prefect_flow.py
   - Пример: C:\Users\Anton_Troya\Python_projects\scraper_project>python -m flows.prefect_flow


5. Проверка аналитики 
   - Выполните (CMD): python -m analytics.py
     Появится информация о статистике по районам Санкт-Петербуога

6. Просмотр результатов
   - Сырая БД: data/raw/spb_rentals.db (можно открыть с помощью DB Browser for SQLite).
   - Графики: reports/district_prices.png 






1. CHROMEDRIVER
   - Убедитесь, что установлен браузер Google Chrome.
   - Скачайте ChromeDriver под вашу версию Chrome с https://chromedriver.chromium.org/
   - Поместите chromedriver.exe (или chromedriver) в папку, которая есть в переменной PATH,
     либо укажите полный путь в файле scraper/config.py в переменной CHROME_DRIVER_PATH.

* При запуске: bn_scraper.py совершается поиск на соответствие актуальной версии и ее установку. 

2. Проверка скрапера
   - Выполните (CMD): python -m scraper.bn_scraper.py (пример:C:\Users\Anton_Troya\Python_projects\scraper_project>python -m scraper.bn_scraper.py)
   - Должны появиться сообщения о сборе данных. В папке data/raw/ создастся файл spb_rentals.db.

3. Запуск непрерывного мониторинга (Prefect)
   - В отдельном терминале запустите сервер: prefect server start
   - В другом терминале создайте деплой: python flows/deployment.py
   - Запустите воркера: prefect worker start --pool default
   - Flow будет автоматически запускаться ежедневно в 9:00 по Москве.

4. Ручной запуск Flow (без расписания)
   - Выполните: python flows/prefect_flow.py
   - Пример: C:\Users\Anton_Troya\Python_projects\scraper_project>python -m flows.prefect_flow


5. Просмотр 
   - Сырая БД: data/raw/spb_rentals.db (можно открыть с помощью DB Browser for SQLite).
   - Аналитика/График:  reports/district_prices.png

   *В папке: screenshots приложены скриншоты работоспособности проекта

