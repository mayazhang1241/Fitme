import os
import random
import shutil

# Paths
images_dir = "images/img"  # Directory containing all images
train_dir = "images/train"  # Directory for training images
val_dir = "images/val"  # Directory for validation images

# Create train and val directories if they don't exist
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Get all image files from the images directory
image_files = []
for root, _, files in os.walk(images_dir):
    for file in files:
        if file.endswith(".jpg"):
            image_files.append(os.path.join(root, file))

# Shuffle the images to randomize the split
random.shuffle(image_files)

# Split the data into 80% train and 20% validation
split_idx = int(len(image_files) * 0.8)
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

# Move files to the respective folders
for file in train_files:
    shutil.move(file, os.path.join(train_dir, os.path.basename(file)))

for file in val_files:
    shutil.move(file, os.path.join(val_dir, os.path.basename(file)))

print(f"Dataset split complete! {len(train_files)} images moved to train, {len(val_files)} images moved to val.")
