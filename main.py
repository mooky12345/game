from typing import Tuple
import pygame as py
import sys
from Platform import *
from Test_plat import *
from pygame.constants import K_k
from character import *
from attack import *
from BG import background_test
from all_menu.setting_menu import Setting_menu
from main_menu import main_Menu
from all_of_generate import all_generate
from blood import bloodline
from auto_cannon import Auto_cannon
sys.path.append(".")
mainpage_Run = True
setting = False
HEIGHT = 800
WIDTH = 1500

py.init()
py.mixer.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
background = py.Surface(screen.get_size())
background = background.convert()
times = py.time.Clock()

post = py.USEREVENT + 5
py.time.set_timer(post, 3000)
# main_sound=py.mixer.Sound("music/123.wav")
# effect = py.mixer.Sound("music/123.mp3")
# effect.play()
# main_sound.play(-1)
main_page = main_Menu("start","two","Fantastic","Guide","Setting")
setting_page = Setting_menu()
already_start=False
main_page_buttons = {
    "first":main_page.button_01,
    'second': main_page.button_02,
    'third': main_page.button_03,
    'forth': main_page.button_04,
    'fifth':main_page.button_05
}
playing=False
Firstgame=False
Secondgame=False
options=[Firstgame,Secondgame,setting]
def turn_false(options):
    for game in options:
        game = False






