import pygame
import random 

def show_menu(screen, WIDTH,HEIGHT, font):
    title_font = pygame.font.SysFont(None,72)
    button_font = pygame.font.SysFont(None,48)

    while True:
        screen.fill((255,255,255))

        #Title
        title_text = title_font.render("Blossom Basket", True, (255,105,180))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 200))

        #Play button 
        play_text = button_font.render("Play", True, (0,0,0))
        play_rect = play_text.get_rect(center=(WIDTH // 2, 400))
        pygame.draw.rect(screen, (255,182,193), play_rect.inflate(40,20))
        screen.blit(play_text, play_rect)

        #Quit button 
        quit_text = button_font.render("Quit", True, (0,0,0))
        quit_rect = quit_text.get_rect(center = (WIDTH // 2, 500))
        pygame. draw.rect(screen, (255,182,193), quit_rect.inflate(40,20))
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    return True
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    return False
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

    #Game loop 
    running = True
    spawn_timer = 0 

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        #Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move Basket 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_rect.left > 0:
            basket_rect.x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_rect.right < WIDTH:
            basket_rect.x += basket_speed 

        #Spawn items 
        spawn_timer += 1
        if spawn_timer >=60:
            spawn_item()
            spawn_timer = 0

        #Move items / collision
        for item in items[:]:
            item.y += 4
            if item.colliderect(basket_rect):
                items.remove(item)
                score += 1
                if score >= 50:
                    return
            elif item.y > HEIGHT:
                items.remove(item)
                
        screen.blit(basket_img,basket_rect)
        for item in items:
            screen.blit(item_img, item)
        score_text = font.render(f"Score: {score}", True, (0,0,0))
        screen.blit(score_text, (10,10))

        pygame.display.flip()

    #Win 
    win_font = pygame.font.SysFont(None, 64)
    win_text = win_font.render("Amazing Picnic!", True, (0,150,0))
    screen.fill(WHITE)
    screen.blit(win_text,(WIDTH // 2 - 150, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(3000)



    pygame.quit()

    
if __name__ == "__main__":
    main()