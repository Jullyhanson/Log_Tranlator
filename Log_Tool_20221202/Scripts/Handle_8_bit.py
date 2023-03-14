'''
解析8-bit相关文件
'''
import csv


class File_8_bit():
    def __init__(self,file_8_bit):
        self.file = open(file_8_bit)
        self.reader = csv.DictReader(self.file)

    def hex2bin(self,hex_content):
        bag_0 = bin(int(hex_content,16)).replace('0b','')
        # 二进制高位补零
        bag = bag_0.zfill(8)
        return bag


    def csv_dic_trans(self,Num_8_bit):
        csv_bit_dic={}
        for row in self.reader:
            if row['Num'] == Num_8_bit:
                for key in row.keys():
                    try :
                        # 解析0:PC心跳关闭;1:心跳开启，改为字典模式，如bit0:{'0': '手闸触发', '1': '软件触发'}
                        key_value = row[key]
                        value_dic=dict(x.split(':') for x in key_value.split(';'))
                        csv_bit_dic[key]=value_dic
                        # print('转换后,%s:%s'%(key,csv_bit_dic[key]))
                    except:
                        # print("---'%s'无法转化为字典---"%row[key])
                        csv_bit_dic[key]=row[key]
                # 该Num下，打印所有的字典
                # print('%s：%s'%(Num_8_bit,csv_bit_dic))
                return csv_bit_dic

    def bag_dic_trans(self,bag_content):
        bag_bit_dic = {}
        bag_content_bin = self.hex2bin(bag_content)
        bag_content_bin_sort = bag_content_bin[::-1]
        # print(bag_content_bin)
        # print(bag_content_bin_sort)
        bit_wei = 0
        for bit in list(bag_content_bin_sort):
            key='bit'+ str(bit_wei)
            bit_wei +=1
            bag_bit_dic[key] = bit
        # print(bag_bit_dic)
        return bag_bit_dic

    def trans_8_bit(self,Num_8_bit,bag_content):
        # print(Num_8_bit)
        csv_bit_dic=self.csv_dic_trans(Num_8_bit)
        # print(csv_bit_dic)

        bag_bit_dic=self.bag_dic_trans(bag_content)
        # print(bag_bit_dic)

        for bag_bit in bag_bit_dic:
            # 查询bag中的bit键对应的值，如bit0对应的值为1
            bag_bit_value = bag_bit_dic[bag_bit]
            # 查询csv中的bit键对应的值，如bit0对应的值为{'0': '手闸触发', '1': '软件触发'}
            csv_bit_value = csv_bit_dic[bag_bit]
            if type(csv_bit_value) == dict :
                # 判断bag中bit0为1对应的csv中的翻译为“软件触发”
                csv_bit_value2=csv_bit_value[bag_bit_value]
                bag_bit_dic[bag_bit] = csv_bit_value2
                # print('bag翻译：%s'%bag_bit_dic)
            else:
                bag_bit_dic[bag_bit] = csv_bit_value
                # print('bag翻译：%s' % bag_bit_dic)

        str_8_bit=''
        for bag_value in bag_bit_dic.values():
            str_8_bit +=str(bag_value)+','
        str_8_bit += ''
        # print('8_bit翻译字符串：%s'% str_8_bit)
        return str_8_bit


if __name__ == '__main__':
    file_8_bit = r'./Files/8_bit.csv'
    # File_8_bit(file_8_bit).bag_trans('00-1')
    File_8_bit(file_8_bit).trans_8_bit(Num_8_bit='C_00_1',bag_content='76')