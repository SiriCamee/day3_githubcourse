import pandas as pd

#print headers of columns when present
def x(a, print_columns=False):
   '''
   Args: excel_file for (a)
   output: 
   '''
   b = pd.read_excel(a)
   column_headers = list(b.columns.values)
   if print_columns:
       print("\n".join(column_headers))
   return column_headers
