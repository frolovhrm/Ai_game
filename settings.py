class Settings:
    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.alien_speed = 2  # - 0,6
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # / 1 движение в право / -1 движение в лево

        """Параметры снаряда"""
        self.bullet_speed = 2
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (40, 100, 40)
        self.bullet_allowed = 10

        """ Темп игры"""
        self.speedup_scale = 1.1

        """ Темп роста стоимости пришельца"""
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        self.alien_points = 50  # подсчет очков

        self.fleet_direction = 1  # / 1 движение в право / -1 движение в лево

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
