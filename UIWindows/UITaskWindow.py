import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UITaskWindow(QWidget):
    def __init__(self, parent=None):
        super(UITaskWindow, self).__init__(parent)
        
        self.label = QLabel("Choose your Task")
        self.label.setFont(QFont("Choose your Task", 12))
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
        self.Abstand_v = QLabel()
        self.Abstand_v.setFixedHeight(120)
        
        self.Abstand_button = QLabel()
        self.Abstand_button.setFixedWidth(10)
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar', 'GUI_step_3.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)        
        
        self.ImageClassification = QPushButton(self)
        self.ImageClassification.setIcon(QIcon(os.path.join('Images', 'ImageCl.png')))
        self.ImageClassification.setIconSize(QSize(200, 250))
        self.ImageClassification.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
        self.ImageRegression = QPushButton(self)
        self.ImageRegression.setIcon(QIcon(os.path.join('Images', 'ImageRE.png')))
        self.ImageRegression.setIconSize(QSize(200, 250))
        self.ImageRegression.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
    
        self.TextClassification = QPushButton(self)
        self.TextClassification.setIcon(QIcon(os.path.join('Images', 'TextCI.png')))
        self.TextClassification.setIconSize(QSize(200, 250))
        self.TextClassification.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
        
        self.TextRegression = QPushButton(self)
        self.TextRegression.setIcon(QIcon(os.path.join('Images', 'TextRE.png')))
        self.TextRegression.setIconSize(QSize(200, 250))
        self.TextRegression.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
        self.DataClassification = QPushButton(self)
        self.DataClassification.setIcon(QIcon(os.path.join('Images', 'DataCI.png')))
        self.DataClassification.setIconSize(QSize(200, 250))
        self.DataClassification.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
        self.DataRegression = QPushButton(self)
        self.DataRegression.setIcon(QIcon(os.path.join('Images', 'DataRE.png')))
        self.DataRegression.setIconSize(QSize(200, 250))
        self.DataRegression.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(10, 100, 200);"
                             "}") 
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.Abstand)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Abstand_button)
        self.horizontal_box[2].addWidget(self.ImageClassification)
        self.horizontal_box[2].addWidget(self.Abstand_button)
        self.horizontal_box[2].addWidget(self.ImageRegression)
        self.horizontal_box[2].addWidget(self.Abstand_button)
        self.horizontal_box[2].addWidget(self.TextClassification)
        self.horizontal_box[2].addWidget(self.Abstand_button)
        
        #self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.label)
        self.horizontal_box[3].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addWidget(self.Abstand_button)
        self.horizontal_box[4].addWidget(self.TextRegression)
        self.horizontal_box[4].addWidget(self.Abstand_button)
        self.horizontal_box[4].addWidget(self.DataClassification)
        self.horizontal_box[4].addWidget(self.Abstand_button)
        self.horizontal_box[4].addWidget(self.DataRegression)
        self.horizontal_box[4].addWidget(self.Abstand_button)
        
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addWidget(self.Abstand_v)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.Schritt, 0, 1)
        sublayout.addWidget(self.Abstand, 0, 2)
        self.horizontal_box[6].addLayout(sublayout)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])

        self.setLayout(self.vertical_box)