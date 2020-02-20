# инструкция

требования:
    python 3.x
    Windows 10
    Google Chrome

1. распаковать архив тестирующего приложения

2. в папку drivers положить chromedriver.exe, соответствующий версии установленного браузера Google Chrome (скачать на сайте производителся) 

3. заменить в файле bizone\conftest.py строку
    driver_path = os.path.join(os.getcwd(), 'driver', 'chromedriver')
    на
    driver_path = os.path.join(os.getcwd(), 'driver', 'chromedriver.exe')

4. запустить bizone\run.py интерпретатором python 3.х, дождаться завершения тестирования (в папке bizone\buffer появятся результаты в виде json-файлов)

5. перейти в папку bizone\allure-report и выполнить serve.bat, дождаться открытия в браузере по-умолчанию отчета о тестировании
(либо выполнить генерацию отчета вручную, запустив generate.py, в папке bizone\allure-report\report появится/обновится отчет в виде web-приложения, которое можно открыть в старой версии браузера FireFox)
