#!/usr/bin/env python
import argparse
from os import path

from cdi_tracker import CDITracker


def main(arguments):
    '''
    main func
    '''

    cleaned_args = {}
    cleaned_args['sheetId'] = arguments.url.split('/d/')[-1].split('/')[0] if arguments.url is not None else None # noqa: C0301 # pylint: disable=C0301
    cleaned_args['sheetName'] = 'Sheet1' if arguments.sheet_name is None else arguments.sheet_name # noqa: C0301 # pylint: disable=C0301
    cleaned_args['csvPath'] = None if not path.exists(str(arguments.csv_path)) else arguments.csv_path # noqa: C0301 # pylint: disable=C0301

    if cleaned_args['csvPath'] is None and cleaned_args['sheetId'] is None:
        print(
            "\033[1;31m",
            "Arquivo não existe, confira a path informada.",
            "\033[0m"
        )


    tracker = CDITracker(
        cleaned_args['sheetId'],
        cleaned_args['sheetName'],
        cleaned_args['csvPath']
    )

    quant = tracker.calculate_capital()
    total_invested = tracker.get_total_invested()

    print(f'Total investido:                         R$ {total_invested:.2f}')
    print(f'Aumento de patrimônio pelo CDI:          R$ {(quant - total_invested):.2f}')
    print(f'Patrimônio equivalente pelo CDI:         R$ {quant:.2f}')




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Investimentos x CDI')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        '-u',
        '--url',
        metavar='',
        type=str,
        help='O URL (link) acessível publicamente da sua planilha.'
    )

    group.add_argument(
        '-c',
        '--csv_path',
        metavar='',
        type=str,
        help='Caminho para a planílha .csv, neste caso o programa utilizara a\
        planilha ao invés do Google Sheet. Caso haja espaços no caminho, utilize\
        "aspas" no mesmo.'
    )

    parser.add_argument(
        '-n',
        '--sheet_name',
        metavar='',
        type=str,
        help='Sheet Name, encontrado no canto inferior esquerdo da página web.'
    )


    args = parser.parse_args()

    main(args)
