# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alpha.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 627)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 571, 351))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.name = QtWidgets.QLabel(self.groupBox)
        self.name.setGeometry(QtCore.QRect(10, 40, 67, 21))
        self.name.setObjectName("name")
        self.name_out = QtWidgets.QLabel(self.groupBox)
        self.name_out.setGeometry(QtCore.QRect(120, 40, 311, 21))
        self.name_out.setStyleSheet("border-color: rgb(164, 0, 0);")
        self.name_out.setAlignment(QtCore.Qt.AlignCenter)
        self.name_out.setObjectName("name_out")
        self.vendor_id = QtWidgets.QLabel(self.groupBox)
        self.vendor_id.setGeometry(QtCore.QRect(10, 90, 67, 21))
        self.vendor_id.setObjectName("vendor_id")
        self.vendor_id_out = QtWidgets.QLabel(self.groupBox)
        self.vendor_id_out.setGeometry(QtCore.QRect(130, 90, 311, 21))
        self.vendor_id_out.setAlignment(QtCore.Qt.AlignCenter)
        self.vendor_id_out.setObjectName("vendor_id_out")
        self.family = QtWidgets.QLabel(self.groupBox)
        self.family.setGeometry(QtCore.QRect(10, 150, 67, 21))
        self.family.setObjectName("family")
        self.family_out = QtWidgets.QLabel(self.groupBox)
        self.family_out.setGeometry(QtCore.QRect(80, 150, 67, 21))
        self.family_out.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.family_out.setAlignment(QtCore.Qt.AlignCenter)
        self.family_out.setObjectName("family_out")
        self.model = QtWidgets.QLabel(self.groupBox)
        self.model.setGeometry(QtCore.QRect(180, 150, 67, 21))
        self.model.setAlignment(QtCore.Qt.AlignCenter)
        self.model.setObjectName("model")
        self.model_out = QtWidgets.QLabel(self.groupBox)
        self.model_out.setGeometry(QtCore.QRect(260, 150, 67, 21))
        self.model_out.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.model_out.setAlignment(QtCore.Qt.AlignCenter)
        self.model_out.setObjectName("model_out")
        self.stepping = QtWidgets.QLabel(self.groupBox)
        self.stepping.setGeometry(QtCore.QRect(360, 150, 67, 21))
        self.stepping.setAlignment(QtCore.Qt.AlignCenter)
        self.stepping.setObjectName("stepping")
        self.stepping_out = QtWidgets.QLabel(self.groupBox)
        self.stepping_out.setGeometry(QtCore.QRect(450, 150, 67, 21))
        self.stepping_out.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.stepping_out.setAlignment(QtCore.Qt.AlignCenter)
        self.stepping_out.setObjectName("stepping_out")
        self.siblings = QtWidgets.QLabel(self.groupBox)
        self.siblings.setGeometry(QtCore.QRect(10, 200, 67, 21))
        self.siblings.setObjectName("siblings")
        self.siblings_out = QtWidgets.QLabel(self.groupBox)
        self.siblings_out.setGeometry(QtCore.QRect(80, 200, 71, 21))
        self.siblings_out.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.siblings_out.setAlignment(QtCore.Qt.AlignCenter)
        self.siblings_out.setObjectName("siblings_out")
        self.speed = QtWidgets.QLabel(self.groupBox)
        self.speed.setGeometry(QtCore.QRect(10, 250, 81, 21))
        self.speed.setObjectName("speed")
        self.speed_out = QtWidgets.QLabel(self.groupBox)
        self.speed_out.setGeometry(QtCore.QRect(100, 250, 321, 21))
        self.speed_out.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.speed_out.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_out.setObjectName("speed_out")
        self.cache = QtWidgets.QLabel(self.groupBox)
        self.cache.setGeometry(QtCore.QRect(10, 290, 81, 21))
        self.cache.setObjectName("cache")
        self.cache_out = QtWidgets.QLabel(self.groupBox)
        self.cache_out.setGeometry(QtCore.QRect(100, 290, 321, 21))
        self.cache_out.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.cache_out.setAlignment(QtCore.Qt.AlignCenter)
        self.cache_out.setObjectName("cache_out")
        self.pro = QtWidgets.QLabel(self.groupBox)
        self.pro.setGeometry(QtCore.QRect(350, 200, 91, 21))
        self.pro.setAlignment(QtCore.Qt.AlignCenter)
        self.pro.setObjectName("pro")
        self.pro_out = QtWidgets.QLabel(self.groupBox)
        self.pro_out.setGeometry(QtCore.QRect(450, 200, 67, 21))
        self.pro_out.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.pro_out.setAlignment(QtCore.Qt.AlignCenter)
        self.pro_out.setObjectName("pro_out")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 550, 571, 51))
        self.widget.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.selection = QtWidgets.QLabel(self.widget)
        self.selection.setGeometry(QtCore.QRect(10, 20, 81, 17))
        self.selection.setObjectName("selection")
        self.cores = QtWidgets.QLabel(self.widget)
        self.cores.setGeometry(QtCore.QRect(360, 20, 67, 17))
        self.cores.setObjectName("cores")
        self.cores_out = QtWidgets.QLabel(self.widget)
        self.cores_out.setGeometry(QtCore.QRect(460, 20, 67, 17))
        self.cores_out.setAlignment(QtCore.Qt.AlignCenter)
        self.cores_out.setObjectName("cores_out")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(100, 10, 211, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 370, 571, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.l1data = QtWidgets.QLabel(self.groupBox_2)
        self.l1data.setGeometry(QtCore.QRect(10, 40, 121, 21))
        self.l1data.setAlignment(QtCore.Qt.AlignCenter)
        self.l1data.setObjectName("l1data")
        self.l1inst = QtWidgets.QLabel(self.groupBox_2)
        self.l1inst.setGeometry(QtCore.QRect(10, 70, 111, 21))
        self.l1inst.setAlignment(QtCore.Qt.AlignCenter)
        self.l1inst.setObjectName("l1inst")
        self.lvl2 = QtWidgets.QLabel(self.groupBox_2)
        self.lvl2.setGeometry(QtCore.QRect(10, 100, 111, 21))
        self.lvl2.setAlignment(QtCore.Qt.AlignCenter)
        self.lvl2.setObjectName("lvl2")
        self.lvl3 = QtWidgets.QLabel(self.groupBox_2)
        self.lvl3.setGeometry(QtCore.QRect(10, 130, 111, 21))
        self.lvl3.setAlignment(QtCore.Qt.AlignCenter)
        self.lvl3.setObjectName("lvl3")
        self.l1data_out = QtWidgets.QLabel(self.groupBox_2)
        self.l1data_out.setGeometry(QtCore.QRect(140, 40, 341, 25))
        self.l1data_out.setAlignment(QtCore.Qt.AlignCenter)
        self.l1data_out.setObjectName("l1data_out")
        self.l1inst_out = QtWidgets.QLabel(self.groupBox_2)
        self.l1inst_out.setGeometry(QtCore.QRect(140, 70, 341, 25))
        self.l1inst_out.setAlignment(QtCore.Qt.AlignCenter)
        self.l1inst_out.setObjectName("l1inst_out")
        self.lvl2_out = QtWidgets.QLabel(self.groupBox_2)
        self.lvl2_out.setGeometry(QtCore.QRect(140, 100, 341, 25))
        self.lvl2_out.setAlignment(QtCore.Qt.AlignCenter)
        self.lvl2_out.setObjectName("lvl2_out")
        self.lvl3_out = QtWidgets.QLabel(self.groupBox_2)
        self.lvl3_out.setGeometry(QtCore.QRect(140, 130, 341, 25))
        self.lvl3_out.setAlignment(QtCore.Qt.AlignCenter)
        self.lvl3_out.setObjectName("lvl3_out")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPU Info"))
        self.groupBox.setTitle(_translate("MainWindow", "CPU"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.name_out.setText(_translate("MainWindow", model_name))
        self.vendor_id.setText(_translate("MainWindow", "Vendor ID"))
        self.vendor_id_out.setText(_translate("MainWindow", vendor_idd))
        self.family.setText(_translate("MainWindow", "Family"))
        self.family_out.setText(_translate("MainWindow", family))
        self.model.setText(_translate("MainWindow", "Model"))
        self.model_out.setText(_translate("MainWindow", model))
        self.stepping.setText(_translate("MainWindow", "Stepping"))
        self.stepping_out.setText(_translate("MainWindow", stepping))
        self.siblings.setText(_translate("MainWindow", "Siblings"))
        self.siblings_out.setText(_translate("MainWindow", siblings))
        self.speed.setText(_translate("MainWindow", "Core Speed"))
        self.speed_out.setText(_translate("MainWindow", speed))
        self.cache.setText(_translate("MainWindow", "Cache Size"))
        self.cache_out.setText(_translate("MainWindow", cache))
        self.pro.setText(_translate("MainWindow", "Processor ID"))
        self.pro_out.setText(_translate("MainWindow", processor))
        self.selection.setText(_translate("MainWindow", "Selection"))
        self.cores.setText(_translate("MainWindow", "Cores"))
        self.cores_out.setText(_translate("MainWindow", cores))
        self.comboBox.setItemText(0, _translate("MainWindow", "Processor #0"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Processor #1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Processor #2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Processor #3"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Processor #4"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Processor #5"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Processor #6"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Processor #7"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Cache"))
        self.l1data.setText(_translate("MainWindow", "L1 Data"))
        self.l1inst.setText(_translate("MainWindow", "L1 Inst"))
        self.lvl2.setText(_translate("MainWindow", "Level 2"))
        self.lvl3.setText(_translate("MainWindow", "Level 3"))
        self.l1data_out.setText(_translate("MainWindow", l1d))
        self.l1inst_out.setText(_translate("MainWindow", l1i))
        self.lvl2_out.setText(_translate("MainWindow", l2))
        self.lvl3_out.setText(_translate("MainWindow", l3))

        self.comboBox.currentTextChanged.connect(self.combsignal)

    def combsignal(self):
            index = self.comboBox.currentIndex()
            details(index)

            self.updateui(MainWindow)

    def updateui(self,MainWindow):
           	pass
           	_translate = QtCore.QCoreApplication.translate
           	self.name_out.setText(_translate("MainWindow", model_name))
           	self.vendor_id_out.setText(_translate("MainWindow", vendor_idd))
           	self.family_out.setText(_translate("MainWindow", family))
           	self.model_out.setText(_translate("MainWindow", model))
           	self.stepping_out.setText(_translate("MainWindow", stepping))
           	self.siblings_out.setText(_translate("MainWindow", siblings))
           	self.speed_out.setText(_translate("MainWindow", speed))
           	self.cache_out.setText(_translate("MainWindow", cache))
           	self.pro_out.setText(_translate("MainWindow", processor))
           	self.cores_out.setText(_translate("MainWindow", cores))
           	

def details(key):

        a = os.popen("cat /proc/cpuinfo | grep 'model name' " ).read()
        aa=a.split('\n')
        model_name_var = aa[key]
        global model_name
        model_name = model_name_var[13:]
        print(model_name)

        a = os.popen("cat /proc/cpuinfo | grep 'vendor_id' " ).read()
        aa= a.split('\n')
        model_name_var = aa[key]
        global vendor_idd
        vendor_idd =model_name_var[12:]
        print(vendor_idd)

        a = os.popen("cat /proc/cpuinfo | grep 'cpu family' " ).read()
        aa= a.split('\n')
        model_name_var = aa[key]
        global family
        family =model_name_var[13:]
        print(family)

        a = os.popen("cat /proc/cpuinfo | grep 'model' | uniq " ).read()
        aa= a.split('\n')
        model_name_var = aa[0]
        global model
        model =model_name_var[9:]
        print(model)

        a = os.popen("cat /proc/cpuinfo | grep 'stepping' " ).read()
        aa= a.split('\n')
        model_name_var = aa[key]
        global stepping
        stepping =model_name_var[11:]
        print(stepping)

        a = os.popen("cat /proc/cpuinfo | grep 'siblings' " ).read()
        aa= a.split('\n')
        model_name_var = aa[key]
        global siblings
        siblings =model_name_var[11:]
        print(siblings)

        a = os.popen("cat /proc/cpuinfo | grep 'processor' " ).read()
        aa= a.split('\n')
        model_name_var = aa[key]
        global processor
        processor =model_name_var[12:]
        print(processor)

       


        a = os.popen("cat /proc/cpuinfo | grep 'cpu MHz' " ).read()
        aa= a.split('\n')
        model_name_var = aa[key]
        global speed
        speed =model_name_var[11:] + " MHz"
        print(speed)

        a = os.popen("cat /proc/cpuinfo | grep 'cache size' " ).read()
        aa= a.split('\n')
        model_name_var = aa[key]
        global cache
        cache =model_name_var[13:]
        print(cache)

        global cores
        cores = os.popen(" cat /proc/cpuinfo | grep processor | wc -l" ).read()
        print(cores)

        a=os.popen("lscpu | grep 'L1d cache' | uniq" ).read()
        global l1d
        l1d = a[21:]
        print(l1d)

        a=os.popen("lscpu | grep 'L1i cache' | uniq" ).read()
        global l1i
        l1i = a[21:]
        print(l1i)

        a=os.popen("lscpu | grep 'L2 cache' | uniq" ).read()
        global l2
        l2 = a[21:]
        print(l2)

        a=os.popen("lscpu | grep 'L3 cache' | uniq" ).read()
        global l3
        l3 = a[21:]
        print(l3) 






if __name__ == "__main__":
    import sys
    details(0)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
