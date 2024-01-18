import xlsxwriter
from blocks import TopPayersBlock, TopCitiesBlock, AccountStatusBlock, HeaderBlock

class XlsAnalyticPaymentWriter:
    ANALYTICS_BLOCKS_CLASSES = [
        HeaderBlock,
        TopPayersBlock,
        TopCitiesBlock,
        AccountStatusBlock
    ]

    def __init__(self, data):
        self.data = data

    def write_excel_report(self, output_file):
        workbook = xlsxwriter.Workbook(output_file)
        worksheet = workbook.add_worksheet('analytics')
        worksheet.set_column(0, 0, 40)
        worksheet.set_column(1, 5, 40)
        row = 0
        col = 0

        for block_class in self.ANALYTICS_BLOCKS_CLASSES:
            block_instance = block_class(worksheet, workbook, row, col, self.data)
            block_instance.write_header()
            block_instance.write_data()
            if row == 0:
                row -= 9
            row += 14

        workbook.close()
