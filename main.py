import requests as rq
import logging
import requests.exceptions

# объект логирования и форматирование записей для вывода в консоль
formatting = '[%(levelname)s]: %(message)s:'
logging.basicConfig(format=formatting,level=logging.INFO, filename='requests_response.log')
logger = logging.getLogger('RequestsLogger')
GetParams = {'param1': 'value1', 'param2': 'value2'}
response = rq.get('https://google.com', GetParams)

print(response.url)
sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com',
         'https://tiktok.com', 'https://www.ozon.ru']
# файлы для записи результатов
success_log = 'success_response.log'  # INFO
bad_log = 'bad_responses.log'  # WARNING
blocked_log = 'blocked_response.log'  # ERROR


def write_to_file(file_name, message):
    '''запись в файл лога'''
    with open(file_name, 'a') as file:
        file.write(message + '\n')


for site in sites:
    try:
        response = rq.get(site, timeout=3)

        if response.status_code == 200:
            logging.info(f'{response.status_code} {site}')
            write_to_file(success_log, message=f'{response.status_code} {site}')

        elif response.status_code != 200:
            logging.warning(f'{response.status_code} {site}')
            write_to_file(bad_log, message=f'{response.status_code} {site}')

    except requests.exceptions.RequestException as e:
        logging.error(f'No Connection {site}')
        write_to_file(blocked_log, str(site) + ':' + str(e))
