import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Threads.Loading_images_thread import * 
from Threads.Create_project_thread import *
from Threads.Prune_model_thread import *



class UIMarcusWindow1(QWidget):
    def __init__(self, parent=None):
        super(UIMarcusWindow1, self).__init__(parent)
        
        self.label = QLabel("load or train a model?")
        self.label.setFont(QFont("load or train a model?", 12))
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
        self.Abstand_v = QLabel()
        self.Abstand_v.setFixedHeight(120)
        
        self.Abstand_button = QLabel()
        self.Abstand_button.setFixedWidth(10)
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar', 'GUI_step_1.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.load_model = QPushButton(self)
        self.load_model.setIcon(QIcon(os.path.join('Images', 'Loadmodel.png')))
        self.load_model.setIconSize(QSize(200, 250))
        self.load_model.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
        self.train_model = QPushButton(self)
        self.train_model.setIcon(QIcon(os.path.join('Images', 'Trainmodel.png')))
        self.train_model.setIconSize(QSize(200, 250))
        self.train_model.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}")
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())        
        self.horizontal_box[1].addWidget(self.Abstand_button)
        self.horizontal_box[1].addWidget(self.load_model)
        self.horizontal_box[1].addWidget(self.Abstand_button)
        self.horizontal_box[1].addWidget(self.train_model)
        self.horizontal_box[1].addWidget(self.Abstand_button)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Abstand_v)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Abstand, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.Schritt, 0, 1)
        sublayout.addWidget(self.Abstand, 0, 2, Qt.AlignBottom)
        self.horizontal_box[3].addLayout(sublayout)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)