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
                
def show_win_screen(screen, WIDTH, HEIGHT, font):
    win_font = pygame.font.SysFont(None, 64)
    button_font = pygame.font.SysFont(None, 48)

    while True: 
        screen.fill((255,255,255))

        #Win Text
        win_text = win_font.render("Amazing Picnic!", True, (0,150,0))
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, 200))

        #Play Again 
        play_text = button_font.render("Play Again", True, (0,0,0))
        play_rect = play_text.get_rect(center=(WIDTH // 2, 400))
        pygame.draw.rect(screen, (200,255,200), play_rect.inflate(40, 20))
        screen.blit(play_text, play_rect)

        #Quit button
        quit_text = button_font.render("Quit", True,(0,0,0))
        quit_rect = quit_text.get_rect(center=(WIDTH // 2,500))
        pygame.draw.rect(screen, (255,200,200), quit_rect.inflate(40,20))
        screen.blit(quit_text, quit_rect)

        pygame. display.flip()

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
    font = pygame.font.SysFont(None, 36)
    #Basket
    basket_img = pygame.Surface((100,50))
    basket_img.fill(PINK)
    basket_rect = basket_img.get_rect(center=(WIDTH//2, HEIGHT - 50))
    base_basket_speed = 7
    # Falling items 
    item_img = pygame.Surface((30,30))
    item_img.fill((200,100,150))
    items = []
    spawn_timer = 0
    #Score 
    score = 0 
    goal = 100

    #Combo System
    combo_active = False
    combo_start_time = 0
    combo_score = 0
    combo_streak = 0
    combo_thresholds = [20,40,60,80,100]
    next_combo_index = 0

    running = True

    while running:
        dt = clock.tick(FPS)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            
        #Combo Timer 
        if combo_active and pygame.time.get_ticks() - combo_start_time >= 10000:
            combo_active = False
            combo_score = 0

        #Adjust speeds
        current_basket_speed = base_basket_speed + 3 if combo_active else base_basket_speed
        current_fall_speed = 4 + 3 if combo_active else 4

        #Move Basket 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_rect.left > 0:
            basket_rect.x -= current_basket_speed
        if keys[pygame.K_RIGHT] and basket_rect.right < WIDTH:
            basket_rect.x += current_basket_speed

        #Spawn items 
        spawn_timer += dt
        if spawn_timer >= 1000:
            x = random.randint(0, WIDTH - 30)
            items.append(pygame.Rect(x, -30, 30, 30))
            spawn_timer = 0

        #Move items / collision
        for item in items[:]:
            item.y += current_fall_speed
            if item.colliderect(basket_rect):
                items.remove(item)
                score += 1
                combo_streak += 1

                if combo_active:
                    combo_score += 1

                if (next_combo_index < len(combo_thresholds) and
                    combo_streak == combo_thresholds[next_combo_index]):
                    combo_active = True
                    combo_start_time = pygame.time.get_ticks()
                    combo_score = 0
                    next_combo_index += 1
                   
                if score >= goal:
                    return True
                
            elif item.y > HEIGHT:
                items.remove(item)
                combo_streak = 0
                next_combo_index = 0 
                combo_active = False
                combo_score = 0

        # Glow basket during combo
        if combo_active:
            basket_img.fill((255, 105, 180))  
        else:
            basket_img.fill(PINK)


        #Draw everything 
        screen.blit(basket_img, basket_rect)
        for item in items:
            if combo_active:
                glowing_item = pygame.Surface((30, 30))
                glowing_item.fill((255, 200, 220))  # light pink glow
                glowing_item.set_alpha(200)
                screen.blit(glowing_item, item)
            else:
                screen.blit(item_img, item)

        score_text = font.render(f"Score: {score}", True, (0,0,0))
        streak_text = font.render(f"Streak: {combo_streak}", True, (100,100,100))
        screen.blit(score_text, (10, 10))
        screen.blit(streak_text, (10, 50))

        if combo_active:
            combo_text = font.render(f"Amazing Combo x {combo_score}!", True, (255,100,100))
            screen.blit(combo_text, (WIDTH // 2 - combo_text.get_width() // 2, 50))


        pygame.display.flip()

    pygame.quit()
    return False
  
if __name__ == "__main__":
    pygame.init()
    WIDTH, HEIGHT = 800, 1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blossom Basket")
    font = pygame.font.SysFont(None, 36)

    while True:
        if not show_menu(screen, WIDTH, HEIGHT, font):
            break
        if main():
            if not show_win_screen(screen, WIDTH, HEIGHT, font):
                break
        else:
            break

    pygame.quit()
