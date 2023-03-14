import os,re

def Log_simple(in_file,out_file):
    with open(in_file,'r',encoding='utf-8') as in_f:
        with open(out_file,'a+',encoding='utf-8') as out_f:
            for line in in_f.readlines():
                if 'AA-55' in line or '33-BB' in line or 'A5-5A' in line:
                    out_f.writelines(line)

Log_simple(in_file='./Files/20220930.log',out_file='./Files/out_file.log')