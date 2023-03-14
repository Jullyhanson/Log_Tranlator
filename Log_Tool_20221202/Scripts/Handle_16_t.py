'''
解析16进制相关文件
'''
import csv

class File_16_t():
    def __init__(self,file_16_t):
        self.file = open(file_16_t)
        self.reader = csv.DictReader(self.file)

    def bag_trans(self,bag_header,bag_content):
        str_16_t =''
        bag_16_t_dic={}
        bag_content_new = '0×' + bag_content
        for key in self.reader:
            # print(key)
            # print(key['Num'])
            if key['Num']== bag_header:
                key_value=key[bag_content_new]
                str_16_t += str(key_value)
        return str_16_t

if __name__ == '__main__':
    file_16_t=r'16_t.csv'
    bag='0f'
    File_16_t(file_16_t).bag_trans(bag_header='C_00',bag_content=bag)