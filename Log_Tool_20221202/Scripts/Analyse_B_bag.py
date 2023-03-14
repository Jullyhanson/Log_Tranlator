'''
解析C包
'''
import csv
from Scripts import Handle_8_bit,Handle_16_t,Handle_SameValue

file_8_bit = './Files/8_bit.csv'
file_16_t='./Files/16_t.csv'

class B_bag_Analyse():
    def __init__(self,file_b_bag):
        self.file = open(file_b_bag)
        self.reader = csv.DictReader(self.file)

    def C_bag_cut(self,b_bag):
        # print(b_bag)
        bag_header=b_bag[12:14]
        bag_content=b_bag[15:29].split('-')
        # print(bag_header,bag_content)
        return bag_header,bag_content

    def csv_ele_handle(self, csv_content):
        try:
            csv_ele_dic={}
            csv_ele= csv_content.split(':')
            csv_ele_dic[csv_ele[0]]=csv_ele[1]
            # print(csv_ele_dic)
            return csv_ele_dic
        except:
            # print('---%s无法转化为字典---' % csv_content)
            pass
            return csv_content

    def Hex2dec(self,hex_value):
        dec_value=int(hex_value,16)
        # print(dec_value)
        return dec_value

    def byte_dic_tran(self,bag_header):
        byte_dic={}
        # 遍历C_bag.csv中所有的row,将目标值添加到byte_dic
        for row in self.reader:
            # 修改Num=00为Num=B_00
            bag_header_num = 'B_' + bag_header
            # 找出C_bag.csv中对应row的字典
            if row['Num'] == bag_header_num:
                # 将该row里面所有的内容提取出来，形成一个新的字典byte_dic
                # 替换Num值为字典，如'8_bit: B_00_2'替换为{'8_bit': 'B_00_2'}
                byte_value = row['Num']
                byte_value_dic = self.csv_ele_handle(byte_value)
                # print(byte_value_dic)
                byte_dic['Num'] = byte_value_dic
                # 替换info值为字典
                byte_dic['info'] =  row['info']
                # 替换byte1值为字典
                byte_value = row['byte1']
                byte_value_dic = self.csv_ele_handle(byte_value)
                byte_dic['byte1'] = byte_value_dic
                # 替换byte2值为字典
                byte_value = row['byte2']
                byte_value_dic = self.csv_ele_handle(byte_value)
                byte_dic['byte2'] = byte_value_dic
                # 替换byte3值为字典
                byte_value = row['byte3']
                byte_value_dic = self.csv_ele_handle(byte_value)
                byte_dic['byte3'] = byte_value_dic
                # 替换byte4值为字典
                byte_value = row['byte4']
                byte_value_dic = self.csv_ele_handle(byte_value)
                byte_dic['byte4'] = byte_value_dic
                # 替换byte1值为字典
                byte_value = row['byte5']
                byte_value_dic = self.csv_ele_handle(byte_value)
                byte_dic['byte5'] = byte_value_dic
                # print('byte_dic:', byte_dic)
                #
                # for byte_key in byte_dic.keys():
                #     if '/' in byte_dic[byte_key]:
                #         byte_value_new = byte_value.replace('/', '')
                #         byte_dic[byte_key] = byte_value_new

                # print('byte_dic:%s'%byte_dic)

                return byte_dic

    def Main_B(self,b_bag):
        str_b_bag=''
        try:

            bag_header,bag_content_list=self.C_bag_cut(b_bag)
            byte_dic=self.byte_dic_tran(bag_header=bag_header)

            print(b_bag,byte_dic)
            str_b_bag +=byte_dic['info']
            # 遍历bag_content_list，将实际报文中的bag进行处理翻译
            n=1
            for bag_content in bag_content_list:
                byte_wei = 'byte'+str(n)
                # print(byte_dic)
                byte_value = byte_dic[byte_wei]
                # print(byte_wei,byte_value)
                # 将csv中转化为字典形式，方便查找
                if type(byte_value) == dict:
                    if '8_bit' in byte_value.keys():
                        # 翻译8_bit对应的报文，输出相应的结果值（字典）
                        bag_header_num = byte_value['8_bit']   # 将8_bit的值作为Num传给8_bit分析函数
                        str_8_bit=Handle_8_bit.File_8_bit(file_8_bit).trans_8_bit(bag_header_num,bag_content)
                        str_b_bag += '['+str_8_bit + ']'

                    elif '16_t' in byte_value.keys():
                        bag_header_num = byte_value['16_t']
                        str_16_t=Handle_16_t.File_16_t(file_16_t).bag_trans(bag_header_num,bag_content)
                        str_b_bag += '['+str_16_t + ']'

                elif 'temp1' in byte_value:
                    # print(bag_content_list[n-1],bag_content_list[n])
                    temp2 = bag_content_list[n]
                    # print('温度值：%s_%s'%(bag_content,temp2))
                    temp_value_trans=Handle_SameValue.Handle_sameValue().Temp_handle(byte1=bag_content_list[n-1],byte2=temp2)
                    str_b_bag += '[' +temp_value_trans +']'
                elif 'time1' in byte_value:
                    time2 = bag_content_list[n]
                    time_value_trans = Handle_SameValue.Handle_sameValue().Time_handle(byte1=bag_content_list[n-1], byte2=time2)
                    str_b_bag += '[' + time_value_trans + ']'
                elif '电压1' in byte_value:
                    kV2 = bag_content_list[n-1]
                    kV_value_trans = Handle_SameValue.Handle_sameValue().KvMa_handle(byte1=bag_content_list[n-1], byte2=kV2,kvOrmA=byte_value)
                    str_b_bag += '[' + kV_value_trans + ']'
                elif '电流1' in byte_value:
                    mA2 = bag_content_list[n]
                    mA_value_trans = Handle_SameValue.Handle_sameValue().KvMa_handle(byte1=bag_content_list[n-1], byte2=mA2,kvOrmA=byte_value)
                    str_b_bag += '[' + mA_value_trans + ']'
                elif 'count1' in byte_value:
                    count2 = bag_content_list[n]
                    count_value_trans = Handle_SameValue.Handle_sameValue().Count_handle(byte1=bag_content_list[n-1], byte2=count2)
                    str_b_bag += '[' + count_value_trans + ']'
                elif '/' in byte_value:
                    pass

                elif '2' not in byte_value:
                    byte_value = byte_value + ':' + bag_content_list[n - 1]
                    str_b_bag += '[' + byte_value + ']'

                n +=1
            print('%s翻译：%s'%(b_bag,str_b_bag))
            return str_b_bag
        except:
            error=1
            return error


if __name__ == '__main__':
    file_b_bag= r'./Files/B_All.csv'
    b_bag='33-BB-00-06-00-33-02-00-02-58-94-AF'
    B_bag_Analyse(file_b_bag=file_b_bag).Main_B(b_bag)
