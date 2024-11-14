###########################################
#       OrcaUpscale by Daxya-Dat404       #
# read README.md before use   vers - 0.2  #                 
###########################################

# imports
from os import listdir
from PIL import Image, ImageSequence
import datetime


def png_process(image, x, y):
    
    opened_image = Image.open(f"images/{image}")
    scaled_image = opened_image.resize((x, y), Image.NEAREST)
    scaled_image.save(f"processed/{image[:-3]}_{datetime.datetime.now().microsecond}.png")

def gif_process(image, x, y):

    frames = []    
    
    opened_gif_image = Image.open(f"images/{image}")
    
    for frame in ImageSequence.Iterator(opened_gif_image):
        frame = frame.resize((x, y), Image.NEAREST)
        frames.append(frame)
        
    frames[0].save(f"processed/{image[:-3]}_{datetime.datetime.now().microsecond}.gif", save_all=True, append_images=frames[1:], optimize=False, duration=opened_gif_image.info['duration'], loop=0)
        
    

def main():

    hello = """
        PLEASE, READ README.md !!!
        
        enter x, y (weight height)
        example: > 64 64
    """
    
    x,y = map(int, input(f"{hello}\n> ").split())
    
    images = [ image for image in listdir("images") ]
    
    for image in images:
        if image[-3:] == "png":
            png_process(image, x, y)
        elif image[-3:] == "gif":
            gif_process(image, x, y)
        else:
            print("something wrong in filetype")
            
    print("exit")
            
if __name__ == "__main__":
    main()