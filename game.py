# import pygame
# import random
# import math
# import tkinter as tk
# from PIL import Image, ImageTk

# # Initialize pygame
# pygame.init()

# # Balloon Popping Game Variables
# WIDTH, HEIGHT = 800, 600
# BUBBLE_WIDTH = 20
# BUBBLE_HEIGHT = 30
# BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
# ANGLE_SPEED = 5
# LAUNCH_SPEED = 10
# MAX_DARTS = 10
# MIN_BALLOONS_TO_WIN = 6

# # Screen setup for pygame
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Targeted Balloon Pop Shooter")
# font = pygame.font.Font(None, 36)

# # Load assets
# background_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\game images\\balloon.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
# pygame.mixer.music.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\sounds\\background_music.mp3")
# pygame.mixer.music.play(-1)

# class Balloon:
#     def __init__(self, x, y, color, number):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = BUBBLE_WIDTH
#         self.height = BUBBLE_HEIGHT
#         self.number = number
#         self.active = True

#     def draw(self):
#         pygame.draw.ellipse(screen, self.color, (int(self.x - self.width // 2), int(self.y - self.height // 2), self.width, self.height))
#         pygame.draw.line(screen, (200, 200, 200), (int(self.x), int(self.y + self.height // 2)), (int(self.x), int(self.y + self.height // 2 + 20)), 2)
#         number_text = font.render(str(self.number), True, (0, 0, 0))
#         screen.blit(number_text, (self.x - 10, self.y - 10))

# class Dart:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.angle = 90
#         self.speed = LAUNCH_SPEED
#         self.active = False

#     def draw(self):
#         if self.active:
#             pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

#     def move(self):
#         if self.active:
#             self.x += self.speed * math.cos(math.radians(self.angle))
#             self.y -= self.speed * math.sin(math.radians(self.angle))

# def balloon_popping_game():
#     clock = pygame.time.Clock()
#     running = True
#     score = 0
#     darts_used = 0

#     balloons = []
#     rows, cols = 2, 5
#     x_start = WIDTH // 2 - ((cols - 1) * BUBBLE_WIDTH * 2) // 2
#     y_start = 200
#     row_spacing = BUBBLE_HEIGHT * 2.5

#     for row in range(rows):
#         for col in range(cols):
#             x = x_start + col * BUBBLE_WIDTH * 2
#             y = y_start + row * row_spacing
#             balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), row * cols + col + 1))

#     dart = Dart(WIDTH // 2, HEIGHT - 50)
#     target_number = random.choice([b.number for b in balloons])

#     while running:
#         screen.fill((0, 0, 0))
#         screen.blit(background_image, (0, 0))

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     dart.angle += ANGLE_SPEED
#                 elif event.key == pygame.K_RIGHT:
#                     dart.angle -= ANGLE_SPEED
#                 elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
#                     dart = Dart(WIDTH // 2, HEIGHT - 50)
#                     dart.angle = dart.angle
#                     dart.active = True
#                     darts_used += 1

#         if dart.active:
#             dart.move()
#             for balloon in balloons:
#                 if balloon.active and math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2) < max(BUBBLE_WIDTH, BUBBLE_HEIGHT):
#                     if balloon.number == target_number:
#                         balloon.active = False
#                         score += 10
#                         dart.active = False
#                         balloons.remove(balloon)
#                         if balloons:
#                             target_number = random.choice([b.number for b in balloons])
#                         else:
#                             target_number = None
#                     break
#             if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
#                 dart.active = False

#         for balloon in balloons:
#             if balloon.active:
#                 balloon.draw()
#         dart.draw()

#         target_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0))
#         score_text = font.render(f"Score: {score}", True, (0, 0, 0))
#         darts_text = font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))

#         screen.blit(target_text, (10, HEIGHT - 150))
#         screen.blit(score_text, (10, HEIGHT - 90))
#         screen.blit(darts_text, (10, HEIGHT - 50))

