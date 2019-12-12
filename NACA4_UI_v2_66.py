# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NACA4_v2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DLED_NACA4_ver0924 as DLED
import subprocess as sp
import time
import sys, os
import NACA4_Config as Config
import NACA4_CalADC as CalADC
import NACA4_Log as Log
import NACA4_message as msg
import NACA4_Rinput as Rin
import numpy as np
#print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)
#print(sys.getrecursionlimit())

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
direct_code=os.path.dirname(os.path.realpath(__file__))
direct_RR=os.path.join(direct_code,"Result")
Log.log(None)

Performance_max = [1.5195, 0.115, 0.01168, 0, 0.0036]
Performance_min = [0.0, 0.095, 0.004, -0.4, -0.0020]

Slider_max = 100000
Slider_min = 0

direct_code = os.path.dirname(os.path.realpath('__file__'))
Resultdirect = os.path.join(direct_code,"Result")

ANN_Device = 'GPU'

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1000, 600)

#        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
#        MainWindow.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
#        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        MainWindow.windowOpacity() # Mainwindow's Opacity
#        MainWindow.setWindowOpacity(0.75)
        MainWindow.setStyleSheet("background-color: rgb(70,70,70); color: rgb(255,255,255)")
        
        self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(570, 10, 400, 140))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        ##=================================== XFOIL Analysis Button ================================== ##
        self.XFOIL_Analysis_pushButton = QtWidgets.QPushButton(MainWindow)
        self.XFOIL_Analysis_pushButton.setGeometry(QtCore.QRect(460, 110, 100, 60))
        
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.XFOIL_Analysis_pushButton.setFont(font)
        self.XFOIL_Analysis_pushButton.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 5px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                              "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 5px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.XFOIL_Analysis_pushButton.setAutoRepeat(True)
        self.XFOIL_Analysis_pushButton.setAutoDefault(False)
        self.XFOIL_Analysis_pushButton.setObjectName("XFOIL_Analysis_pushButton")
        
        ##================================ NACA 4-digit Shape Parameter ============================== ##
        
        ## Maximum Camber ##
        
        self.label_Max_camber = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Max_camber.sizePolicy().hasHeightForWidth())
        self.label_Max_camber.setSizePolicy(sizePolicy)
        self.label_Max_camber.setMinimumSize(QtCore.QSize(180, 30))
        self.label_Max_camber.setMaximumSize(QtCore.QSize(180, 30))
        self.label_Max_camber.setObjectName("label_Max_camber")
        self.gridLayout.addWidget(self.label_Max_camber, 0, 0, 1, 1)
        
        self.Max_Camber_value = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Max_Camber_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Max_Camber_value.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"맑은 고딕\";color: rgb(0,0,0);")
        self.Max_Camber_value.setObjectName("Max_Camber_value")
        self.gridLayout.addWidget(self.Max_Camber_value, 0, 1, 1, 1)
        
        ## Maximum Camber Location ##
        
        self.label_Max_camber_Loc = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Max_camber_Loc.sizePolicy().hasHeightForWidth())
        self.label_Max_camber_Loc.setSizePolicy(sizePolicy)
        self.label_Max_camber_Loc.setMinimumSize(QtCore.QSize(180, 30))
        self.label_Max_camber_Loc.setMaximumSize(QtCore.QSize(180, 30))
        self.label_Max_camber_Loc.setObjectName("label_Max_camber_Loc")
        self.gridLayout.addWidget(self.label_Max_camber_Loc, 1, 0, 1, 1)
        
        self.Max_Camber_Loc_value = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Max_Camber_Loc_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Max_Camber_Loc_value.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"맑은 고딕\";color: rgb(0,0,0);")
        self.Max_Camber_Loc_value.setObjectName("Max_Camber_Loc_value")
        self.gridLayout.addWidget(self.Max_Camber_Loc_value, 1, 1, 1, 1)
        
        ## Maximum Thickness ##
                
        self.label_Max_thicknees = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Max_thicknees.sizePolicy().hasHeightForWidth())
        self.label_Max_thicknees.setSizePolicy(sizePolicy)
        self.label_Max_thicknees.setMinimumSize(QtCore.QSize(180, 30))
        self.label_Max_thicknees.setMaximumSize(QtCore.QSize(180, 30))
        self.label_Max_thicknees.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Max_thicknees.setObjectName("label_Max_thicknees")
        self.gridLayout.addWidget(self.label_Max_thicknees, 2, 0, 1, 1)
                
        self.Max_Thickness_value = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Max_Thickness_value.setAlignment(QtCore.Qt.AlignCenter)
        self.Max_Thickness_value.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"맑은 고딕\";color: rgb(0,0,0);")
        self.Max_Thickness_value.setObjectName("Max_Thickness_value")
        self.gridLayout.addWidget(self.Max_Thickness_value, 2, 1, 1, 1)
             
        ##-----------------------------------------------------------------------------------------------------##
        
        self.gridLayoutWidget_2 = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 170, 541, 401))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        ##====================================== Lift Coefficient Section =====================================##
        
        # Push Button: Cl,0 #
        self.Cl_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cl_pushButton.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(65,165,255); background-color: rgb(0,135,255); color: rgb(255,255,255)}" + \
                                         "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(50,170,255); background-color: rgb(65,165,255); color: rgb(255,255,255)}")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.Cl_pushButton.setFont(font)
        self.Cl_pushButton.setAutoDefault(False)
        self.Cl_pushButton.setObjectName("Cl_pushButton")
        self.Cl_pushButton.setMinimumSize(QtCore.QSize(60, 30))
        self.Cl_pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.gridLayout_2.addWidget(self.Cl_pushButton, 0, 0, 1, 1)
                
        # Push Button: Down #
        self.Cl_pushButton_Down = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cl_pushButton_Down.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                              "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cl_pushButton_Down.setAutoRepeat(True)
        self.Cl_pushButton_Down.setAutoDefault(False)
        self.Cl_pushButton_Down.setObjectName("Cl_pushButton_Down")
        self.Cl_pushButton_Down.setMinimumSize(QtCore.QSize(75, 30))
        self.Cl_pushButton_Down.setMaximumSize(QtCore.QSize(75, 30))
        self.gridLayout_2.addWidget(self.Cl_pushButton_Down, 0, 1, 1, 1)
        
        # Slider #
        self.Slider_cl0 = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.Slider_cl0.setMinimumSize(QtCore.QSize(200, 25))
        self.Slider_cl0.setMaximumSize(QtCore.QSize(200, 25))
        self.Slider_cl0.setMaximum(Slider_max)
        self.Slider_cl0.setSingleStep(1)
        self.Slider_cl0.setPageStep(10)
        self.Slider_cl0.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_cl0.setObjectName("Slider_cl0")
        self.gridLayout_2.addWidget(self.Slider_cl0, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        
        # Push Button: up #
        self.Cl_pushButton_up = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cl_pushButton_up.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                            "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cl_pushButton_up.setAutoRepeat(True)
        self.Cl_pushButton_up.setAutoDefault(False)
        self.Cl_pushButton_up.setObjectName("Cl_pushButton_up")
        self.Cl_pushButton_up.setMinimumSize(QtCore.QSize(75, 30))
        self.Cl_pushButton_up.setMaximumSize(QtCore.QSize(75, 30))
        self.gridLayout_2.addWidget(self.Cl_pushButton_up, 0, 3, 1, 1)
        
        # Spin Box #
        self.Cl_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.Cl_doubleSpinBox.setMinimumSize(QtCore.QSize(100, 30))
        self.Cl_doubleSpinBox.setMaximumSize(QtCore.QSize(100, 30))
        self.Cl_doubleSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Cl_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Cl_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons) # No buttons in the spin box
        self.Cl_doubleSpinBox.setKeyboardTracking(False) # No Keyboard Tracking = Typing result will be update after pressing the enter
        self.Cl_doubleSpinBox.setObjectName("Cl_doubleSpinBox")
        self.Cl_doubleSpinBox.setDecimals(5)
        self.Cl_doubleSpinBox.setMaximum(Performance_max[0]*2)
        self.Cl_doubleSpinBox.setMinimum(Performance_min[0])
        self.Cl_doubleSpinBox.setSingleStep(0.01)
        self.gridLayout_2.addWidget(self.Cl_doubleSpinBox, 0, 4, 1, 1)
        
        
        
        ##-------------------------------------- Lift Coefficient Section -------------------------------------##
        
        ##=================================== Lift Slope Coefficient Section ==================================##
        
        # Push Button: Cl,0 #
        self.Cla_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cla_pushButton.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(65,165,255); background-color: rgb(0,135,255); color: rgb(255,255,255)}" + \
                                          "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(50,170,255); background-color: rgb(65,165,255); color: rgb(255,255,255)}")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.Cla_pushButton.setFont(font)
        self.Cla_pushButton.setAutoDefault(False)
        self.Cla_pushButton.setObjectName("Cla_pushButton")
        self.Cla_pushButton.setMinimumSize(QtCore.QSize(60, 30))
        self.Cla_pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.gridLayout_2.addWidget(self.Cla_pushButton, 1, 0, 1, 1)
        
        # Push Button: Down #
        self.Cla_pushButton_down = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cla_pushButton_down.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                               "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cla_pushButton_down.setAutoRepeat(True)
        self.Cla_pushButton_down.setAutoDefault(False)
        self.Cla_pushButton_down.setMinimumSize(QtCore.QSize(75, 30))
        self.Cla_pushButton_down.setMaximumSize(QtCore.QSize(75, 30))
        self.Cla_pushButton_down.setObjectName("Cla_pushButton_down")
        self.gridLayout_2.addWidget(self.Cla_pushButton_down, 1, 1, 1, 1)
        
        # Slider #
        self.Slider_cla0 = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.Slider_cla0.setMinimumSize(QtCore.QSize(200, 25))
        self.Slider_cla0.setMaximumSize(QtCore.QSize(200, 25))
        self.Slider_cla0.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_cla0.setMaximum(Slider_max)
        self.Slider_cla0.setSingleStep(1)
        self.Slider_cla0.setPageStep(10)
        self.Slider_cla0.setObjectName("Slider_cla0")
        self.gridLayout_2.addWidget(self.Slider_cla0, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        
        # Push Button: Up #
        self.Cla_pushButton_up = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cla_pushButton_up.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                             "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cla_pushButton_up.setAutoRepeat(True)
        self.Cla_pushButton_up.setAutoDefault(False)
        self.Cla_pushButton_up.setMinimumSize(QtCore.QSize(75, 30))
        self.Cla_pushButton_up.setMaximumSize(QtCore.QSize(75, 30))
        self.Cla_pushButton_up.setObjectName("Cla_pushButton_up")
        self.gridLayout_2.addWidget(self.Cla_pushButton_up, 1, 3, 1, 1)
        
        # Double Spin Box #
        self.Cla_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.Cla_doubleSpinBox.setMinimumSize(QtCore.QSize(100, 30))
        self.Cla_doubleSpinBox.setMaximumSize(QtCore.QSize(100, 30))
        self.Cla_doubleSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Cla_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Cla_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons) # No buttons in the spin box
        self.Cla_doubleSpinBox.setKeyboardTracking(False) # No Keyboard Tracking = Typing result will be update after pressing the enter
        self.Cla_doubleSpinBox.setObjectName("Cla_doubleSpinBox")
        self.Cla_doubleSpinBox.setMaximum(Performance_max[1]*10)
        self.Cla_doubleSpinBox.setMinimum(Performance_min[1]*-10)
        self.Cla_doubleSpinBox.setDecimals(5)
        self.Cla_doubleSpinBox.setSingleStep(0.01)
        self.gridLayout_2.addWidget(self.Cla_doubleSpinBox, 1, 4, 1, 1)
        
        ##----------------------------------- Lift Slope Coefficient Section ----------------------------------##
        
        ##====================================== Drag Coefficient Section =====================================##
        
        ## Push Button ##
        self.Cd_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cd_pushButton.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(65,165,255); background-color: rgb(0,135,255); color: rgb(255,255,255)}" + \
                                         "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(50,170,255); background-color: rgb(65,165,255); color: rgb(255,255,255)}")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.Cd_pushButton.setFont(font)
        self.Cd_pushButton.setAutoDefault(False)
        self.Cd_pushButton.setObjectName("Cd_pushButton")
        self.Cd_pushButton.setMinimumSize(QtCore.QSize(60, 30))
        self.Cd_pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.gridLayout_2.addWidget(self.Cd_pushButton, 2, 0, 1, 1)
           
        # Push Button: Down #
        self.Cd_pushButton_down = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cd_pushButton_down.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                              "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cd_pushButton_down.setAutoRepeat(True)
        self.Cd_pushButton_down.setAutoDefault(False)
        self.Cd_pushButton_down.setMinimumSize(QtCore.QSize(75, 30))
        self.Cd_pushButton_down.setMaximumSize(QtCore.QSize(75, 30))
        self.Cd_pushButton_down.setObjectName("Cd_pushButton_down")
        self.gridLayout_2.addWidget(self.Cd_pushButton_down, 2, 1, 1, 1)   
        
        # Slider #
        self.Slider_cd0 = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.Slider_cd0.setMinimumSize(QtCore.QSize(200, 25))
        self.Slider_cd0.setMaximumSize(QtCore.QSize(200, 25))
        self.Slider_cd0.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_cd0.setMaximum(Slider_max)
        self.Slider_cd0.setSingleStep(1)
        self.Slider_cd0.setPageStep(10)
        self.Slider_cd0.setObjectName("Slider_cd0")
        self.gridLayout_2.addWidget(self.Slider_cd0, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        
        # Push Button: Up #
        self.Cd_pushButton_up = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cd_pushButton_up.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                            "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cd_pushButton_up.setAutoRepeat(True)
        self.Cd_pushButton_up.setAutoDefault(False)
        self.Cd_pushButton_up.setMinimumSize(QtCore.QSize(75, 30))
        self.Cd_pushButton_up.setMaximumSize(QtCore.QSize(75, 30))
        self.Cd_pushButton_up.setObjectName("Cd_pushButton_up")
        self.gridLayout_2.addWidget(self.Cd_pushButton_up, 2, 3, 1, 1)
        
        # Double Spin Box #
        self.Cd_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.Cd_doubleSpinBox.setMinimumSize(QtCore.QSize(100, 30))
        self.Cd_doubleSpinBox.setMaximumSize(QtCore.QSize(100, 30))
        self.Cd_doubleSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Cd_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Cd_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons) # No buttons in the spin box
        self.Cd_doubleSpinBox.setKeyboardTracking(False) # No Keyboard Tracking = Typing result will be update after pressing the enter
        self.Cd_doubleSpinBox.setObjectName("Cd_doubleSpinBox")
        self.Cd_doubleSpinBox.setMaximum(Performance_max[2]*2)
        self.Cd_doubleSpinBox.setMinimum(Performance_min[2])
        self.Cd_doubleSpinBox.setDecimals(5)
        self.Cd_doubleSpinBox.setSingleStep(0.01)
        self.gridLayout_2.addWidget(self.Cd_doubleSpinBox, 2, 4, 1, 1)
        ##-------------------------------------- Drag Coefficient Section -------------------------------------##
        
        ##===================================== Moment Coefficient Section ====================================##
        # Push Button: Cm,0 #
        self.Cm_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cm_pushButton.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(65,165,255); background-color: rgb(0,135,255); color: rgb(255,255,255)}" + \
                                         "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(50,170,255); background-color: rgb(65,165,255); color: rgb(255,255,255)}")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.Cm_pushButton.setFont(font)
        self.Cm_pushButton.setAutoDefault(False)
        self.Cm_pushButton.setObjectName("Cl_pushButton")
        self.Cm_pushButton.setMinimumSize(QtCore.QSize(60, 30))
        self.Cm_pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.gridLayout_2.addWidget(self.Cm_pushButton, 3, 0, 1, 1)
        
        # Push Button: Down #
        self.Cm_pushButton_down = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cm_pushButton_down.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                              "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cm_pushButton_down.setAutoRepeat(True)
        self.Cm_pushButton_down.setAutoDefault(False)
        self.Cm_pushButton_down.setMinimumSize(QtCore.QSize(75, 30))
        self.Cm_pushButton_down.setMaximumSize(QtCore.QSize(75, 30))
        self.Cm_pushButton_down.setObjectName("Cm_pushButton_down")
        self.gridLayout_2.addWidget(self.Cm_pushButton_down, 3, 1, 1, 1)
        
        # Slider #
        self.Slider_cm0 = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.Slider_cm0.setMinimumSize(QtCore.QSize(200, 25))
        self.Slider_cm0.setMaximumSize(QtCore.QSize(200, 25))
        self.Slider_cm0.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_cm0.setMaximum(Slider_max)
        self.Slider_cm0.setSingleStep(1)
        self.Slider_cm0.setPageStep(10)
        self.Slider_cm0.setObjectName("Slider_cm0")
        self.gridLayout_2.addWidget(self.Slider_cm0, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        
        # Push Button: Up #
        self.Cm_pushButton_up = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cm_pushButton_up.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                            "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cm_pushButton_up.setAutoRepeat(True)
        self.Cm_pushButton_up.setAutoDefault(False)
        self.Cm_pushButton_up.setMinimumSize(QtCore.QSize(75, 30))
        self.Cm_pushButton_up.setMaximumSize(QtCore.QSize(75, 30))
        self.Cm_pushButton_up.setObjectName("Cm_pushButton_up")
        self.gridLayout_2.addWidget(self.Cm_pushButton_up, 3, 3, 1, 1)
        
        # Double Spin Box #
        self.Cm_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.Cm_doubleSpinBox.setMinimumSize(QtCore.QSize(100, 30))
        self.Cm_doubleSpinBox.setMaximumSize(QtCore.QSize(100, 30))
        self.Cm_doubleSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Cm_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Cm_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons) # No buttons in the spin box
        self.Cm_doubleSpinBox.setKeyboardTracking(False) # No Keyboard Tracking = Typing result will be update after pressing the enter
        self.Cm_doubleSpinBox.setObjectName("Cm_doubleSpinBox")
        self.Cm_doubleSpinBox.setMaximum(Performance_max[3]*2)
        self.Cm_doubleSpinBox.setMinimum(Performance_min[3])
        self.Cm_doubleSpinBox.setDecimals(5)
        self.Cm_doubleSpinBox.setSingleStep(0.01)
        self.gridLayout_2.addWidget(self.Cm_doubleSpinBox, 3, 4, 1, 1)
        ##------------------------------------- Moment Coefficient Section ------------------------------------##
        
        ##================================= Moment Slope  Coefficient Section =================================##
        # Push Button: Cma,0 #
        self.Cma_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cma_pushButton.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(65,165,255); background-color: rgb(0,135,255); color: rgb(255,255,255)}" + \
                                          "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(50,170,255); background-color: rgb(65,165,255); color: rgb(255,255,255)}")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        self.Cma_pushButton.setFont(font)
        self.Cma_pushButton.setAutoDefault(False)
        self.Cma_pushButton.setObjectName("Cl_pushButton")
        self.Cma_pushButton.setMinimumSize(QtCore.QSize(60, 30))
        self.Cma_pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.gridLayout_2.addWidget(self.Cma_pushButton, 4, 0, 1, 1)

        # Push Button: Down #
        self.Cma_pushButton_down = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cma_pushButton_down.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                               "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cma_pushButton_down.setAutoRepeat(True)
        self.Cma_pushButton_down.setAutoDefault(False)
        self.Cma_pushButton_down.setMinimumSize(QtCore.QSize(75, 30))
        self.Cma_pushButton_down.setMaximumSize(QtCore.QSize(75, 30))
        self.Cma_pushButton_down.setObjectName("Cma_pushButton_down")
        self.gridLayout_2.addWidget(self.Cma_pushButton_down, 4, 1, 1, 1)

        # Slider #        
        self.Slider_cma0 = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.Slider_cma0.setMinimumSize(QtCore.QSize(200, 25))
        self.Slider_cma0.setMaximumSize(QtCore.QSize(200, 25))
        self.Slider_cma0.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_cma0.setMaximum(Slider_max)
        self.Slider_cma0.setSingleStep(1)
        self.Slider_cma0.setPageStep(10)
        self.Slider_cma0.setObjectName("Slider_cma0")
        self.gridLayout_2.addWidget(self.Slider_cma0, 4, 2, 1, 1)
        
        # Push Button: Up #
        self.Cma_pushButton_up = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Cma_pushButton_up.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                             "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Cma_pushButton_up.setAutoRepeat(True)
        self.Cma_pushButton_up.setAutoDefault(False)
        self.Cma_pushButton_up.setMinimumSize(QtCore.QSize(75, 30))
        self.Cma_pushButton_up.setMaximumSize(QtCore.QSize(75, 30))
        self.Cma_pushButton_up.setObjectName("Cma_pushButton_up")
        self.gridLayout_2.addWidget(self.Cma_pushButton_up, 4, 3, 1, 1)
           
        # Double Spin Box #
        self.Cma_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.Cma_doubleSpinBox.setMinimumSize(QtCore.QSize(100, 30))
        self.Cma_doubleSpinBox.setMaximumSize(QtCore.QSize(100, 30))
        self.Cma_doubleSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Cma_doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.Cma_doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons) # No buttons in the spin box
        self.Cma_doubleSpinBox.setKeyboardTracking(False) # No Keyboard Tracking = Typing result will be update after pressing the enter
        self.Cma_doubleSpinBox.setObjectName("Cma_doubleSpinBox")
        self.Cma_doubleSpinBox.setMaximum(Performance_max[4]*2)
        self.Cma_doubleSpinBox.setMinimum(Performance_min[4])
        self.Cma_doubleSpinBox.setDecimals(5)
        self.Cma_doubleSpinBox.setSingleStep(0.01)
        self.gridLayout_2.addWidget(self.Cma_doubleSpinBox, 4, 4, 1, 1)
        
        ##--------------------------------- Moment Slope  Coefficient Section ---------------------------------##
        
        ##============================================== Plot =================================================##
        # Example code: https://stackoverflow.com/questions/12459811/how-to-embed-matplotlib-in-pyqt-for-dummies
        #               https://wikidocs.net/5252
        
