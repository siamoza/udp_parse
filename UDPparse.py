# Установка диагностики подшипников УДП. База данных в формате DBISAM. Адекватного коннектора на Python под Linux
# не найдено, поэтому применён комбинированный подход.
# Из Windows с помощью программы Database System Utility все нужные таблицы DAT были вручную выгружены в TXT-формат.
# Данный скрипт фильтрует содержимое этих файлов.

import pandas as pd

MEASURE = '/opt/datasets/udp/measure.txt'
FIO = '/opt/datasets/udp/fio.txt'
DEPO = '/opt/datasets/udp/depo.txt'
M_DATASET = '/opt/datasets/udp/measure_dataset.txt'
F_DATASET = '/opt/datasets/udp/fio_dataset.txt'
D_DATASET = '/opt/datasets/udp/depo_dataset.txt'

if __name__ == '__main__':
    measure = pd.read_csv(MEASURE, dtype=str, sep=',', encoding='cp1251')
    measure.columns = ["DepoID", "Date", "Time", "Factory", "Axis", "Left", "Right", "OperatorID"]
    measure['Left'].replace(to_replace=r'годен', value='1', regex=True, inplace=True)
    measure['Right'].replace(to_replace=r'годен', value='1', regex=True, inplace=True)
    measure['Left'].replace(to_replace=r'БРАК!', value='0', regex=True, inplace=True)
    measure['Right'].replace(to_replace=r'БРАК!', value='0', regex=True, inplace=True)
    measure['Axis'].replace(to_replace=r" ", value="", regex=True, inplace=True)
    measure.to_csv(M_DATASET, index=False)

    fio = pd.read_csv(FIO, dtype=str, sep=',', encoding='cp1251')
    fio.columns = ["OperatorID", "FIO"]
    fio['FIO'].replace(to_replace=r'батищев А.В.', value='Батищев А.В.', regex=True, inplace=True)
    fio['FIO'].replace(to_replace=r'Наладчик ПЭ.Б.', value='ПЭБ', regex=True, inplace=True)
    fio['FIO'].replace(to_replace=r'пэб', value='ПЭБ', regex=True, inplace=True)
    fio['FIO'].replace(to_replace=r'пеб', value='ПЭБ', regex=True, inplace=True)
    fio['FIO'].replace(to_replace=r'  ', value=' ', regex=True, inplace=True)
    fio.to_csv(F_DATASET, index=False)

    depo = pd.read_csv(DEPO, dtype=str, sep=',', encoding='cp1251')
    depo.columns = ["DepoID", "DepoName"]
    depo.to_csv(D_DATASET, index=False)
