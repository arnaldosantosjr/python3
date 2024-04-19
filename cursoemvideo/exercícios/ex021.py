#O programa irá abrir e reproduzir um áudio de arquivo mp3.
# pip install playsound==1.2.2

'''import playsound
print ("door.mp3")'''

'''from playsound import playsound
playsound('door.mp3')'''

'''from playsound import playsound
import os

# Obtenha o caminho absoluto para o arquivo door.mp3
caminho_absoluto = os.path.abspath('door.mp3')

# Reproduzir o arquivo de áudio usando o caminho absoluto
playsound(caminho_absoluto)'''

'''import playsound

# Reproduzir o arquivo de áudio
playsound.playsound("door.mp3")'''

'''import playsound

playsound.playsound(r"C:\Users\Arnaldo\OneDrive\Documentos\GitHub\python3\door.mp3")'''
'''import playsound

# Reproduzir o arquivo de áudio
playsound.playsound(r"C:\Users\Arnaldo\OneDrive\Documentos\GitHub\python3\door.mp3")
'''

'''import pygame.mixer

# Inicializar o mixer Pygame
pygame.mixer.init()

# Carregar o arquivo de áudio
pygame.mixer.music.load("C:\\Users\\Arnaldo\\OneDrive\\Documentos\\GitHub\\python3\\door.mp3")

# Reproduzir o arquivo de áudio
pygame.mixer.music.play()

# Aguardar a reprodução terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)'''

'''import pygame.mixer
import os

# Inicializar o mixer Pygame
pygame.mixer.init()

# Obter o caminho absoluto do arquivo de áudio
caminho_arquivo = os.path.abspath("door.mp3")

# Carregar o arquivo de áudio
pygame.mixer.music.load(caminho_arquivo)

# Reproduzir o arquivo de áudio
pygame.mixer.music.play()

# Aguardar a reprodução terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)'''

import  pygame
pygame.init()
pygame.mixer.music.load('door.mp3')
pygame.mixer.music.play()
pygame.event.wait()