while True:
    event_list = py.event.get()
    keys=py.key.get_pressed()
    for event in event_list:
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                mainpage_Run=True
                # if already_start:
                #     main_page.change_text("first", "back ")
        if event.type == post:
             x, y = py.mouse.get_pos()
             print("滑鼠位置[" + str(x) + "," + str(y) + "]")
    if mainpage_Run:
        if main_page_buttons['fifth'].press:
            turn_false(options)
            setting = True
            main_page_buttons['fifth'].press=False
        if main_page_buttons['first'].press:
            turn_false(options)
            Firstgame = True
            main_page_buttons['first'].press=False
            mainpage_Run=False


            ########################### init first game ##################################################1
            generator = [0] * 5
            image_COUNT = py.USEREVENT + 1
            mice_COUNT = py.USEREVENT + 2
            continuous_cnt_COUNT = py.USEREVENT + 3
            weapon_generator_COUNT = py.USEREVENT + 4
            py.time.set_timer(image_COUNT, 100)
            py.time.set_timer(continuous_cnt_COUNT, 1200)
            py.time.set_timer(weapon_generator_COUNT, 10000)

            pressed = py.key.get_pressed()

            player_1 = Character("cats", 150, 150, "character1/L-walk1.png")
            main_Platform_1 = platform(1200, 20, 255, 0, 0, 50, 150, 700)
            float_plat_1 = platform(100, 30, 255, 0, 0, 50, 300, 650)
            float_plat_2 = platform(100, 30, 255, 0, 0, 50, 450, 600)
            float_plat_3 = platform(100, 30, 255, 0, 0, 50, 600, 650)
            attack_character_1 = attack()
            bg = background_test()
            test=test_plat(100, 30, 255, 0, 0, 50, x=900, y=700,cnt=150,v=6,dir=2)
            test2=test_plat(30, 150, 255, 0, 0, 50, x=900, y=700,cnt=150,v=6,dir=1)
            cannon = Auto_cannon(100)
            all_gener = all_generate()
            all_gener.declear()

            

            #grouping
            move_plat=py.sprite.Group()
            can_go_down = py.sprite.Group()
            all_sprites_Group = py.sprite.Group()
            hitbox_group = py.sprite.Group()
            platforms_group = py.sprite.Group()
            weapon_group = py.sprite.Group()
            charater_group = py.sprite.Group()
            bullet_group = py.sprite.Group()
            charater_group.add(player_1)


            move_plat.add(test)
            move_plat.add(test2)

            can_go_down.add(float_plat_1)
            can_go_down.add(float_plat_2)


            platforms_group.add(main_Platform_1)
            platforms_group.add(float_plat_1)
            platforms_group.add(float_plat_2)
            platforms_group.add(float_plat_3)
            platforms_group.add(test)
            platforms_group.add(test2)

            hitbox_group.add(player_1)
            hitbox_group.add(attack_character_1)

            all_sprites_Group.add(bg)
            all_sprites_Group.add(player_1)
            all_sprites_Group.add(float_plat_1)
            all_sprites_Group.add(main_Platform_1)
            all_sprites_Group.add(float_plat_2)
            ################### #############################################################################1


        if main_page_buttons['second'].press:
            turn_false(options)
            Secondgame = True
            main_page_buttons['second'].press=False
            mainpage_Run=False

            ########################### init second game ##################################################2
            generator = [0] * 5
            image_COUNT = py.USEREVENT + 1
            mice_COUNT = py.USEREVENT + 2
            continuous_cnt_COUNT = py.USEREVENT + 3
            weapon_generator_COUNT = py.USEREVENT + 4
            post = py.USEREVENT + 5
            py.time.set_timer(image_COUNT, 100)
            py.time.set_timer(continuous_cnt_COUNT, 1200)
            py.time.set_timer(weapon_generator_COUNT, 10000)
            py.time.set_timer(post, 3000)

            pressed = py.key.get_pressed()


            player_1 = Character("cats", 150, 150, "character1/L-walk1.png")
            main_Platform_1 = platform(554, 20, 255, 0, 0, 50, 0, 266+20)
            float_plat_1 = platform(100, 30, 255, 0, 0, 50, 300, 650)
            float_plat_2 = platform(100, 30, 255, 0, 0, 50, 450, 600)
            float_plat_3 = platform(100, 30, 255, 0, 0, 50, 600, 650)
            attack_character_1 = attack()
            bg = background_test(image="background/2.jpg")
            test=test_plat(100, 30, 255, 0, 0, 50, x=900, y=700,cnt=150,v=6,dir=2)
            test2=test_plat(30, 150, 255, 0, 0, 50, x=900, y=700,cnt=150,v=6,dir=1)

            all_gener = all_generate()
            all_gener.declear()

            bloodline_1=bloodline()

            #grouping
            move_plat=py.sprite.Group()
            can_go_down = py.sprite.Group()
            all_sprites_Group = py.sprite.Group()
            hitbox_group = py.sprite.Group()
            platforms_group = py.sprite.Group()
            weapon_group = py.sprite.Group()
            charater_group = py.sprite.Group()
            bullet_group = py.sprite.Group()
            charater_group.add(player_1)


            move_plat.add(test)
            move_plat.add(test2)

            can_go_down.add(float_plat_1)
            can_go_down.add(float_plat_2)


            platforms_group.add(main_Platform_1)
            platforms_group.add(float_plat_1)
            platforms_group.add(float_plat_2)
            platforms_group.add(float_plat_3)
            platforms_group.add(test)
            platforms_group.add(test2)

            hitbox_group.add(player_1)
            hitbox_group.add(attack_character_1)

            all_sprites_Group.add(bg)
            all_sprites_Group.add(player_1)
            all_sprites_Group.add(float_plat_1)
            all_sprites_Group.add(main_Platform_1)
            all_sprites_Group.add(float_plat_2)
            ################### #############################################################################2
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
        if not setting :
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

        py.display.update()
        times.tick(40)

         ############# run First Game
    elif Firstgame:
        for event in event_list: 
            if event.type == image_COUNT :
                player_1.image_reload()
            if event.type == continuous_cnt_COUNT :
                player_1.all_cnt_del()
            if event.type == weapon_generator_COUNT and not mainpage_Run :
                all_gener.all__generate() 
        
        bullet_group.update(player_1,bullet_group)
        bullet_group.draw(screen)
        already_start=True
        if pressed[py.K_ESCAPE]:
            main_page.button_01.press=False
            mainpage_Run=True
        # py.mixer.Sound.play(main_sound)
        all_gener.detect_hits(player_1)
       
        player_1.key_board_get()

        background.fill((0, 0, 0))
        player_1.blood.update()
        move_x, move_y = player_1.move_position()
        py.display.update()
        
        player_1.movement(main_Platform_1, platforms_group, can_go_down,bullet_group)
        out=player_1.pos_update(platforms_group)

        background.blit(bg.surf, bg.rect)
        cannon.aim_target_rotating(player_1.pos,background)
        cannon.shooting(bullet_group,player_1.pos)
        
        
        for entity in all_gener.generator:
             background.blit(entity.surf, entity.rect)
        for entity in move_plat:
            entity.plat_redraw(move_x,move_y,entity.x/2,entity.y)
        for entity in move_plat:
            background.blit(entity.image, entity.rect)

        background.blit(player_1.shield_image.image,player_1.shield_image.rect)
        background.blit(player_1.blood.surf, (0,0))
        background.blit(main_Platform_1.image,main_Platform_1.rect)
        background.blit(float_plat_1.image,float_plat_1.rect)
        background.blit(float_plat_2.image,float_plat_2.rect)
        background.blit(float_plat_3.image,float_plat_3.rect)
        background.blit(player_1.surf,player_1.rect)
       
        screen.blit(background, (0, 0))
        times.tick(40)

        ############# run Second Game
    elif Secondgame:       
        for event in event_list: 
            if event.type == image_COUNT :
                player_1.image_reload()
            if event.type == continuous_cnt_COUNT :
                player_1.all_cnt_del()
            if event.type == weapon_generator_COUNT and not mainpage_Run :
                all_gener.all__generate() 
        bullet_group.update(player_1,bullet_group)
        bullet_group.draw(screen)
        already_start=True
   
        if pressed[py.K_ESCAPE]:
            main_page.button_01.press=False
            mainpage_Run=True
        # py.mixer.Sound.play(main_sound)
        all_gener.detect_hits(player_1)
       
        player_1.key_board_get()

        background.fill((0, 0, 0))
     
        move_x, move_y = player_1.move_position()
        py.display.update()
        
        player_1.movement(main_Platform_1, platforms_group, can_go_down,bullet_group)
        out=player_1.pos_update(platforms_group)
        bloodline_1.update()

        bloodline_1.cut_blood(20, out)
        background.blit(bg.surf, bg.rect)
        for entity in all_gener.generator:
            background.blit(entity.surf, entity.rect)
        for entity in move_plat:
            entity.plat_redraw(move_x,move_y,entity.x/2,entity.y)
        for entity in move_plat:
            background.blit(entity.image, entity.rect)

        background.blit(player_1.shield_image.image,player_1.shield_image.rect)
        background.blit(bloodline_1.surf, (0,0))
        background.blit(main_Platform_1.image,main_Platform_1.rect)
        background.blit(float_plat_1.image,float_plat_1.rect)
        background.blit(float_plat_2.image,float_plat_2.rect)
        background.blit(float_plat_3.image,float_plat_3.rect)
        background.blit(player_1.surf,player_1.rect)
        background.blit(bloodline_1.surf, (0,0))
       
        screen.blit(background, (0, 0))
        times.tick(40)