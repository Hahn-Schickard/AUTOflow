from src.GUILayout.Start import *
def GUIStart(self):
        """one liner

    explain text
    many lines
    bla
    

    Args:
      self:
        explain text
      parent:
        Optional; text

    Returns:
      text

      {b'Serak': ('Rigel VII', 'Preparer'),
       b'Zim': ('Irk', 'Invader'),
       b'Lrrr': ('Omicron Persei 8', 'Emperor')}

      text

    Raises:
      IOError: An error occurred accessing the smalltable.
        """
        
        self.GUIStart1 = UIMarcusWindow1(self.FONT_STYLE, self)
        
        self.GUIStart1.load_model.clicked.connect(self.AutoMLData)
        self.GUIStart1.train_model.clicked.connect(self.StartWindow)
        
        self.setCentralWidget(self.GUIStart1)
        self.show()