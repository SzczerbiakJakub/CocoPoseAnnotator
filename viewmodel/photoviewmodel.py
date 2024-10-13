
from PyQt5.QtCore import QObject, pyqtSignal


class PhotoViewModel(QObject):
    
    skeleton_changed = pyqtSignal()
    send_skeleton_limbs = pyqtSignal(list)
    
    def __init__(self):
        super().__init__()
        self.skeleton_points_coords = []
        
    def append_new_skeleton_point(self, x: int, y: int):
        if len(self.skeleton_points_coords) < 17:
            self.skeleton_points_coords.append((x, y))
            self.get_limbs_to_be_drawn()
            self.skeleton_changed.emit()
            
    
    
    def clear_skeleton(self):
        self.skeleton_points_coords.clear()
        
        
        
    def get_limbs_to_be_drawn(self):
        
        limbs_coords_list = []
        
        if len(self.skeleton_points_coords) > 1:
            point_1, point_2 = self.skeleton_points_coords[0], self.skeleton_points_coords[1]
            limbs_coords_list.append((point_1, point_2))
        
        if len(self.skeleton_points_coords) > 2:
            point_1, point_2 = self.skeleton_points_coords[0], self.skeleton_points_coords[2]
            limbs_coords_list.append((point_1, point_2))
        
        if len(self.skeleton_points_coords) > 3:
            point_1, point_2 = self.skeleton_points_coords[1], self.skeleton_points_coords[3]
            limbs_coords_list.append((point_1, point_2))
        
        if len(self.skeleton_points_coords) > 4:
            point_1, point_2 = self.skeleton_points_coords[2], self.skeleton_points_coords[4]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 6:
            point_1, point_2 = self.skeleton_points_coords[5], self.skeleton_points_coords[6]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 7:
            point_1, point_2 = self.skeleton_points_coords[5], self.skeleton_points_coords[7]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 8:
            point_1, point_2 = self.skeleton_points_coords[6], self.skeleton_points_coords[8]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 9:
            point_1, point_2 = self.skeleton_points_coords[7], self.skeleton_points_coords[9]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 10:
            point_1, point_2 = self.skeleton_points_coords[8], self.skeleton_points_coords[10]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 11:
            point_1, point_2 = self.skeleton_points_coords[5], self.skeleton_points_coords[11]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 12:
            point_1, point_2 = self.skeleton_points_coords[6], self.skeleton_points_coords[12]
            limbs_coords_list.append((point_1, point_2))
            point_1, point_2 = self.skeleton_points_coords[11], self.skeleton_points_coords[12]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 13:
            point_1, point_2 = self.skeleton_points_coords[11], self.skeleton_points_coords[13]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 14:
            point_1, point_2 = self.skeleton_points_coords[12], self.skeleton_points_coords[14]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 15:
            point_1, point_2 = self.skeleton_points_coords[13], self.skeleton_points_coords[15]
            limbs_coords_list.append((point_1, point_2))
            
        if len(self.skeleton_points_coords) > 16:
            point_1, point_2 = self.skeleton_points_coords[14], self.skeleton_points_coords[16]
            limbs_coords_list.append((point_1, point_2))
            
        self.send_skeleton_limbs.emit(limbs_coords_list)