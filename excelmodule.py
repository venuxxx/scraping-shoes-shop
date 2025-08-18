import xlsxwriter

def add_to_excel(scrap):
    workbook = xlsxwriter.Workbook("shoes.xlsx")
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    worksheet.set_column("A:A",100)
    worksheet.set_column("B:B",15)
    for name,price in scrap():
        worksheet.write(row,col,name)
        worksheet.write(row,col+1,price)
        row +=1

    workbook.close()