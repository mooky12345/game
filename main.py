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
from select_role_screen import *
from select_player_number import select_role_number_screen
from stage_select import *
sys.path.append(".")
mainpage_Run = True
setting = False
HEIGHT = 800
WIDTH = 1500

py.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
player_number_screen=select_role_number_screen()
screen = py.display.set_mode((WIDTH, HEIGHT))
background = py.Surface(screen.get_size())
background = background.convert()
times = py.time.Clock()
main_page = main_Menu("start","two","Fantastic","Guide","Setting")
setting_page = Setting_menu()
already_start=False
main_page_buttons = {
    "start":main_page.button_01,
    'second_stage': main_page.button_02,
    'third': main_page.button_03,
    'forth': main_page.button_04,
    'setting':main_page.button_05
}
options={
    "start" : False,
    "Firstgame" : False,
    "Secondgame" : False,
    "Thirdgame" : False,
    "setting" : False
}
player_option={
    "One": 1,
    "Two": 2,
    "Three": 3
}
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
select_number_player=True
player=0
stage_list = [False,False,False]
player_name_list=[]
select_role=True
trans_to_vs=False
vs_animation=False
select_stage = True        
stage_1 = None
stage_2 = None
pressed = py.key.get_pressed()
dy=0
#init_functions
def turn_false():
    for key, value  in options.items():
        options[key] = False
test = role_screen()
stage_selection = stage_select()
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
        if main_page_buttons['start'].press:
            turn_false()
            options["start"] = True
    
            main_page_buttons['start'].press=False
            mainpage_Run = False
        if main_page_buttons['setting'].press:
            turn_false()
            setting = True
            mainpage_Run = False
            main_page_buttons['setting'].press=False
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
            # # 1.0 * setting_page.Volume_slider.get_volume() / 100
            # #main_sound.set_volume(0)
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
    elif options["start"]:
        if select_number_player:
            background.blit(player_number_screen.surf,(0,0))
            player_number_screen.update()
            for event in event_list:
                    if event.type == py.MOUSEBUTTONDOWN:
                        for button in player_number_screen.buttons:
                            button.mousebuttondown()
            for button in player_number_screen.buttons:
                if button.press:
                    player_cnt=player_option[button.txt]
                    select_number_player=False
            screen.blit(background, (0, 0))
                
        elif select_role:
            if player!=player_cnt:
                test.update()
                background.blit(test.surf,(0,0))
                screen.blit(background, (0, 0))
                for event in event_list:
                    if event.type == py.MOUSEBUTTONDOWN:
                        for i in test.all_player:
                            i.mouse_press()
                for i in test.all_player:
                    if i.press and not (i in player_name_list):
                        player+=1
                        player_name_list.append(i)
                        i.press=False
            else:
                select_role=False
                trans_to_vs=True
        elif trans_to_vs: 
            background.fill((0,0,0))
            background.blit(test.surf,(0,-dy))
            screen.blit(background, (0, 0))
            dy+=12
            if dy>=Height:
                trans_to_vs=False
                vs_animation=True
        elif vs_animation:
            background.fill((0,0,0))
            test.select_complete_animation(player_name_list[0],player_name_list[1])
            for i in player_name_list:
                i.change_size(2,3)
            background.blit(test.surf,(0,0))
            screen.blit(background, (0, 0))
            test.dx+=5
            if test.dx>Width/2-400:
                py.time.delay(500)
                vs_animation=False
        elif select_stage:
            background.fill((255,255,255))
            stage_selection.update(event_list,background,stage_list)
            screen.blit(background, (0, 0))
            for num in range(3):
                if stage_list[num] == True:
                    select_stage = False
                    if num == 0:
                        stage_1 = first(player_cnt,player_name_list)
                        stage_1.init_factor()
                        options["Firstgame"] = True
                    if num == 1:
                        stage_2 = second(player_cnt,player_name_list)
                        stage_2.init_factor()
                        options["Secondgame"] = True
                    if num == 2:
                        options["Thirdgame"] = True
        elif options["Firstgame"]:
            stage_1.getjoystick_event(0)
            for event in event_list: 
                if event.type == image_COUNT:
                    for Player in stage_1.player_own_play_list:
                        Player.image_reload()
                if event.type == continuous_cnt_COUNT:
                    for Player in stage_1.player_own_play_list:
                        Player.all_cnt_del()
                if event.type == weapon_generator_COUNT and not mainpage_Run:
                    stage_1.all_gener.all__generate() 
                if event.type == JOYBUTTONDOWN or event.type == JOYBUTTONUP or  event.type == JOYHATMOTION:
                    stage_1.getjoystick_event(event)
            stage_1.action()
            stage_1.bliting(background)
            screen.blit(background, (0, 0))
        elif options["Secondgame"]:
            for event in event_list: 
                if event.type == image_COUNT :
                    stage_2.player_1.image_reload()
                if event.type == continuous_cnt_COUNT:
                    stage_2.player_1.all_cnt_del()
                if event.type == weapon_generator_COUNT and not mainpage_Run :
                    stage_2.all_gener.all__generate() 
            stage_2.action()
            stage_2.bliting(background)
            screen.blit(background, (0, 0))
        elif options["Thirdgame"]:
            pass
    py.display.update()
    times.tick(40)