from deviation import deviation
import cv2

def load_image():
    
    # add path to source and target images
    source = cv2.imread('images/red_nature.jpg')
    target = cv2.imread('images/frog.jpg')
    
    return (source,target)
 
 
def show_images(source,target,tranformedImage):
    
    draw_image("Source", source)
    draw_image("Target", target)
    draw_image("Output", tranformedImage)
    
    cv2.imwrite("images/output.jpg",tranformedImage)
    cv2.waitKey(0) 


def draw_image(title, image):   
    
    #change the image size 
    height = 700
    resize = cv2.resize(image,(height,int((height/float(image.shape[1]))*image.shape[0])))
    cv2.imshow(title, resize)
 
 
if __name__ == '__main__':
    
    source,target=load_image()
    
    # Select required Algorithm
    tranformedImage = deviation(source, target)
    
    show_images(source,target,tranformedImage)
         