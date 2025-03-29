import pygame

# Base do codigo para iniciar a criação do jogo, que é a janela de abertura do jogo
print('Setup Start')
pygame.init()  # inicializar os modulos da biblioteca
window = pygame.display.set_mode(size=(600, 480))  # pixels da imagem
print('Setup End')

print('Loop Start')
while True:
    # check for all events (verificar todos os eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event QUIT is close, close the window
            print(''...)
            pygame.quit()  # close window
            quit()  # end pygame
# finalização do codigo da janela de abertura do jogo
