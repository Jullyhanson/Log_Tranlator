import xlrd

class C_analyse():
    def __init__(self,filename):
        self.wb = xlrd.open_workbook(filename)

    def Bit_8(self,content):
        print(content)
        if content[0] == 'A5':
            print('C包')
            c_sheet=self.wb.sheet_by_name('C-All')
            all_rows=c_sheet.col_values(0)
            c_row_loc=all_rows.index(content[4])
            print(c_row_loc)
            all_cols=c_sheet.row_values(c_row_loc)
            c_col_loc=all_cols.index(content[4])
            print(all_rows)
            print(all_cols)
            loc_content=(c_col_loc,c_row_loc)
            print(loc_content)
            print(c_sheet.cell(c_row_loc,c_col_loc).value)

if __name__ == '__main__':
    file = r'C:\Users\yuanjiajia\Desktop\Info_all.xlsx'
    bag = 'A5-5A-00-06-00-E3-04-28-00-04-26-63'
    bag_new=bag.split('-')
    C_analyse(filename=file).Bit_8(bag_new)
