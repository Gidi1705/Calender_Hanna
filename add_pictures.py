import os
import random
import shutil
from PIL import Image

# Define the folder where the images are stored
IMAGE_FOLDER = "static/iCloud"  # Change this to the correct path
OUTPUT_FOLDER = "static/images"  # Folder where renamed images will be stored

# Ensure output folder exists and clear it first
if os.path.exists(OUTPUT_FOLDER):
    shutil.rmtree(OUTPUT_FOLDER)  # Remove all existing files
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Get all files in the folder
files = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]

# Filter out MOV files and count them
mov_files = [f for f in files if f.lower().endswith(".mov")]
image_files = [f for f in files if not f.lower().endswith(".mov")]

# Shuffle the image files randomly
random.shuffle(image_files)

# Process the images and rename them
for index, filename in enumerate(image_files, start=1):
    old_path = os.path.join(IMAGE_FOLDER, filename)
    new_filename = f"foto_{index:03d}.jpg"
    new_path = os.path.join(OUTPUT_FOLDER, new_filename)
    
    try:
        # Convert image to JPG format
        with Image.open(old_path) as img:
            rgb_img = img.convert("RGB")  # Ensure it's in RGB mode
            rgb_img.save(new_path, "JPEG")
        print(f"✅ Converted and saved: {filename} → {new_filename}")
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

# Report MOV files
if mov_files:
    print("\n🚨 MOV files detected! These were skipped:")
    for mov in mov_files:
        print(f"   - {mov}")
    print(f"Total MOV files: {len(mov_files)}")
else:
    print("\n✅ No MOV files found!")

print("🎉 Finished renaming and converting all images!")
