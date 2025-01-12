import os
import shutil

# Paths
images_train_dir = "images/train"
images_val_dir = "images/val"
annotations_dir = "annotations/yolo_annotations/img"
annotations_train_dir = "annotations/yolo_annotations/train"
annotations_val_dir = "annotations/yolo_annotations/val"

# Ensure train and val annotation folders exist
os.makedirs(annotations_train_dir, exist_ok=True)
os.makedirs(annotations_val_dir, exist_ok=True)

# Recursively find all annotation files
annotation_files = {}
for root, _, files in os.walk(annotations_dir):
    for file in files:
        if file.endswith(".txt"):
            base_name = os.path.splitext(file)[0]
            annotation_files[base_name] = os.path.join(root, file)

# Function to get the base name without extension
def get_base_name(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

# Move train annotations
for img_file in os.listdir(images_train_dir):
    img_base_name = get_base_name(img_file)
    if img_base_name in annotation_files:
        src = annotation_files[img_base_name]
        dst = os.path.join(annotations_train_dir, f"{img_base_name}.txt")
        shutil.copy(src, dst)
    else:
        print(f"Annotation file not found for {img_file}")

# Move val annotations
for img_file in os.listdir(images_val_dir):
    img_base_name = get_base_name(img_file)
    if img_base_name in annotation_files:
        src = annotation_files[img_base_name]
        dst = os.path.join(annotations_val_dir, f"{img_base_name}.txt")
        shutil.copy(src, dst)
    else:
        print(f"Annotation file not found for {img_file}")

print("Annotations successfully split into train and val folders!")
