import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 750
BUBBLE_WIDTH = 20  # Smaller width
BUBBLE_HEIGHT = 30  # Smaller height
BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
ANGLE_SPEED = 5
LAUNCH_SPEED = 10
COLUMN_SPACING = BUBBLE_WIDTH * 2  # Adjusted spacing for smaller balloons
ROW_SPACING = BUBBLE_HEIGHT * 2    # Adjusted spacing for smaller balloons
MAX_DARTS = 10
MIN_BALLOONS_TO_WIN = 6

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Targeted Balloon Pop Shooter")

# Font for displaying text
font = pygame.font.Font(None, 36)

# Load background image and music
background_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\game images\\balloon.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale to fit screen
pygame.mixer.music.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\sounds\\background_music.mp3")  # Path to background music file
pygame.mixer.music.play(-1)  # Play music in loop


# Balloon class
class Balloon:
    def __init__(self, x, y, color, number):
        self.x = x
        self.y = y
        self.color = color
        self.width = BUBBLE_WIDTH
        self.height = BUBBLE_HEIGHT
        self.number = number
        self.active = True

    def draw(self):
        # Draw the balloon as an ellipse
        pygame.draw.ellipse(screen, self.color, (int(self.x - self.width // 2), int(self.y - self.height // 2), self.width, self.height))
        # Draw the balloon string
        pygame.draw.line(screen, (200, 200, 200), (int(self.x), int(self.y + self.height // 2)), (int(self.x), int(self.y + self.height // 2 + 20)), 2)
        # Draw the balloon number in black
        number_text = font.render(str(self.number), True, (0, 0, 0))  # Set color to black
        screen.blit(number_text, (self.x - 10, self.y - 10))

# Function to check collision between a balloon and dart
def check_collision(balloon, dart):
    distance = math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2)
    return distance < max(BUBBLE_WIDTH, BUBBLE_HEIGHT)

# Dart class
class Dart:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 90  # Initially pointing upwards
        self.speed = LAUNCH_SPEED
        self.active = False

    def draw(self):
        if self.active:
            pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

    def move(self):
        if self.active:
            # Move dart according to angle
            self.x += self.speed * math.cos(math.radians(self.angle))
            self.y -= self.speed * math.sin(math.radians(self.angle))

# Main game function
def main():
    clock = pygame.time.Clock()
    running = True
    score = 0
    darts_used = 0

    # Initialize balloons with unique numbers from 1 to 10
    balloons = []
    balloon_numbers = list(range(1, 11))
    num_cols = 5
    num_rows = 2

    # Calculate the dimensions of the grid and center it on the screen
    grid_width = (num_cols - 1) * COLUMN_SPACING
    grid_height = (num_rows - 1) * ROW_SPACING
    x_offset = (WIDTH - grid_width) // 2
    y_offset = (HEIGHT - grid_height) // 3  # Slightly higher than center

    for row in range(num_rows):
        for col in range(num_cols):
            if not balloon_numbers:
                break
            number = balloon_numbers.pop(0)
            x = x_offset + col * COLUMN_SPACING
            y = y_offset + row * ROW_SPACING
            color = random.choice(BUBBLE_COLORS)
            balloons.append(Balloon(x, y, color, number))

    # Select a random target balloon number
    target_number = random.choice([b.number for b in balloons])

    # Active dart                                       
    dart = Dart(WIDTH // 2, HEIGHT - 50)

    while running:
        screen.fill((0, 0, 0))  # Fill the screen with black
        screen.blit(background_image, (0, 0))  # Draw the background image

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dart.angle += ANGLE_SPEED  # Adjust dart angle to the left
                elif event.key == pygame.K_RIGHT:
                    dart.angle -= ANGLE_SPEED  # Adjust dart angle to the right
                elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
                    # Launch the dart only if it's not already active and darts_used is less than MAX_DARTS
                    dart = Dart(WIDTH // 2, HEIGHT - 50)
                    dart.angle = dart.angle
                    dart.active = True
                    darts_used += 1

        # Move the dart
        if dart.active:
            dart.move()

            # Check for collision with the target balloon
            for balloon in balloons:
                if balloon.active and check_collision(balloon, dart):
                    # Only destroy balloon if it matches the target number
                    if balloon.number == target_number:
                        balloon.active = False
                        score += 10
                        dart.active = False
                        balloons.remove(balloon)

                        # Choose a new target if there are balloons left
                        if balloons:
                            target_number = random.choice([b.number for b in balloons])
                        else:
                            target_number = None  # No balloons left
                    break

            # Check if dart goes out of bounds
            if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
                dart.active = False

        # Draw all balloons
        for balloon in balloons:
            if balloon.active:
                balloon.draw()

        # Draw the dart
        dart.draw()

        # Draw the aiming line
        aim_x = WIDTH // 2 + math.cos(math.radians(dart.angle)) * 50
        aim_y = HEIGHT - 50 - math.sin(math.radians(dart.angle)) * 50
        pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2, HEIGHT - 50), (aim_x, aim_y), 2)

        # Display score, darts used, and target number at bottom left
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # Set color to black
        screen.blit(score_text, (10, HEIGHT - 90))
        darts_text = font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))
        screen.blit(darts_text, (10, HEIGHT - 50))

        if target_number is not None:
            target_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0))  # Set color to black
            screen.blit(target_text, (10, HEIGHT - 130))
        else:
            # Initialize win_text and loss_text to avoid unbound errors
            win_text = font.render("", True, (0, 255, 0))
            loss_text = font.render("", True, (255, 0, 0))

            # Determine win or loss
            if score >= MIN_BALLOONS_TO_WIN * 10:
                win_text = font.render("Congratulations! You win!", True, (0, 255, 0))
                screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
            else:
                loss_text = font.render("Game over! Try again!", True, (255, 0, 0))
                screen.blit(loss_text, (WIDTH // 2 - 100, HEIGHT // 2))
            running = False

        # End game if all darts are used
        if darts_used >= MAX_DARTS and running:
            if score >= MIN_BALLOONS_TO_WIN * 10:
                win_text = font.render("Congratulations! You win!", True, (0, 255, 0))
                screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
            else:
                loss_text = font.render("Game over! Try again!", True, (255, 0, 0))
                screen.blit(loss_text, (WIDTH // 2 - 100, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)  # Display final message for 3 seconds
            running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
