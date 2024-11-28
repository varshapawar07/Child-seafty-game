from ursina import *
import pygame
import random
import math

# Initialize Pygame for the second part
pygame.init()

# Global variable to transition between games
start_balloon_game = False

def start_safety_game():
    app = Ursina()

    class SafetyGame:
        def __init__(self):
            window.title = "Child Safety Game"
            window.color = color.black

            # Initial screen setup
            self.background = Entity(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/startPage4.png",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            self.start_button = Button(
                text="Start Game",
                color=color.azure,
                scale=(0.4, 0.15),
                position=(0, 0),
                text_color=color.white,
                on_click=self.show_character_selection
            )

        def show_character_selection(self):
            self.start_button.disable()
            self.background.disable()

            self.character_selection_bg = Entity(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/startPage4.png",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            self.character_text = Text(
                "Choose Your Character",
                position=(-0.3, 0.4),
                scale=2.5,
                color=color.black
            )

            self.boy_button = Button(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/characters/boy/boy2.png",
                scale=(0.3, 0.6),
                position=(-0.4, -0.2),
                color=color.white,
                on_click=self.show_dressing_screen
            )

            self.girl_button = Button(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/characters/girl/girl1.png",
                scale=(0.3, 0.6),
                position=(0.4, -0.2),
                color=color.white,
                on_click=self.show_dressing_screen
            )

        def show_dressing_screen(self):
            self.character_selection_bg.disable()
            self.character_text.disable()
            self.boy_button.disable()
            self.girl_button.disable()

            self.dressing_bg = Entity(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/back2.png",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            self.start_game_button = Button(
                text="Start Game",
                color=color.orange,
                scale=(0.25, 0.1),
                position=(0, -0.4),
                text_color=color.white,
                on_click=self.show_scenario_selection
            )

        def show_scenario_selection(self):
            self.dressing_bg.disable()
            self.start_game_button.disable()

            self.scenario_bg = Entity(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/back1.jpg",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            self.playground_button = Button(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/playG3.jpg",
                scale=(0.4, 0.3),
                position=(-0.3, -0.0),
                color=color.white,
                on_click=self.show_navigation_screen
            )
            self.playground_label = Text(
                "Playground",
                position=(-0.4, -0.2),
                scale=1.5,
                color=color.black
            )

            self.school_button = Button(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/School1.jpg",
                scale=(0.4, 0.3),
                position=(0.4, -0.0),
                color=color.white
            )
            self.school_label = Text(
                "School (Locked)",
                position=(0.3, -0.2),
                scale=1.5,
                color=color.black
            )

        def show_navigation_screen(self):
            # Disable previous screen elements
            self.scenario_bg.disable()
            self.playground_button.disable()
            self.playground_label.disable()
            self.school_button.disable()
            self.school_label.disable()

            # Navigation screen setup
            self.navigation_bg = Entity(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/navi.png",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            # Girl character setup
            self.girl = Entity(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/characters/girl/girl1.png",  # Make sure to use the correct path to the texture
                scale=(0.2, 0.4),
                position=(-0.7, -0.2)  # Initial position of the girl
            )

            # Play Game Button
            self.play_game_button = Button(
                text="Play Game",
                color=color.orange,
                scale=(0.2, 0.1),
                position=(0.3, -0.2),
                text_color=color.white,
                on_click=self.start_balloon_game
            )

            # Navigation speed (how fast the girl moves)
            self.speed = 0.03

            # Update function for handling movement
            def update():
                # Handle forward and backward movement with 'A' and 'D' keys
                if held_keys['d']:  # Move forward (right)
                    self.girl.x += self.speed
                if held_keys['a']:  # Move backward (left)
                    self.girl.x -= self.speed

                # Optional: Keep the girl within the screen boundaries (left and right limits)
                if self.girl.x > 1.0:  # Right boundary
                    self.girl.x = 1.0
                elif self.girl.x < -1.0:  # Left boundary
                    self.girl.x = -1.0

            # Update the game with the movement logic
            app.update = update

        def start_balloon_game(self):
            # Disable previous screen elements
            self.navigation_bg.disable()
            self.girl.disable()
            self.play_game_button.disable()

            # Transition to Balloon Popping Game
            balloon_popping_game()

    game = SafetyGame()
    app.run()

def balloon_popping_game():
    # Game Variables
    WIDTH, HEIGHT = 800, 600
    BUBBLE_WIDTH = 20
    BUBBLE_HEIGHT = 30
    BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
    ANGLE_SPEED = 5
    LAUNCH_SPEED = 10
    MAX_DARTS = 10
    MIN_BALLOONS_TO_WIN = 6

    # Initialize pygame window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Targeted Balloon Pop Shooter")
    font = pygame.font.Font(None, 36)

    # Load assets
    background_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\game images\\balloon.jpg")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    pygame.mixer.music.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\sounds\\background_music.mp3")
    pygame.mixer.music.play(-1)


    # Load images for explanation screen
    good_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch1.jpg"
    good_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch2.jpg"
    bad_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch1.jpg"
    bad_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch2.jpg"
        
        # Additional images
    bad_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch3.jpg"
    bad_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch4.jpg"
    good_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch3.jpg"
    good_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch4.jpg"
    good_img = pygame.image.load(good_img_path)
    bad_img = pygame.image.load(bad_img_path)
    good_img = pygame.transform.scale(good_img, (200, 200))
    bad_img = pygame.transform.scale(bad_img, (200, 200))

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
            pygame.draw.ellipse(screen, self.color, (int(self.x - self.width // 2), int(self.y - self.height // 2), self.width, self.height))
            pygame.draw.line(screen, (200, 200, 200), (int(self.x), int(self.y + self.height // 2)), (int(self.x), int(self.y + self.height // 2 + 20)), 2)
            number_text = font.render(str(self.number), True, (0, 0, 0))
            screen.blit(number_text, (self.x - 10, self.y - 10))

    class Dart:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.angle = 90
            self.speed = LAUNCH_SPEED
            self.active = False

        def draw(self):
            if self.active:
                pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

        def move(self):
            if self.active:
                self.x += self.speed * math.cos(math.radians(self.angle))
                self.y -= self.speed * math.sin(math.radians(self.angle))

    # Balloon popping game logic
    clock = pygame.time.Clock()
    running = True
    score = 0
    darts_used = 0

    balloons = []
    rows, cols = 2, 5
    x_start = WIDTH // 2 - ((cols - 1) * BUBBLE_WIDTH * 2) // 2
    y_start = 200
    row_spacing = BUBBLE_HEIGHT * 2.5

    for row in range(rows):
        for col in range(cols):
            x = x_start + col * BUBBLE_WIDTH * 2
            y = y_start + row * row_spacing
            balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), row * cols + col + 1))

    dart = Dart(WIDTH // 2, HEIGHT - 50)
    target_number = random.choice([b.number for b in balloons])

    while running:
        screen.fill((0, 0, 0))
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dart.angle += ANGLE_SPEED
                elif event.key == pygame.K_RIGHT:
                    dart.angle -= ANGLE_SPEED
                elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
                    dart = Dart(WIDTH // 2, HEIGHT - 50)
                    dart.angle = dart.angle
                    dart.active = True
                    darts_used += 1

        if dart.active:
            dart.move()
            for balloon in balloons:
                if balloon.active and math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2) < max(BUBBLE_WIDTH, BUBBLE_HEIGHT):
                    if balloon.number == target_number:
                        balloon.active = False
                        score += 10
                        dart.active = False
                        balloons.remove(balloon)
                        if balloons:
                            target_number = random.choice([b.number for b in balloons])
                        else:
                            target_number = None
                    break
            if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
                dart.active = False

        for balloon in balloons:
            if balloon.active:
                balloon.draw()
        dart.draw()

        target_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0))
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        darts_text = font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))

        screen.blit(target_text, (10, HEIGHT - 150))
        screen.blit(score_text, (10, HEIGHT - 90))
        screen.blit(darts_text, (10, HEIGHT - 50))

        if target_number is None or darts_used >= MAX_DARTS:
            show_completion_screen(score >= MIN_BALLOONS_TO_WIN * 10)
            running = False

        pygame.display.flip()
        clock.tick(30)


        def show_completion_screen(user_wins):
            screen.fill((255, 255, 255))

            if user_wins:
                message = "Yeah, you win the game! Which appreciation would you choose?"
            else:
                message = "Nice try! Keep it up, you'll get there! Which appreciation would you choose?"

            message_text = font.render(message, True, (0, 0, 0))
            screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 100))

            # Display images for touch choices without an OK button
            screen.blit(good_img, (150, 200))
            screen.blit(bad_img, (450, 200))

            pygame.display.flip()

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if 150 < x < 350 and 200 < y < 400:
                            display_explanation("good")
                        elif 450 < x < 650 and 200 < y < 400:
                            display_explanation("bad")

        def display_explanation(label):
            explanation = "This is a friendly touch." if label == "good" else "A  unusual touch is a touch that makes you feel uncomfortable, scared, or hurt, and should never happen."
            screen.fill((255, 255, 255))
            explanation_text = font.render(explanation, True, (0, 0, 0))
            screen.blit(explanation_text, (WIDTH // 2 - explanation_text.get_width() // 2, HEIGHT // 2))

            # Draw the "OK, Got It" button with rounded edges
            ok_button_rect = pygame.Rect(WIDTH // 2 - 70, HEIGHT - 80, 140, 40)
            pygame.draw.rect(screen, (100, 200, 255), ok_button_rect, border_radius=15)
            ok_text = font.render("OK, Got It", True, (255, 255, 255))
            screen.blit(ok_text, (ok_button_rect.x + 15, ok_button_rect.y + 5))

            pygame.display.flip()

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if ok_button_rect.collidepoint(event.pos):
                            running = False  # Exit the explanation screen loop

if __name__ == "__main__":
    start_safety_game()
