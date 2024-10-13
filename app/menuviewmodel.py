from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QObject, pyqtSignal


class MenuViewModel(QObject):
    
    load_files = pyqtSignal(str)
    files_loaded = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        

    def select_input_dir(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.Directory)
        
        if file_dialog.exec_():
            filepath = file_dialog.selectedFiles()
            
            if filepath:
                print(filepath)
                self.load_files.emit(filepath[0])
        