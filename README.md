# Image-Resizer-Tool

# 🖼️ Automated Image Resizer Tool

A Python-based utility that automates the task of resizing and converting images in batch. Ideal for preparing assets for web, mobile, or machine learning pipelines.

## 🚀 Features

- 📂 Batch processes all images in a folder
- 📐 Resizes images to a fixed dimension (default: 800×600)
- 🔄 Converts images to a specified format (default: JPEG)
- 🧠 Automatically creates output folder if it doesn't exist
- 🛡️ Handles common image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Library**: [Pillow](https://python-pillow.org/) (Python Imaging Library)

## 📦 Installation

1. **Clone the repository or copy the script**

``bash
git clone https://github.com/your-username/image-resizer-tool.git
cd image-resizer-tool

2. Install dependencies

bash
pip install Pillow

3. Prepare your folders
Place your images in the input_images/ folder.
The resized images will be saved in output_images/.

4. Run the script
bash
python resize_images.py
Replace resize_images.py with your actual filename if different.

5. 📁 Folder Structure
image-resizer-tool/
├── input_images/       # Original images go here
├── output_images/      # Resized images will be saved here
└── resize_images.py    # Main Python script

5.⚙️ Configuration
You can customize the following variables in the script:
TARGET_SIZE = (800, 600)       # Resize dimensions
OUTPUT_FORMAT = 'JPEG'         # Output format: 'JPEG'

6. Sample Output
✅ Resized and saved: photo1.jpeg
✅ Resized and saved: banner.jpeg
❌ Failed to process corrupted_image.png: cannot identify image file
