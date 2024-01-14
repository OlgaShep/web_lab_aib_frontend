from datetime import datetime
import json
import os
from writter import XlsAnalyticPaymentWriter

def load_data(file_path):
    full_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

if __name__ == '__main__':
    data_clients = load_data('clients.json')
    data_payments = load_data('payments.json')

    data = {'clients': data_clients['clients'], 'payments': data_payments['payments']}
    output_file = f'my_payments_analytics_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.xlsx'
    output = XlsAnalyticPaymentWriter(data)
    output.write_excel_report(output_file)

    print(f"Report generated successfully. Output file: {output_file}")