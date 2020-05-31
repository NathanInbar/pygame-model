import pygame
pygame.font.init()

WIDTH = 800
HEIGHT = 600
bkg_color = (30,30,30)
txt_color = (225,225,225)
txt_x,txt_y = 300,300
font = pygame.font.SysFont("consolas", 30)
text = font.render("Example Text", 1, txt_color)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Example Window")

def update():
    render()

def render():
    win.fill(bkg_color)
    win.blit(text, (txt_x,txt_y))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        update()

main()
