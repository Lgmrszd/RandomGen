#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import matplotlib
import random
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
from matplotlib.pyplot import xkcd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import randomcalc

histwidth=600
histheight=300


class BarCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        self.axes = fig.add_subplot(111)
        self.axes.hold(False)


        super().__init__(fig)
        self.setParent(parent)

        self.setSizePolicy(
                QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Expanding)
        self.updateGeometry()

    def redraw(self,q,ml1=False,n=-1):
        self.data=q
        self.ml1=ml1
        self.n=n
        self.update_figure()

    def update_figure(self):
        if self.n==-1:
            self.axes.bar(range(1,1+len(self.data)), self.data, align='center', color='pink')
        else:
            self.axes.bar(range(1,1+len(self.data)), self.data, align='center', color=['yellow']*self.n+['green']*(len(self.data)-self.n-1)+['red'])
        if self.ml1:
           self.axes.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=1))
        self.draw()

class Ui_Form(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def readSimpleVar(self):
        self.a_lineedit.setText(self.a_lineedit.text()+'0'*(1//(len(self.a_lineedit.text())+1)))
        self.b_lineedit.setText(self.b_lineedit.text()+'0'*(1//(len(self.b_lineedit.text())+1)))
        self.c_lineedit.setText(self.c_lineedit.text()+'1'*(1//(len(self.c_lineedit.text())+1)))
        self.x0_lineedit.setText(self.x0_lineedit.text()+'0'*(1//(len(self.x0_lineedit.text())+1)))
        return int(self.a_lineedit.text()), int(self.b_lineedit.text()), int(self.c_lineedit.text()), int(self.x0_lineedit.text())

    def readHardVar(self):
        self.a_lineedit.setText(self.a_lineedit.text()+'0'*(1//(len(self.a_lineedit.text())+1)))
        self.b_lineedit.setText(self.b_lineedit.text()+'0'*(1//(len(self.b_lineedit.text())+1)))
        self.c_lineedit.setText(self.c_lineedit.text()+'0'*(1//(len(self.c_lineedit.text())+1)))
        self.d_lineedit.setText(self.d_lineedit.text()+'1'*(1//(len(self.d_lineedit.text())+1)))
        self.x0_lineedit.setText(self.x0_lineedit.text()+'0'*(1//(len(self.x0_lineedit.text())+1)))
        self.x1_lineedit.setText(self.x1_lineedit.text()+'0'*(1//(len(self.x1_lineedit.text())+1)))
        return int(self.a_lineedit.text()), int(self.b_lineedit.text()), int(self.c_lineedit.text()), int(self.d_lineedit.text()), int(self.x0_lineedit.text()), int(self.x1_lineedit.text())

    def calculateSimple(self):
        a,b,c,x0=self.readSimpleVar()
        lp=randomcalc.findsimplelp(a,b,c,x0)
        ln=randomcalc.findsimpleln(a,b,c,x0,lp)
        s,q=randomcalc.simplequality(a,b,c,x0)
        self.ln_text.setText('<b>'+str(ln)+'</b>')
        self.lp_text.setText('<b>'+str(lp)+'</b>')
        self.q_text.setText('<b>'+str(s)+'</b>')
        print(lp,ln,s,q)
        with xkcd():
            self.quality_bar.redraw(q,ml1=True)
        if self.draw_data_btn.isChecked():
            self.data_bar.redraw(randomcalc.calculatesimple(lp+ln+1,a,b,c,x0),n=ln)

    def calculateHard(self):
        a,b,c,d,x0,x1=self.readHardVar()
        lp=randomcalc.findhardlp(a,b,c,d,x0,x1)
        ln=randomcalc.findhardln(a,b,c,d,x0,x1,lp)
        s,q=randomcalc.hardquality(a,b,c,d,x0,x1)
        self.ln_text.setText('<b>'+str(ln)+'</b>')
        self.lp_text.setText('<b>'+str(lp)+'</b>')
        self.q_text.setText('<b>'+str(s)+'</b>')
        print(lp,ln,s,q)
        with xkcd():
            self.quality_bar.redraw(q,ml1=True)
        if self.draw_data_btn.isChecked():
            self.data_bar.redraw(randomcalc.calculatehard(lp+ln+1,a,b,c,d,x0,x1),n=ln)

    def drawSimple(self):
        if self.draw_data_btn.isChecked():
            self.calculateSimple()

    def drawHard(self):
        if self.draw_data_btn.isChecked():
            self.calculateHard()

    def openSimple(self):
        a,b,c,x0=self.readSimpleVar()
        lp=randomcalc.findsimplelp(a,b,c,x0)
        ln=randomcalc.findsimpleln(a,b,c,x0,lp)
        data=randomcalc.calculatesimple(lp+ln+1,a,b,c,x0)
        plt.bar(range(1,1+len(data)), data, align='center', color=['yellow']*ln+['green']*(len(data)-ln-1)+['red'])
        plt.show()

    def openHard(self):
        a,b,c,d,x0,x1=self.readHardVar()
        lp=randomcalc.findhardlp(a,b,c,d,x0,x1)
        ln=randomcalc.findhardln(a,b,c,d,x0,x1,lp)
        data=randomcalc.calculatehard(lp+ln+1,a,b,c,d,x0,x1)
        plt.bar(range(1,1+len(data)), data, align='center', color=['yellow']*ln+['green']*(len(data)-ln-1)+['red'])
        plt.show()

    def drawBtnClick(self):
        if self.draw_data_btn.isChecked():
            if self.hard_GroupBox.isChecked():
                self.drawHard()
            else:
                self.drawSimple()
        else:
            self.data_bar.redraw([],n=0)


    def openBtnClick(self):
        if self.hard_GroupBox.isChecked():
            self.openHard()
        else:
            self.openSimple()

    def btnClick(self):
        if self.hard_GroupBox.isChecked():
            self.calculateHard()
        else:
            self.calculateSimple()

    def initUI(self):
        line_valid=QtGui.QIntValidator(0,300000)

        self.a_label=QtWidgets.QLabel('A:')
        self.a_lineedit=QtWidgets.QLineEdit()
        self.a_lineedit.setFixedWidth(50)
        self.a_lineedit.setValidator(line_valid)

        self.b_label=QtWidgets.QLabel('B:')
        self.b_lineedit=QtWidgets.QLineEdit()
        self.b_lineedit.setFixedWidth(50)
        self.b_lineedit.setValidator(line_valid)

        self.c_label=QtWidgets.QLabel('C:')
        self.c_lineedit=QtWidgets.QLineEdit()
        self.c_lineedit.setFixedWidth(50)
        self.c_lineedit.setValidator(line_valid)

        self.x0_label=QtWidgets.QLabel('X0:')
        self.x0_lineedit=QtWidgets.QLineEdit()
        self.x0_lineedit.setFixedWidth(50)
        self.x0_lineedit.setValidator(line_valid)

        self.x1_label=QtWidgets.QLabel('X1:')
        self.x1_lineedit=QtWidgets.QLineEdit()
        self.x1_lineedit.setFixedWidth(50)
        self.x1_lineedit.setValidator(line_valid)

        self.d_label=QtWidgets.QLabel('D:')
        self.d_lineedit=QtWidgets.QLineEdit()
        self.d_lineedit.setFixedWidth(50)
        self.d_lineedit.setValidator(line_valid)

        self.a_VBox=QtWidgets.QVBoxLayout()
        self.a_VBox.addWidget(self.a_label)
        self.a_VBox.addWidget(self.a_lineedit)

        self.b_VBox=QtWidgets.QVBoxLayout()
        self.b_VBox.addWidget(self.b_label)
        self.b_VBox.addWidget(self.b_lineedit)

        self.c_VBox=QtWidgets.QVBoxLayout()
        self.c_VBox.addWidget(self.c_label)
        self.c_VBox.addWidget(self.c_lineedit)

        self.x0_VBox=QtWidgets.QVBoxLayout()
        self.x0_VBox.addWidget(self.x0_label)
        self.x0_VBox.addWidget(self.x0_lineedit)

        self.simple_prefHBox=QtWidgets.QHBoxLayout()
        self.simple_prefHBox.addLayout(self.a_VBox)
        self.simple_prefHBox.addLayout(self.b_VBox)
        self.simple_prefHBox.addLayout(self.c_VBox)
        self.simple_prefHBox.addLayout(self.x0_VBox)

        self.simple_GroupBox=QtWidgets.QGroupBox('Основные параметры')
        self.simple_GroupBox.setLayout(self.simple_prefHBox)

        self.x1_VBox=QtWidgets.QVBoxLayout()
        self.x1_VBox.addWidget(self.x1_label)
        self.x1_VBox.addWidget(self.x1_lineedit)

        self.d_VBox=QtWidgets.QVBoxLayout()
        self.d_VBox.addWidget(self.d_label)
        self.d_VBox.addWidget(self.d_lineedit)

        self.hard_prefHBox=QtWidgets.QHBoxLayout()
        self.hard_prefHBox.addLayout(self.x1_VBox)
        self.hard_prefHBox.addLayout(self.d_VBox)

        self.hard_GroupBox=QtWidgets.QGroupBox('Сложный генератор')
        self.hard_GroupBox.setLayout(self.hard_prefHBox)
        self.hard_GroupBox.setCheckable(True)
        self.hard_GroupBox.setChecked(False)

        self.calculate_btn=QtWidgets.QPushButton('Рассчитать')
        self.calculate_btn.clicked.connect(self.btnClick)
        self.calculate_btn.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.ln_text=QtWidgets.QLabel('0')
        self.ln_text.setFixedWidth(40)

        self.lp_text=QtWidgets.QLabel('0')
        self.lp_text.setFixedWidth(40)

        self.q_text=QtWidgets.QLabel('0')
        self.q_text.setFixedWidth(40)

        self.prefHBox=QtWidgets.QHBoxLayout()
        self.prefHBox.addWidget(self.simple_GroupBox)
        self.prefHBox.addWidget(self.hard_GroupBox)
        self.prefHBox.addWidget(self.calculate_btn)

        self.resultHBox=QtWidgets.QHBoxLayout()
        self.resultHBox.addWidget(QtWidgets.QLabel('Предпериод:'))
        self.resultHBox.addWidget(self.ln_text)
        self.resultHBox.addWidget(QtWidgets.QLabel('Период:'))
        self.resultHBox.addWidget(self.lp_text)
        self.resultHBox.addWidget(QtWidgets.QLabel('Качество:'))
        self.resultHBox.addWidget(self.q_text)

        self.quality_bar = BarCanvas(width=5, height=4, dpi=100)
        self.quality_bar.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Maximum)
        self.quality_bar.setMinimumHeight(200)

        self.data_bar = BarCanvas(width=5, height=4, dpi=100)
        self.data_bar.setMinimumHeight(200)
        self.draw_data_btn=QtWidgets.QPushButton('\n'.join(list('Отрисовывать')))
        self.draw_data_btn.setCheckable(True)
        self.draw_data_btn.setChecked(True)
        self.draw_data_btn.clicked.connect(self.drawBtnClick)
        self.draw_data_btn.setFixedWidth(20)
        self.draw_data_btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.show_data_btn=QtWidgets.QPushButton('\n'.join(list('Открыть в окне')))
        self.show_data_btn.clicked.connect(self.openBtnClick)
        self.show_data_btn.setFixedWidth(20)
        self.show_data_btn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)

        self.advancedHBox=QtWidgets.QHBoxLayout()
        self.advancedHBox.addWidget(self.draw_data_btn)
        self.advancedHBox.addWidget(self.data_bar)
        self.advancedHBox.addWidget(self.show_data_btn)

        self.mainVBox = QtWidgets.QVBoxLayout()
        self.mainVBox.addLayout(self.prefHBox)
        self.mainVBox.addLayout(self.resultHBox)
        self.mainVBox.addWidget(QtWidgets.QLabel('Оценка качества:'))
        self.mainVBox.addWidget(self.quality_bar)
        self.mainVBox.addWidget(QtWidgets.QLabel('Первые <b>ln+lp+1</b> элементов:'))
        self.mainVBox.addLayout(self.advancedHBox)
        self.mainVBox.addStretch(1)

        self.uiwidget = QtWidgets.QWidget()
        self.uiwidget.setLayout(self.mainVBox)

        self.setCentralWidget(self.uiwidget)
        self.setGeometry(0, 0, 500, 300)
        self.setWindowTitle('Генератор псевдослучайных чисел')

app = QtWidgets.QApplication(sys.argv)
Form = Ui_Form()
Form.show()
sys.exit(app.exec_())
