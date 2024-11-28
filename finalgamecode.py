from ursina import *

def start_safety_game():
    app = Ursina()

    class SafetyGame:
        def __init__(self):
            window.title = "Child Safety Game"
            window.color = color.black

            # Set up the initial screen
            self.background = Entity(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/startPage4.png",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            # Start Game Button
            self.start_button = Button(
                text="Start Game",
                color=color.azure,
                scale=(0.4, 0.15),
                position=(0, 0),
                text_color=color.white,
                on_click=self.show_character_selection
            )

        def show_character_selection(self):
            # Transition to character selection
            self.start_button.disable()
            self.background.disable()

            self.character_selection_bg = Entity(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/startPage4.png",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            # Display text for character selection
            self.character_text = Text(
                "Choose Your Character",
                position=(0, 0.4),
                scale=2,
                color=color.white
            )

            self.boy_button = Button(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/characters/boy/boy2.png",
                scale=(0.3, 0.6),
                position=(-0.4, -0.2),
                color=color.white,
                on_click=lambda: self.show_dressing_screen()
            )

            self.girl_button = Button(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/characters/girl/girl1.png",
                scale=(0.3, 0.6),
                position=(0.4, -0.2),
                color=color.white,
                on_click=lambda: self.show_dressing_screen()
            )

        def show_dressing_screen(self):
            # Disable all character selection elements
            self.character_selection_bg.disable()
            self.boy_button.disable()
            self.girl_button.disable()
            self.character_text.disable()

            # Transition to dressing screen
            self.dressing_bg = Entity(
                parent=camera.ui,
                model='quad',
                texture="D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\environments\\dressup.png",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            # Only display the "Start Game" button
            self.start_game_button = Button(
                text="Start Game",
                color=color.orange,
                scale=(0.25, 0.1),
                position=(0, -0.4),
                text_color=color.white,
                on_click=self.show_scenario_selection
            )

        def show_scenario_selection(self):
            # Disable dressing screen elements
            self.dressing_bg.disable()
            self.start_game_button.disable()

            # Transition to scenario selection
            self.scenario_bg = Entity(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/back1.jpg",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            # Playground button
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

            # School button
            self.school_button = Button(
                parent=camera.ui,
                model='quad',
                texture="Assets/images/environments/School1.jpg",
                scale=(0.4, 0.3),
                position=(0.4, -0.0),
                color=color.white
            )
            self.school_label = Text(
                "School(Locked)",
                position=(0.3, -0.2),
                scale=1.5,
                color=color.black
            )

        def show_navigation_screen(self):
            # Disable scenario selection elements
            self.scenario_bg.disable()
            self.playground_button.disable()
            self.playground_label.disable()
            self.school_button.disable()
            self.school_label.disable()

            # Transition to navigation screen
            self.navigation_bg = Entity(
                parent=camera.ui,
                model='quad',
                texture="D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\environments\\house2.jpg",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            self.navigation_bg = Entity(
                parent=camera.ui,
                model='quad',
                texture="D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\environments\\navi.png",
                scale=(2, 1),
                position=(0, 0, 1)
            )

            # Girl character
            self.girl = Entity(
                parent=camera.ui,
                model='quad',
                texture="D:\\Game_Miniproject\\game and touch selection\\Assets\\images\\characters\\girl\\girl1.png",
                scale=(0.2, 0.5),
                position=(-0.8, -0.2)
            )

            self.speed = 0.03

            def update():
                # Movement for the girl character
                if held_keys['d']:
                    self.girl.x += self.speed
                if held_keys['a']:
                    self.girl.x -= self.speed

            app.update = update

    game = SafetyGame()
    app.run()

start_safety_game()
