from typing import Tuple
import pygame as py
import sys
from Platform import *
from Test_plat import *
from pygame.constants import K_k
from character import *
from BG import background_test
from all_menu.setting_menu import Setting_menu
from main_menu import main_Menu
from all_of_generate import all_generate
from auto_cannon import Auto_cannon
from Stages.first import first
from Stages.second import second
sys.path.append(".")
mainpage_Run = True
setting = False
HEIGHT = 800
WIDTH = 1500

py.init()
cnt = 1
screen = py.display.set_mode((WIDTH, HEIGHT))
background = py.Surface(screen.get_size())
background = background.convert()
times = py.time.Clock()
main_page = main_Menu("start","two","Fantastic","Guide","Setting")
setting_page = Setting_menu()
already_start=False
main_page_buttons = {
    "first_stage":main_page.button_01,
    'second_stage': main_page.button_02,
    'third': main_page.button_03,
    'forth': main_page.button_04,
    'fifth':main_page.button_05
}
options={
    "Firstgame" : False,
    "Secondgame" : False,
    "setting" : False
}
#joystick
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
#timer
image_COUNT = py.USEREVENT + 1
continuous_cnt_COUNT = py.USEREVENT + 3
weapon_generator_COUNT = py.USEREVENT + 4
post = py.USEREVENT + 5
py.time.set_timer(post, 3000)
py.time.set_timer(image_COUNT, 100)
py.time.set_timer(continuous_cnt_COUNT, 1200)
py.time.set_timer(weapon_generator_COUNT, 6000)
#key
pressed = py.key.get_pressed()
#init_functions
def turn_false():
    for key, value  in options.items():
        options[key] = False



while True:
    event_list = py.event.get()
    for event in event_list:
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                mainpage_Run=True
    if mainpage_Run:
        if main_page_buttons['fifth'].press:
            turn_false()
            setting = True
            main_page_buttons['fifth'].press=False
        if main_page_buttons['second_stage'].press:
            turn_false()
            options["Secondgame"] = True
            main_page_buttons['second_stage'].press=False
            mainpage_Run=False
            stage_2 = second()
            stage_2.init_factor()
        if main_page_buttons['first_stage'].press:
            turn_false()
            options["Firstgame"] = True
            main_page_buttons['first_stage'].press=False
            mainpage_Run=False
            stage_1 = first()
            stage_1.init_factor()
        if setting:
            for event in event_list:
                if event.type == py.MOUSEBUTTONDOWN:
                    setting_page.button_back.mousebuttondown()
            if setting_page.button_back.press:
                setting_page.button_back.press = False
                setting = False
            setting_page.draw(event_list)
            background.blit(setting_page.surf, (0, 0))
            screen.blit(background, (0, 0))
            # 1.0 * setting_page.Volume_slider.get_volume() / 100
            #main_sound.set_volume(0)
        elif not setting:
            for event in event_list:
                if event.type == py.MOUSEBUTTONDOWN and mainpage_Run:
                    main_page.button_01.mousebuttondown()
                    main_page.button_02.mousebuttondown()
                    main_page.button_03.mousebuttondown()
                    main_page.button_04.mousebuttondown()
                    main_page.button_05.mousebuttondown()
            main_page.draw()
            background.blit(main_page.surf, (0, 0))
            screen.blit(background, (0, 0))
    elif options["Firstgame"]:
        for event in event_list: 
            if event.type == image_COUNT:
                stage_1.player.image_reload()
            if event.type == continuous_cnt_COUNT :
                stage_1.player.all_cnt_del()
            if event.type == weapon_generator_COUNT and not mainpage_Run:
                stage_1.all_gener.all__generate()
            if event.type == JOYBUTTONDOWN or event.type == JOYBUTTONUP:
                stage_1.player.keyboard_control(event)
            else:
                print(123)
                stage_1.player.keyboard_control(0)
        stage_1.action()
        stage_1.bliting(background)
        screen.blit(background, (0, 0))
    elif options["Secondgame"]:
        for event in event_list: 
            if event.type == image_COUNT :
                stage_2.player.image_reload()
            if event.type == continuous_cnt_COUNT:
                stage_2.player.all_cnt_del()
            if event.type == weapon_generator_COUNT and not mainpage_Run :
                stage_2.all_gener.all__generate()
        stage_2.action()
        stage_2.bliting(background)
        screen.blit(background, (0, 0))
    py.display.update()
    times.tick(40)