#        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
#        self.gridLayout.setContentsMargins(0, 0, 0, 0)
#        self.gridLayout.setObjectName("gridLayout")
        
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setObjectName("Airfoil_Shape")

        self.plotWidget = QtWidgets.QWidget(MainWindow)
        self.plotWidget.setGeometry(QtCore.QRect(570,170,400,400))
        self.plotWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plotWidget.setObjectName("plotWidget")
        self.plotLayout = QtWidgets.QVBoxLayout(self.plotWidget)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.plotLayout.setObjectName("plotLayout")
        self.pushButton = QtWidgets.QPushButton(self.plotWidget)
        self.pushButton.setObjectName("pushButton")
        self.plotLayout.addWidget(self.canvas)
        

        ##---------------------------------------------- Plot -------------------------------------------------##
        
        ##============================================ Signiture ==============================================##      
        self.CK_sign = QtWidgets.QLabel(MainWindow)
        self.CK_sign.setGeometry(QtCore.QRect(820, 580, 151, 16))
                
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.CK_sign.setFont(font)
        self.CK_sign.setObjectName("CK_sign")

        self.retranslateUi(MainWindow)
        ##-------------------------------------------- Signiture ----------------------------------------------##
        
        ##=========================================== Initialize ==============================================##
        ## Initial Condition ##
        time_start = time.time()
        time_start_init = time.time() 
        self.ANN = DLED.N4_FCNN_Load(20)
    
        time_import_tf = time.time() - time_start
        
        message = str("Import time: {:.4f} mili sec, {:.4f} sec".format(time_import_tf*1000, time_import_tf))
        msg.debuginfo(message)
        
        time_start = time.time()
        
        
        # Initial configuration
        self.x = np.array([0.24444, 0.11067, 0.00535, -0.05005, 0.0004])
        self.pre_Cl = self.x[0]
        self.pre_Cla = self.x[1]
        self.pre_Cd = self.x[2]
        self.pre_Cm = self.x[3]
        self.pre_Cma = self.x[4]
        
        
        Performance_max[3] = self.x[3] + (-0.14/1.4)*abs(self.x[0]-0.8)+0.14
        Performance_min[3] = self.x[3] - 0.001
        
        Performance_max[4] = self.x[4]+0.0015
        Performance_min[4] = self.x[4]-0.0015
        
        self.Cl_doubleSpinBox.setValue(self.x[0])
        self.Cl2Slide(self.x[0])
        
        self.Cla_doubleSpinBox.setValue(self.x[1])
        self.Cla2Slide(self.x[1])
        
        self.Cd_doubleSpinBox.setValue(self.x[2])
        self.Cd2Slide(self.x[2])
        
        self.Cm_doubleSpinBox.setValue(self.x[3])
        self.Cm2Slide(self.x[3])
        
        self.Cma_doubleSpinBox.setValue(self.x[4])
        self.Cma2Slide(self.x[4])
        
        self.y = self.ANN.init_Run_ANN(self.x,ANN_Device)
        
        self.Max_Camber_value.setText(str("{:.5f}".format(self.y[0,0])))
        self.Max_Camber_Loc_value.setText(str("{:.5f}".format(self.y[0,1])))
        self.Max_Thickness_value.setText(str("{:.5f}".format(self.y[0,2])))
        
        up, lo = Config.NACA4(160,self.y[0,0],self.y[0,1],self.y[0,2],Resultdirect)
        self.Plot_NACA4_AF(up,lo)
        
        
        time_predict = time.time() - time_start
        
        message = str("Design time: {:.4f} mili sec, {:.4f} sec".format(time_predict*1000, time_predict))
        msg.debuginfo(message)
        
        time_start = time.time()
                
        time_Analysis = time.time() - time_start
        time_processing = time.time() - time_start_init
        
        message = str("Re_Analysis time: {:.4f} mili sec, {:.4f} sec".format(time_Analysis*1000, time_Analysis))
        msg.debuginfo(message)
        message = str("Run time: {:.4f} mili sec, {:.4f} sec".format(time_processing*1000, time_processing))
        msg.debuginfo(message)
        ##------------------------------------------- Initialize ----------------------------------------------##
       
        
        ##============================================== Signal ===============================================##        
        # XFOIL Analysis #
        self.XFOIL_Analysis_pushButton.clicked.connect(self.Run_XFOIL)
        
        # CL #
        self.Cl_pushButton.clicked.connect(self.Cl_Button)
        self.Cl_doubleSpinBox.valueChanged.connect(self.Cl2Slide) # Double spin box value --> Slider value
        self.Cl_doubleSpinBox.valueChanged.connect(self.Check_Cl) # Check the input value over the setted range
        self.Cl_doubleSpinBox.valueChanged.connect(self.Cl2AI)    # AI will be predict the shape with new input
        self.Slider_cl0.valueChanged.connect(self.Slide2Cl)       # Slider value --> Double spin box value
        self.Cl_pushButton_Down.clicked.connect(self.Cl_doubleSpinBox.stepDown) # Push down button change the value
        self.Cl_pushButton_up.clicked.connect(self.Cl_doubleSpinBox.stepUp)     # Push up button change the value
        
        # CLa #
        self.Cla_pushButton.clicked.connect(self.Cla_Button)
        self.Cla_doubleSpinBox.valueChanged.connect(self.Cla2Slide) # Double spin box value --> Slider value
        self.Cla_doubleSpinBox.valueChanged.connect(self.Check_Cla) # Check the input value over the setted range
        self.Cla_doubleSpinBox.valueChanged.connect(self.Cla2AI)    # AI will be predict the shape with new input
        self.Slider_cla0.valueChanged.connect(self.Slide2Cla)       # Slider value --> Double spin box value
        self.Cla_pushButton_down.clicked.connect(self.Cla_doubleSpinBox.stepDown) # Push down button change the value
        self.Cla_pushButton_up.clicked.connect(self.Cla_doubleSpinBox.stepUp)     # Push up button change the value
        
        # CD #
        self.Cd_pushButton.clicked.connect(self.Cd_Button)
        self.Cd_doubleSpinBox.valueChanged.connect(self.Cd2Slide) # Double spin box value --> Slider value
        self.Cd_doubleSpinBox.valueChanged.connect(self.Check_Cd) # Check the input value over the setted range
        self.Cd_doubleSpinBox.valueChanged.connect(self.Cd2AI)    # AI will be predict the shape with new input
        self.Slider_cd0.valueChanged.connect(self.Slide2Cd)       # Slider value --> Double spin box value
        self.Cd_pushButton_down.clicked.connect(self.Cd_doubleSpinBox.stepDown) # Push down button change the value
        self.Cd_pushButton_up.clicked.connect(self.Cd_doubleSpinBox.stepUp)     # Push up button change the value
        
        # CM #
        self.Cm_pushButton.clicked.connect(self.Cm_Button)
        self.Cm_doubleSpinBox.valueChanged.connect(self.Cm2Slide) # Double spin box value --> Slider value
        self.Cm_doubleSpinBox.valueChanged.connect(self.Check_Cm) # Check the input value over the setted range
        self.Cm_doubleSpinBox.valueChanged.connect(self.Cm2AI)    # AI will be predict the shape with new input
        self.Slider_cm0.valueChanged.connect(self.Slide2Cm)       # Slider value --> Double spin box value
        self.Cm_pushButton_down.clicked.connect(self.Cm_doubleSpinBox.stepDown) # Push down button change the value
        self.Cm_pushButton_up.clicked.connect(self.Cm_doubleSpinBox.stepUp)     # Push up button change the value
        
        
        # CMa #
        self.Cma_pushButton.clicked.connect(self.Cma_Button)
        self.Cma_doubleSpinBox.valueChanged.connect(self.Cma2Slide) # Double spin box value --> Slider value
        self.Cma_doubleSpinBox.valueChanged.connect(self.Check_Cma) # Check the input value over the setted range
        self.Cma_doubleSpinBox.valueChanged.connect(self.Cma2AI)    # AI will be predict the shape with new input
        self.Slider_cma0.valueChanged.connect(self.Slide2Cma)       # Slider value --> Double spin box value
        self.Cma_pushButton_down.clicked.connect(self.Cma_doubleSpinBox.stepDown) # Push down button change the value
        self.Cma_pushButton_up.clicked.connect(self.Cma_doubleSpinBox.stepUp)     # Push up button change the value      
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DLED: NACA4", "DLED: NACA4"))
        self.XFOIL_Analysis_pushButton.setText(_translate("MainWindow", "Run\nXFOIL"))
        
        self.label_Max_camber.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Max. Camber</span></p></body></html>"))
        self.label_Max_thicknees.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Max. Thickness</span></p></body></html>"))
        self.label_Max_camber_Loc.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Max. Camber Location</span></p></body></html>"))
        
        self.Max_Camber_value.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">0</span></p></body></html>"))
        self.Max_Camber_Loc_value.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">0</span></p></body></html>"))
        self.Max_Thickness_value.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">0</span></p></body></html>"))
                
        self.Cl_pushButton.setText(_translate("MainWindow", "Cl,0"))
        self.Cla_pushButton.setText(_translate("MainWindow", "Cla,0"))
        self.Cd_pushButton.setText(_translate("MainWindow", "Cd,0"))
        self.Cm_pushButton.setText(_translate("MainWindow", "Cm,0"))
        self.Cma_pushButton.setText(_translate("MainWindow", "Cma,0"))
        
        self.Cl_pushButton_Down.setText(_translate("MainWindow", "Down"))
        self.Cl_pushButton_up.setText(_translate("MainWindow", "Up"))
        self.Cla_pushButton_down.setText(_translate("MainWindow", "Down"))
        self.Cla_pushButton_up.setText(_translate("MainWindow", "Up"))
        self.Cd_pushButton_down.setText(_translate("MainWindow", "Down"))
        self.Cd_pushButton_up.setText(_translate("MainWindow", "Up"))        
        self.Cm_pushButton_down.setText(_translate("MainWindow", "Down"))
        self.Cm_pushButton_up.setText(_translate("MainWindow", "Up"))
        self.Cma_pushButton_down.setText(_translate("MainWindow", "Down"))
        self.Cma_pushButton_up.setText(_translate("MainWindow", "Up"))
        
        self.CK_sign.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-style:italic;\">Made By CK CHOI</span></p></body></html>"))

    ## Coefficient Button ##
    def Cl_Button(self):
        self.MainWindow_range = QtWidgets.QMainWindow()
        ui = Ui_Coeff_range()
        ui.setupUi(self.MainWindow_range,"Cl,0",Performance_max[0],Performance_min[0])
        self.MainWindow_range.show()
        
    def Cla_Button(self):
        self.MainWindow_range = QtWidgets.QMainWindow()
        ui = Ui_Coeff_range()
        ui.setupUi(self.MainWindow_range,"Cla,0",Performance_max[1],Performance_min[1])
        self.MainWindow_range.show()
        
    def Cd_Button(self):
        self.MainWindow_range = QtWidgets.QMainWindow()
        ui = Ui_Coeff_range()
        ui.setupUi(self.MainWindow_range,"Cd,0",Performance_max[2],Performance_min[2])
        self.MainWindow_range.show()
        
    def Cm_Button(self):
        self.MainWindow_range = QtWidgets.QMainWindow()
        ui = Ui_Coeff_range()
        ui.setupUi(self.MainWindow_range,"Cm,0",Performance_max[3],Performance_min[3])
        self.MainWindow_range.show()
        
    def Cma_Button(self):
        self.MainWindow_range = QtWidgets.QMainWindow()
        ui = Ui_Coeff_range()
        ui.setupUi(self.MainWindow_range,"Cm,0",Performance_max[4],Performance_min[4])
        self.MainWindow_range.show()
    ## Coefficient Button ##
    ##--------------------##

    ## Float Number Box to Slide ##
    def Cl2Slide(self,value):
        Slide_val = int(Slider_max*(value-Performance_min[0])/(Performance_max[0]-Performance_min[0]))
        self.Slider_cl0.setValue(Slide_val)
        
    def Cla2Slide(self,value):
        Slide_val = int(Slider_max*(value-Performance_min[1])/(Performance_max[1]-Performance_min[1]))
        self.Slider_cla0.setValue(Slide_val)

    def Cd2Slide(self,value):
        Slide_val = int(Slider_max*(value-Performance_min[2])/(Performance_max[2]-Performance_min[2]))
        self.Slider_cd0.setValue(Slide_val)
        
    def Cm2Slide(self,value):
        Slide_val = int(Slider_max*(value-Performance_min[3])/(Performance_max[3]-Performance_min[3]))
        self.Slider_cm0.setValue(Slide_val)
        
    def Cma2Slide(self,value):
        Slide_val = int(Slider_max*(value-Performance_min[4])/(Performance_max[4]-Performance_min[4]))
        self.Slider_cma0.setValue(Slide_val)
        
    ## Float Number Box to Slide ##
    ##---------------------------##
    
    ## Slide to Float Numver Box ##
    def Slide2Cl(self,value_slide):
        Floatnum = (value_slide*(Performance_max[0]-Performance_min[0])/(Slider_max))+Performance_min[0]
        Cm = ((-0.4)/1.5)*(Floatnum)
        
        if Floatnum == 0.0:
            self.Cla_doubleSpinBox.setValue(0.11250)
            self.Cm_doubleSpinBox.setValue(0.0)
            self.Cma_doubleSpinBox.setValue(0.0002)
        
        if Floatnum <= 0.8:
            Performance_max[3] = (-0.12-0.01168/0.9)*(Floatnum) + 0.01168
        else:
            Performance_max[3] = (-0.40+0.108)/(1.5195-0.9)*(Floatnum-0.9) - 0.108
        Performance_min[3] = Cm - 0.01168
        
        Cm_DSPBox = self.Cm_doubleSpinBox.value()
        if Cm_DSPBox >= Performance_max[3]:
            self.Cm_doubleSpinBox.setValue(Performance_max[3]-0.001)
        elif Cm_DSPBox <= Performance_min[3]:
            self.Cm_doubleSpinBox.setValue(Performance_min[3]+0.001)

        self.Cl_doubleSpinBox.setValue(Floatnum)
        
    def Slide2Cla(self,value_slide):
        Floatnum = (value_slide*(Performance_max[1]-Performance_min[1])/(Slider_max))+Performance_min[1]
        Cma = (-0.002-0.0036)/(0.115-0.095)*(Floatnum-0.095)+0.0036
        
        if Cma+0.002 > 0.0036:
            Performance_max[4] = 0.0036 + 0.0001
        else:
            Performance_max[4] = Cma + 0.002
            
        if Cma-0.002 > -0.0020:
            Performance_min[4] = -0.002 - 0.0001
        else:
            Performance_min[4] = Cma - 0.002
            
        self.Cma_doubleSpinBox.setValue((Performance_max[4]+Performance_min[4])/2)
       
        self.Cla_doubleSpinBox.setValue(Floatnum)

        
    def Slide2Cd(self,value_slide):
        Floatnum = (value_slide*(Performance_max[2]-Performance_min[2])/(Slider_max))+Performance_min[2]
        self.Cd_doubleSpinBox.setValue(Floatnum)
        
    def Slide2Cm(self,value_slide):
        Floatnum = (value_slide*(Performance_max[3]-Performance_min[3])/(Slider_max))+Performance_min[3]
        self.Cm_doubleSpinBox.setValue(Floatnum)
        
    def Slide2Cma(self,value_slide):
        Floatnum = (value_slide*(Performance_max[4]-Performance_min[4])/(Slider_max))+Performance_min[4]
        self.Cma_doubleSpinBox.setValue(Floatnum)  
    ## Slide to Float Numver Box ##
    ##---------------------------##
    
    ## Float Number Box to A.I ##
    def Cl2AI(self,value):
        self.x[0]=value        
        self.y = self.ANN.Run_ANN(self.x)
        
        self.Max_Camber_value.setText(str("{:.5f}".format(self.y[0,0])))
        self.Max_Camber_Loc_value.setText(str("{:.5f}".format(self.y[0,1])))
        self.Max_Thickness_value.setText(str("{:.5f}".format(self.y[0,2])))
        
        self.Check_configure(self.y[0,0], self.y[0,1], self.y[0,2])

        up, lo = Config.NACA4(160,self.y[0,0],self.y[0,1],self.y[0,2],Resultdirect)
        self.Plot_NACA4_AF(up,lo)
        
    def Cla2AI(self,value):
        self.x[1]=value        
        self.y = self.ANN.Run_ANN(self.x)
        
        self.Max_Camber_value.setText(str("{:.5f}".format(self.y[0,0])))
        self.Max_Camber_Loc_value.setText(str("{:.5f}".format(self.y[0,1])))
        self.Max_Thickness_value.setText(str("{:.5f}".format(self.y[0,2])))
        
        self.Check_configure(self.y[0,0], self.y[0,1], self.y[0,2])
        
        up, lo = Config.NACA4(160,self.y[0,0],self.y[0,1],self.y[0,2],Resultdirect)
        self.Plot_NACA4_AF(up,lo)

    def Cd2AI(self,value):
        self.x[2]=value        
        
        self.y = self.ANN.Run_ANN(self.x)
        self.Max_Camber_value.setText(str("{:.5f}".format(self.y[0,0])))
        self.Max_Camber_Loc_value.setText(str("{:.5f}".format(self.y[0,1])))
        self.Max_Thickness_value.setText(str("{:.5f}".format(self.y[0,2])))
        
        self.Check_configure(self.y[0,0], self.y[0,1], self.y[0,2])
        
        up, lo = Config.NACA4(160,self.y[0,0],self.y[0,1],self.y[0,2],Resultdirect)
        self.Plot_NACA4_AF(up,lo)
        
    def Cm2AI(self,value):
        self.x[3]=value        
        
        self.y = self.ANN.Run_ANN(self.x)
        self.Max_Camber_value.setText(str("{:.5f}".format(self.y[0,0])))
        self.Max_Camber_Loc_value.setText(str("{:.5f}".format(self.y[0,1])))
        self.Max_Thickness_value.setText(str("{:.5f}".format(self.y[0,2])))
        
        self.Check_configure(self.y[0,0], self.y[0,1], self.y[0,2])
        
        up, lo = Config.NACA4(160,self.y[0,0],self.y[0,1],self.y[0,2],Resultdirect)
        self.Plot_NACA4_AF(up,lo)
        
    def Cma2AI(self,value):
        self.x[4]=value        
        
        self.y = self.ANN.Run_ANN(self.x)
        self.Max_Camber_value.setText(str("{:.5f}".format(self.y[0,0])))
        self.Max_Camber_Loc_value.setText(str("{:.5f}".format(self.y[0,1])))
        self.Max_Thickness_value.setText(str("{:.5f}".format(self.y[0,2])))
        
        self.Check_configure(self.y[0,0], self.y[0,1], self.y[0,2])
        
        up, lo = Config.NACA4(160,self.y[0,0],self.y[0,1],self.y[0,2],Resultdirect)
        self.Plot_NACA4_AF(up,lo)
        
    def Check_configure(self,MC, MCL, MT):
        if 0 < MC < 1.5 or MC > 10:
            self.Max_Camber_value.setStyleSheet("background-color: rgb(255, 100, 100);\n"
                                                    "font: 16pt \"맑은 고딕\";color: rgb(255,255,255);")
        else:
            self.Max_Camber_value.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                    "font: 16pt \"맑은 고딕\";color: rgb(0,0,0);")
        
        
        if MCL < 2.5 or MCL > 5.5:
            self.Max_Camber_Loc_value.setStyleSheet("background-color: rgb(255, 100, 100);\n"
                                                    "font: 16pt \"맑은 고딕\";color: rgb(255,255,255);")
        else:
            self.Max_Camber_Loc_value.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                    "font: 16pt \"맑은 고딕\";color: rgb(0,0,0);")
            
        if MT > 20 or MT < 6:
            self.Max_Thickness_value.setStyleSheet("background-color: rgb(255, 100, 100);\n"
                                                    "font: 16pt \"맑은 고딕\";color: rgb(255,255,255);")
        else:
            self.Max_Thickness_value.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "font: 16pt \"맑은 고딕\";color: rgb(0,0,0);")
        
    ## Float Number Box to Slide ##
    ##---------------------------##

    ## Check the value is out of the range Without Warning to User##
    def Check_Cl_noWarning(self,value):
        if value > Performance_max[0]:
            self.Cl_doubleSpinBox.setValue(Performance_max[0])
            
        elif value < Performance_min[0]:
            self.Cl_doubleSpinBox.setValue(Performance_min[0])
            
        return value
    
    def Check_Cla_noWarning(self,value):
        if value > Performance_max[1]:
            self.Cla_doubleSpinBox.setValue(Performance_max[1])
            
        elif value < Performance_min[1]:
            self.Cla_doubleSpinBox.setValue(Performance_min[1])
            
        return value
    
    def Check_Cd_noWarning(self,value):
        if value > Performance_max[2]:
            self.Cd_doubleSpinBox.setValue(Performance_max[2])
            
        elif value < Performance_min[2]:
            self.Cd_doubleSpinBox.setValue(Performance_min[2])
            
        return value
    
    def Check_Cm_noWarning(self,value):
        if value > Performance_max[3]:
            self.Cm_doubleSpinBox.setValue(Performance_max[3])
            
        elif value < Performance_min[3]:
            self.Cm_doubleSpinBox.setValue(Performance_min[3])
            
        return value
    
    def Check_Cma_noWarning(self,value):
        if value > Performance_max[4]:
            self.Cma_doubleSpinBox.setValue(Performance_max[4])
            
        elif value < Performance_min[4]:
            self.Cma_doubleSpinBox.setValue(Performance_min[4])
                        
        return value    
    
    ## Check the value is out of the range and Warning to User##
    def Check_Cl(self,value):
        if value > Performance_max[0]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_max[0])
            self.MainWindow_warning.show()
            self.Cl_doubleSpinBox.setValue(Performance_max[0])
            
        elif value < Performance_min[0]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_min[0])
            self.MainWindow_warning.show()
            self.Cl_doubleSpinBox.setValue(Performance_min[0])
            
        return value
    
    def Check_Cla(self,value):
        if value > Performance_max[1]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_max[1])
            self.MainWindow_warning.show()
            self.Cla_doubleSpinBox.setValue(Performance_max[1])
            
        elif value < Performance_min[1]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_min[1])
            self.MainWindow_warning.show()
            self.Cla_doubleSpinBox.setValue(Performance_min[1])
            
        return value
    
    def Check_Cd(self,value):
        if value > Performance_max[2]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_max[2])
            self.MainWindow_warning.show()
            self.Cd_doubleSpinBox.setValue(Performance_max[2])
            
        elif value < Performance_min[2]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_min[2])
            self.MainWindow_warning.show()
            self.Cd_doubleSpinBox.setValue(Performance_min[2])
            
        return value
    
    def Check_Cm(self,value):
        if value > Performance_max[3]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_max[3])
            self.MainWindow_warning.show()
            self.Cm_doubleSpinBox.setValue(Performance_max[3])
            
        elif value < Performance_min[3]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_min[3])
            self.MainWindow_warning.show()
            self.Cm_doubleSpinBox.setValue(Performance_min[3])
            
        return value
    
    def Check_Cma(self,value):
        if value > Performance_max[4]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_max[4])
            self.MainWindow_warning.show()
            self.Cma_doubleSpinBox.setValue(Performance_max[4])
            
        elif value < Performance_min[4]:
            self.MainWindow_warning = QtWidgets.QMainWindow()
            ui = Ui_Warning()
            ui.setupUi(self.MainWindow_warning,Performance_min[4])
            self.MainWindow_warning.show()
            self.Cma_doubleSpinBox.setValue(Performance_min[4])
                        
        return value
        
    def Plot_NACA4_AF(self,Up_point,Lo_point):
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(Up_point[:,0],Up_point[:,1],label='Upper')
        ax.plot(Lo_point[:,0],Lo_point[:,1],label='Lower')
        
        range_plot = 1.2
        ax.set_xlim([-0.1,-0.1+range_plot])
        ax.set_ylim([0.0-range_plot/2,0.0+range_plot/2])
        ax.grid(True)
        ax.legend()
        
        self.canvas.draw()
    
    def Run_XFOIL(self):
        Config.NACA4_save(200,self.y[0,0],self.y[0,1],self.y[0,2],Resultdirect)
        
        msg.debuginfo('Coordinate file was created')
        msg.debuginfo(Resultdirect)
        
        self.Subwindow_XFOIL = QtWidgets.QMainWindow()
        self.ui_XFOIL = Ui_XFOIL_Results()
        self.ui_XFOIL.setupUi(self.Subwindow_XFOIL,self.x)
        self.Subwindow_XFOIL.show()
        
        self.Subwindow_XFOIL.show()
        
        print('XFOIL: Calculating...')
        
        var, val = Rin.Rinput(os.path.join(direct_code,'Input'),'Xfoil setting.txt',1)
        
        Iter = val[1]
        Re = val[2]
        M = val[3]
        timelim = float(val[4])
        
        os.chdir(direct_RR)
        AoA = [-1, 0, 1]
        file='Predicted NACA Aero.txt'
        direct_file=os.path.join(direct_RR,file)
        Xfoildirect=os.path.join(direct_RR,"xfoil.exe")
        # If there are same savefile, remove it before save
        if os.path.isfile(direct_file):
            os.remove(direct_file)
        name_file = 'Predicted NACA.txt'
        # Popen: Excute Subprocess
        # cwd = Current Working Directory
        p=sp.Popen(Xfoildirect,shell=False,stdin=sp.PIPE,stdout=sp.PIPE,stderr=None, encoding='utf-8')
        
        # Command to Xfoil    
        command=str("plop\n g\n \n"+\
                    "load\n" + name_file+"\n" +\
                    "oper\n" +\
                    "iter\n" + Iter + "\n" + \
                    "visc\n" + Re + "\n" + \
                    "m\n" + M + "\n" +\
                    "pacc\n" + file + "\n \n" +\
                    "a\n" + str(AoA[0]) + "\n" +\
                    "a\n" + str(AoA[1]) + "\n" +\
                    "a\n" + str(AoA[2]) + "\n" +\
                    "\n \n \n quit\n")
        try:
            com=p.communicate(command,timeout=timelim)
            p.kill()
        
        # If xfoil run over the [timelim] skip to next step
        except sp.TimeoutExpired:
            p.kill()
            # print("오래걸림") 
        # For the case that program does not killed, call p.kill() one more time
        p.kill()
        msg.debuginfo('Xfoil was closed')
        
        # Calculate Coefficients #
        Coeff = CalADC.run_Restore()
