# import pygame
# import sys
# import time

# # Initialize Pygame
# pygame.init()

# # Screen settings
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Game')

# # Colors
# white = (255, 255, 255)

# # Load images for scenario selection
# background_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\environments\\back1.jpg").convert()
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# playground_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\playG3.jpg").convert_alpha()
# school_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\School1.jpg").convert_alpha()

# # Scale images for scenario selection
# playground_image = pygame.transform.scale(playground_image, (200, 150))
# school_image = pygame.transform.scale(school_image, (200, 150))

# # Set up fonts
# font = pygame.font.Font(None, 48)
# small_font = pygame.font.Font(None, 36)

# # Render text for scenario selection
# title_text = font.render('Select Scenario', True, (255, 69, 0))
# playground_text = small_font.render('Playground', True, (255, 69, 0))
# school_text = small_font.render('School(Locked)', True, (255, 69, 0))

# # Get text and image positions
# title_rect = title_text.get_rect(center=(screen_width // 2, 170))
# playground_rect = playground_image.get_rect(center=(screen_width // 2 - 150, screen_height // 2))
# playground_text_rect = playground_text.get_rect(center=(playground_rect.centerx, playground_rect.bottom + 20))
# school_rect = school_image.get_rect(center=(screen_width // 2 + 150, screen_height // 2))
# school_text_rect = school_text.get_rect(center=(school_rect.centerx, school_rect.bottom + 20))

# # Load navigation images
# home_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\house2.jpg").convert()
# carnival_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\funfair1.jpg").convert()
# girl_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\characters\\girl\\girl1.png").convert_alpha()

# # Scale navigation images
# home_image = pygame.transform.scale(home_image, (screen_width, screen_height))
# carnival_image = pygame.transform.scale(carnival_image, (screen_width, screen_height))
# girl_image = pygame.transform.scale(girl_image, (100, 150))

# # Navigation settings
# bg_x = 0
# scroll_speed = 0.5
# bg_images = [home_image, carnival_image]
# current_bg_index = 0
# next_bg_index = 1
# girl_position = (50, screen_height - girl_image.get_height() - 50)

# # Game state
# SCENARIO_SELECTION = 0
# NAVIGATION = 1
# game_state = SCENARIO_SELECTION

# # Timer for closing the game
# start_time = None

# # Main loop
# running = True
# moving_right = False
# moving_left = False

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = True
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = True
#         elif event.type == pygame.KEYUP:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = False
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = False
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             mouse_pos = pygame.mouse.get_pos()
#             if game_state == SCENARIO_SELECTION:
#                 # Check if playground or school is clicked
#                 if playground_rect.collidepoint(mouse_pos):
#                     game_state = NAVIGATION
#                     start_time = time.time()  # Start timer after scenario is selected
#                 elif school_rect.collidepoint(mouse_pos):
#                     print("School selected (add code for school navigation if needed)")

#     # Check if 1 second has passed since starting navigation
#     if game_state == NAVIGATION and start_time and time.time() - start_time >= 1.9:
#         running = False  # Stop the game loop after 1 second

#     # Game states
#     if game_state == SCENARIO_SELECTION:
#         # Draw scenario selection screen
#         screen.blit(background_image, (0, 0))
#         screen.blit(title_text, title_rect)
#         screen.blit(playground_image, playground_rect)
#         screen.blit(playground_text, playground_text_rect)
#         screen.blit(school_image, school_rect)
#         screen.blit(school_text, school_text_rect)

#     elif game_state == NAVIGATION:
#         # Navigation background scrolling logic
#         if moving_right:
#             bg_x -= scroll_speed
#             if bg_x <= -screen_width:
#                 bg_x = 0
#                 current_bg_index = (current_bg_index + 1) % len(bg_images)
#                 next_bg_index = (current_bg_index + 1) % len(bg_images)
#         elif moving_left:
#             bg_x += scroll_speed
#             if bg_x >= screen_width:
#                 bg_x = 0
#                 current_bg_index = (current_bg_index - 1) % len(bg_images)
#                 next_bg_index = (current_bg_index - 1) % len(bg_images)

#         # Draw navigation screen
#         screen.blit(bg_images[current_bg_index], (bg_x, 0))
#         screen.blit(bg_images[next_bg_index], (bg_x + screen_width, 0))
#         screen.blit(girl_image, girl_position)

