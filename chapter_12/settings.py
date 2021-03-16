# This class contains the settings for the Alien Invasion Game

class Settings:
    def __init__(self):
        # Screen Settings
        self.screen_width = 600
        self.screen_height = 400
        self.default_bg_color = (230, 230, 230)
        self.blue_bg_color = (135, 206, 250)
        self.white_bg_color = (247, 247, 247)
        self.rocket_bg_color = (255, 255, 255)

        # Ship Settings
        self.ship_speed = 1.5

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
