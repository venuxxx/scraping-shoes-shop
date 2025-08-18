import xlsxwriter

workbook = xlsxwriter.Workbook("shoes.xlsx")
worksheet = workbook.add_worksheet()

row = 0
col = 0


workbook.close()