#     # Update display
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()
# sys.exit()




#########################################################################
# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Screen settings
# screen_width, screen_height = 1200, 750
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Game')

# # Colors
# white = (255, 255, 255)

# # Load images for scenario selection
# background_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\environments\\back1.jpg").convert()
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# playground_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\playG3.jpg").convert_alpha()
# school_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\School1.jpg").convert_alpha()

# # Scale images for scenario selection
# playground_image = pygame.transform.scale(playground_image, (200, 150))
# school_image = pygame.transform.scale(school_image, (200, 150))

# # Set up fonts
# font = pygame.font.Font(None, 48)
# small_font = pygame.font.Font(None, 36)

# # Render text for scenario selection
# title_text = font.render('Select Scenario', True, (255, 69, 0))
# playground_text = small_font.render('Playground', True, (255, 69, 0))
# school_text = small_font.render('School(Locked)', True, (255, 69, 0))

# # Get text and image positions
# title_rect = title_text.get_rect(center=(screen_width // 2, 170))
# playground_rect = playground_image.get_rect(center=(screen_width // 2 - 150, screen_height // 2))
# playground_text_rect = playground_text.get_rect(center=(playground_rect.centerx, playground_rect.bottom + 20))
# school_rect = school_image.get_rect(center=(screen_width // 2 + 150, screen_height // 2))
# school_text_rect = school_text.get_rect(center=(school_rect.centerx, school_rect.bottom + 20))

# # Load navigation images
# home_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\house2.jpg").convert()
# carnival_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\funfair1.jpg").convert()
# girl_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\characters\\girl\\girl1.png").convert_alpha()

# # Scale navigation images
# home_image = pygame.transform.scale(home_image, (screen_width, screen_height))
# carnival_image = pygame.transform.scale(carnival_image, (screen_width, screen_height))
# girl_image = pygame.transform.scale(girl_image, (100, 150))

# # Navigation settings
# bg_x = 0
# scroll_speed = 0.5
# bg_images = [home_image, carnival_image]
# current_bg_index = 0
# next_bg_index = 1
# girl_position = [50, screen_height - girl_image.get_height() - 50]  # Updated for mutable position

# # Play button
# play_button_text = font.render("Play", True, (0, 255, 0))
# play_button_rect = play_button_text.get_rect(center=(screen_width // 2, screen_height // 2))

# # Game state
# SCENARIO_SELECTION = 0
# NAVIGATION = 1
# game_state = SCENARIO_SELECTION

# # Main loop
# running = True
# moving_right = False
# moving_left = False

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = True
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = True
#         elif event.type == pygame.KEYUP:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = False
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = False
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             mouse_pos = pygame.mouse.get_pos()
#             if game_state == SCENARIO_SELECTION:
#                 # Check if playground or school is clicked
#                 if playground_rect.collidepoint(mouse_pos):
#                     game_state = NAVIGATION
#                 elif school_rect.collidepoint(mouse_pos):
#                     print("School selected (add code for school navigation if needed)")
#             elif game_state == NAVIGATION:
#                 # Check if play button is clicked
#                 if play_button_rect.collidepoint(mouse_pos):
#                     print("Play button clicked! Add logic to start the game.")

#     # Game states
#     if game_state == SCENARIO_SELECTION:
#         # Draw scenario selection screen
#         screen.blit(background_image, (0, 0))
#         screen.blit(title_text, title_rect)
#         screen.blit(playground_image, playground_rect)
#         screen.blit(playground_text, playground_text_rect)
#         screen.blit(school_image, school_rect)
#         screen.blit(school_text, school_text_rect)

#     elif game_state == NAVIGATION:
#         # Navigation background scrolling logic
#         if moving_right:
#             girl_position[0] += 5  # Move right
#         if moving_left:
#             girl_position[0] -= 5  # Move left

#         # Keep character within screen bounds
#         girl_position[0] = max(0, min(screen_width - girl_image.get_width(), girl_position[0]))

#         # Draw navigation screen
#         screen.blit(bg_images[current_bg_index], (0, 0))
#         screen.blit(girl_image, girl_position)

#         # Draw play button
#         screen.blit(play_button_text, play_button_rect)

#     # Update display
#     pygame.display.flip()

