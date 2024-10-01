import cv2
import numpy as np
import os
import shutil
from createfolderscript import getimg



# Função para calcular o erro médio quadrático (RMSE)
def calcular_rmse(imagem1, imagem2):
    erro = np.sum((imagem1.astype("float") - imagem2.astype("float")) ** 2)
    erro /= float(imagem1.shape[0] * imagem1.shape[1])
    return np.sqrt(erro)

# Carregar as imagens

def compara(imagem1,imagem2):
    if imagem1.shape == imagem2.shape:
        rmse = calcular_rmse(imagem1, imagem2)
        if rmse == 0:
            print("As imagens são iguais.")
            return True
        else:
            print(f"As imagens são diferentes. RMSE: {rmse}")
            return False
    else:
        print("As imagens têm dimensões diferentes e, portanto, são diferentes.")
        return False


imagens = getimg();
contadorfixo = 1
for i in range(1,len(imagens)+1):
    atual = i
    prox = i + 1
    
    imgatual = cv2.imread(imagens[f'{atual}.jpg'])
    imgprox = cv2.imread(imagens[f'{prox}.jpg'])
    

    if(compara(imgatual,imgprox)):
        if(os.path.exists(f'saída/{contadorfixo}')):
            shutil.copy(imagens[f'{atual}.jpg'],f'saída/{contadorfixo}/{atual}.jpg')
            shutil.copy(imagens[f'{prox}.jpg'],f'saída/{contadorfixo}/{prox}.jpg')
        else:
            os.mkdir(f'saída/{contadorfixo}')
            shutil.copy(imagens[f'{atual}.jpg'],f'saída/{contadorfixo}/{atual}.jpg')
            shutil.copy(imagens[f'{prox}.jpg'],f'saída/{contadorfixo}/{prox}.jpg')
    else:
        if(i==1):
            os.mkdir(f'saída/{contadorfixo}')
            shutil.copy(imagens[f'{atual}.jpg'],f'saída/{contadorfixo}/{atual}.jpg')
            contadorfixo+=1;
            os.mkdir(f'saída/{contadorfixo}')
            shutil.copy(imagens[f'{prox}.jpg'],f'saída/{contadorfixo}/{prox}.jpg')
        else:
            contadorfixo+=1
            os.mkdir(f'saída/{contadorfixo}')
            shutil.copy(imagens[f'{prox}.jpg'],f'saída/{contadorfixo}/{prox}.jpg')
    if(prox == (len(imagens))):break







