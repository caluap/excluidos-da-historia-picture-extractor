import json

excluidos = {}

def setup():
    pixelDensity(displayDensity())
    size(1280, 720)
    
    filename = "../excluidos.json"
    with open(filename, 'r') as f:
        excluidos = json.load(f)
    
    
def draw():
    background(0)