# # Quit Pygame
# pygame.quit()
# sys.exit()



########################################################################################################
# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Screen settings
# screen_width, screen_height = 1200, 750
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Game')

# # Load images for scenario selection
# background_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\environments\\back1.jpg").convert()
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# playground_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\playG3.jpg").convert_alpha()
# school_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\School1.jpg").convert_alpha()

# # Scale images for scenario selection
# playground_image = pygame.transform.scale(playground_image, (200, 150))
# school_image = pygame.transform.scale(school_image, (200, 150))

# # Set up fonts
# font = pygame.font.Font(None, 48)
# small_font = pygame.font.Font(None, 36)

# # Render text for scenario selection
# title_text = font.render('Select Scenario', True, (255, 69, 0))
# playground_text = small_font.render('Playground', True, (255, 69, 0))
# school_text = small_font.render('School(Locked)', True, (255, 69, 0))

# # Get text and image positions
# title_rect = title_text.get_rect(center=(screen_width // 2, 170))
# playground_rect = playground_image.get_rect(center=(screen_width // 2 - 150, screen_height // 2))
# playground_text_rect = playground_text.get_rect(center=(playground_rect.centerx, playground_rect.bottom + 20))
# school_rect = school_image.get_rect(center=(screen_width // 2 + 150, screen_height // 2))
# school_text_rect = school_text.get_rect(center=(school_rect.centerx, school_rect.bottom + 20))

# # Load navigation images
# house_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\house2.jpg").convert()
# funfair_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\funfair1.jpg").convert()
# girl_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\characters\\girl\\girl1.png").convert_alpha()

# # Scale navigation images
# house_image = pygame.transform.scale(house_image, (screen_width, screen_height))
# funfair_image = pygame.transform.scale(funfair_image, (screen_width, screen_height))
# girl_image = pygame.transform.scale(girl_image, (100, 150))

# # Create a combined navigation surface
# combined_width = screen_width * 2  # Two images side by side
# navigation_surface = pygame.Surface((combined_width, screen_height))
# navigation_surface.blit(house_image, (0, 0))  # Place house image first
# navigation_surface.blit(funfair_image, (screen_width, 0))  # Place funfair image next

# girl_position = [50, screen_height - girl_image.get_height() - 50]

# # Game state
# SCENARIO_SELECTION = 0
# NAVIGATION = 1
# game_state = SCENARIO_SELECTION

# # Main loop
# running = True
# moving_right = False
# moving_left = False

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = True
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = True
#         elif event.type == pygame.KEYUP:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = False
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = False
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             mouse_pos = pygame.mouse.get_pos()
#             if game_state == SCENARIO_SELECTION:
#                 # Check if playground or school is clicked
#                 if playground_rect.collidepoint(mouse_pos):
#                     game_state = NAVIGATION
#                 elif school_rect.collidepoint(mouse_pos):
#                     print("School selected (add code for school navigation if needed)")

#     # Game states
#     if game_state == SCENARIO_SELECTION:
#         screen.blit(background_image, (0, 0))
#         screen.blit(title_text, title_rect)
#         screen.blit(playground_image, playground_rect)
#         screen.blit(playground_text, playground_text_rect)
#         screen.blit(school_image, school_rect)
#         screen.blit(school_text, school_text_rect)

#     elif game_state == NAVIGATION:
#         if moving_right:
#             girl_position[0] += 5  # Move character right
#         if moving_left:
#             girl_position[0] -= 5  # Move character left

#         # Keep character within bounds
#         girl_position[0] = max(0, min(combined_width - girl_image.get_width(), girl_position[0]))

#         # Draw navigation screen
#         screen.blit(navigation_surface, (-girl_position[0] + screen_width // 2, 0))
#         screen.blit(girl_image, (screen_width // 2 - girl_image.get_width() // 2, girl_position[1]))

#     pygame.display.flip()

# pygame.quit()
# sys.exit()


##################################################################################################################



# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Screen settings
# screen_width, screen_height = 1200, 750
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Game')

# # Load images for scenario selection
# background_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\environments\\back1.jpg").convert()
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# playground_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\playG3.jpg").convert_alpha()
# school_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\School1.jpg").convert_alpha()

# # Scale images for scenario selection
# playground_image = pygame.transform.scale(playground_image, (200, 150))
# school_image = pygame.transform.scale(school_image, (200, 150))

