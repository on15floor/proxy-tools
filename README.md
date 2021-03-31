# Proxy Tools
Основной файл для корректной работы проекта: `main.py`

В зависимости от того, какой вы хотите получить результат, раскомментируйте соответствующие строчки кода.

---
## Что умеет:
### 1. Парсинг прокси
Предусмотрено 2 режима
* Быстрый парсинг. Парсинг осуществляется с сайтов, которые хранят прокси в открытом виде
Список сайтов находится в файле `sites.txt` (в случае необходимости, можно его дополнять известными вам сайтами).
* Полный парсинг. Помимо быстрого парсинга, собирает прокси с сайтов (`echolink.org, foxtools.ru, ip-adress.com, nntime.com`), которые хранят прокси в искаженном виде.

### 2. Проверка прокси
Умеет проверять:
* HTTP
* HTTPS