import os
import sys
import csv

import pandas as pd
import numpy as np 

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#from PyQt5.QtMultimedia import *
#from PyQt5.QtMultimediaWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
###############################################################################
######################## B A S E  U I #########################################
from uiMainWIndow import Ui_MainWindow

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

################################### Lib###

import pickle
import gib_detect_train
###################################custom#############

model_data = pickle.load(open('gib_model.pki', 'rb'))


class MainWindow(QMainWindow, Ui_MainWindow,QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()
        self.show()

 

         
    def initUI(self):
        print("function 2 RUnning")
        
        self.gib_Text = QLineEdit(self)
        self.gib_Text.setPlaceholderText("Enter data here") 
        self.gib_Text.move(10,90)
        self.gib_Text.resize(521,51)
        
        
        
        self.pushButton.pressed.connect(self.on_click)
        
        self.show()
    
    def on_click(self):
        textBOxValue = self.gib_Text.text()
        #QMessageBox.question(self,message',"you have tyeped:",+ textBOxValue,QMessageBox.ok,QMessageBox.ok)

        #self.gib_Text.setText("")


        
        l = textBOxValue
        model_mat = model_data['mat']
        threshold = model_data['thresh']
        print(gib_detect_train.avg_transition_prob(l, model_mat) > threshold)

        
        #print(textBOxValue)
if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Calculon")

    window = MainWindow()
    
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30,30,30))
    palette.setColor(QPalette.WindowText, QColor(255,255,255))
    app.setPalette(palette)
    
    app.exec_()
