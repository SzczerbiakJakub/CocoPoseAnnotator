import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
from . import mainwindowviewmodel
from . import photowidget
from . import menuwidget




class MainWindow(QMainWindow):
    
    show_next_sample = pyqtSignal()
    show_prev_sample = pyqtSignal()
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coco Pose Annotator")
        self.showMaximized()
        
        self.view_model = mainwindowviewmodel.MainWindowViewModel()
        self.central_widget = None
        
        self.create_ui()
        
        
        
    def create_ui(self):
        self.create_menu_bar()
        self.central_widget = MainWindowCentralWidget(self)
        self.setCentralWidget(self.central_widget)
        

    def create_menu_bar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)


    def keyReleaseEvent(self, event):
        
        if event.key() == Qt.Key_Right:
            self.show_next_sample.emit()
            
        elif event.key() == Qt.Key_Left:
            self.show_prev_sample.emit()

        super().keyReleaseEvent(event)
        


class MainWindowCentralWidget(QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.create_ui()
        self.bind_slots_signals()
        

    def create_ui(self):
        self.menu_widget = menuwidget.MenuWidget()
        self.layout.addWidget(self.menu_widget)
        self.photo_widget = photowidget.PhotoWidget()
        self.layout.addWidget(self.photo_widget)
        

    def bind_slots_signals(self):
        self.menu_widget.view_model.files_loaded.connect(self.photo_widget.display_image)
        


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