#        print(Coeff)
        if np.shape(Coeff)[0] > 0:
            self.ui_XFOIL.label_XFOIL_Cl0.setText(str("{:.5f}".format(Coeff[0,0])))
            self.ui_XFOIL.label_XFOIL_Cla0.setText(str("{:.5f}".format(Coeff[0,1])))
            self.ui_XFOIL.label_XFOIL_Cd0.setText(str("{:.5f}".format(Coeff[0,2])))
            self.ui_XFOIL.label_XFOIL_Cm0.setText(str("{:.5f}".format(Coeff[0,3])))
            self.ui_XFOIL.label_XFOIL_Cma0.setText(str("{:.5f}".format(Coeff[0,4])))
            
            Error = Coeff[0]-self.x
            self.ui_XFOIL.label_Err_Cl0.setText(str("{:.5f}".format(Error[0])))
            self.ui_XFOIL.label_Err_Cla0.setText(str("{:.5f}".format(Error[1])))
            self.ui_XFOIL.label_Err_Cd0.setText(str("{:.5f}".format(Error[2])))
            self.ui_XFOIL.label_Err_Cm0.setText(str("{:.5f}".format(Error[3])))
            self.ui_XFOIL.label_Err_Cma0.setText(str("{:.5f}".format(Error[4])))
            
            
        else:
            self.ui_XFOIL.label_XFOIL_Cl0.setText('not Converged')
            self.ui_XFOIL.label_XFOIL_Cla0.setText('not Converged')
            self.ui_XFOIL.label_XFOIL_Cd0.setText('not Converged')
            self.ui_XFOIL.label_XFOIL_Cm0.setText('not Converged')
            self.ui_XFOIL.label_XFOIL_Cma0.setText('not Converged')

            self.ui_XFOIL.label_Err_Cl0.setText('not Converged')
            self.ui_XFOIL.label_Err_Cla0.setText('not Converged')
            self.ui_XFOIL.label_Err_Cd0.setText('not Converged')
            self.ui_XFOIL.label_Err_Cm0.setText('not Converged')
            self.ui_XFOIL.label_Err_Cma0.setText('not Converged')
        
        
            
