from pickle import *

FILE = "config.pkl"

def data_init():
    data = {"elasticite":1,
            "couleur":0,
            "taille":5,
            "map_actuelle":1,
            "poids":5,
            "nb_boules":0}

    with open(FILE,"wb") as f:
        dump(data,f)

def update(prop, val):
    with open(FILE,"rb") as f:
        data = load(f)
        data[prop]=val
        
    with open("config.pkl","wb") as f:
        dump(data,f)

def get_data(prop):
    with open(FILE,"rb") as f:
        data = load(f)
    return data[prop]
   
def read_datas():
    with open(FILE,"rb") as f:
        data = load(f)
    print(data)

if __name__=="__main__":
    read_datas()