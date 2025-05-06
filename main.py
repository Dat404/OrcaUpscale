###########################################
#       OrcaUpscale by Daxya-Dat404       #
# read README.md before use   vers - 0.2  #                 
###########################################

# imports
from os import listdir
from PIL import Image, ImageSequence
import datetime


def png_process(image, x, y, i, o):

    opened_image = Image.open(f"{i}\\{image}")
    scaled_image = opened_image.resize((x, y), Image.NEAREST)
    scaled_image.save(f"{o}\\{image[:-4]}_{datetime.datetime.now().microsecond}.png")

def gif_process(image, x, y, i, o):

    frames = []    
    
    opened_gif_image = Image.open(f"{i}\\{image}")
    
    for frame in ImageSequence.Iterator(opened_gif_image):
        frame = frame.resize((x, y), Image.NEAREST)
        frames.append(frame)
        
    frames[0].save(f"{o}\\{image[:-4]}_{datetime.datetime.now().microsecond}.gif", save_all=True, append_images=frames[1:], optimize=False, duration=opened_gif_image.info['duration'], loop=0)
        
    

def main():

    path_to_images = "images"
    path_to_processed_images = "processed"

    hello = """
        PLEASE, READ README.md !!!
        
        enter x, y (width, height)
        example: > 64 64
    """
    while True:

        user_input = input(hello).split()

        if user_input[0] == "C":
            break

        if user_input[0] in ["I", "O"]:
            if user_input[0] == "I":
                path_to_images = user_input[1]
            else:
                path_to_processed_images = user_input[1]
        else:
            x = int(user_input[0])
            y = int(user_input[1])

    images = [ image for image in listdir(path_to_images) ]
    
    for image in images:
        if image[-3:] == "png":
            png_process(image, x, y, path_to_images, path_to_processed_images)
        elif image[-3:] == "gif":
            gif_process(image, x, y, path_to_images, path_to_processed_images)
            
    print("exit")
            
if __name__ == "__main__":
    main()