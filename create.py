import os

def createPage():
    """
    createPage() creates a webpage with thumbnail links to all jpg images within a folder which is specified by the user
    """
    #Scale of thumbnail
    scale = 8
    #Ask user for folder
    path = setMediaPath()
    #Create Beginning of HTML page
    htmlPage = "<!DOCTYPE html><head><title>Jeremys Hike In Montecito</title></head><body><h1>Jeremy's Hike</h1><h2>Select a thumbnail to see a larger picture</h2>"
    #Find all jpg images
    for file in os.listdir(path):
        if file.endswith(".jpg") or file.endswith(".JPG"):
            #Retrieves the full path to the image file
            fileDir = getMediaPath(file)
            #Creates a picture from the file path
            picture = makePicture(fileDir)            
            #Create thumbnails
            writePictureTo(shrinkImage(picture,scale), path + "half_" + file)
            #Add thumbnail and link to HTML page
            htmlPage += buildLink(file)
    #Close HTML page
    htmlPage += "</body></html>"
    #Write the HTML Page    
    page = open(getMediaPath("index.html"),"wt")
    page.write(htmlPage)
    page.close() 

def shrinkImage(oldImage, scale):
    """
    shrinkImage() scales down a provided image by the specified scale.
    
    Parameters:
        oldImage(picture): The image that you sat to scale down
        scale(int): The ratio that you want to scale down. 
        
    Returns: picture scaled down
    """
    
    #Get the dimensions of the old Image
    width = getWidth(oldImage)
    height = getHeight(oldImage)
    
    #Create a new image for the scale
    canvas = makeEmptyPicture(int(width/scale), int(height/scale))
    #The Scale Loops
    oY = 0
    for nY in range(0, int(height/scale)):
        oX = 0
        for nX in range(0, int(width/scale)):
            tempColor = getColor(getPixel(oldImage, oX, oY))
            setColor(getPixel(canvas, nX, nY), tempColor)
            oX = oX + scale
        oY = oY + scale
    
    return(canvas)

def buildLink(fileName):
    """
    buildLink() builds a link to the passed image file and returns the text to be inserted into the html page
    """
    link = "<p><a href='" + fileName + "'><image src='half_" + fileName + "' style='border:0'></a></p>"
    return link

#Execute the program
createPage()