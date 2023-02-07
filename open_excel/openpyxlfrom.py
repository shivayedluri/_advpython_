import openpyxl
wb=openpyxl.load_workbook("D://data//dataformula.xlsx")
sheet=wb.active

sheet['A7']='=SUM(A1=A6)'
wb.save("d://data//newsheet.xlsx")