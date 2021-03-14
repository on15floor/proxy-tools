from utils import write_list_w
from proxy_grab import full_grab, fast_grab
from proxy_check import proxy_check

# Быстрый грабинг прокси
write_list_w('source.txt', fast_grab())
# Полный грабинг прокси
# write_list_w('source.txt', full_grab())
# Проверка HTTP прокси
# proxy_check('source.txt', 'http')
# Проверка HTTPS прокси
# proxy_check('source.txt', 'https')
