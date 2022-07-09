'''
'''

from datetime import datetime, timedelta

import pandas as pd

from cdi_tracker_utils import Utils


class CDITracker:
    '''
    '''

    def __init__(self, sheet_id, sheet_name='Sheet1', csv_path=None,):
        self.url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}" # noqa=C0301 # pylint: disable=C0301
        self.df = self._get_df(csv_path)


    def _get_df(self, csv_path):
        '''
        '''

        if csv_path is not None:
            self.df = pd.read_csv(csv_path)
        else:
            self.df = pd.read_csv(self.url)

        self.df.rename(columns = {
            self.df.columns[0]:'transf_ammount', self.df.columns[1]:'transf_date'
        }, inplace = True)

        date_objs = []
        for _, row in self.df.iterrows():
            date = datetime.strptime(Utils.fix_time(row['transf_date'])[2::], "/%m/%Y")
            date_objs.append(date)

        self.df['date_obj'] = date_objs

        return self.df

    def _log(self, verboise):
        '''
        '''


    def calculate_capital(self):
        '''
        '''

        cdi = Utils.get_cdi()
        total = 0
        now = datetime.now()

        first_month = self.df.iloc[0]['date_obj']
        days_delta = (now - first_month).days
        curr_date = first_month

        for _ in range(int(days_delta + 1)):

            if datetime.strftime(curr_date, '%m/%Y') == datetime.strftime(now, '%m/%Y'):
                break

            if datetime.strftime(curr_date, '%d') == '01': # se for o primeiro dia do mes
                month = datetime.strftime(curr_date, '%b/%Y').lower()
                # key = datetime.strftime(curr_date, '%d/%m/%Y')

                invested_values = self.df.loc[self.df['date_obj'] == curr_date]['transf_ammount']

                if invested_values.shape[0] > 0:
                    for invested_value in invested_values:
                        taxa = (1 + cdi.loc[cdi['mes'] == month]['taxa'] / 12)
                        total = float(total + float(invested_value)) * float(taxa)

                else:
                    taxa = 1 + (cdi.loc[cdi['mes'] == month]['taxa'] / 12)
                    total = float(total) * float(taxa)


            curr_date += timedelta(days=1)

        return total


    def get_total_invested(self):
        '''
        '''

        return self.df['transf_ammount'].sum()
