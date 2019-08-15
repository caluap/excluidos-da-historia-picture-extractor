import json

excluidos = {}
fonts = {}
colors = {}

border = 12

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
            createFont("fonts/IBMPlexSerif-Regular.ttf", 30),
            createFont("fonts/JeanLuc-Thin.otf", 34),
        ],
        "infini": [            
            createFont("fonts/infini-romain.otf", 28),
            createFont("fonts/infini-romain.otf", 28),
        ],
        "syne": [
            createFont("fonts/GangsterGrotesk-Regular.otf", 30),
            createFont("fonts/Syne-Italic.otf", 35),
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
    img = loadImage(imgUrl)
    
    img.filter(GRAY)
    tint(255, 240, 224)
    
    auxBorder = border * 5

    ratio = 1.0 * (height - 2 * auxBorder) / img.height
    newWidth = img.width * ratio
    deltaX = (width - 2 * border)/2 - (newWidth / 2)
    
    image(img, deltaX, auxBorder, img.width * ratio, height - 2*auxBorder)
    
def printInfo(name, life, layout):
    global fonts
    
    fill(255, 255, 255)    
    textFont(fonts[layout][0])
    text(name, 20, 40)
    
    textFont(fonts[layout][1])
    text(life, 20, 75)
    
def printCityState(city, state):
    global fonts
    s = city + ", " + state
    textFont(fonts["syne"][0])
    textSize(20)
    text(s, 20, height - 20)
    
    
def draw():
    i = 0
    for entry in excluidos[i:]:
        global colors, border
        
        background(colors[entry["paleta_cores"]])
        fill(0)
        
        rect(border, border, width - (border*2), height - (border*2))
                            
        imgUrl = "https://prova.olimpiadadehistoria.com.br/attachments/onhb11/transfer/img/" + entry["imagem_capa"]
        printImg(imgUrl)
        
        date = entry["nascimento"] + u"—"
        if entry["viva"] == "morta":
            date += entry["morte"]
        
        printInfo(entry["nome_personalidade"], date, entry["layout"])
        
        printCityState(entry["cidade_personalidade"], entry["estado_personalidade"])
        
        outputFile = "../output/" + entry["id"].rjust(5,'0') + ".jpg"
        print('(' + str(i) + ') will now save: ' + outputFile)
        save(outputFile)
        
        i += 1
        
        
    exit()
