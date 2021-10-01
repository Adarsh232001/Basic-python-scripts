import random
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
for i in range(1,58):
    ws.append([random.randint(1,8)])

wb.save("moblie_application_development_internals.xlsx")