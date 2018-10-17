# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pytest3.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import *
import sys
import os
from PyQt5.QtCore import Qt
from PIL import Image


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

global label_text
global label_2_text
global label_3_text

label_text = ""
label_2_text = ""
label_3_text = ""

global path_dict

# 遍历文件夹下面的文件
def listDir(rootDir):
    dirlist = []
    for filename in os.listdir(rootDir):
        pathname = os.path.join(rootDir, filename)
        if os.path.isfile(pathname):
            dirlist.append(pathname)

    return dirlist

path_dict = {}

#filenames = listDir(os.path.join(os.getcwd(), "images"))
filenames = listDir(os.path.join("/home/lebo/faceqt", "images"))

for filename in filenames:
    key = filename.split(os.sep)[-1].split('.')[0]
    path_dict.update({str(key): filename})
# print(path_dict)


# # resize图片
# def resize_img(star):
#     img = Image.open(path_dict.get(star, ''))
#     if not os.path.exists(os.path.join(os.getcwd(), "resizeimg")):
#         os.mkdir(os.path.join(os.getcwd(), "resizeimg"))
#
#     out = img.resize((259, 289), Image.ANTIALIAS)  # resize image with high-quality
#     out.save(os.path.join(os.getcwd(), "resizeimg"+os.sep+"%s.jpg" % star))



# 保存图片
def savepath(star):
    """
    :param star: 明星
    :return: 返回保存文件的路径
    """
    if os.path.exists('/home/lebo/faceqt/path.txt'):
        f = open('/home/lebo/faceqt/path.txt', 'w')
        global path_dict
        f.write(path_dict.get(star))
        f.close()
    
    if os.path.getsize("/home/lebo/faceqt/path.txt"):
        # 执行shell命令
        f = open('/home/lebo/faceqt/path.txt', 'r')
        path = f.readline()
        print("##" * 40)
        print(path)
        print("##" * 40)
        f.close()
        os.system("killall -9 /home/PoseFaceSwap/openpose_face.py")
        os.system("/usr/bin/python3 /home/PoseFaceSwap/openpose_face.py %s &" % path)
    # if os.path.getsize("path.txt"):
    # 执行shell命令
    # os.system("python zad2")


class MyLabel(QtWidgets.QLabel):
    def mousePressEvent(self, ev=QtGui.QMouseEvent):
        savepath(label_text)


class MyLabel2(QtWidgets.QLabel):
    def mousePressEvent(self, ev=QtGui.QMouseEvent):
        savepath(label_2_text)


class MyLabel3(QtWidgets.QLabel):
    def mousePressEvent(self, ev=QtGui.QMouseEvent):
        savepath(label_3_text)


class Ui_Form(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setObjectName("Form")
        self.resize(957, 629)

        # 明星变量
        self.is_default = True

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 120, 791, 291))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = MyLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(0, 0, 259, 289))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = MyLabel2(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 259, 289))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = MyLabel3(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 259, 289))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.frame)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(10, 260, 41, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 250, 41, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(370, 20, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # 图片下标
        self.start_index = 0
        self.end_index = 3
        self.current_star = []
        self.length = len(list(path_dict.keys()))

        if self.is_default:
            self.showImage(list(path_dict.keys())[self.start_index:self.end_index])

        # 左移
        self.pushButton.clicked.connect(lambda: self.leftmove())
        # 右移
        self.pushButton_2.clicked.connect(lambda: self.rightmove())


        # self.label.linkActivated.connect(lambda: self.labelfunc())
        # self.label_2.triggered.connect(lambda: self.label2func())
        # self.label_3.triggered.connect(lambda: self.label3func())


    # 左移
    def leftmove(self):
        self.is_default = False
        if self.start_index != 0:
            self.start_index = self.start_index - 1
            self.end_index = self.end_index - 1

            self.showImage(list(path_dict.keys())[self.start_index:self.end_index])

    # 右移
    def rightmove(self):
        self.is_default = False
        if self.end_index != self.length:
            self.start_index = self.start_index + 1
            self.end_index = self.end_index + 1

            self.showImage(list(path_dict.keys())[self.start_index:self.end_index])

    def showImage(self, starlist):
        self.showImage1(star=starlist[0])
        self.showImage2(star=starlist[1])
        self.showImage3(star=starlist[2])

    # label 上设置图片标签
    def showImage1(self, star):
        """
        :param star: 哪个明星
        :return: 设置图片
        """
        # if not os.path.exists(os.path.join(os.getcwd(), "resizeimg"+os.sep+"%s.jpg" % star)):
        #     resize_img(star)

        img = QImage(path_dict.get(star))
        img = img.scaled(259, 289)
        self.label.setText(star)
        global label_text
        label_text = self.label.text()

        self.label.setPixmap(QPixmap.fromImage(img))

    # label_3 上设置图片标签
    def showImage2(self, star):
        """
        :param star: 哪个明星
        :return: 设置图片
        """
        # if not os.path.exists(os.path.join(os.getcwd(), "images"+os.sep+"%s.jpg" % star)):
        #     resize_img(star)

        img = QImage(path_dict.get(star))
        img = img.scaled(259, 289)
        self.label_2.setText(star)
        global label_2_text
        label_2_text = self.label_2.text()

        self.label_2.setPixmap(QPixmap.fromImage(img))

    # label_2 上设置图片标签
    def showImage3(self, star):
        """
        :param star: 哪个明星
        :return: 设置图片
        """
        # if not os.path.exists(os.path.join(os.getcwd(), "resizeimg"+os.sep+"%s.jpg" % star)):
        #     resize_img(star)

        img = QImage(path_dict.get(star))
        img = img.scaled(259, 289)
        self.label_3.setText(star)
        global label_3_text
        label_3_text = self.label_3.text()

        self.label_3.setPixmap(QPixmap.fromImage(img))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "明星换脸"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        # self.pushButton.setText(_translate("Form", "左移"))
        self.pushButton.setIcon(QIcon('/home/lebo/faceqt/left.png'))
        # self.pushButton_2.setText(_translate("Form", "右移"))
        self.pushButton_2.setIcon(QIcon('/home/lebo/faceqt/right.png'))
        self.label_4.setText(_translate("Form", " 明星换脸"))
        self.label_4.setAlignment(Qt.AlignCenter)

        # pe = QPalette()
        # pe.setColor(QPalette.WindowText, Qt.red)
        # self.label_4.setAutoFillBackground(True)

        # self.label_4.setFont(QFont("Roman times", 18, QFont.Bold))


        self.pushButton.setStyleSheet("QPushButton{color:white}"
                                      # "QPushButton{background-color:green}"
                                      "QPushButton{border:1px}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{padding:2px 4px}")
        self.pushButton_2.setStyleSheet("QPushButton{color:white}"
                                      # "QPushButton{background-color:green}"
                                      "QPushButton{border:1px}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{padding:2px 4px}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Ui_Form()
    win.show()
    sys.exit(app.exec_())
