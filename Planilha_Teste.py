import openpyxl as ex

wb = ex.load_workbook('Primeira_Planilha.xls')

folhas = wb.get_sheet_names()
sheet = wb.get_sheet_names('Pasta1')

nr = sheet.get_highest_row()
nc = sheet.get_highest_column()
print('rows = ', nr)
print('columns = ',nc)
