#!/usr/bin/python
import os,re
from Scripts import Analyse_C_bag,Analyse_A_bag,Analyse_B_bag

a_bag_file = './Files/A_All.csv'
b_bag_file = './Files/B_All.csv'
c_bag_file = './Files/C_All.csv'

class Log_Translator():
    def __init__(self,log_path,log_new_path,PCHeart_state=True,CHeart_state=True,OnlyBag_state=True):
        self.log = open(log_path,'a+',encoding='utf-8')
        self.out_log=open(log_new_path,'a+',encoding='utf-8')
        # self.out_log.truncate(0)
        self.PCHeart=PCHeart_state
        self.CHeart=CHeart_state
        self.OnlyBag=OnlyBag_state


    def Log_Trans(self):
        for line in self.log.readlines():
            result_a = re.findall('(?=AA-55)[\w-]+', str(line))
            result_b = re.findall('(?=33-BB)[\w-]+', str(line))
            result_c = re.findall('(?=A5-5A)[\w-]+', str(line))
            if 'AA-55' in line and result_a != []:
                if self.PCHeart ==False:
                    A_trans=Analyse_A_bag.A_bag_Analyse(file_a_bag=a_bag_file).Main_A(result_a[0])
                    if A_trans==1:
                        self.out_log.writelines('[翻译失败：%s]'%line)
                    else:
                        line_new=line.replace('\n','')+'--->'+A_trans+'\n'
                        self.out_log.writelines(line_new)
                        print(line)
                        print(line_new)
                else:
                    if 'AA-55-01-06-93' not in line:
                        A_trans = Analyse_A_bag.A_bag_Analyse(file_a_bag=a_bag_file).Main_A(result_a[0])
                        if A_trans == 1:
                            self.out_log.writelines('[翻译失败：%s]' % line)
                        else:
                            line_new = line.replace('\n', '') + '--->' + A_trans + '\n'
                            self.out_log.writelines(line_new)
                            print(line)
                            print(line_new)
            elif '33-BB' in line and result_b != []:
                if self.PCHeart == False:
                    print('line:', line)
                    B_trans = Analyse_B_bag.B_bag_Analyse(file_b_bag=b_bag_file).Main_B(result_b[0])
                    if B_trans == 1:
                        self.out_log.writelines('[翻译失败：%s]' % line)
                    else:
                        line_new = line.replace('\n', '') + '<---' + B_trans + '\n'
                        self.out_log.writelines(line_new)
                        print(line)
                        print(line_new)
                else:
                    if '33-BB-00-06-93' not in line:
                        print('line:', line)
                        B_trans = Analyse_B_bag.B_bag_Analyse(file_b_bag=b_bag_file).Main_B(result_b[0])
                        if B_trans == 1:
                            self.out_log.writelines('[翻译失败：%s]' % line)
                        else:
                            line_new = line.replace('\n', '') + '<---' + B_trans + '\n'
                            self.out_log.writelines(line_new)
                            print(line)
                            print(line_new)
            elif 'A5-5A' in line and result_c != []:
                if self.CHeart ==False:
                    C_trans=Analyse_C_bag.C_bag_Analyse(file_c_bag=c_bag_file).Main_C(result_c[0])
                    if C_trans==1:
                        self.out_log.writelines('[翻译失败：%s]'%line)
                    else:
                        line_new=line.replace('\n','')+'<---'+C_trans+'\n'
                        self.out_log.writelines(line_new)
                        print(line)
                        print(line_new)
                else:
                    if 'A5-5A-00-06-00' not in line:
                        C_trans = Analyse_C_bag.C_bag_Analyse(file_c_bag=c_bag_file).Main_C(result_c[0])
                        if C_trans == 1:
                            self.out_log.writelines('[翻译失败：%s]' % line)
                        else:
                            line_new = line.replace('\n', '') + '<---' + C_trans + '\n'
                            self.out_log.writelines(line_new)
                            print(line)
                            print(line_new)
            else:
                if self.OnlyBag ==False:
                    self.out_log.writelines(line)
                else:
                    pass
        self.log.close()

if __name__ == '__main__':
    # log_path = './Files/out_file.log'
    log_path = r'D:\DownLoad\feishu_download\20221230.log'
    a_bag_file = 'D:\JullyBackup\Jully\PythonScripts\Log_Tool_20220929\Files/A_All.csv'
    b_bag_file = 'D:\JullyBackup\Jully\PythonScripts\Log_Tool_20220929\Files/B_All.csv'
    c_bag_file = 'D:\JullyBackup\Jully\PythonScripts\Log_Tool_20220929\Files/C_All.csv'
    Log_Translator(log_path=log_path,log_new_path=r'C:\Users\yuanjiajia\Desktop\20221230_翻译后.log').Log_Trans()




