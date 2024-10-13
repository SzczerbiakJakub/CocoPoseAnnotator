
from PyQt5.QtCore import QObject, pyqtSignal

import os
import numpy as np



class DatasetInput(QObject):
    
    send_current_sample = pyqtSignal(str)
    
    
    pic_extensions = ["jpg", "png"]
    
    input_files = np.array([])
    input_annotations = np.array([])
    
    sample_index = 0
    
    
    def __init__(self):
        super().__init__()
        
        self.input_files = np.array([])
        self.input_annotations = np.array([])
        
        self.sample_index = 0
    
    
    def get_input_from_directory(self, filepath: str):
        
        self.input_files = np.array([])
        
        dir_list = np.array(os.listdir(filepath))
        for file in dir_list:
            if file.split(".")[-1] in DatasetInput.pic_extensions:
                self.add_input_filepath(file, filepath)
    
        self.sample_index = 0
        self.send_current_sample.emit(self.input_files[self.sample_index])
    
    
    def add_input_filepath(self, filepath: str, dir_filepath: str):
        self.input_files = np.append(self.input_files, f"{dir_filepath}/{filepath}")
        
        
    def set_next_sample_index(self):
        if self.sample_index < self.input_files.size - 1:
            self.sample_index += 1
            self.send_current_sample.emit(self.input_files[self.sample_index])
    
    
    def set_prev_sample_index(self):
        if self.sample_index > 0:
            self.sample_index -= 1
            self.send_current_sample.emit(self.input_files[self.sample_index])