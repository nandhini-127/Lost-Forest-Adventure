import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adventure of the Lost Forest")

# Colors
CYAN = (0, 255, 255)
GREEN = (0, 128, 0)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.Font(None, 36)

# Game states
INTRO, FOREST, LAKE, MAGIC, KNOWLEDGE, EXIT_PATH, GAME_OVER = 1, 2, 3, 4, 5, 6, 7
current_state = INTRO
choices = []

# Text drawing function
def draw_text(text, color, y_offset=0):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text_surface, text_rect)

# Scene handlers
def handle_intro():
    screen.fill(CYAN)
    draw_text("Welcome to the Lost Forest!", BLACK, -50)
    draw_text("Press 'Y' to enter or 'N' to leave.", BLACK, 50)

def handle_forest():
    screen.fill(GREEN)
    draw_text("You step into the forest. The trees whisper in the wind.", WHITE, -50)
    draw_text("Press 'Y' to follow a glowing light or 'N' to stay and explore.", WHITE, 50)

def handle_lake():
    screen.fill(MAGENTA)
    draw_text("You arrive at a shimmering lake. A mysterious figure stands in the water.", WHITE, -50)
    draw_text("Press '1' to drink from the lake or '2' to speak with the figure.", WHITE, 50)

def handle_magic():
    screen.fill(BLUE)
    draw_text("You gain magical powers from the lake's energy.", WHITE)

def handle_knowledge():
    screen.fill(RED)
    draw_text("You gain ancient wisdom from the figure.", WHITE, 50)

def handle_exit_path():
    screen.fill(YELLOW)
    draw_text("You find a path leading out of the forest, but mysteries remain unsolved.", BLACK)

def game_over():
    screen.fill(BLACK)
    draw_text("Game Over. Thanks for playing!", WHITE, -50)
    draw_text("Press 'R' to restart or 'Q' to quit.", WHITE, 50)

def restart_game():
    global current_state, choices
    current_state = INTRO
    choices = []

# Main game loop
def game_loop():
    global current_state
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if current_state == INTRO:
                    if event.key == pygame.K_y:
                        choices.append("adventurous")
                        current_state = FOREST
                    elif event.key == pygame.K_n:
                        current_state = GAME_OVER

                elif current_state == FOREST:
                    if event.key == pygame.K_y:
                        choices.append("adventurous")
                        current_state = LAKE
                    elif event.key == pygame.K_n:
                        choices.append("cautious")
                        current_state = EXIT_PATH

                elif current_state == LAKE:
                    if event.key == pygame.K_1:
                        choices.append("adventurous")
                        current_state = MAGIC
                    elif event.key == pygame.K_2:
                        choices.append("cautious")
                        current_state = KNOWLEDGE

                elif current_state in [MAGIC, KNOWLEDGE, EXIT_PATH]:
                    current_state = GAME_OVER

                elif current_state == GAME_OVER:
                    if event.key == pygame.K_r:
                        restart_game()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

        # Draw current scene
        if current_state == INTRO:
            handle_intro()
        elif current_state == FOREST:
            handle_forest()
        elif current_state == LAKE:
            handle_lake()
        elif current_state == MAGIC:
            handle_magic()
        elif current_state == KNOWLEDGE:
            handle_knowledge()
        elif current_state == EXIT_PATH:
            handle_exit_path()
        elif current_state == GAME_OVER:
            game_over()

        # Show choices
        if choices:
            choice_summary = f"Choices made: {' -> '.join(choices)}"
            draw_text(choice_summary, WHITE, 150)

        pygame.display.flip()

game_loop()
