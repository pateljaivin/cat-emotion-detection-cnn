import os
import shutil

# Set the path to the folder containing the images
image_folder_path = "relaxed"

# Create a list of all the image filenames
image_filenames = os.listdir(image_folder_path)

# Calculate the number of images per folder
images_per_folder = len(image_filenames) // 4

# Create the four subfolders
for i in range(4):
    folder_path = os.path.join(image_folder_path, f"folder_{i+1}")
    os.makedirs(folder_path, exist_ok=True)

# Move the images into the subfolders
for i, image_filename in enumerate(image_filenames):
    folder_index = i // images_per_folder
    folder_path = os.path.join(image_folder_path, f"folder_{folder_index+1}")
    image_path = os.path.join(image_folder_path, image_filename)
    shutil.move(image_path, folder_path)
