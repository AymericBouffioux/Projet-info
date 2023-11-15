from pickle import *

FILE = "config.pkl"

def data_init():
    data = {"elasticite":1,
            "couleur":"rouge",
            "taille":5,
            "poids":1}

    with open(FILE,"wb") as f:
        dump(data,f)

def update(prop, val):
    # if not(os.isfile(FILE)):
    #     data_init()
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