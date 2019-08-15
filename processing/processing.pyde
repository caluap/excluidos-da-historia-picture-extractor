import json

excluidos = {}

def setup():
    pixelDensity(displayDensity())
    size(1280, 720)
    
    filename = "../excluidos.json"
    with open(filename, 'r') as f:
        global excluidos
        excluidos = json.load(f)
    
def printImg(imgUrl):
    print(imgUrl)
    img = loadImage(imgUrl)

    ratio = 1.0 * height / img.height
    newWidth = img.width * ratio
    deltaX = width/2 - (newWidth/2)
    
    image(img, deltaX, 0, img.width * ratio, height)
    
    
def draw():
    background(0)
    for entry in excluidos:        
        printImg(entry["photo"])
        
    noLoop()
