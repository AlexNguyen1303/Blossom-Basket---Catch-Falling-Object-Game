import pygame
import random 

def main():

    pygame.init()

    #Screen
    WIDTH, HEIGHT = 800,1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blossom Basket")
    clock = pygame.time.Clock()
    FPS = 60 
    #Colors
    WHITE = (255,255,255)
    PINK = (255,182,193)
    #Basket
    basket_img = pygame.Surface((100,50))
    basket_img.fill(PINK)
    basket_rect = basket_img.get_rect(center=(WIDTH//2, HEIGHT - 50))
    basket_speed = 7
    # Falling items 
    item_img = pygame.Surface((30,30))
    item_img.fill((200,100,150))
    items = []
    #Score 
    score = 0 
    font = pygame.font.SysFont(None,36)

    #Function to spawn items
    def spawn_item():
        x = random.randint(0,WIDTH - 30)
        y = -30
        items.append(pygame.Rect(x,y,30, 30))

   
if __name__ == "__main__":
    main()