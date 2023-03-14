from Scripts import Analyse_A_bag,Analyse_B_bag,Analyse_C_bag

a_bag_file = './Files/A_All.csv'
b_bag_file = './Files/B_All.csv'
c_bag_file = './Files/C_All.csv'

class Bag_Translator():

    def Bag_trans(self,Bag_input):
        if 'AA-55' in Bag_input:
            return Analyse_A_bag.A_bag_Analyse(file_a_bag=a_bag_file).Main_A(Bag_input)
        elif '33-BB' in Bag_input:
            return Analyse_B_bag.B_bag_Analyse(file_b_bag=b_bag_file).Main_B(Bag_input)
        elif 'A5-5A' in Bag_input:
            return Analyse_C_bag.C_bag_Analyse(file_c_bag=c_bag_file).Main_C(Bag_input)
        else:
            warn_word='非法报文！！！'
            return warn_word


