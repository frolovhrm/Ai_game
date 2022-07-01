import pygame
import sys
from settings import Settings
from cube import Cube
from bullet import Bullet
from alien import Alien


class Tetris:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # или окно или fullscreen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Tetris')

        self.cube = Cube(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_evens()
            self.cube.update()
            self._update_dullets()

            print(len(self.bullets))
            self._update_aliens()

            self._update_screen()

    def _check_evens(self):
        """Обработка нажатия клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_aliens(self):
        """ Обновляет позиции всех пришельцев во флоте"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.cube.moving_right = True
            print(event)
        elif event.key == pygame.K_LEFT:
            self.cube.moving_left = True
            print(event)
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.cube.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.cube.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_dullets(self):
        """Обновляет позиции снарядов и уничтожает старые"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Проверка попаданияб, при обнаружении удаляем пришельца
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not  self.aliens:
            # Уничтожение существующих снарядов и создание нового флота
            self.bullets.empty()
            self._create_fleet()

    def _update_screen(self):
        """Обновление изображения на экране"""
        self.screen.fill(self.settings.bg_color)
        self.cube.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _create_fleet(self):
        """Создание флота"""
        # Создание первого ряда пришельцев
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_spase_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_spase_x // (2 * alien_width)

        """Определяем количество рядов"""
        cube_heigth = self.cube.rect.height
        available_spase_y = (self.settings.screen_height - (3 * alien_height) - cube_heigth)
        numbers_rows = available_spase_y // (3 * alien_height)

        """ пилим остальные ряды"""
        for row_number in range(numbers_rows):
            for alien_number in range(number_aliens_x):
                self._creat_alien(alien_number, row_number)

    def _creat_alien(self, alien_number, row_number):

        # создание пришельца в размещение в ряду
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 3 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_directions()
                break

    def _change_fleet_directions(self):
        """Опускает весь флот и меняет направление движения"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    te = Tetris()
    te.run_game()
