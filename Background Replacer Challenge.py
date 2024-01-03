from PIL import Image

image1 = Image.open('/Users/emmanuelleyva/Desktop/Project 2/hoerberlin.jpeg')
image2 = Image.open('/Users/emmanuelleyva/Desktop/Project 2/deejay.jpg')
image3 = Image.open('/Users/emmanuelleyva/Desktop/Project 2/speaker.jpg')
newImage = Image.new(mode="RGB", size=(1920,1080))

allWhite = []
allWhite2 = []

#this function goes through every pixel in the given image and looks for pixels within a given r,g,b value threshold, 
#and stores the coordinates of those values into a given list
def getBackground(img, list, r1, r2, g1, g2, b1, b2):
    width, height = img.size
    #this for loop goes through every pixel in the given image
    for x in range(width):
        for y in range(height):
            r,g,b = img.getpixel((x,y))
            #this portion of the code finds the rgb values within the given parameters
            if  r >= r1 and r<= r2:
                if g >= g1 and g <= g2:
                    if b >= b1 and b <= b2:
                        list.append((x,y))
                  
getBackground(image2, allWhite, 150, 250, 120, 250, 140, 250)
getBackground(image3, allWhite2, 190, 255, 190, 255, 190, 255)

#this function replaces the pixels in the list made in getBackground() with pixels of a single color
def removeBackground(img, list, r, g, b):
    for item in list:
        img.putpixel((item[0], item[1]), (r,g,b))

removeBackground(image2, allWhite, 255, 87, 51)
removeBackground(image3, allWhite2, 255, 87, 51)

#this function puts a given image onto another image at given coordinates
def pasteImage(img1, img2, xP, yP):
    width, height = img2.size
    #this for loop goes through every pixel in the given image
    for x in range(width):
        for y in range(height):
            r,g,b = img2.getpixel((x,y))
            #this segment of code allows for the image to be placed at a certain coordinate
            #adding xP and yP to x and y respectively change the starting coordiate of where the pixel is placed
            img1.putpixel((x + xP, y + yP), (r,g,b))

pasteImage(newImage, image1, 0, 0)
pasteImage(newImage, image2, 600, 63)
pasteImage(newImage, image3, 1300, 90)

#this function takes two image parameters. newImg, which is a culimnation of all the images pasted onto each other, and img, the original background image
#it goes through the first image searching for a certain color (in this case, the color of the pixels replaced in removeBackground) and appends into a list
#it takes this new list, and replaces the coordinates given with the exact same coordinates from img1
#in doing so, it effectively removes the background of the image, while replacing it with the original background image. 
def combineImage(newImg,img1, rG, gG ,bG):
    wrongPixels = []
    width, height = newImg.size
    #this for loop goes through every pixel in the given image
    for x in range(width):
        for y in range(height):
            r,g,b = newImg.getpixel((x,y))
            #this function checks if the pixel that is being examined is a certain color.
            #rG, gG, bG should be the same coordinates given in removeBackground
            if  r == rG and g == gG and b == bG:
                wrongPixels.append((x,y))
    # this for loop goes through every item in the wrongPixels list, and replaces the coordinates given in the list with the pixels at the same coordinates in the other image
    for item in wrongPixels:
        r1, g1, b1 = img1.getpixel((item[0],item[1]))
        newImage.putpixel((item[0], item[1]), (r1,g1,b1))

combineImage(newImage, image1, 255, 87, 51)

newImage.show()

