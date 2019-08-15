import json

excluidos = {}
fonts = {}
colors = {}

border = 10

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
    
    global colors
    colors = {
        "sol_de_sabado": color(247, 147, 16),
        "sol_de_segunda": color(0, 155, 217),
        "paisagem_celta": color(226, 60, 143),
        "a_solidao_das_pedras": color(162, 103, 135)
    }
    
def printImg(imgUrl):
    global border
    print(imgUrl)
    img = loadImage(imgUrl)

    ratio = 1.0 * (height - 2*border) / img.height
    newWidth = img.width * ratio
    deltaX = (width - 2*border)/2 - (newWidth/2)
    
    image(img, deltaX, border, img.width * ratio, height - 2*border)
    
def printInfo(name, life):
    global fonts
    
    fill(255, 255, 255)    
    textFont(fonts["syne"][0])
    text(name, 20, 50)
    
    textFont(fonts["syne"][1])
    text(life, 20, 95)
    
    
def draw():
    for entry in excluidos:        
        printImg(entry["photo"])
        printInfo(entry["name"], entry["life"])
        global colors, border
        
        background(colors[entry["paleta_cores"]])
        fill(0)
        
        rect(border, border, width - (border*2), height - (border*2))
        
        outputFile = "../output/" + entry["id"].rjust(5,'0') + ".jpg"
        save(outputFile)
        
        
    noLoop()
