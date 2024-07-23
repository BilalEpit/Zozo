import matplotlib.pyplot as plt
from data_loader import DataPreparer
import cv2

class CheckData:    
    @staticmethod
    def visualize_images(images, labels, num_images=5):
        plt.figure(figsize=(10, 10))
        for i in range(min(num_images, len(images))):
            plt.subplot(1, num_images, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  
            plt.xlabel('Pneumonia' if labels[i] == 1 else 'Normal')
        plt.show()


data_dir = '/Users/arendt/Desktop/T-DEV-810-PAR_1/lilbay/data/NORMAL'
train_images, train_labels = DataPreparer.load_data(data_dir)


CheckData.visualize_images(train_images, train_labels)

# 3. Resize the images
resized_images = DataPreparer.resize_images(train_images)
print(f"Resized images shape: {resized_images.shape}")