#         if target_number is None or darts_used >= MAX_DARTS:
#             message = "Congratulations! You win!" if score >= MIN_BALLOONS_TO_WIN * 10 else "Game over! Try again!"
#             show_completion_message(message, score >= MIN_BALLOONS_TO_WIN * 10)
#             running = False

#         pygame.display.flip()
#         clock.tick(30)

# def show_completion_message(message, user_wins):
#     root = tk.Tk()
#     root.title("Game Completed")
#     root.geometry("800x600")

#     label = tk.Label(root, text=message, font=("Arial", 16), fg="#333333", wraplength=350, justify="center")
#     label.pack(pady=20)

#     if user_wins:
#         statement = "Yeah, you win the game! Which appreciation would you choose?"
#     else:
#         statement = "Nice try! Keep it up, you'll get there! Which appreciation would you choose?"

#     message_label = tk.Label(root, text=statement, font=("Comic Sans MS", 16), fg="#333333")
#     message_label.pack(pady=20)

#     # Path for only one good touch image and one bad touch image
#     # Load images
# image_paths = {
#     "good": [
#         "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch1.jpg",
#         "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch2.jpg",
#         "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch3.jpg",
#         "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch4.jpg"
#     ],
#     "bad": [
#         "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch1.jpg",
#         "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch2.jpg",
#         "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch3.jpg",
#         "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch4.jpg"
#     ]
# }

# def show_completion_message(message, user_wins):
#     root = tk.Tk()
#     root.title("Game Completed")
#     root.geometry("800x600")

#     label = tk.Label(root, text=message, font=("Arial", 16), fg="#333333", wraplength=350, justify="center")
#     label.pack(pady=20)

#     if user_wins:
#         statement = "Yeah, you win the game! Which appreciation would you choose?"
#     else:
#         statement = "Nice try! Keep it up, you'll get there! Which appreciation would you choose?"

#     message_label = tk.Label(root, text=statement, font=("Comic Sans MS", 16), fg="#333333")
#     message_label.pack(pady=20)

#     # Randomly choose one good touch and one bad touch image
#     good_touch_path = random.choice(image_paths["good"])
#     bad_touch_path = random.choice(image_paths["bad"])

#     good_touch_explanation = "This is a friendly touch, like a pat on the back.A Usual touch is a friendly touch that makes you feel happy and safe, like a hug or a high-five."
#     bad_touch_explanation = "A  unusual touch is a touch that makes you feel uncomfortable, scared, or hurt, and should never happen."

#     # Display the two images
#     def on_image_click(label):
#         explanation = good_touch_explanation if label == "good" else bad_touch_explanation
#         show_explanation_window(label, explanation)

#     # Load and resize images
#     good_img = Image.open(good_touch_path).resize((400, 400))  # Increased size
#     bad_img = Image.open(bad_touch_path).resize((400, 400))    # Increased size

#     good_img_tk = ImageTk.PhotoImage(good_img)
#     bad_img_tk = ImageTk.PhotoImage(bad_img)

#     # Create buttons for the images
#     good_button = tk.Button(root, image=good_img_tk, command=lambda: on_image_click("good"))
#     good_button.image = good_img_tk
#     good_button.pack(side="left", padx=20, pady=20)

#     bad_button = tk.Button(root, image=bad_img_tk, command=lambda: on_image_click("bad"))
#     bad_button.image = bad_img_tk
#     bad_button.pack(side="right", padx=20, pady=20)

#     root.protocol("WM_DELETE_WINDOW", root.destroy)
#     root.mainloop()

# def show_explanation_window(label, explanation):
#     explanation_window = tk.Toplevel()
#     explanation_window.title("Explanation")
#     explanation_window.geometry("400x300")
#     explanation_window.configure(bg="#FFF0E6")

#     result_text = "Why this is usual touch" if label == "good" else "Why this is unusual touch"
#     result_label = tk.Label(explanation_window, text=result_text, font=("Comic Sans MS", 18, "bold"), bg="#FFF0E6", fg="#333333")
#     result_label.pack(pady=10)

