
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QFileDialog
from viewmodel import menuviewmodel


class MenuWidget(QLabel):
    
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)
        
        self.setFixedSize(250, 1000)
        self.setStyleSheet("border: 2px solid black;")
        
        self.view_model = menuviewmodel.MenuViewModel()
        
        self.build_ui()
        
        
    def build_ui(self):
        dir_button = QPushButton("Select input directory...", self)
        dir_button.clicked.connect(self.view_model.select_input_dir)
        self.layout.addWidget(dir_button)