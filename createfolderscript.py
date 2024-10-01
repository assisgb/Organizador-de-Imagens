import os
imagens = {}
cont = 1;
true = True;

#rastreia imagens da pasta de entrada
def getimg():
    imagens = {}
    cont = 1;
    true = True;
    while (true):
        
        atual = {f'{cont}.jpg':f'entrada/{cont}.jpg'}
        if(os.path.exists(atual[f'{cont}.jpg'])):
            imagens.update(atual)
        else:
            true=False
        cont+=1 

    return imagens





