#     explanation_label = tk.Label(explanation_window, text=explanation, font=("Comic Sans MS", 14), bg="#FFF0E6", fg="#333333", wraplength=350, justify="center")
#     explanation_label.pack(pady=10)

#     ok_button = tk.Button(explanation_window, text="OK, got it", command=explanation_window.destroy, font=("Comic Sans MS", 14), bg="#4CAF50", fg="white")
#     ok_button.pack(pady=20)

# if __name__ == "__main__":
#     balloon_popping_game()
#     pygame.quit()




###############################################################################################
# import pygame
# import random
# import math
# from PIL import Image

# # Initialize pygame
# pygame.init()

# # Balloon Popping Game Variables
# WIDTH, HEIGHT = 800, 600
# BUBBLE_WIDTH = 20
# BUBBLE_HEIGHT = 30
# BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
# ANGLE_SPEED = 5
# LAUNCH_SPEED = 10
# MAX_DARTS = 10
# MIN_BALLOONS_TO_WIN = 6

# # Screen setup for pygame
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Targeted Balloon Pop Shooter")
# font = pygame.font.Font(None, 36)

# # Load assets
# background_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\game images\\balloon.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# class Balloon:
#     def __init__(self, x, y, color, number):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = BUBBLE_WIDTH
#         self.height = BUBBLE_HEIGHT
#         self.number = number
#         self.active = True

#     def draw(self):
#         pygame.draw.ellipse(screen, self.color, (int(self.x - self.width // 2), int(self.y - self.height // 2), self.width, self.height))
#         pygame.draw.line(screen, (200, 200, 200), (int(self.x), int(self.y + self.height // 2)), (int(self.x), int(self.y + self.height // 2 + 20)), 2)
#         number_text = font.render(str(self.number), True, (0, 0, 0))
#         screen.blit(number_text, (self.x - 10, self.y - 10))

# class Dart:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.angle = 90
#         self.speed = LAUNCH_SPEED
#         self.active = False

#     def draw(self):
#         if self.active:
#             pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

#     def move(self):
#         if self.active:
#             self.x += self.speed * math.cos(math.radians(self.angle))
#             self.y -= self.speed * math.sin(math.radians(self.angle))

# def balloon_popping_game():
#     clock = pygame.time.Clock()
#     running = True
#     score = 0
#     darts_used = 0

#     balloons = []
#     rows, cols = 2, 5
#     x_start = WIDTH // 2 - ((cols - 1) * BUBBLE_WIDTH * 2) // 2
#     y_start = 200
#     row_spacing = BUBBLE_HEIGHT * 2.5

#     for row in range(rows):
#         for col in range(cols):
#             x = x_start + col * BUBBLE_WIDTH * 2
#             y = y_start + row * row_spacing
#             balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), row * cols + col + 1))

#     dart = Dart(WIDTH // 2, HEIGHT - 50)
#     target_number = random.choice([b.number for b in balloons])

#     while running:
#         screen.fill((0, 0, 0))
#         screen.blit(background_image, (0, 0))

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     dart.angle += ANGLE_SPEED
#                 elif event.key == pygame.K_RIGHT:
#                     dart.angle -= ANGLE_SPEED
#                 elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
#                     dart = Dart(WIDTH // 2, HEIGHT - 50)
#                     dart.angle = dart.angle
#                     dart.active = True
#                     darts_used += 1

#         if dart.active:
#             dart.move()
#             for balloon in balloons:
#                 if balloon.active and math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2) < max(BUBBLE_WIDTH, BUBBLE_HEIGHT):
#                     if balloon.number == target_number:
#                         balloon.active = False
#                         score += 10
#                         dart.active = False
#                         balloons.remove(balloon)
#                         if balloons:
#                             target_number = random.choice([b.number for b in balloons])
#                         else:
#                             target_number = None
#                     break
#             if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
#                 dart.active = False

#         for balloon in balloons:
#             if balloon.active:
#                 balloon.draw()
#         dart.draw()

#         target_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0))
#         score_text = font.render(f"Score: {score}", True, (0, 0, 0))
#         darts_text = font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))

