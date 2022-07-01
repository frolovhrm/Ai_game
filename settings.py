class Settings:
    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.cobe_speed = 1.5
        self.alien_speed = 0.4
        self.fleet_drop_speed = 10
        self.fleet_direction = 1                # / 1 движение в право / -1 движение в лево


        """Параметры снаряда"""
        self.bullet_speed = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3


