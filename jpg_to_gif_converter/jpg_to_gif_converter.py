import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        gif_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".gif")
        im.save(gif_path, format="GIF", quality=100)

def main():
    print("Welcome to JPG to GIF Converter!")
    while True:
        jpg_folder = input("Enter the path to the folder containing JPG images: ")
        if os.path.exists(jpg_folder):
            break
        else:
            print("The folder does not exist.")
    while True:
        gif_folder = input("Enter the path to the folder where converted GIF images will be saved: ")
        if os.path.exists(gif_folder):
            break
        else:
            print("The folder does not exist.")
    # Create the GIF folder if it doesn't exist yet
    if not os.path.exists(gif_folder):
        os.makedirs(gif_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, gif_folder)
    print("All images converted successfully to GIF format and saved in the chosen folder!")

if __name__ == "__main__":
    main()

# softy_plug