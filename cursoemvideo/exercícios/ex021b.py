import  pygame
pygame.init()
pygame.mixer.music.load('C:\Users\Arnaldo\OneDrive\Documentos\GitHub\python3\doo.mp') # type: ignore
pygame.mixer.music.play()
pygame.event.wait()
'''while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)'''