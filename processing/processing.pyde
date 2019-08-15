import json

excluidos = {}
fonts = {}

def setup():
    pixelDensity(displayDensity())
    size(960, 540)
    
    filename = "../excluidos.json"
    with open(filename, 'r') as f:
        global excluidos
        excluidos = json.load(f)
        
    global fonts
    fonts = {
        "jean-luc": [            
            createFont("fonts/IBMPlexSerif-Regular.ttf", 40),
            createFont("fonts/JeanLuc-Thin.otf", 40),
        ],
        "infini": [            
            createFont("fonts/infini-romain.otf", 40),
            createFont("fonts/infini-romain.otf", 40),
        ],
        "syne": [
            createFont("fonts/GangsterGrotesk-Regular.otf", 40),
            createFont("fonts/Syne-Italic.otf", 40),
        ]
    }
    
def printImg(imgUrl):
    print(imgUrl)
    img = loadImage(imgUrl)

    ratio = 1.0 * height / img.height
    newWidth = img.width * ratio
    deltaX = width/2 - (newWidth/2)
    
    image(img, deltaX, 0, img.width * ratio, height)
    
def printInfo(name, life):
    global fonts
    
    fill(255, 255, 255)    
    textFont(fonts["syne"][0])
    text(name, 20, 50)
    
    textFont(fonts["syne"][1])
    text(life, 20, 95)
    
    
def draw():
    background(0)
    for entry in excluidos:        
        printImg(entry["photo"])
        printInfo(entry["name"], entry["life"])
        
    noLoop()