#         screen.blit(target_text, (10, HEIGHT - 150))
#         screen.blit(score_text, (10, HEIGHT - 90))
#         screen.blit(darts_text, (10, HEIGHT - 50))

#         if target_number is None or darts_used >= MAX_DARTS:
#             show_completion_screen(score >= MIN_BALLOONS_TO_WIN * 10)
#             running = False

#         pygame.display.flip()
#         clock.tick(30)

# def show_completion_screen(user_wins):
#     screen.fill((255, 255, 255))

#     if user_wins:
#         message = "Congratulations! You win! Choose an appreciation."
#     else:
#         message = "Nice try! Keep going. Choose an appreciation."

#     message_text = font.render(message, True, (0, 0, 0))
#     screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 100))

#     # Load images
#     good_img = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch1.jpg")
#     bad_img = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch1.jpg")
#     good_img = pygame.transform.scale(good_img, (200, 200))
#     bad_img = pygame.transform.scale(bad_img, (200, 200))

#     screen.blit(good_img, (150, 200))
#     screen.blit(bad_img, (450, 200))

#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 if 150 < x < 350 and 200 < y < 400:
#                     display_explanation("good")
#                 elif 450 < x < 650 and 200 < y < 400:
#                     display_explanation("bad")
        
# def display_explanation(label):
#     explanation = "This is a friendly touch." if label == "good" else "This touch makes you feel uncomfortable."
#     screen.fill((255, 255, 255))
#     explanation_text = font.render(explanation, True, (0, 0, 0))
#     screen.blit(explanation_text, (WIDTH // 2 - explanation_text.get_width() // 2, HEIGHT // 2))

#     pygame.display.flip()

#     # Wait for a while or until the user clicks to return
#     pygame.time.delay(2000)

# if __name__ == "__main__":
#     balloon_popping_game()
#     pygame.quit()


# ##########################################################################################################################
# import pygame
# import random
# import math
# from PIL import Image

# # Initialize pygame
# pygame.init()

# # Game Variables
# WIDTH, HEIGHT = 800, 600
# BUBBLE_WIDTH = 20
# BUBBLE_HEIGHT = 30
# BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
# ANGLE_SPEED = 5
# LAUNCH_SPEED = 10
# MAX_DARTS = 10
# MIN_BALLOONS_TO_WIN = 6

# # Screen setup for pygame
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Targeted Balloon Pop Shooter")
# font = pygame.font.Font(None, 36)

# # Load assets
# background_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\game images\\balloon.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# # Load images for explanation screen
# good_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch1.jpg"
# bad_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch1.jpg"
# good_img = pygame.image.load(good_img_path)
# bad_img = pygame.image.load(bad_img_path)
# good_img = pygame.transform.scale(good_img, (200, 200))
# bad_img = pygame.transform.scale(bad_img, (200, 200))

# class Balloon:
#     def __init__(self, x, y, color, number):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = BUBBLE_WIDTH
#         self.height = BUBBLE_HEIGHT
#         self.number = number
#         self.active = True

#     def draw(self):
#         pygame.draw.ellipse(screen, self.color, (int(self.x - self.width // 2), int(self.y - self.height // 2), self.width, self.height))
#         pygame.draw.line(screen, (200, 200, 200), (int(self.x), int(self.y + self.height // 2)), (int(self.x), int(self.y + self.height // 2 + 20)), 2)
#         number_text = font.render(str(self.number), True, (0, 0, 0))
#         screen.blit(number_text, (self.x - 10, self.y - 10))

# class Dart:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.angle = 90
#         self.speed = LAUNCH_SPEED
#         self.active = False

#     def draw(self):
#         if self.active:
#             pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

#     def move(self):
#         if self.active:
#             self.x += self.speed * math.cos(math.radians(self.angle))
#             self.y -= self.speed * math.sin(math.radians(self.angle))

# def balloon_popping_game():
#     clock = pygame.time.Clock()
#     running = True
#     score = 0
#     darts_used = 0

