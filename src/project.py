import pygame
import random 
import math
import os

def show_menu(screen, WIDTH,HEIGHT, font):
    title_font = pygame.font.SysFont("Comic Sans MS",72)
    button_font = pygame.font.SysFont(None,48)

    #basket image
    basket_image = pygame.image.load("FullBasket.png").convert_alpha()
    basket_scaled = pygame.transform.scale(basket_image, (250, 250))
    basket_rect = basket_scaled.get_rect(center=(WIDTH // 2, 380))

    while True:
        screen.fill((255,255,255))

        #Title
        title_text = title_font.render("Blossom Basket", True, (255,105,180))
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))

        # Floating basket
        offset = int(5 * math.sin(pygame.time.get_ticks() / 300))
        floaty_rect = basket_rect.copy()
        floaty_rect.centery += offset
        screen.blit(basket_scaled, floaty_rect)

        #Play button 
        play_text = button_font.render("Play", True, (0,0,0))
        play_rect = play_text.get_rect(center=(WIDTH // 2, 550))
        pygame.draw.rect(screen, (255,182,193), play_rect.inflate(40,20), border_radius=20)
        screen.blit(play_text, play_rect)

        #Quit button 
        quit_text = button_font.render("Quit", True, (0,0,0))
        quit_rect = quit_text.get_rect(center = (WIDTH // 2, 640))
        pygame.draw.rect(screen, (255,182,193), quit_rect.inflate(40,20), border_radius=20)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    return True
                elif quit_rect.collidepoint(event.pos):
                    return False
                
def show_win_screen(screen, WIDTH, HEIGHT, font, highest_streak):
    pygame.font.init()
    win_font = pygame.font.SysFont("Comic Sans MS", 64)
    button_font = pygame.font.SysFont(None, 48)
    streak_font = pygame.font.SysFont(None, 40)


    #basket image
    basket_image = pygame.image.load("FullBasket.png").convert_alpha()
    basket_scaled = pygame.transform.scale(basket_image, (250, 250))  
    basket_rect = basket_scaled.get_rect(center=(WIDTH // 2, 390)) 

    while True: 
        screen.fill((255,255,255))

        #Win Text
        win_text = win_font.render("Amazing Picnic!", True, (0,150,0))
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, 150))

        #Highest Streak
        streak_text = streak_font.render(f"Highest Streak: {highest_streak}", True, (80, 50, 120))
        screen.blit(streak_text, (WIDTH // 2 - streak_text.get_width() // 2, 530))

        #basket image
        # Floating effect
        offset = int(5 * math.sin(pygame.time.get_ticks() / 300))  
        floaty_rect = basket_rect.copy()
        floaty_rect.centery = 380 + offset  
        screen.blit(basket_scaled, floaty_rect)

        #Play Again 
        play_text = button_font.render("Play Again", True, (0,0,0))
        play_rect = play_text.get_rect(center=(WIDTH // 2, 620))
        pygame.draw.rect(screen, (200,255,200), play_rect.inflate(40, 20), border_radius=20)
        screen.blit(play_text, play_rect)

        #Quit button
        quit_text = button_font.render("Quit", True,(0,0,0))
        quit_rect = quit_text.get_rect(center=(WIDTH // 2,700))
        pygame.draw.rect(screen, (255,200,200), quit_rect.inflate(40,20), border_radius=20)
        screen.blit(quit_text, quit_rect)

        pygame. display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    return True
                elif quit_rect.collidepoint(event.pos):
                    return False
def show_game_over_screen(screen, WIDTH, HEIGHT, font):
    pygame.font.init()
    over_font = pygame.font.SysFont("Comic Sans MS", 64)
    button_font = pygame.font.SysFont(None, 48)

    # basket image
    empty_basket_image = pygame.image.load("Empty_Basket.png").convert_alpha()
    empty_basket_scaled = pygame.transform.scale(empty_basket_image, (200, 200))
    empty_basket_rect = empty_basket_scaled.get_rect(center=(WIDTH // 2, 370))

    while True:
        screen.fill((255, 255, 255))

        # Game Over Text
        over_text = over_font.render("Game Over! Bad Picnic!", True, (200, 0, 0))
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, 150))

        # Floating basket
        offset = int(5 * math.sin(pygame.time.get_ticks() / 300))
        floaty_rect = empty_basket_rect.copy()
        floaty_rect.centery += offset
        screen.blit(empty_basket_scaled, floaty_rect)

        # Replay button
        play_text = button_font.render("Play Again", True, (0, 0, 0))
        play_rect = play_text.get_rect(center=(WIDTH // 2, 550))
        pygame.draw.rect(screen, (255, 200, 200), play_rect.inflate(40, 20), border_radius=20)
        screen.blit(play_text, play_rect)

        # Quit button
        quit_text = button_font.render("Quit", True, (0, 0, 0))
        quit_rect = quit_text.get_rect(center=(WIDTH // 2, 640))
        pygame.draw.rect(screen, (200, 200, 200), quit_rect.inflate(40, 20), border_radius=20)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    return True
                elif quit_rect.collidepoint(event.pos):
                    return False
def main():

    pygame.init()
    
    # Load sounds
    pygame.mixer.music.load("background music.mp3")
    pygame.mixer.music.set_volume(0.05)  # soft background music

    collect_sound = pygame.mixer.Sound("Collectible.wav")
    collect_sound.set_volume(0.5)

    buzz_sound = pygame.mixer.Sound("buzz.flac")
    buzz_sound.set_volume(0.7)

    win_sound = pygame.mixer.Sound("Win.wav")
    win_sound.set_volume(0.8)

    lose_sound = pygame.mixer.Sound("lose.wav")
    lose_sound.set_volume(0.5)

    combo_sound = pygame.mixer.Sound("Combo.wav")
    combo_sound.set_volume(0.5)

    # Start background music
    pygame.mixer.music.play(-1)

    #Screen
    WIDTH, HEIGHT = 800,1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blossom Basket")
    clock = pygame.time.Clock()
    FPS = 60 

    background_img = pygame.image.load("NaturalBackground.png").convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    
    #Colors
    WHITE = (255,255,255)
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
    good_items = [
        {"emoji": "🍓", "points": 3, "type": "good"},
        {"emoji": "🥪", "points": 2, "type": "good"},
        {"emoji": "🧃", "points": 1, "type": "good"}
    ]

    bad_items = [
        {"emoji": "🪳", "type": "bug"},     
        {"emoji": "👢", "type": "boot"},    
        {"emoji": "🗑️", "type": "moldy"}
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
    floating_texts = []
    running = True 
    
    #Pre-Game Instruction
    instruction_start = pygame.time.get_ticks()
    instruction_duration = 5000 

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((255, 255, 255, 220)) 

    header_font = pygame.font.SysFont(None, 60)
    emoji_font_size = 48
    emoji_font = pygame.font.SysFont("Segoe UI Emoji", emoji_font_size)
    countdown_font = pygame.font.SysFont(None, 80)

    while pygame.time.get_ticks() - instruction_start < instruction_duration:
        now = pygame.time.get_ticks()
        elapsed = now - instruction_start
        remaining_seconds = max(0, 5 - elapsed // 1000)

        #Scale animation
        scale_factor = 1 + 0.05 * math.sin(now / 200)
        pulse_size = int(emoji_font_size * scale_factor)
        pulse_font = pygame.font.SysFont("Segoe UI Emoji", pulse_size)

        screen.blit(background_img, (0, 0))
        screen.blit(overlay, (0, 0))

        center_y = HEIGHT // 2

        #Countdown
        countdown_surface = countdown_font.render(str(remaining_seconds) if remaining_seconds > 0 else "Go!", True, (50, 50, 150))
        screen.blit(countdown_surface, (WIDTH // 2 - countdown_surface.get_width() // 2, center_y - 260))

        #Get Ready!
        get_ready_font = pygame.font.SysFont(None, 48)
        get_ready_text = get_ready_font.render("Get Ready!", True, (100, 60, 150))
        screen.blit(get_ready_text, (WIDTH // 2 - get_ready_text.get_width() // 2, center_y - 200))

        #Catch These!
        catch_text = header_font.render("Catch These!", True, (0, 120, 0))
        screen.blit(catch_text, (WIDTH // 2 - catch_text.get_width() // 2, center_y - 130))

        catch_emojis = pulse_font.render("🍓  🥪  🧃", True, (0, 120, 0))
        screen.blit(catch_emojis, (WIDTH // 2 - catch_emojis.get_width() // 2, center_y - 70))

        #Avoid These!
        avoid_text = header_font.render("Avoid These!", True, (180, 0, 0))
        screen.blit(avoid_text, (WIDTH // 2 - avoid_text.get_width() // 2, center_y + 20))

        avoid_emojis = pulse_font.render("🪳  👢  🗑️", True, (180, 0, 0))
        screen.blit(avoid_emojis, (WIDTH // 2 - avoid_emojis.get_width() // 2, center_y + 90))

        pygame.display.flip()
        clock.tick(FPS)

    while running:
        dt = clock.tick(FPS)
        screen.blit(background_img, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
            if random.random() < 0.85:
                item = random.choice(good_items).copy()
            else:
                item = random.choice(bad_items).copy()
            x = random.randint(0, WIDTH - 30)
            item["rect"] = pygame.Rect(x, -30, 30, 30)
            items.append(item)
            spawn_timer = 0

        #Move items / collision
        current_time = pygame.time.get_ticks()
        for item in items[:]:
            item["rect"].y += current_fall_speed
            if item["rect"].colliderect(basket_rect):
                items.remove(item)
                #good items
                if item.get("type") == "good":
                    collect_sound.play()
                    combo_streak += 1
                    points = item["points"]
                    score += points * 2 if combo_active else points

                    #floating text for good item
                    floating_texts.append({
                        "text": f"+{points * 2 if combo_active else points}",
                        "pos": item["rect"].center,
                        "color": (255, 235, 100),
                        "start": current_time
                    })

                    if score >= goal:
                        win_sound.play()
                        return {"won": True, "highest_streak": combo_streak}

                    if combo_streak % 20 == 0:
                        if not combo_active:
                            combo_active = True
                            combo_start_time = pygame.time.get_ticks()
                            pop_start_time = pygame.time.get_ticks()
                            combo_sound.play()

                #bad items
                elif item["type"] == "bug":
                    lose_sound.play()
                    return False  # Game over
                elif item["type"] == "boot":
                    score = max(0, score - 2)
                    buzz_sound.play()

                    #floating text for score loss
                    floating_texts.append({
                        "text": "-2",
                        "pos": item["rect"].center,
                        "color": (200, 0, 0),
                        "start": current_time
                    })

                elif item["type"] == "moldy":
                    combo_streak = 0
                    buzz_sound.play()
                    #floating text for streak loss
                    floating_texts.append({
                        "text": "Streak Lost",
                        "pos": item["rect"].center,
                        "color": (120, 0, 120),
                        "start": current_time
                    })
                
            elif item["rect"].y > HEIGHT:
                items.remove(item)
                if item.get("type") == "good":
                    combo_streak = 0
                    combo_active = False

        #Draw everything 
        screen.blit(basket_img, basket_rect)
        for item in items:
            if combo_active:
                # Get center position
                center = item["rect"].center

                # Create a circular glow (soft halo)
                glow_radius = 25
                glow_surface = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
                pygame.draw.circle(glow_surface, (255, 240, 100, 140), (glow_radius, glow_radius), glow_radius)
                screen.blit(glow_surface, glow_surface.get_rect(center=center))
            emoji_font = pygame.font.SysFont("Segoe UI Emoji", 40)
            emoji_text = emoji_font.render(item["emoji"], True, (0, 0, 0))
            text_rect = emoji_text.get_rect(center=item["rect"].center)
            screen.blit(emoji_text, text_rect)

        #score panel
        panel_width = 200
        panel_height = 80
        panel_surface = pygame.Surface((panel_width, panel_height), pygame.SRCALPHA)
        pygame.draw.rect(panel_surface, (255, 200, 220, 200), (0, 0, panel_width, panel_height), border_radius=15)
        screen.blit(panel_surface, (10, 10))

        # Score/Streak text
        score_text = font.render(f"Score: {score}", True, (60, 40, 80))
        streak_text = font.render(f"Streak: {combo_streak}", True, (100, 80, 120))
        screen.blit(score_text, (20, 20))
        screen.blit(streak_text, (20, 50))

        if combo_active:
            combo_text = font.render(f"AMAZING COMBO !! x {combo_streak}!", True, (80,40,120))
            screen.blit(combo_text, (WIDTH // 2 - combo_text.get_width() // 2, 20))

            # Show popped effect : 
            elapsed = pygame.time.get_ticks() - pop_start_time
            scale = 1.0
            if elapsed < pop_duration:
                scale = 1.2 - 0.2 * (elapsed / pop_duration) 

            # Show popped text :
            pop_font = pygame.font.SysFont(None, int(36 * scale))
            pop_text = pop_font.render(f"DOUBLE POINT!x2", True, (100, 50, 180))
            screen.blit(pop_text, (WIDTH // 2 - pop_text.get_width() // 2, 110))


            #Combo countdown bar 
            remaining_time = 10000 - (pygame.time.get_ticks() - combo_start_time)
            bar_width = int((remaining_time / 10000) * 300)
            bar_height = 15
            bar_x = WIDTH // 2 - 150
            bar_y = 80
            remaining_seconds = remaining_time // 1000
            countdown_text = font.render(f"{remaining_seconds + 1}s", True, (50, 80, 120))
            screen.blit(countdown_text, (WIDTH // 2 - countdown_text.get_width() // 2, bar_y - 25))

            # Draw the bar 
            pygame.draw.rect(screen, (200, 200, 200), (bar_x, bar_y, 300, bar_height))
            # Draw remaining time on a bar 
            tick = (pygame.time.get_ticks() // 5) % 255
            glow_color = (100 + tick % 100, 120 + tick % 70, 180 + tick % 50)
            pygame.draw.rect(screen, glow_color, (bar_x, bar_y, bar_width, bar_height))

        now = pygame.time.get_ticks()
        for text_data in floating_texts[:]:
            elapsed = now - text_data["start"]
            if elapsed > 800:
                floating_texts.remove(text_data)
            else:
                alpha = max(0, 255 - int(255 * (elapsed / 800)))  
                float_font = pygame.font.SysFont(None, 28)
                text_surface = float_font.render(text_data["text"], True, text_data["color"])
                text_surface.set_alpha(alpha)
                float_offset = - (elapsed // 20)  
                text_pos = (text_data["pos"][0], text_data["pos"][1] + float_offset)
                screen.blit(text_surface, text_surface.get_rect(center=text_pos))

        pygame.display.flip()

    return False
  
if __name__ == "__main__":

    pygame.init()
    pygame.font.init()

    WIDTH, HEIGHT = 800, 1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blossom Basket")
    font = pygame.font.SysFont(None, 36)

    while True:
        if not show_menu(screen, WIDTH, HEIGHT, font):
            break
        result = main()

        if result == "quit":
            break
        elif isinstance(result, dict) and result.get("won"):
            highest_streak = result.get("highest_streak", 0)
            if not show_win_screen(screen, WIDTH, HEIGHT, font, highest_streak):
                break
        else:
            if not show_game_over_screen(screen, WIDTH, HEIGHT, font):
                break
    pygame.quit()
