import pandas as pd

class ExcelImporter:
    def read_file(self):
        return pd.read_excel('./test.xlsx')