class Ui_Warning(object):
    def setupUi(self, Warning_message,limit_value):
        truncate_point = 5
        limit_value = round(limit_value*(10**truncate_point))/(10**truncate_point)
        
        Warning_message.setObjectName("Warning")
        Warning_message.resize(240, 100)
        Warning_message.setStyleSheet("background-color: rgb(70,70,70); color: rgb(255,255,255)")
        
        self.verticalFrame = QtWidgets.QFrame(Warning_message)
        self.verticalFrame.setGeometry(QtCore.QRect(10, 10, 200, 80))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 20))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Warning_message,limit_value)
        self.pushButton.clicked.connect(Warning_message.close)
        QtCore.QMetaObject.connectSlotsByName(Warning_message)

    def retranslateUi(self, Warning_message,limit_value):
        _translate = QtCore.QCoreApplication.translate
        Warning_message.setWindowTitle(_translate("Warning", "Warning"))
        self.label.setText(_translate("Warning", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Value is</span></p>\n"
"<p align=\"center\" style=\" margin-top:5px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">out of the range("+str(limit_value)+")!</span></p></body></html>"))
        self.pushButton.setText(_translate("Warning", "Ok"))
        
        
class Ui_Coeff_range(object):
    def setupUi(self,Coeff_range,Coeff_name,val_max,val_min):
        
        truncate_point = 5
        val_max = round(val_max*(10**truncate_point))/(10**truncate_point)
        val_min = round(val_min*(10**truncate_point))/(10**truncate_point)
        
        Coeff_range.setObjectName("MainWindow")
        Coeff_range.resize(312, 72)
        Coeff_range.setStyleSheet("background-color: rgb(70,70,70); color: rgb(255,255,255)")
        
        ## Cl,0 max ##
        self.max_frame = QtWidgets.QFrame(Coeff_range)
        self.max_frame.setGeometry(QtCore.QRect(10, 10, 80, 20))
        self.max_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.max_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.max_frame.setObjectName("max_frame")
        self.max_label = QtWidgets.QLabel(self.max_frame)
        self.max_label.setGeometry(QtCore.QRect(20, 1, 40, 18))
        self.max_label.setObjectName("max_label")
        self.max_textBrowser = QtWidgets.QTextBrowser(Coeff_range)
        self.max_textBrowser.setGeometry(QtCore.QRect(110, 10, 110, 20))
        self.max_textBrowser.setFrameShape(QtWidgets.QFrame.Panel)
        self.max_textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.max_textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.max_textBrowser.setObjectName("max_textBrowser")
        ## Cl,0 max ##
        ##----------##
        
        ## Cl,0 min ##
        self.min_frame = QtWidgets.QFrame(Coeff_range)
        self.min_frame.setGeometry(QtCore.QRect(10, 40, 80, 20))
        self.min_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.min_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.min_frame.setObjectName("min_frame")
        self.min_label = QtWidgets.QLabel(self.min_frame)
        self.min_label.setGeometry(QtCore.QRect(20, 1, 40, 18))
        self.min_label.setObjectName("min_label")
        self.min_textBrowser = QtWidgets.QTextBrowser(Coeff_range)
        self.min_textBrowser.setGeometry(QtCore.QRect(110, 40, 110, 20))
        self.min_textBrowser.setFrameShape(QtWidgets.QFrame.Panel)
        self.min_textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.min_textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.min_textBrowser.setObjectName("min_textBrowser")
        ## Cl,0 min ##
        ##----------##
        
        ## Ok Button ##
        self.pushButton_Ok = QtWidgets.QPushButton(Coeff_range)
        self.pushButton_Ok.setGeometry(QtCore.QRect(230, 40, 75, 20))
        self.pushButton_Ok.setObjectName("pushButton_Ok")
        ## Ok Button ##
        ##-----------##

        self.retranslateUi(Coeff_range,Coeff_name,val_max,val_min)
        self.pushButton_Ok.clicked.connect(Coeff_range.close)
        QtCore.QMetaObject.connectSlotsByName(Coeff_range)

    def retranslateUi(self, Coeff_range,Coeff_name,val_max,val_min):
        _translate = QtCore.QCoreApplication.translate
        Coeff_range.setWindowTitle(_translate(Coeff_name + ": Value Range", Coeff_name+": Value Range"))
        self.max_label.setText(_translate(Coeff_name + ": Value Range", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\"> max</span></p></body></html>"))
        self.min_label.setText(_translate(Coeff_name + ": Value Range", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\"> min</span></p></body></html>"))
        self.max_textBrowser.setHtml(_translate(Coeff_name + ": Value Range", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(val_max)+"</p></body></html>"))
        self.min_textBrowser.setHtml(_translate(Coeff_name + ": Value Range", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+str(val_min)+"</p></body></html>"))
        self.pushButton_Ok.setText(_translate(Coeff_name + ": Value Range", "OK"))

class Ui_XFOIL_Results(object):
    def setupUi(self, XFOIL_Results, Value_Required):
        XFOIL_Results.setObjectName("XFOIL_Results")
        XFOIL_Results.resize(640, 300)
        XFOIL_Results.setWindowOpacity(0.95)
        XFOIL_Results.setStyleSheet("background-color: rgb(80, 80, 80);")
        self.centralwidget = QtWidgets.QWidget(XFOIL_Results)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 30, 618, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
                
        ##================================== Requirement Performance ==================================##
        self.Requirement = QtWidgets.QVBoxLayout()
        self.Requirement.setObjectName("Requirement")
        
        self.Requirement_Description = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Requirement_Description.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                              "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.Requirement_Description.setMinimumSize(QtCore.QSize(130, 30))
        self.Requirement_Description.setMaximumSize(QtCore.QSize(200, 30))
        self.Requirement_Description.setObjectName("Requirement_Description")
        self.Requirement.addWidget(self.Requirement_Description)
        
        self.label_Req_Cl0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Req_Cl0.setMinimumSize(QtCore.QSize(130, 35))
        self.label_Req_Cl0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Req_Cl0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Req_Cl0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Req_Cl0.setObjectName("label_Req_Cl0")
        self.Requirement.addWidget(self.label_Req_Cl0)
        
        self.label_Req_Cla0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Req_Cla0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_Req_Cla0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Req_Cla0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Req_Cla0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Req_Cla0.setObjectName("label_Req_Cla0")
        self.Requirement.addWidget(self.label_Req_Cla0)
        
        self.label_Req_Cd0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Req_Cd0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_Req_Cd0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Req_Cd0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Req_Cd0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Req_Cd0.setObjectName("label_Req_Cd0")
        self.Requirement.addWidget(self.label_Req_Cd0)
        
        self.label_Req_Cm0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Req_Cm0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_Req_Cm0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Req_Cm0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Req_Cm0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Req_Cm0.setObjectName("label_Req_Cm0")
        self.Requirement.addWidget(self.label_Req_Cm0)
        
        self.label_Req_Cma0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Req_Cma0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_Req_Cma0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Req_Cma0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Req_Cma0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Req_Cma0.setObjectName("label_Req_Cma0")
        self.Requirement.addWidget(self.label_Req_Cma0)
        
        self.gridLayout.addLayout(self.Requirement, 0, 1, 1, 1)
        
        
        ##================================== XFOIL Analysis Results ===================================##
        self.XFOIL_Analysis = QtWidgets.QVBoxLayout()
        self.XFOIL_Analysis.setObjectName("XFOIL_Analysis")
        self.XFOIL_Analysis_Description = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.XFOIL_Analysis_Description.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                              "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        self.XFOIL_Analysis_Description.setMinimumSize(QtCore.QSize(130, 30))
        self.XFOIL_Analysis_Description.setMaximumSize(QtCore.QSize(200, 30))
        self.XFOIL_Analysis_Description.setObjectName("Requirement_Description_2")
        self.XFOIL_Analysis.addWidget(self.XFOIL_Analysis_Description)
        
        self.label_XFOIL_Cl0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_XFOIL_Cl0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_XFOIL_Cl0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_XFOIL_Cl0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_XFOIL_Cl0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_XFOIL_Cl0.setObjectName("label_XFOIL_Cl0")
        self.XFOIL_Analysis.addWidget(self.label_XFOIL_Cl0)
        
        self.label_XFOIL_Cla0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_XFOIL_Cla0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_XFOIL_Cla0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_XFOIL_Cla0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_XFOIL_Cla0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_XFOIL_Cla0.setObjectName("label_XFOIL_Cla0")
        self.XFOIL_Analysis.addWidget(self.label_XFOIL_Cla0)
        
        self.label_XFOIL_Cd0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_XFOIL_Cd0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_XFOIL_Cd0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_XFOIL_Cd0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_XFOIL_Cd0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_XFOIL_Cd0.setObjectName("label_XFOIL_Cd0")
        self.XFOIL_Analysis.addWidget(self.label_XFOIL_Cd0)
        
        self.label_XFOIL_Cm0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_XFOIL_Cm0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_XFOIL_Cm0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_XFOIL_Cm0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_XFOIL_Cm0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_XFOIL_Cm0.setObjectName("label_XFOIL_Cm0")
        self.XFOIL_Analysis.addWidget(self.label_XFOIL_Cm0)
        
        self.label_XFOIL_Cma0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_XFOIL_Cma0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_XFOIL_Cma0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_XFOIL_Cma0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_XFOIL_Cma0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_XFOIL_Cma0.setObjectName("label_XFOIL_Cma0")
        self.XFOIL_Analysis.addWidget(self.label_XFOIL_Cma0)
        
        self.gridLayout.addLayout(self.XFOIL_Analysis, 0, 2, 1, 1)
        
        ##=============================== Absolute Error of Performance ===============================##
        self.Error = QtWidgets.QVBoxLayout()
        self.Error.setObjectName("Error")
        self.Error_Description = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Error_Description.setStyleSheet("QPushButton {margin: 1px;border-style: outset; border-radius: 3px; border-width: 1px; padding: 1px; border-color: rgb(80,80,80); background-color: rgb(40,40,40); color: rgb(255,255,255)}" + \
                                              "QPushButton:pressed {margin: 1px; border-style: inset; border-radius: 3px; border-width: 2px; padding: 1px; border-color: rgb(150,150,150); background-color: rgb(100,100,100); color: rgb(255,255,255)}")
        
        self.Error_Description.setMinimumSize(QtCore.QSize(130, 30))
        self.Error_Description.setMaximumSize(QtCore.QSize(200, 30))
        self.Error_Description.setObjectName("Error_Description")
        self.Error.addWidget(self.Error_Description)
        
        self.label_Err_Cl0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Err_Cl0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_Err_Cl0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Err_Cl0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Err_Cl0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Err_Cl0.setObjectName("label_Err_Cl0")
        self.Error.addWidget(self.label_Err_Cl0)
        
        self.label_Err_Cla0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Err_Cla0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_Err_Cla0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Err_Cla0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Err_Cla0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Err_Cla0.setObjectName("label_Err_Cla0")
        self.Error.addWidget(self.label_Err_Cla0)
        
        self.label_Err_Cd0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Err_Cd0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_Err_Cd0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Err_Cd0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Err_Cd0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Err_Cd0.setObjectName("label_Err_Cd0")
        self.Error.addWidget(self.label_Err_Cd0)
        
        self.label_Err_Cm0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Err_Cm0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_Err_Cm0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Err_Cm0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Err_Cm0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Err_Cm0.setObjectName("label_Err_Cm0")
        self.Error.addWidget(self.label_Err_Cm0)
        
        self.label_Err_Cma0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_Err_Cma0.setMinimumSize(QtCore.QSize(130, 30))
        self.label_Err_Cma0.setMaximumSize(QtCore.QSize(200, 200))
        self.label_Err_Cma0.setStyleSheet("background-color: rgb(255, 255, 255);font: 10pt \"맑은 고딕\";")
        self.label_Err_Cma0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Err_Cma0.setObjectName("label_Err_Cma0")
        self.Error.addWidget(self.label_Err_Cma0)
        
        self.gridLayout.addLayout(self.Error, 0, 3, 1, 1)
        
        ##=============================== Absolute Error of Performance ===============================##
        self.Variables = QtWidgets.QVBoxLayout()
        self.Variables.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Variables.setObjectName("Variables")
        
        self.Lable_Variables = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Lable_Variables.setMinimumSize(QtCore.QSize(100, 35))
        self.Lable_Variables.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.Lable_Variables.setFont(font)
        self.Lable_Variables.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable_Variables.setObjectName("Lable_Variables")
        self.Variables.addWidget(self.Lable_Variables, 0, QtCore.Qt.AlignHCenter)
        
        self.Lable_Cl0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Lable_Cl0.setMinimumSize(QtCore.QSize(50, 30))
        self.Lable_Cl0.setMaximumSize(QtCore.QSize(50, 200))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.Lable_Cl0.setFont(font)
        self.Lable_Cl0.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable_Cl0.setObjectName("Lable_Cl0")
        self.Variables.addWidget(self.Lable_Cl0, 0, QtCore.Qt.AlignHCenter)
        
        self.Lable_Cla0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Lable_Cla0.setMinimumSize(QtCore.QSize(50, 30))
        self.Lable_Cla0.setMaximumSize(QtCore.QSize(50, 200))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.Lable_Cla0.setFont(font)
        self.Lable_Cla0.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable_Cla0.setObjectName("Lable_Cla0")
        self.Variables.addWidget(self.Lable_Cla0, 0, QtCore.Qt.AlignHCenter)
        
        self.Lable_Cd0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Lable_Cd0.setMinimumSize(QtCore.QSize(50, 30))
        self.Lable_Cd0.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.Lable_Cd0.setFont(font)
        self.Lable_Cd0.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable_Cd0.setObjectName("Lable_Cd0")
        self.Variables.addWidget(self.Lable_Cd0, 0, QtCore.Qt.AlignHCenter)
        
        self.Lable_Cm0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Lable_Cm0.setMinimumSize(QtCore.QSize(50, 30))
        self.Lable_Cm0.setMaximumSize(QtCore.QSize(50, 200))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.Lable_Cm0.setFont(font)
        self.Lable_Cm0.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable_Cm0.setObjectName("Lable_Cm0")
        self.Variables.addWidget(self.Lable_Cm0, 0, QtCore.Qt.AlignHCenter)
        
        self.Lable_Cma0 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Lable_Cma0.setMinimumSize(QtCore.QSize(50, 30))
        self.Lable_Cma0.setMaximumSize(QtCore.QSize(50, 200))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.Lable_Cma0.setFont(font)
        self.Lable_Cma0.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable_Cma0.setObjectName("Lable_Cma0")
        self.Variables.addWidget(self.Lable_Cma0, 0, QtCore.Qt.AlignHCenter)
        
        self.gridLayout.addLayout(self.Variables, 0, 0, 1, 1)
        
        XFOIL_Results.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(XFOIL_Results)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        XFOIL_Results.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(XFOIL_Results)
        self.statusbar.setObjectName("statusbar")
        XFOIL_Results.setStatusBar(self.statusbar)

        self.retranslateUi(XFOIL_Results,Value_Required)
        QtCore.QMetaObject.connectSlotsByName(XFOIL_Results)
        
        ##====================================== Run XFOIL ======================================##
        

    def retranslateUi(self, XFOIL_Results,Value_Required):
        _translate = QtCore.QCoreApplication.translate
        XFOIL_Results.setWindowTitle(_translate("XFOIL_Results", "XFOIL Results"))
        self.Requirement_Description.setText(_translate("XFOIL_Results", "Required"))
        self.label_Req_Cl0.setText(_translate("XFOIL_Results", str(Value_Required[0])))
        self.label_Req_Cla0.setText(_translate("XFOIL_Results", str(Value_Required[1])))
        self.label_Req_Cd0.setText(_translate("XFOIL_Results", str(Value_Required[2])))
        self.label_Req_Cm0.setText(_translate("XFOIL_Results", str(Value_Required[3])))
        self.label_Req_Cma0.setText(_translate("XFOIL_Results", str(Value_Required[4])))
        
        self.XFOIL_Analysis_Description.setText(_translate("XFOIL_Results", "XFOIL Results"))
        self.label_XFOIL_Cl0.setText(_translate("XFOIL_Results", "Calculating..."))
        self.label_XFOIL_Cla0.setText(_translate("XFOIL_Results", "Calculating..."))
        self.label_XFOIL_Cd0.setText(_translate("XFOIL_Results", "Calculating..."))
        self.label_XFOIL_Cm0.setText(_translate("XFOIL_Results", "Calculating..."))
        self.label_XFOIL_Cma0.setText(_translate("XFOIL_Results", "Calculating..."))
        
        self.Error_Description.setText(_translate("XFOIL_Results", "Error"))
        self.label_Err_Cl0.setText(_translate("XFOIL_Results", "Calculating..."))
        self.label_Err_Cla0.setText(_translate("XFOIL_Results", "Calculating..."))
        self.label_Err_Cd0.setText(_translate("XFOIL_Results", "Calculating..."))
        self.label_Err_Cm0.setText(_translate("XFOIL_Results", "Calculating..."))
        self.label_Err_Cma0.setText(_translate("XFOIL_Results", "Calculating..."))
        
        self.Lable_Variables.setText(_translate("XFOIL_Results", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">Variables</span></p></body></html>"))
        self.Lable_Cl0.setText(_translate("XFOIL_Results", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">C</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff; vertical-align:sub;\">l,0</span></p></body></html>"))
        self.Lable_Cla0.setText(_translate("XFOIL_Results", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">C</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff; vertical-align:sub;\">la,0</span></p></body></html>"))
        self.Lable_Cd0.setText(_translate("XFOIL_Results", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">C</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff; vertical-align:sub;\">d,0</span></p></body></html>"))
        self.Lable_Cm0.setText(_translate("XFOIL_Results", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">C</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff; vertical-align:sub;\">m,0</span></p></body></html>"))
        self.Lable_Cma0.setText(_translate("XFOIL_Results", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">C</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff; vertical-align:sub;\">ma,0</span></p></body></html>"))



if __name__ == "__main__":
#    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()