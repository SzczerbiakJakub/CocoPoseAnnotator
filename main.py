from view.gui import MainWindow
from model.dataset import DatasetInput
import sys

from PyQt5.QtWidgets import QApplication


def main():
    
    dataset = DatasetInput()
    
    app = QApplication(sys.argv)

    window = MainWindow()
    
    #   CONNECT NEXT SAMPLE DISPLAY
    window.show_next_sample.connect(dataset.set_next_sample_index)
    
    #   CONNECT PREV SAMPLE DISPLAY
    window.show_prev_sample.connect(dataset.set_prev_sample_index)
    
    #   CONNECT LOAD INPUTS
    window.central_widget.menu_widget.view_model.load_files.connect(dataset.get_input_from_directory)
    
    #   CONNECT CURRENT SAMPLE DISPLAY
    dataset.send_current_sample.connect(window.central_widget.photo_widget.display_image)
    
    window.show()
    sys.exit(app.exec_())
    
    
    
    
if __name__ == "__main__":
    main()