#     balloons = []
#     rows, cols = 2, 5
#     x_start = WIDTH // 2 - ((cols - 1) * BUBBLE_WIDTH * 2) // 2
#     y_start = 200
#     row_spacing = BUBBLE_HEIGHT * 2.5

#     for row in range(rows):
#         for col in range(cols):
#             x = x_start + col * BUBBLE_WIDTH * 2
#             y = y_start + row * row_spacing
#             balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), row * cols + col + 1))

#     dart = Dart(WIDTH // 2, HEIGHT - 50)
#     target_number = random.choice([b.number for b in balloons])

#     while running:
#         screen.fill((0, 0, 0))
#         screen.blit(background_image, (0, 0))

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     dart.angle += ANGLE_SPEED
#                 elif event.key == pygame.K_RIGHT:
#                     dart.angle -= ANGLE_SPEED
#                 elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
#                     dart = Dart(WIDTH // 2, HEIGHT - 50)
#                     dart.angle = dart.angle
#                     dart.active = True
#                     darts_used += 1

#         if dart.active:
#             dart.move()
#             for balloon in balloons:
#                 if balloon.active and math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2) < max(BUBBLE_WIDTH, BUBBLE_HEIGHT):
#                     if balloon.number == target_number:
#                         balloon.active = False
#                         score += 10
#                         dart.active = False
#                         balloons.remove(balloon)
#                         if balloons:
#                             target_number = random.choice([b.number for b in balloons])
#                         else:
#                             target_number = None
#                     break
#             if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
#                 dart.active = False

#         for balloon in balloons:
#             if balloon.active:
#                 balloon.draw()
#         dart.draw()

#         target_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0))
#         score_text = font.render(f"Score: {score}", True, (0, 0, 0))
#         darts_text = font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))

#         screen.blit(target_text, (10, HEIGHT - 150))
#         screen.blit(score_text, (10, HEIGHT - 90))
#         screen.blit(darts_text, (10, HEIGHT - 50))

#         if target_number is None or darts_used >= MAX_DARTS:
#             show_completion_screen(score >= MIN_BALLOONS_TO_WIN * 10)
#             running = False

#         pygame.display.flip()
#         clock.tick(30)

# def show_completion_screen(user_wins):
#     screen.fill((255, 255, 255))

#     if user_wins:
#         message = "Congratulations! You win! Choose an appreciation."
#     else:
#         message = "Nice try! Keep going. Choose an appreciation."

#     message_text = font.render(message, True, (0, 0, 0))
#     screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 100))

#     # Display images
#     screen.blit(good_img, (150, 200))
#     screen.blit(bad_img, (450, 200))

#     # Draw the OK button
#     ok_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 100, 100, 50)
#     pygame.draw.rect(screen, (0, 255, 0), ok_button_rect)
#     ok_text = font.render("OK", True, (0, 0, 0))
#     screen.blit(ok_text, (ok_button_rect.x + 20, ok_button_rect.y + 10))

#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 if 150 < x < 350 and 200 < y < 400:
#                     display_explanation("good")
#                 elif 450 < x < 650 and 200 < y < 400:
#                     display_explanation("bad")
#                 elif ok_button_rect.collidepoint(x, y):
#                     running = False  # Exit the completion screen loop and end the game

# def display_explanation(label):
#     explanation = "This is a friendly touch." if label == "good" else "This touch makes you feel uncomfortable."
#     screen.fill((255, 255, 255))
#     explanation_text = font.render(explanation, True, (0, 0, 0))
#     screen.blit(explanation_text, (WIDTH // 2 - explanation_text.get_width() // 2, HEIGHT // 2))

#     # Draw the OK button
#     ok_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 100, 100, 50)
#     pygame.draw.rect(screen, (0, 255, 0), ok_button_rect)
#     ok_text = font.render("OK", True, (0, 0, 0))
#     screen.blit(ok_text, (ok_button_rect.x + 20, ok_button_rect.y + 10))

#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 if ok_button_rect.collidepoint(x, y):
#                     running = False  # Exit the explanation screen loop

