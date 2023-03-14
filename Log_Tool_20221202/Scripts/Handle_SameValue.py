
class Handle_sameValue():

    def Temp_handle(self,byte1,byte2):
        temp_byte=byte1 + byte2
        time_value_trans ='射源温度：' +str(float(temp_byte)/10)+'℃'
        return time_value_trans

    def Time_handle(self,byte1,byte2):
        time_byte = byte1 +byte2
        time_value_trans = '光电开关时间：' + str(int(time_byte))+'ms'
        return time_value_trans

    def KvMa_handle(self,kvOrmA,byte1,byte2):
        if '电压1' in kvOrmA:
            kV_byte=byte1+byte2
            kV_value = str(float(kV_byte)/10)
            kV_value_trans = '管电压：'+kV_value + 'kV'
            return kV_value_trans
        elif '电流1' in kvOrmA:
            mA_byte = byte1 + byte2
            kV_value = str(float(mA_byte) * 0.01)
            mA_value_trans = '管电流：' + kV_value + 'mA'
            return mA_value_trans

    def Count_handle(self,byte1,byte2):
        count_byte = byte1+byte2
        count_value = int(count_byte, 16)
        count_value_trans = '出图数量：'+str(int(count_value)) + ']'
        print(count_value_trans)
        return count_value_trans

    def AnCount_handle(self,byte1,byte2):
        Ancount_byte = byte1+byte2
        Ancount_value_trans = '亮暗场图像数量：'+str(int(Ancount_byte)) + ']'
        return Ancount_value_trans


if __name__ == '__main__':
    # Handle_sameValue().Temp_handle(byte1='02',byte2='94')
    Handle_sameValue().Count_handle(byte1='03',byte2='50')


