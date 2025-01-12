import cv2
import os

# Paths to directories
images_dir = "images/train"  # Change to "images/val" for validation set
annotations_dir = "annotations/yolo_annotations/train"  # Update for validation set if needed
output_dir = "verify_output"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load a few sample images for verification
sample_images = os.listdir(images_dir)[:10]  # Adjust number as needed

for img_file in sample_images:
    img_path = os.path.join(images_dir, img_file)
    annotation_file = os.path.join(annotations_dir, f"{os.path.splitext(img_file)[0]}.txt")
    
    # Read the image
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error loading image: {img_path}")
        continue

    height, width, _ = img.shape

    # Read the corresponding annotation file
    if not os.path.exists(annotation_file):
        print(f"Annotation not found for image: {img_file}")
        continue

    with open(annotation_file, "r") as f:
        for line in f.readlines():
            class_id, x_center, y_center, bbox_width, bbox_height = map(float, line.strip().split())
            x_center, y_center = int(x_center * width), int(y_center * height)
            bbox_width, bbox_height = int(bbox_width * width), int(bbox_height * height)

            # Draw bounding box on the image
            top_left = (x_center - bbox_width // 2, y_center - bbox_height // 2)
            bottom_right = (x_center + bbox_width // 2, y_center + bbox_height // 2)
            cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(img, str(int(class_id)), top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Save the output image
    cv2.imwrite(os.path.join(output_dir, img_file), img)

print(f"Verification complete! Check the output in {output_dir}.")
