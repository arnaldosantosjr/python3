#O programa irá abrir e reproduzir um áudio de arquivo mp3.
# pip install playsound==1.2.2

'''import playsound
print ("door.mp3")'''

'''from playsound import playsound
playsound('door.mp3')'''

from playsound import playsound
import os

# Obtenha o caminho absoluto para o arquivo door.mp3
caminho_absoluto = os.path.abspath('door.mp3')

# Reproduzir o arquivo de áudio usando o caminho absoluto
playsound(caminho_absoluto)