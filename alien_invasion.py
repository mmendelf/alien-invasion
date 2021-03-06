from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
import pygame

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)
    bullets = Group()
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        for bullet in bullets: # הורדתי פה את הפונק' copy
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
