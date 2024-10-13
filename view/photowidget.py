
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, pyqtSignal

import cv2
from viewmodel import photoviewmodel


class PhotoWidget(QLabel):
    
    append_new_skeleton_point = pyqtSignal(int, int)
    clear_skeleton = pyqtSignal()
    get_limbs_to_be_drawn = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(1250, 1000)
        self.setStyleSheet("background-color: red;")
        
        self.view_model = photoviewmodel.PhotoViewModel()
        self.skeleton_limbs = []
        
        self.bind_signals_slots()
        self.display_image()



    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.append_new_skeleton_point.emit(event.x(), event.y())
            self.repaint()

        super().mouseReleaseEvent(event)
        
        
    def paintEvent(self, event):
        super().paintEvent(event)
        
        self.draw_pose()
        
        
    def bind_signals_slots(self):
        self.append_new_skeleton_point.connect(self.view_model.append_new_skeleton_point)
        self.clear_skeleton.connect(self.view_model.clear_skeleton)
        self.get_limbs_to_be_drawn.connect(self.view_model.get_limbs_to_be_drawn)
        self.view_model.skeleton_changed.connect(self.repaint)
        self.view_model.send_skeleton_limbs.connect(self.set_skeleton_limbs_coords)
        

    def set_skeleton_limbs_coords(self, points_list):
        self.skeleton_limbs = points_list
        

    def draw_pose(self):
        
        width = 6
        radius = 10
        
        painter = QPainter(self)
        
        pen = QPen(QColor("blue"), width)
        painter.setPen(pen)
        painter.setBrush(QColor("lightblue"))
        
        skeleton_points = self.view_model.skeleton_points_coords
        
        for (limb_a, limb_b) in self.skeleton_limbs:
            painter.drawLine(limb_a[0], limb_a[1], limb_b[0], limb_b[1])
        
        for point in skeleton_points:
            painter.drawEllipse(point[0], point[1], radius, radius)
            
        
        

    def display_image(self, img_path=None):
        
        if img_path is not None:
        
            self.clear_skeleton.emit()
            self.skeleton_limbs.clear()
            
            img = cv2.imread(img_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            height, width, _ = img_rgb.shape
            bytes_per_line = 3 * width
            q_img = QImage(img_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(q_img)

            self.setPixmap(pixmap)