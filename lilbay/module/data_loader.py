import pandas as pd
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

class DataPreparer:
    @staticmethod
    def load_data(data_dir):
        images = []
        labels = []
        for img_file in os.listdir(data_dir):
            img = cv2.imread(os.path.join(data_dir, img_file))
            if img is not None:  
                images.append(img)
                label = 1 if 'pneumonia' in img_file else 0
                labels.append(label)
            else:
                print(f"Warning: Failed to load image {img_file}")
        return images, labels

    @staticmethod
    def resize_images(images, size=(128, 128)):
        resized_images = []
        for img in images:
            img_resized = cv2.resize(img, size)
            resized_images.append(img_resized)
        return np.array(resized_images)

    
    
