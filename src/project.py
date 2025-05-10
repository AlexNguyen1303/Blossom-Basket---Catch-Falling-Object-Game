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
    original_img = pygame.image.load("Empty_Basket.png").convert_alpha()
    target_height = 150
    aspect_ratio = original_img.get_width() / original_img.get_height()
    new_width = int(target_height * aspect_ratio)
    basket_img = pygame.transform.scale(original_img, (new_width, target_height))
    basket_rect = basket_img.get_rect(center=(WIDTH // 2, HEIGHT - target_height // 2))
    base_basket_speed = 7
    # Falling items 
    emoji_items = [
    {"emoji": "🍓", "points": 3},
    {"emoji": "🥪", "points": 2},
    {"emoji": "🧃", "points": 1}
    ]
    items = []
    spawn_timer = 0
    #Score 
    score = 0 
    goal = 100

    #Combo System
    combo_active = False
    combo_start_time = 0
    combo_streak = 0
    pop_start_time = 0
    pop_duration = 300

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
            item = random.choice(emoji_items).copy()
            x = random.randint(0, WIDTH - 30)
            item["rect"] = pygame.Rect(x, -30, 30, 30)
            items.append(item)
            spawn_timer = 0

        #Move items / collision
        for item in items[:]:
            item["rect"].y += current_fall_speed
            if item["rect"].colliderect(basket_rect):
                items.remove(item)
                combo_streak += 1
                points = item["points"]
                if combo_active:
                    score += points * 2
                else:
                    score += points

            if combo_streak > 0 and combo_streak % 20 == 0:
                if not combo_active:
                    combo_active = True
                    combo_start_time = pygame.time.get_ticks()
                    pop_start_time = pygame.time.get_ticks()
                   
                if score >= goal:
                    return True
                
            elif item["rect"].y > HEIGHT:
                items.remove(item)
                combo_streak = 0
                combo_active = False

        #Draw everything 
        screen.blit(basket_img, basket_rect)
        for item in items:
            if combo_active:
                # glowing behind emoji
                glow = pygame.Surface((30, 30), pygame.SRCALPHA)
                glow.fill((255, 200, 220, 180))
                screen.blit(glow, item["rect"])
            emoji_font = pygame.font.SysFont(None, 40)
            emoji_text = emoji_font.render(item["emoji"], True, (0, 0, 0))
            text_rect = emoji_text.get_rect(center=item["rect"].center)
            screen.blit(emoji_text, text_rect)

        score_text = font.render(f"Score: {score}", True, (0,0,0))
        streak_text = font.render(f"Streak: {combo_streak}", True, (100,100,100))
        screen.blit(score_text, (10, 10))
        screen.blit(streak_text, (10, 50))

        if combo_active:
            combo_text = font.render(f"AMAZING COMBO !! x {combo_streak}!", True, (255,100,100))
            screen.blit(combo_text, (WIDTH // 2 - combo_text.get_width() // 2, 20))

            # Show popped effect : 
            elapsed = pygame.time.get_ticks() - pop_start_time
            scale = 1.0
            if elapsed < pop_duration:
                scale = 1.2 - 0.2 * (elapsed / pop_duration)  # Shrinks back to normal

            # Show popped text :
            pop_font = pygame.font.SysFont(None, int(36 * scale))
            pop_text = pop_font.render(f"DOUBLE POINT!x2", True, (255, 50, 150))
            screen.blit(pop_text, (WIDTH // 2 - pop_text.get_width() // 2, 110))


            #Combo countdown bar 
            remaining_time = 10000 - (pygame.time.get_ticks() - combo_start_time)
            bar_width = int((remaining_time / 10000) * 300)
            bar_height = 15
            bar_x = WIDTH // 2 - 150
            bar_y = 80
            remaining_seconds = remaining_time // 1000
            countdown_text = font.render(f"{remaining_seconds + 1}s", True, (120, 120, 120))
            screen.blit(countdown_text, (WIDTH // 2 - countdown_text.get_width() // 2, bar_y - 25))

            # Draw the bar 
            pygame.draw.rect(screen, (200, 200, 200), (bar_x, bar_y, 300, bar_height))
            # Draw remaining time on a bar 
            glow_color = (255, 105 + (pygame.time.get_ticks() // 30) % 50, 180)
            pygame.draw.rect(screen, glow_color, (bar_x, bar_y, bar_width, bar_height))


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