# # Set up fonts
# font = pygame.font.Font(None, 48)
# small_font = pygame.font.Font(None, 36)

# # Render text for scenario selection
# title_text = font.render('Select Scenario', True, (255, 69, 0))
# playground_text = small_font.render('Playground', True, (255, 69, 0))
# school_text = small_font.render('School(Locked)', True, (255, 69, 0))

# # Get text and image positions
# title_rect = title_text.get_rect(center=(screen_width // 2, 170))
# playground_rect = playground_image.get_rect(center=(screen_width // 2 - 150, screen_height // 2))
# playground_text_rect = playground_text.get_rect(center=(playground_rect.centerx, playground_rect.bottom + 20))
# school_rect = school_image.get_rect(center=(screen_width // 2 + 150, screen_height // 2))
# school_text_rect = school_text.get_rect(center=(school_rect.centerx, school_rect.bottom + 20))

# # Load navigation images
# house_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\house2.jpg").convert()
# funfair_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\funfair1.jpg").convert()
# girl_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\characters\\girl\\girl1.png").convert_alpha()

# # Scale navigation images
# house_image = pygame.transform.scale(house_image, (screen_width, screen_height))
# funfair_image = pygame.transform.scale(funfair_image, (screen_width, screen_height))
# girl_image = pygame.transform.scale(girl_image, (100, 150))

# # Create a combined navigation surface
# combined_width = screen_width * 2  # Two images side by side
# navigation_surface = pygame.Surface((combined_width, screen_height))
# navigation_surface.blit(house_image, (0, 0))  # Place house image first
# navigation_surface.blit(funfair_image, (screen_width, 0))  # Place funfair image next

# girl_position = [50, screen_height - girl_image.get_height() - 50]  # Starting position for the girl

# # Game state
# SCENARIO_SELECTION = 0
# NAVIGATION = 1
# game_state = SCENARIO_SELECTION

# # Main loop
# running = True
# moving_right = False
# moving_left = False

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = True
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = True
#         elif event.type == pygame.KEYUP:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = False
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = False
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             mouse_pos = pygame.mouse.get_pos()
#             if game_state == SCENARIO_SELECTION:
#                 # Check if playground or school is clicked
#                 if playground_rect.collidepoint(mouse_pos):
#                     game_state = NAVIGATION  # Transition to navigation state
#                     girl_position[0] = 0  # Reset girl position to start of the navigation
#                 elif school_rect.collidepoint(mouse_pos):
#                     print("School selected (add code for school navigation if needed)")

#     # Game states
#     if game_state == SCENARIO_SELECTION:
#         screen.blit(background_image, (0, 0))
#         screen.blit(title_text, title_rect)
#         screen.blit(playground_image, playground_rect)
#         screen.blit(playground_text, playground_text_rect)
#         screen.blit(school_image, school_rect)
#         screen.blit(school_text, school_text_rect)

#     elif game_state == NAVIGATION:
#         if moving_right:
#             girl_position[0] += 5  # Move character right
#         if moving_left:
#             girl_position[0] -= 5  # Move character left

#         # Keep character within bounds
#         girl_position[0] = max(0, min(combined_width - screen_width, girl_position[0]))

#         # Draw navigation screen
#         screen.blit(navigation_surface, (-girl_position[0], 0))  # Adjust surface offset for scrolling
#         screen.blit(girl_image, (screen_width // 2 - girl_image.get_width() // 2, girl_position[1]))

#     pygame.display.flip()

# pygame.quit()
# sys.exit()


####################################################################################################################


# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Screen settings
# screen_width, screen_height = 1200, 750
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Game')

# # Load images for scenario selection
# background_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\environments\\back1.jpg").convert()
# background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# playground_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\playG3.jpg").convert_alpha()
# school_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\School1.jpg").convert_alpha()

# # Scale images for scenario selection
# playground_image = pygame.transform.scale(playground_image, (200, 150))
# school_image = pygame.transform.scale(school_image, (200, 150))

# # Set up fonts
# font = pygame.font.Font(None, 48)
# small_font = pygame.font.Font(None, 36)

# # Render text for scenario selection
# title_text = font.render('Select Scenario', True, (255, 69, 0))
# playground_text = small_font.render('Playground', True, (255, 69, 0))
# school_text = small_font.render('School(Locked)', True, (255, 69, 0))

