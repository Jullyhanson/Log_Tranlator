# -*- coding: utf-8 -*-
import time,os,sys
from PyQt5.QtWidgets import QApplication, QWidget,QMessageBox,QMainWindow
from PyQt5 import QtWidgets
from log_translator import Ui_Form
import tkinter as tk
from tkinter import filedialog
from Scripts import Main_trans,Bag_translator

current_time=time.strftime('%Y%m%d',time.localtime())

class Log_Translator(QMainWindow,Ui_Form):
    def __init__(self):
        super(Log_Translator, self).__init__()
        self.setupUi(self)
        self.Bag_group.setVisible(True)
        self.Log_inview_button.clicked.connect(lambda:self.select_path(self.Log_inview_button))
        self.Log_outview_button.clicked.connect(lambda:self.select_path(self.Log_outview_button))
        self.Log_trans_button.clicked.connect(self.Log_trans)
        self.Bag_trans_button.clicked.connect(self.Bag_trans)
        self.Close_button.clicked.connect(self.close)

    def Log_trans(self):
        PCHeart=self.checkBox_PCclose.isChecked()
        CHeart=self.checkBox_Cclose.isChecked()
        OnlyBag=self.checkBox_OnlyBag.isChecked()
        Log_input_file=self.Log_input_textbrowser.toPlainText()
        Log_trans_file=self.Log_output_textbrowser.toPlainText()
        print(Log_input_file,Log_trans_file)
        Main_trans.Log_Translator(Log_input_file,Log_trans_file,PCHeart_state=PCHeart,CHeart_state=CHeart,OnlyBag_state=OnlyBag).Log_Trans()
        self.Finished_box()

    def Bag_trans(self):
        Bag_content=self.Bag_input_textEdit.toPlainText()
        trans_result=Bag_translator.Bag_Translator().Bag_trans(Bag_input=Bag_content)
        self.Bag_output_textbrowser.setText(trans_result)


    def select_path(self, view_button):
        # 实例化
        root = tk.Tk()
        root.withdraw()
        if view_button == self.Log_inview_button:
            # 获取文件路径
            file_path = filedialog.askopenfilename()
            self.Log_input_textbrowser.setText(file_path)
        elif view_button == self.Log_outview_button:
            folder_path = filedialog.askdirectory()
            file_save_path = folder_path+'/'+current_time + '_翻译后.log'
            self.Log_output_textbrowser.setText(file_save_path)

    def Finished_box(self):
        finished_box=QMessageBox(QMessageBox.Information,'提示','Log翻译结束')
        finished_box.exec_()

    def closeEvent(self, event):  # 关闭窗口触发以下事件
        a = QMessageBox.question(self, '退出', '你确定要退出吗?', QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)  # "退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
        if a == QMessageBox.Yes:
            event.accept()  # 接受关闭事件
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Log_Translator()
    w.setWindowTitle('Log翻译工具')
    w.show()
    sys.exit(app.exec_())