# if __name__ == "__main__":
#     balloon_popping_game()
#     pygame.quit()




# #E#######################################################################
# import pygame
# import random
# import math
# from PIL import Image

# # Initialize pygame
# pygame.init()

# # Game Variables
# WIDTH, HEIGHT = 800, 600
# BUBBLE_WIDTH = 20
# BUBBLE_HEIGHT = 30
# BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
# ANGLE_SPEED = 5
# LAUNCH_SPEED = 10
# MAX_DARTS = 10
# MIN_BALLOONS_TO_WIN = 6

# # Screen setup for pygame
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Targeted Balloon Pop Shooter")
# font = pygame.font.Font(None, 36)

# # Load assets
# background_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\game images\\balloon.jpg")
# background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# # Load images for explanation screen
# good_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\good_touch1.jpg"
# bad_img_path = "D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\good and bad images\\bad_touch1.jpg"
# good_img = pygame.image.load(good_img_path)
# bad_img = pygame.image.load(bad_img_path)
# good_img = pygame.transform.scale(good_img, (200, 200))
# bad_img = pygame.transform.scale(bad_img, (200, 200))

# class Balloon:
#     def __init__(self, x, y, color, number):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = BUBBLE_WIDTH
#         self.height = BUBBLE_HEIGHT
#         self.number = number
#         self.active = True

#     def draw(self):
#         pygame.draw.ellipse(screen, self.color, (int(self.x - self.width // 2), int(self.y - self.height // 2), self.width, self.height))
#         pygame.draw.line(screen, (200, 200, 200), (int(self.x), int(self.y + self.height // 2)), (int(self.x), int(self.y + self.height // 2 + 20)), 2)
#         number_text = font.render(str(self.number), True, (0, 0, 0))
#         screen.blit(number_text, (self.x - 10, self.y - 10))

# class Dart:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.angle = 90
#         self.speed = LAUNCH_SPEED
#         self.active = False

#     def draw(self):
#         if self.active:
#             pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

#     def move(self):
#         if self.active:
#             self.x += self.speed * math.cos(math.radians(self.angle))
#             self.y -= self.speed * math.sin(math.radians(self.angle))

# def balloon_popping_game():
#     clock = pygame.time.Clock()
#     running = True
#     score = 0
#     darts_used = 0

#     balloons = []
#     rows, cols = 2, 5
#     x_start = WIDTH // 2 - ((cols - 1) * BUBBLE_WIDTH * 2) // 2
#     y_start = 200
#     row_spacing = BUBBLE_HEIGHT * 2.5

#     for row in range(rows):
#         for col in range(cols):
#             x = x_start + col * BUBBLE_WIDTH * 2
#             y = y_start + row * row_spacing
#             balloons.append(Balloon(x, y, random.choice(BUBBLE_COLORS), row * cols + col + 1))

#     dart = Dart(WIDTH // 2, HEIGHT - 50)
#     target_number = random.choice([b.number for b in balloons])

#     while running:
#         screen.fill((0, 0, 0))
#         screen.blit(background_image, (0, 0))

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     dart.angle += ANGLE_SPEED
#                 elif event.key == pygame.K_RIGHT:
#                     dart.angle -= ANGLE_SPEED
#                 elif event.key == pygame.K_SPACE and not dart.active and darts_used < MAX_DARTS:
#                     dart = Dart(WIDTH // 2, HEIGHT - 50)
#                     dart.angle = dart.angle
#                     dart.active = True
#                     darts_used += 1

#         if dart.active:
#             dart.move()
#             for balloon in balloons:
#                 if balloon.active and math.sqrt((balloon.x - dart.x) ** 2 + (balloon.y - dart.y) ** 2) < max(BUBBLE_WIDTH, BUBBLE_HEIGHT):
#                     if balloon.number == target_number:
#                         balloon.active = False
#                         score += 10
#                         dart.active = False
#                         balloons.remove(balloon)
#                         if balloons:
#                             target_number = random.choice([b.number for b in balloons])
#                         else:
#                             target_number = None
#                     break
#             if dart.x < 0 or dart.x > WIDTH or dart.y < 0:
#                 dart.active = False