# # Get text and image positions
# title_rect = title_text.get_rect(center=(screen_width // 2, 170))
# playground_rect = playground_image.get_rect(center=(screen_width // 2 - 150, screen_height // 2))
# playground_text_rect = playground_text.get_rect(center=(playground_rect.centerx, playground_rect.bottom + 20))
# school_rect = school_image.get_rect(center=(screen_width // 2 + 150, screen_height // 2))
# school_text_rect = school_text.get_rect(center=(school_rect.centerx, school_rect.bottom + 20))

# # Load navigation images
# house_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\house2.jpg").convert()
# funfair_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\funfair1.jpg").convert()
# girl_image = pygame.image.load("D:\\Game_Miniproject\\SendToVarsha\\ass\\characters\\girl\\girl1.png").convert_alpha()

# # Scale navigation images
# house_image = pygame.transform.scale(house_image, (screen_width, screen_height))
# funfair_image = pygame.transform.scale(funfair_image, (screen_width, screen_height))
# girl_image = pygame.transform.scale(girl_image, (150, 300))

# # Create a combined navigation surface
# combined_width = screen_width * 2  # Two images side by side
# navigation_surface = pygame.Surface((combined_width, screen_height))
# navigation_surface.blit(house_image, (0, 0))  # Place house image first
# navigation_surface.blit(funfair_image, (screen_width, 0))  # Place funfair image next

# girl_position = [50, screen_height - girl_image.get_height() - 50]  # Starting position for the girl

# # Game state
# SCENARIO_SELECTION = 0
# NAVIGATION = 1
# game_state = SCENARIO_SELECTION

# # Play Game button settings
# play_game_button = pygame.Rect(screen_width + (screen_width // 2) - 100, (screen_height // 2) - 25, 200, 50)
# button_color = (0, 255, 0)  # Green
# button_text = font.render("Play Game", True, (255, 255, 255))  # White text
# button_text_rect = button_text.get_rect(center=play_game_button.center)

# # Main loop
# running = True
# moving_right = False
# moving_left = False

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = True
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = True
#         elif event.type == pygame.KEYUP:
#             if game_state == NAVIGATION:
#                 if event.key == pygame.K_RIGHT:
#                     moving_right = False
#                 elif event.key == pygame.K_LEFT:
#                     moving_left = False
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             mouse_pos = pygame.mouse.get_pos()
#             if game_state == SCENARIO_SELECTION:
#                 # Check if playground or school is clicked
#                 if playground_rect.collidepoint(mouse_pos):
#                     game_state = NAVIGATION
#                     girl_position[0] = 0
#                 elif school_rect.collidepoint(mouse_pos):
#                     print("School selected (add code for school navigation if needed)")
#             elif game_state == NAVIGATION:
#                 # Check if Play Game button is clicked
#                 if play_game_button.collidepoint(mouse_pos) and girl_position[0] >= screen_width:
#                     print("Play Game button clicked!")

#     # Game states
#     if game_state == SCENARIO_SELECTION:
#         screen.blit(background_image, (0, 0))
#         screen.blit(title_text, title_rect)
#         screen.blit(playground_image, playground_rect)
#         screen.blit(playground_text, playground_text_rect)
#         screen.blit(school_image, school_rect)
#         screen.blit(school_text, school_text_rect)

#     elif game_state == NAVIGATION:
#         if moving_right:
#             girl_position[0] += 5
#         if moving_left:
#             girl_position[0] -= 5

#         # Keep character within bounds
#         girl_position[0] = max(0, min(combined_width - screen_width, girl_position[0]))

#         # Draw navigation screen
#         screen.blit(navigation_surface, (-girl_position[0], 0))
#         screen.blit(girl_image, (screen_width // 2 - girl_image.get_width() // 2, girl_position[1]))

#         # Render Play Game button if within the funfair image region
#         if girl_position[0] >= screen_width:
#             pygame.draw.rect(screen, button_color, play_game_button)
#             screen.blit(button_text, button_text_rect)

#     pygame.display.flip()

# pygame.quit()
# sys.exit()


#############################################################################################


import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width, screen_height = 1200, 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game')

# Load images for scenario selection
background_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\environments\\back1.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

