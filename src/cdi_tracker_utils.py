import pandas as pd

from bs4 import BeautifulSoup
import requests

class Utils:
    '''
    Utils for using other classes. (?)
    '''

    @staticmethod
    def fix_time(time_str):
        '''
        Fixes the time to the expected model by the filter.
        Args:
            time_str (str): '1/7/22'

        Returns:
            time_str (str): '01/07/2022'
        '''

        time_str = time_str.split('/')

        for i in range(0, 2):
            if len(time_str[i]) == 1:
                time_str[i] = f'0{time_str[i]}'

        if len(time_str[-1]) == 2:
            time_str[-1] = f'20{time_str[-1]}'

        return '/'.join(time_str)


    @staticmethod
    def get_cdi():
        '''
        gets cdi table with dates
        '''

        url = 'https://recieri.com/taxa-cdi/'

        source = requests.get(url, 'lxml', headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36' # noqa=C0301 # pylint: disable=C0301
        })

        # if source.status_code == 200:
        #     return

        soup = BeautifulSoup(source.text, features="html.parser")

        df_cdi = pd.DataFrame([], columns=('mes', 'taxa'))

        for tr_element in soup.findAll('table')[0].findAll('tr')[1::]:
            new_row = pd.DataFrame([[
                Utils._get_eng(str(tr_element)[8:14][0:3]) + '/20' + str(tr_element)[8:14][4::],
                float(str(tr_element)[72:79].replace('>', '').replace('<', '').replace('%', '').replace(',', '.')) / 100 # noqa=C0301 # pylint: disable=C0301
            ]], columns=('mes', 'taxa'))

            df_cdi = pd.concat([df_cdi, new_row]) # df_cdi.append(new_row, ignore_index=True)

        return df_cdi


    @staticmethod
    def _get_eng(mes):
        '''
        gets eng month
        '''

        traducao = {
            'jan': 'jan',
            'fev': 'feb',
            'mar': 'mar',
            'abr': 'apr',
            'mai': 'may',
            'jun': 'jun',
            'jul': 'jul',
            'ago': 'aug',
            'set': 'sep',
            'out': 'oct',
            'nov': 'nov',
            'dez': 'dec',
        }

        return traducao[mes]
