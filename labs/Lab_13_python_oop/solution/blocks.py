from base import BaseXlsBlock
from datetime import datetime
from collections import Counter

format_h1 = {'bold': True, 'font_size': '14', 'border': 2, 'align': 'center',
             'font_name': 'Arial', 'bg_color': '#fcd5b4'}
format_h2 = {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center',
             'font_name': 'Arial', 'bg_color': '#c5d9f1'}

class HeaderBlock(BaseXlsBlock):
    NAME = 'Параметры запроса'
    HEADERS = ['Дата выгрузки', 'Период выгрузки']

    def write_header(self):
        header_format = self.workbook.add_format(format_h1)
        subheader_format = self.workbook.add_format(format_h2)
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.HEADERS):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def write_data(self):
        subheader_format = self.workbook.add_format(format_h2)
        maxDate, minDate = datetime(1, 1, 1), datetime(3000, 12, 31)
        self.worksheet.write(self.row, 0, datetime.now().strftime('%Y-%m-%d'), subheader_format)
        for payData in self.data['payments']:
            maxDate = max(datetime(*list(map(int, payData["created_at"][:10].split('-')))), maxDate)
            minDate = min(datetime(*list(map(int, payData["created_at"][:10].split('-')))), minDate)
        self.worksheet.write(self.row, 1, f'{minDate.strftime("%Y-%m-%d")} - {maxDate.strftime("%Y-%m-%d")}',
                             subheader_format)

class TopPayersBlock(BaseXlsBlock):
    NAME = 'Отчёт по активным клиентам'
    HEADERS = ['Топ клиентов', 'Q4 2023', 'Q3 2023', 'Q2 2023', 'Q1 2023', 'Q4 2022']

    def write_header(self):
        header_format = self.workbook.add_format(format_h1)
        subheader_format = self.workbook.add_format(format_h2)
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.HEADERS):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def write_data(self):
        cell_format = self.workbook.add_format({'font_size': '11', 'align': 'center'})
        quarters = {
            'Q4 2023': [],
            'Q3 2023': [],
            'Q2 2023': [],
            'Q1 2023': [],
            'Q4 2022': [],
        }
        for payment in self.data['payments']:
            client_id = payment['client_id']
            created_at = datetime.strptime(payment['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
            quarter = f'Q{(created_at.month - 1) // 3 + 1} {created_at.year}'
            quarters[quarter].append(client_id)

        for quarter in quarters.values():
            self.col += 1
            most_common = Counter(quarter).most_common()[:10]
            for idx, most in enumerate(most_common):
                self.worksheet.write(self.row + idx, self.col,
                                     f'{idx + 1}. {self.data["clients"][most[0] - 1]["fio"]}', cell_format)

class TopCitiesBlock(BaseXlsBlock):
    NAME = 'География клиентов'
    HEADERS = ['Статистика распределения', 'Город', 'Кол-во клиентов']

    def write_header(self):
        header_format = self.workbook.add_format(format_h1)
        subheader_format = self.workbook.add_format(format_h2)
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.HEADERS):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def write_data(self):
        cell_format = self.workbook.add_format({'font_size': '11', 'align': 'center'})
        city_counts = {}
        for client in self.data['clients']:
            city = client['city']
            city_counts[city] = city_counts.get(city, 0) + 1

        popular_cities = sorted(city_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        idx = 0
        for city, count in popular_cities:
            self.worksheet.write(self.row + idx, 1, f'{idx + 1}. {city}', cell_format)
            self.worksheet.write(self.row + idx, 2, count, cell_format)
            idx += 1

class AccountStatusBlock(BaseXlsBlock):
    NAME = 'Анализ состояния счёта'
    HEADERS = ['статистика состояния счета', 'Клиенты', 'Состояние счета']

    def write_header(self):
        header_format = self.workbook.add_format(format_h1)
        subheader_format = self.workbook.add_format(format_h2)
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.HEADERS):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def write_data(self):
        self.col += 1
        self.row += 1
        clients = self.data['clients']
        payments = self.data['payments']

        account_balances = {}
        for payment in payments:
            client_id = payment['client_id']
            amount = payment['amount']
            account_balances[client_id] = account_balances.get(client_id, 0) + amount

        top_balances = sorted(account_balances.items(), key=lambda x: x[1], reverse=True)[:10]

        for i, (client_id, balance) in enumerate(top_balances, start=1):
            client_info = next(client for client in clients if client['id'] == client_id)
            fio = client_info['fio']
            self.worksheet.write(self.row + i - 1, self.col, f"{i}. {fio}")
            self.worksheet.write(self.row + i - 1, self.col + 1, f"{balance}")