playground_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\environments\\playG3.jpg").convert_alpha()
school_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\environments\\School1.jpg").convert_alpha()

# Scale images for scenario selection
playground_image = pygame.transform.scale(playground_image, (200, 150))
school_image = pygame.transform.scale(school_image, (200, 150))

# Set up fonts
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 36)

# Render text for scenario selection
title_text = font.render('Select Scenario', True, (255, 69, 0))
playground_text = small_font.render('Playground', True, (255, 69, 0))
school_text = small_font.render('School(Locked)', True, (255, 69, 0))

# Get text and image positions
title_rect = title_text.get_rect(center=(screen_width // 2, 170))
playground_rect = playground_image.get_rect(center=(screen_width // 2 - 150, screen_height // 2))
playground_text_rect = playground_text.get_rect(center=(playground_rect.centerx, playground_rect.bottom + 20))
school_rect = school_image.get_rect(center=(screen_width // 2 + 150, screen_height // 2))
school_text_rect = school_text.get_rect(center=(school_rect.centerx, school_rect.bottom + 20))

# Load navigation images
house_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\environments\\house2.jpg").convert()
funfair_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\environments\\funfair1.jpg").convert()
girl_image = pygame.image.load("D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\characters\\girl\\girl1.png").convert_alpha()

# Scale navigation images
house_image = pygame.transform.scale(house_image, (screen_width, screen_height))
funfair_image = pygame.transform.scale(funfair_image, (screen_width, screen_height))
girl_image = pygame.transform.scale(girl_image, (150, 300))

# Create a combined navigation surface
combined_width = screen_width * 2  # Two images side by side
navigation_surface = pygame.Surface((combined_width, screen_height))
navigation_surface.blit(house_image, (0, 0))  # Place house image first
navigation_surface.blit(funfair_image, (screen_width, 0))  # Place funfair image next

girl_position = [50, screen_height - girl_image.get_height() - 50]  # Starting position for the girl

# Game state
SCENARIO_SELECTION = 0
NAVIGATION = 1
game_state = SCENARIO_SELECTION

# Play Game button settings (for funfair page)
button_width, button_height = 200, 50
button_color = (173, 216, 230)  # Light blue
button_text_color = (255, 255, 255)  # White
play_game_button = pygame.Rect(screen_width + (screen_width // 2) - button_width // 2, screen_height // 2 - button_height // 2, button_width, button_height)

button_text = font.render("Play Game", True, button_text_color)  # White text
button_text_rect = button_text.get_rect(center=play_game_button.center)

# Main loop
running = True
moving_right = False
moving_left = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == NAVIGATION:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                elif event.key == pygame.K_LEFT:
                    moving_left = True
        elif event.type == pygame.KEYUP:
            if game_state == NAVIGATION:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                elif event.key == pygame.K_LEFT:
                    moving_left = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if game_state == SCENARIO_SELECTION:
                # Check if playground or school is clicked
                if playground_rect.collidepoint(mouse_pos):
                    game_state = NAVIGATION
                    girl_position[0] = 0
                elif school_rect.collidepoint(mouse_pos):
                    print("School selected (add code for school navigation if needed)")
            elif game_state == NAVIGATION:
                # Check if Play Game button is clicked
                if play_game_button.collidepoint(mouse_pos) and girl_position[0] >= screen_width:
                    print("Play Game button clicked!")

    # Game states
    if game_state == SCENARIO_SELECTION:
        screen.blit(background_image, (0, 0))
        screen.blit(title_text, title_rect)
        screen.blit(playground_image, playground_rect)
        screen.blit(playground_text, playground_text_rect)
        screen.blit(school_image, school_rect)
        screen.blit(school_text, school_text_rect)

    elif game_state == NAVIGATION:
        if moving_right:
            girl_position[0] += 5
        if moving_left:
            girl_position[0] -= 5

        # Keep character within bounds
        girl_position[0] = max(0, min(combined_width - screen_width, girl_position[0]))

        # Draw navigation screen
        screen.blit(navigation_surface, (-girl_position[0], 0))
        screen.blit(girl_image, (screen_width // 2 - girl_image.get_width() // 2, girl_position[1]))

        # Render Play Game button if within the funfair image region
        if girl_position[0] >= screen_width:
            pygame.draw.rect(screen, button_color, play_game_button)
            screen.blit(button_text, button_text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
