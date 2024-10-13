
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

import cv2


class PhotoWidget(QLabel):
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: red;")
        self.display_image()



    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            ...
        elif event.button() == Qt.RightButton:
            ...

        super().mouseReleaseEvent(event)
        
    

    def display_image(self, img_path=None):
        
        if img_path is not None:
        
            img = cv2.imread(img_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            height, width, _ = img_rgb.shape
            bytes_per_line = 3 * width
            q_img = QImage(img_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_img)

            self.setPixmap(pixmap)