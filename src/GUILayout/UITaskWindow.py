''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UITaskWindow(QWidget):
    """Select the task to interpret the data.

    In this window you can choose on which task the neural network
    should execute. You can choose the task by clicking the 
    corresponding button.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UITaskWindow, self).__init__(parent)
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE
        
        self.label = QLabel("Choose your Task")
        self.label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
	
        self.placeholder = QLabel()
        self.placeholder.setFixedWidth(0.02*self.WINDOW_HEIGHT)
        self.placeholder.setFixedHeight(0.05*self.WINDOW_HEIGHT)        

        self.ImageClassification = QPushButton(self)
        self.ImageClassification.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'ImageCl.png')))
        self.ImageClassification.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.ImageClassification.setToolTip('...')
        self.ImageClassification.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""")
        self.ImageClassification.setFixedHeight(0.3*self.WINDOW_HEIGHT)
        self.ImageClassification.setFixedWidth(0.3*self.WINDOW_WIDTH)
        
        self.ImageRegression = QPushButton(self)
        self.ImageRegression.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'ImageRE.png')))
        self.ImageRegression.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.ImageRegression.setToolTip('...')
        self.ImageRegression.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""")
        self.ImageRegression.setFixedHeight(0.3*self.WINDOW_HEIGHT)
        self.ImageRegression.setFixedWidth(0.3*self.WINDOW_WIDTH)
        
        self.DataClassification = QPushButton(self)
        self.DataClassification.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'DataCI.png')))
        self.DataClassification.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.DataClassification.setToolTip('...')
        self.DataClassification.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""")
        self.DataClassification.setFixedHeight(0.3*self.WINDOW_HEIGHT)
        self.DataClassification.setFixedWidth(0.3*self.WINDOW_WIDTH)
        
        self.DataRegression = QPushButton(self)
        self.DataRegression.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'DataRE.png')))
        self.DataRegression.setIconSize(QSize(0.25*self.WINDOW_WIDTH, 0.35*self.WINDOW_HEIGHT))
        self.DataRegression.setToolTip('...')
        self.DataRegression.setStyleSheet("""QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}""")
        self.DataRegression.setFixedHeight(0.3*self.WINDOW_HEIGHT)
        self.DataRegression.setFixedWidth(0.3*self.WINDOW_WIDTH)
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_train_step_3.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        
        self.back = QPushButton(self)
        self.back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.back.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.back.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addItem(QSpacerItem(0.1*self.WINDOW_WIDTH, 0.1*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.ImageClassification)
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.ImageRegression)
        self.horizontal_box[2].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addItem(QSpacerItem(0.1*self.WINDOW_WIDTH, 0.1*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.DataClassification)
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.DataRegression)
        self.horizontal_box[4].addStretch()
        
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addItem(QSpacerItem(0.15*self.WINDOW_WIDTH, 0.15*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1, Qt.AlignCenter)
        sublayout.addWidget(self.placeholder, 0, 2, Qt.AlignRight)
        self.horizontal_box[6].addLayout(sublayout)
        self.horizontal_box[6].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])

        self.setLayout(self.vertical_box)