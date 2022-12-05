# Установка диагностики подшипников УДП. База данных в формате DBISAM. Адекватного коннектора на Python под Linux
# не найдено, поэтому применён комбинированный подход.
# Из Windows с помощью программы Database System Utility все таблицы DAT были выгружены в TXT-формат.
# Данный скрипт фильтрует содержимое этих файлов.

import os
import sys
from datetime import datetime

SOURCE = '/opt/datasets/udp/'
DATASET = '/opt/datasets/udp/dataset.txt'

if __name__ == '__main__':
    udp = []
    dir_list = [x[0] for x in os.walk(SOURCE)]  # список каталогов
    dir_list.pop(0)  # лишний элемент, имя родительского каталога
    for i in dir_list:

