# import pandas as pd

# import os
# import cv2

# def load_data(data_dir):
#     images = []
#     labels = []
#     for img_file in os.listdir(data_dir):
#         img = cv2.imread(os.path.join(data_dir, img_file))
#         if img is not None: 
#             images.append(img)
    
#             label = 1 if 'pneumonia' in img_file else 0
#             labels.append(label)
#         else:
#             print(f"Warning: Failed to load image {img_file}")
#     return images, labels


# data_dir = '/Users/arendt/Desktop/T-DEV-810-PAR_1/lilbay/data/img'
# train_images, train_labels = load_data(data_dir) 




# # Vérifiez le contenu des images et des étiquettes
# print(f"Loaded {len(train_images)} images.")
# print(f"Loaded {len(train_labels)} labels.")
# print(f"First image shape: {train_images[0].shape if len(train_images) > 0 else 'No images loaded'}")
# print(f"First label: {train_labels[0] if len(train_labels) > 0 else 'No labels loaded'}")
