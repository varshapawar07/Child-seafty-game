import pygame
import random
import math
import tkinter as tk
from PIL import Image, ImageTk

# Initialize pygame
pygame.init()

# Balloon Popping Game Variables
WIDTH, HEIGHT = 800, 600
BUBBLE_WIDTH = 20
BUBBLE_HEIGHT = 30
BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
ANGLE_SPEED = 5
LAUNCH_SPEED = 10
COLUMN_SPACING = BUBBLE_WIDTH * 2  # Adjusted spacing for smaller balloons
ROW_SPACING = BUBBLE_HEIGHT * 2    # Adjusted spacing for smaller balloons
MAX_DARTS = 10
MIN_BALLOONS_TO_WIN = 6

# Screen setup for pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Targeted Balloon Pop Shooter")
font = pygame.font.Font(None, 36)
background_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\game images\\balloon.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pygame.mixer.music.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\sounds\\background_music.mp3")  # Path to background music file
pygame.mixer.music.play(-1)  # Play music in loop
# Define the Balloon and Dart classes
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

def balloon_popping_game():
    clock = pygame.time.Clock()
    running = True
    score = 0
    darts_used = 0
    # Calculate balloon positions for two rows
    shift_amount = 100
    balloons = []
    
    for i in range(10):
        if i < 5:
            x = WIDTH // 2 - 150 + shift_amount + i * (BUBBLE_WIDTH + 10)
            y = 200
        else:
            x = WIDTH // 2 - 150 + shift_amount + (i - 5) * (BUBBLE_WIDTH + 10)
            y = 300
        balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), i + 1))

    dart = Dart(WIDTH // 2, HEIGHT - 50)
    target_number = random.choice([b.number for b in balloons])

    target_number = random.choice([b.number for b in balloons])
    dart = Dart(WIDTH // 2, HEIGHT - 50)

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

        # Draw target text above the score
        screen.blit(target_text, (10, HEIGHT - 150))  # Positioned above the score
        screen.blit(score_text, (10, HEIGHT - 90))
        screen.blit(darts_text, (10, HEIGHT - 50))

        if target_number is None or darts_used >= MAX_DARTS:
            message = "Congratulations! You win!" if score >= MIN_BALLOONS_TO_WIN * 10 else "Game over! Try again!"
            show_completion_message(message)
            running = False

        pygame.display.flip()
        clock.tick(30)

def show_completion_message(message):
    root = tk.Tk()
    root.title("Game Completed")
    root.geometry("400x250")  # Window size adjustment for a compact look

    # Create and style the message label
    label = tk.Label(root, text=message, font=("Arial", 16), fg="#333333", wraplength=350, justify="center")
    label.pack(pady=20)

    # Define a function for when the "Next" button is clicked
    def go_to_question_page():
        root.destroy()
        touch_identification_game()

    # Center and style the "Next" button
    next_button = tk.Button(
        root,
        text="Next",
        command=go_to_question_page,
        font=("Comic Sans MS", 16, "bold"),
        bg="#4CAF50",  # Attractive green background color
        fg="white",  # White text color
        activebackground="#388E3C",  # Darker green when clicked
        activeforeground="white",  # White text when clicked
        relief=tk.RAISED,  # Raised button style for emphasis
        padx=20,  # Padding for a larger button
        pady=10
    )
    next_button.pack(pady=20)

    # Position the button at the center using pack with padding
    next_button.place(relx=0.5, rely=0.6, anchor="center")

    # Ensure cleanup if the window is closed directly
    root.protocol("WM_DELETE_WINDOW", lambda: close_game(root))
    root.mainloop()


def touch_identification_game():
    # Initialize the main application window
    root = tk.Tk()
    root.title("Touch Identification Game")
    root.geometry("500x600")
    root.configure(bg="#FFEBB7")

    # Title Label
    title_label = tk.Label(
        root,
        text="Is this touch good or bad?",
        font=("Comic Sans MS", 22, "bold"),
        bg="#FFEBB7",
        fg="#0066CC"
    )
    title_label.pack(pady=20)

    # Image display label
    image_label = tk.Label(root, bg="#FFEBB7")
    image_label.pack(pady=20)

    # Define the images dictionary with example data
    images = {
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch1.jpg": {"label": "good", "explanation": "This is a friendly touch, like a pat on the back."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch2.jpg": {"label": "good", "explanation": "This is a safe touch, like a high-five with a friend."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch1.jpg": {"label": "bad", "explanation": "This is an inappropriate touch and is not safe."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch2.jpg": {"label": "bad", "explanation": "This is a touch that makes you uncomfortable, so it's considered bad."},
    
    # Additional images
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch3.jpg": {"label": "bad", "explanation": "This shows an uncomfortable or unwanted touch. It's important to speak up in such situations."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch4.jpg": {"label": "bad", "explanation": "An inappropriate or unsafe touch. Always tell a trusted adult if this happens."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch3.jpg": {"label": "good", "explanation": "A friendly handshake, which is generally considered a good and safe touch."},
    "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch4.jpg": {"label": "good", "explanation": "A safe hug between friends or family members, showing care and affection."}
}

    # Load new image
    def load_new_image():
        global current_image, current_label, current_explanation
        current_image, details = random.choice(list(images.items()))
        current_label = details["label"]
        current_explanation = details["explanation"]

        img = Image.open(current_image)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

    # Check answer function
    def check_answer(answer):
        result_text = "Correct! 😊" if (answer == "Bad" and current_label == "bad") or (answer == "Good" and current_label == "good") else "Incorrect! 😔"
        result_color = "#66FF66" if result_text == "Correct! 😊" else "#FF6666"
        show_explanation_window(result_text, result_color, current_explanation)
        load_new_image()

    # Explanation window
    def show_explanation_window(result_text, result_color, explanation_text):
        explanation_window = tk.Toplevel(root)
        explanation_window.title("Explanation")
        explanation_window.geometry("400x350")
        explanation_window.configure(bg="#FFF0E6")

        result_label = tk.Label(explanation_window, text=result_text, font=("Comic Sans MS", 24, "bold"), bg="#FFF0E6", fg=result_color)
        result_label.pack(pady=10)

        explanation_label = tk.Label(explanation_window, text=explanation_text, font=("Comic Sans MS", 14), bg="#FFF0E6", fg="#333333", wraplength=350, justify="center")
        explanation_label.pack(pady=10)

        close_button = tk.Button(explanation_window, text="Got it!", font=("Comic Sans MS", 14, "bold"), command=explanation_window.destroy)
        close_button.pack(pady=20)

    # Setup buttons
    button_frame = tk.Frame(root, bg="#FFEBB7")
    button_frame.pack(pady=30)

    bad_button = tk.Button(button_frame, text="❌ Bad Touch", command=lambda: check_answer("Bad"), font=("Comic Sans MS", 16, "bold"), bg="#FF6666", fg="white")
    bad_button.grid(row=0, column=0, padx=20)

    good_button = tk.Button(button_frame, text="✔️ Good Touch", command=lambda: check_answer("Good"), font=("Comic Sans MS", 16, "bold"), bg="#4CAF50", fg="white")
    good_button.grid(row=0, column=1, padx=20)

    load_new_image()
    root.mainloop()

def close_game(window):
    window.destroy()
    pygame.quit()  # Close Pygame window after Tkinter interaction is complete

if __name__ == "__main__":
    balloon_popping_game()