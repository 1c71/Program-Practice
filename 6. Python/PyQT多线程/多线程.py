# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\eric4-4.3.9\eric\database.ui'
#
# Created: Sat Nov 21 22:51:20 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 621)
        self.thread=Worker()
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 270, 611, 251))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 591, 201))
        self.textEdit.setObjectName("textEdit")
        self.getDataButton = QtGui.QCommandLinkButton(self.tab)
        self.getDataButton.setEnabled(True)
        self.getDataButton.setGeometry(QtCore.QRect(270, 80, 71, 31))
        self.getDataButton.setObjectName("getDataButton")
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 10, 261, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 2, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_12.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 3, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)
        self.cancelButton = QtGui.QPushButton(self.tab)
        self.cancelButton.setGeometry(QtCore.QRect(520, 540, 81, 41))
        self.cancelButton.setObjectName("cancelButton")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 251, 171))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_9.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 2, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 190, 611, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(120, 30, 91, 31))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        Form.addTab(self.tab, "")
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName("tab1")
        Form.addTab(self.tab1, "")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.thread, QtCore.SIGNAL("start()"), self.update1)
        QtCore.QObject.connect(self.thread, QtCore.SIGNAL("terminated()"),self.update2)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), Form.close)
        QtCore.QObject.connect(self.thread, QtCore.SIGNAL("log(QString)"),self.log)
        QtCore.QObject.connect(self.getDataButton, QtCore.SIGNAL("clicked()"),self.test )
        QtCore.QMetaObject.connectSlotsByName(Form)
    def update1(self):
       self.getDataButton.setDisabled(True)


    def update2(self):
        self.getDataButton.setDisabled(False)

    def log(self,text):
        self.textEdit.append(text)
    def test(self):
        self.thread.render()



    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "日志信息", None, QtGui.QApplication.UnicodeUTF8))
        self.getDataButton.setText(QtGui.QApplication.translate("Form", "导入", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "目标服务器", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "目标服务器", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "用户", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "密码", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "连接测试", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Form", "关闭", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "源服务器", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "源服务器", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "用户", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "密码", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "连接测试", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "目标数据库", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "s1config", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Form", "xstudio", None, QtGui.QApplication.UnicodeUTF8))
        Form.setTabText(Form.indexOf(self.tab), QtGui.QApplication.translate("Form", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        Form.setTabText(Form.indexOf(self.tab1), QtGui.QApplication.translate("Form", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))


class Worker(QtCore.QThread):

    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.exiting = False

    def __del__(self):

        self.exiting = True
        self.wait()

    def render(self):
        self.start()

    def run(self):
        self.emit(QtCore.SIGNAL("start()"))
        time.sleep(2)
        self.emit(QtCore.SIGNAL("log(QString)"),u'text')
        time.sleep(2)
        self.emit(QtCore.SIGNAL("terminated()"))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QTabWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())