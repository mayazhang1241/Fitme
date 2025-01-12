import os

# Paths to the files
bbox_file = "annotations/Anno_coarse/list_bbox.txt"
category_file = "annotations/Anno_coarse/list_category_cloth.txt"
output_dir = "annotations/yolo_annotations"
images_dir = "images"  # Directory where images will be stored

os.makedirs(output_dir, exist_ok=True)

# Step 1: Map categories to class IDs
category_mapping = {}
with open(category_file, "r") as f:
    lines = f.readlines()[2:]  # Skip the first two lines (header)
    for idx, line in enumerate(lines):
        category_name = line.strip()
        category_mapping[category_name] = idx

# Step 2: Process bounding box file
with open(bbox_file, "r") as f:
    lines = f.readlines()[2:]  # Skip the first two lines (header)
    for line in lines:
        parts = line.strip().split()
        image_name = parts[0]
        x_min, y_min, x_max, y_max = map(int, parts[1:])
        
        # Get image dimensions (use a placeholder for now; replace with actual later)
        img_width, img_height = 256, 256  # Update with actual dimensions if available
        
        # Convert to YOLO format
        x_center = ((x_min + x_max) / 2) / img_width
        y_center = ((y_min + y_max) / 2) / img_height
        width = (x_max - x_min) / img_width
        height = (y_max - y_min) / img_height

        # Assume all images are of the same category for now (e.g., T-shirt)
        # Replace with actual logic to fetch category if needed
        class_id = 0  # Replace with actual class_id using category_mapping

        # Create YOLO annotation string
        yolo_annotation = f"{class_id} {x_center} {y_center} {width} {height}\n"

        # Save to a .txt file with the same name as the image
        annotation_file = os.path.join(output_dir, f"{image_name.split('.')[0]}.txt")
        os.makedirs(os.path.dirname(annotation_file), exist_ok=True)
        with open(annotation_file, "w") as out_file:
            out_file.write(yolo_annotation)
