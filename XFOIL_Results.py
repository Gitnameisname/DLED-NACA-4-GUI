# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XFOIL_Results.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
direct_code = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(direct_code)


class Ui_XFOIL_Results(object):
    def setupUi(self, XFOIL_Results,Value_Required):
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
    
    app = QtWidgets.QApplication(sys.argv)
    XFOIL_Results = QtWidgets.QMainWindow()
    ui = Ui_XFOIL_Results()
    ui.setupUi(XFOIL_Results,[0,0,0,0,0])
    XFOIL_Results.show()
    
    app.exec_()
    
    
