import json

excluidos = {}

def setup():
    pixelDensity(displayDensity())
    size(1280, 720)
    
    filename = "../excluidos.json"
    with open(filename, 'r') as f:
        global excluidos
        excluidos = json.load(f)
    
    
def draw():
    background(0)
    for entry in excluidos:
        photoUrl = entry["photo"]
        print(photoUrl)
        img = loadImage(photoUrl)
    noLoop()
