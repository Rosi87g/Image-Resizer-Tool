import os
from PIL import Image

# Configuration
INPUT_FOLDER = 'input_images'
OUTPUT_FOLDER = 'output_images'
TARGET_SIZE = (800, 600)  # Width x Height
OUTPUT_FORMAT = 'JPEG'    # Options: 'JPEG', 'PNG', etc.

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Supported image extensions
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# Process each image
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(valid_extensions):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_filename = os.path.splitext(filename)[0] + '.' + OUTPUT_FORMAT.lower()
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize(TARGET_SIZE)
                resized_img.save(output_path, OUTPUT_FORMAT)
                print(f"✅ Resized and saved: {output_filename}")
        except Exception as e:
            print(f"❌ Failed to process {filename}: {e}")