#         for balloon in balloons:
#             if balloon.active:
#                 balloon.draw()
#         dart.draw()

#         target_text = font.render(f"Target Balloon: {target_number}", True, (0, 0, 0))
#         score_text = font.render(f"Score: {score}", True, (0, 0, 0))
#         darts_text = font.render(f"Darts Used: {darts_used}/{MAX_DARTS}", True, (0, 0, 0))

#         screen.blit(target_text, (10, HEIGHT - 150))
#         screen.blit(score_text, (10, HEIGHT - 90))
#         screen.blit(darts_text, (10, HEIGHT - 50))

#         if target_number is None or darts_used >= MAX_DARTS:
#             show_completion_screen(score >= MIN_BALLOONS_TO_WIN * 10)
#             running = False

#         pygame.display.flip()
#         clock.tick(30)

# def show_completion_screen(user_wins):
#     screen.fill((255, 255, 255))

#     if user_wins:
#         message = "Congratulations! You win! Choose an appreciation."
#     else:
#         message = "Nice try! Keep going. Choose an appreciation."

#     message_text = font.render(message, True, (0, 0, 0))
#     screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 100))

#     # Display images
#     screen.blit(good_img, (150, 200))
#     screen.blit(bad_img, (450, 200))

#     # Draw the OK button
#     ok_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 100, 100, 50)
#     pygame.draw.rect(screen, (0, 255, 0), ok_button_rect, border_radius=10)  # Rounded rectangle for OK button
#     ok_text = font.render("OK", True, (0, 0, 0))
#     screen.blit(ok_text, (ok_button_rect.x + 20, ok_button_rect.y + 10))

#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 x, y = event.pos
#                 if 150 < x < 350 and 200 < y < 400:
#                     display_explanation("good")
#                 elif 450 < x < 650 and 200 < y < 400:
#                     display_explanation("bad")
#                 elif ok_button_rect.collidepoint(x, y):
#                     running = False  # Exit the completion screen loop and end the game

# def display_explanation(label):
#     explanation = "This is a friendly touch." if label == "good" else "This touch makes you feel uncomfortable."
#     screen.fill((255, 255, 255))
#     explanation_text = font.render(explanation, True, (0, 0, 0))
#     screen.blit(explanation_text, (WIDTH // 2 - explanation_text.get_width() // 2, HEIGHT // 2))

#     # Draw the "OK, Got It" button with rounded edges
#     ok_button_rect = pygame.Rect(WIDTH // 2 - 70, HEIGHT - 80, 140, 40)
#     pygame.draw.rect(screen, (100, 200, 255), ok_button_rect, border_radius=15)
#     ok_text = font.render("OK, Got It", True, (255, 255, 255))
#     screen.blit(ok_text, (ok_button_rect.x + 15, ok_button_rect.y + 5))

#     pygame.display.flip()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if ok_button_rect.collidepoint(event.pos):
#                     running = False  # Exit the explanation screen loop

# if __name__ == "__main__":
#     balloon_popping_game()
#     pygame.quit()


##################################################################################



import pygame
import random
import math
from PIL import Image

# Initialize pygame
pygame.init()

# Game Variables
WIDTH, HEIGHT = 800, 600
BUBBLE_WIDTH = 20
BUBBLE_HEIGHT = 30
BUBBLE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
ANGLE_SPEED = 5
LAUNCH_SPEED = 10
MAX_DARTS = 10
MIN_BALLOONS_TO_WIN = 6

# Screen setup for pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Targeted Balloon Pop Shooter")
font = pygame.font.Font(None, 36)

# Load assets
background_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\game images\\balloon.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
pygame.mixer.music.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\sounds\\background_music.mp3")  # Path to background music file
pygame.mixer.music.play(-1)  # Play music in loop

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

def balloon_popping_game():
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
    balloon_popping_game()
    pygame.quit()
