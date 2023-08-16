# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:07:03 2023

@author: 1
"""

import pygame
import time
from ship_control import *
import math
import numpy as np
    
# Colors
WHITE = (255, 255, 255)
GRAY  = (170, 170, 170)
BLACK = (0, 0, 0)
      
# Initialize
pygame.init()
# GUI frame (width, height)
GUI_X, GUI_Y = 1920, 1080
window = pygame.display.set_mode((GUI_X, GUI_Y))
# GUI caption
pygame.display.set_caption('Untitled Game')
# Press Play font 
pressplay_font = pygame.font.SysFont('chalkduster.ttf', 30)
# Press Play text idle mouse
pressplay_text_idle = pressplay_font.render('Start Game', True, WHITE)
# Press Play text hovering mouse
pressplay_text_hover = pressplay_font.render('Start Game', True, GRAY)
# Game Name text
gametitle_text = pressplay_font.render('Pocket Squadrons', True, WHITE)
# Press Play text pos (center?)
pressplay_X, pressplay_Y = GUI_X/2.1, GUI_Y/2.5
# Image
img = pygame.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\Main_Background.png")

# Main Menu loop
flag = True
while flag:
    # Get mouse pos
    mouse = pygame.mouse.get_pos()
    # Main Menu Background
    window.blit(img, (150,100))
    window.blit(gametitle_text, (pressplay_X-30, pressplay_Y-50))
    # Press Play text displayed
    window.blit(pressplay_text_idle, (pressplay_X, pressplay_Y))
    for event in pygame.event.get():
        # Check for clicking 'X' to quit
        if event.type == pygame.QUIT:
            # Quit Pygame
            pygame.quit()
    # Check if mouse in Press Play's pos
    if pressplay_X <= mouse[0] <= pressplay_X + 100 and pressplay_Y <= mouse[1] <= pressplay_Y+20:
        # Turn Press Play gray
        window.blit(pressplay_text_hover, (pressplay_X, pressplay_Y))
        # If mouse down too then hids press play
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = False
    # Updates GUI
    pygame.display.update()

def buildaship():
    choose_ship_font = pygame.font.SysFont('chalkduster.ttf', 40)
    ainfo = ['SHIP: A-WING INTERCEPTER','SPEED: 210','HULL: 750','SHIELDS: 500','ACCELERATION: 246']
    xinfo = ['SHIP: X-WING FIGHTER','SPEED: 145','HULL: 1200','SHIELDS: 800','ACCELERATION: 160']
    img2 = pygame.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\Hanger (1).png")
    pygame.display.update()
    window.blit(img2, (150,100))

    # Pick Ship Loop
    flag = True
    while flag:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Check for clicking 'X'
            if event.type == pygame.QUIT:
                # Quit Pygame
                pygame.quit()
        # If clikcing X-Wing
        if 1066 <= mouse[0] <= 1517 and 569 <= mouse[1] <= 885 and event.type == pygame.MOUSEBUTTONDOWN:
            # Open X-Wing Hanger
            xhang = pygame.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\XHanger.png")
            window.blit(xhang, (150,100))
            # Prints X-Wing Stats
            for i in range(len(xinfo)):
                f = choose_ship_font.render(xinfo[i], True, BLACK)
                j = 150+(i*30)
                window.blit(f, (844, j))
            shipid = 'X_Wing'
            break

        # If clicking A-Wing
        if 532 <= mouse[0] <= 856 and 421 <= mouse[1] <= 760 and event.type == pygame.MOUSEBUTTONDOWN:
            # Open X-Wing Hanger
            ahang = pygame.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\A-Wing Hanger.png")
            window.blit(ahang, (150,100))
            # Print A-Wing stats
            for i in range(len(ainfo)):
                f = choose_ship_font.render(ainfo[i], True, BLACK)
                j = 150+(i*30)
                window.blit(f, (844, j))
            shipid = 'A_Wing'
            break
        pygame.display.update()
    pygame.display.update()
    primary_weapon, hull, shield, engine = 'NONE SELECTED',0,0,0
    flag = True
    while flag:
        select_color = (0, 100, 255)
        unselect_color = (61, 73, 89)
        for event in pygame.event.get():
            # Check for clicking 'X'
            if event.type == pygame.QUIT:
                # Quit Pygame
                pygame.quit()
                
        ## Primary Weapon Select       
        def deselect_pri_weap():
            rect = (333,517),(44,43)
            pygame.draw.rect(window, unselect_color, (rect), 3)  # width = 3
            rect = (263,517),(43,43)
            pygame.draw.rect(window, unselect_color, (rect), 3)  # width = 3  
        # If Standard Laser Cannon Clicked
        mouse = pygame.mouse.get_pos()
        #print(mouse)
        if 263 <= mouse[0] <= 303 and 517 <= mouse[1] <= 558 and event.type == pygame.MOUSEBUTTONDOWN:
            deselect_pri_weap()
            # selects standard
            rect = (263,517),(43,43)
            pygame.draw.rect(window, select_color, (rect), 3)  # width = 3
            primary_weapon = 'STANDARD LASER CANNON'
        # If Burst Laser Cannon Clicked
        mouse = pygame.mouse.get_pos()
        if 333 <= mouse[0] <= 373 and 517 <= mouse[1] <= 558 and event.type == pygame.MOUSEBUTTONDOWN:
            deselect_pri_weap()
            # selects burst
            rect = (333,517),(44,43)
            pygame.draw.rect(window, select_color, (rect), 3)  # width = 3
            primary_weapon = 'BURST LASER CANNON'
        
        ## Hull Select
        def deselect_hull():
            rect = (263,620),(44,43)
            pygame.draw.rect(window, unselect_color, (rect), 3)  # width = 3
            rect = (335,620),(44,43)
            pygame.draw.rect(window, unselect_color, (rect), 3)  # width = 3
            rect = (406,620),(44,43)
            pygame.draw.rect(window, unselect_color, (rect), 3)  # width = 3
        # If Standard Hull Clicked    
        if 263 <= mouse[0] <= 303 and 620 <= mouse[1] <= 662 and event.type == pygame.MOUSEBUTTONDOWN:
            deselect_hull()
            # Selects standard
            rect = (263,620),(44,43)
            pygame.draw.rect(window, select_color, (rect), 3)  # width = 3
            hull = 'standard'
        # If Lightweight Hull Clicked    
        if 335 <= mouse[0] <= 377 and 620 <= mouse[1] <= 663 and event.type == pygame.MOUSEBUTTONDOWN:
            deselect_hull()
            # selects lightweigh
            rect = (335,620),(44,43)
            pygame.draw.rect(window, select_color, (rect), 3)  # width = 3
            hull = 'lightweight'
        # If Reinforced Hull Clicked    
        if 406 <= mouse[0] <= 450 and 620 <= mouse[1] <= 662 and event.type == pygame.MOUSEBUTTONDOWN:
            deselect_hull()
            # selects reinforced
            rect = (406,620),(44,43)
            pygame.draw.rect(window, select_color, (rect), 3)  # width = 3
            hull = 'reinforced'
        
        ## Shield Select
        def deselect_shield():
            rect = (263,732),(44,43)
            pygame.draw.rect(window, unselect_color, (rect), 3)  # width = 3
            rect = (335,732),(44,43)
            pygame.draw.rect(window, unselect_color, (rect), 3)  # width = 3
        # if standard selected
        if 263 <= mouse[0] <= 306 and 732 <= mouse[1] <= 773 and event.type == pygame.MOUSEBUTTONDOWN:
            deselect_shield()
            # Selects standard
            rect = (263,732),(44,43)
            pygame.draw.rect(window, select_color, (rect), 3)  # width = 3
            shield = 'standard'
        # If Reinforced Shield Clicked    
        if 335 <= mouse[0] <= 377 and 732 <= mouse[1] <= 774 and event.type == pygame.MOUSEBUTTONDOWN:
            deselect_shield()
            # selects reinforced
            rect = (335,732),(44,43)
            pygame.draw.rect(window, select_color, (rect), 3)  # width = 3
            shield = 'reinforced'
        
        ## Engine Select
        def deselect_engine():
            rect = (263,833),(44,43)
            pygame.draw.rect(window, unselect_color, (rect), 3)  # width = 3
            rect = (335,833),(44,43)
            pygame.draw.rect(window, unselect_color, (rect), 3)  # width = 3    
        # if standard selected
        if 263 <= mouse[0] <= 306 and 833 <= mouse[1] <= 877 and event.type == pygame.MOUSEBUTTONDOWN:
            deselect_engine()
            # selects standard
            rect = (263,833),(44,43)
            pygame.draw.rect(window, select_color, (rect), 3)  # width = 3
            engine = 'standard'
        # if experimental selected
        if 335 <= mouse[0] <= 377 and 833 <= mouse[1] <= 877 and event.type == pygame.MOUSEBUTTONDOWN:
            deselect_engine()
            # selects experimental
            rect = (335,833),(44,43)
            pygame.draw.rect(window, select_color, (rect), 3)  # width = 3
            engine = 'experimental'
            
        ## Check for Continue
        if 1467 <= mouse[0] <= 1719 and 125 <= mouse[1] <= 193 and event.type == pygame.MOUSEBUTTONDOWN:
            flag = False
        pygame.display.update()

    ## Calc X-Wing Stats
    # custom stats
    hull_stats = {0:0,'standard':500,'lightweight':250,'reinforced':1000}
    shield_stats = {0:0,'standard':200,'reinforced':400}
    engine_stats = {0:0,'standard':150,'experimental':300}
    class X_Wing(object):
        ship_type = 'X-Wing'
        # base stats
        base_hull = 1200
        base_shield = 800   
        base_speed = 145
        base_accel = 160
        def __init__(self, primary_weapon, hull, shield, engine):
            self.engine = engine
            self.shield_type = shield
            self.primary_weapon, self.hull, self.shield, self.engine = primary_weapon, hull, shield, engine
            # current stats
            self.hull = X_Wing.base_hull + hull_stats[hull]
            self.shield = X_Wing.base_shield + shield_stats[shield]
            self.speed = X_Wing.base_speed + engine_stats[engine]
            self.accel = X_Wing.base_accel + engine_stats[engine]
            self.speed -= ((hull_stats[hull]//250)*50)
            self.accel -= ((hull_stats[hull]//250)*50)
        def display_stats(self,x):
            self.speedcalc = engine_stats[engine]-((hull_stats[hull]/10))
            self.accelcalc = engine_stats[engine]-((hull_stats[hull]/10))
            xinfo = ['PRIMARY WEAPON: ','HULL: '+str(self.base_hull)+' + '+str(hull_stats[hull]),'SHIELD: '+str(self.base_shield)+' + '+str(shield_stats[shield]), 'SPEED: '+str(self.base_speed)+' + '+str(self.speedcalc),'ACCELERATION: '+str(self.base_accel)+' + '+str(self.accelcalc)]
            for i in range(len(xinfo)):
                txt = choose_ship_font.render(xinfo[i], True, BLACK)
                y = 420+(110*i)
                window.blit(txt, (210+x,y))
            txt = choose_ship_font.render(str(self.primary_weapon), True, BLACK)
            window.blit(txt, (210+x,445))
            
    class A_Wing(object):
        ship_type = 'A-Wing'
        # base stats
        base_hull = 750
        base_shield = 500
        base_speed = 210
        base_accel = 246
        def __init__(self, primary_weapon, hull, shield, engine):
            self.engine = engine
            self.shield_type = shield
            self.primary_weapon, self.hull, self.shield, self.engine = primary_weapon, hull, shield, engine
            # current stats
            self.hull = A_Wing.base_hull + hull_stats[hull]
            self.shield = A_Wing.base_shield + shield_stats[shield]
            self.speed = A_Wing.base_speed + engine_stats[engine]
            self.accel = A_Wing.base_accel + engine_stats[engine]
            self.speed -= ((hull_stats[hull]//250)*50)
            self.accel -= ((hull_stats[hull]//250)*50)
        def display_stats(self,x):
            self.speedcalc = engine_stats[engine]-(hull_stats[hull]/10)
            self.accelcalc = engine_stats[engine]-(hull_stats[hull]/10)
            ainfo = ['PRIMARY WEAPON: ','HULL: '+str(self.base_hull)+' + '+str(hull_stats[hull]),'SHIELD: '+str(self.base_shield)+' + '+str(shield_stats[shield]), 'SPEED: '+str(self.base_speed)+' + '+str(self.speedcalc),'ACCELERATION: '+str(self.base_accel)+' + '+str(self.accelcalc)]
            for i in range(len(ainfo)):
                txt = choose_ship_font.render(ainfo[i], True, BLACK)
                y = 420+(110*i)
                window.blit(txt, (210+x,y))
            txt = choose_ship_font.render(str(self.primary_weapon), True, BLACK)
            window.blit(txt, (210+x,445))

    # Creates Player 1's ship based on ship ID
    if shipid == 'X_Wing':
        player1ship = X_Wing(primary_weapon, hull, shield, engine)
        return(player1ship)
    if shipid == 'A_Wing':
        player1ship = A_Wing(primary_weapon, hull, shield, engine) 
        return(player1ship)

player1ship = buildaship()
player2ship = buildaship()

xleftstat = pygame.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\Stats X-Wing Left.png")
xrightstat = pygame.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\Stats X-Wing Right.png")
aleftstat = pygame.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\Stats A-Wing Left.png")
arightstat = pygame.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\Stats A-Wing Right.png")
window.fill((0,0,0))
pygame.display.flip()
pygame.display.update()
if player2ship.ship_type == 'A-Wing':
    window.blit(arightstat, (870,0))
    player2ship.display_stats(x=835)
if player2ship.ship_type == 'X-Wing':
    window.blit(xrightstat, (870,0))
    player2ship.display_stats(x=835)
if player1ship.ship_type == 'A-Wing':
    window.blit(aleftstat, (100,0))
    player1ship.display_stats(x=0)
if player1ship.ship_type == 'X-Wing':
    window.blit(xleftstat, (100,0))
    player1ship.display_stats(x=0)

# load p1 sprite
x_move, y_move = GUI_X//2, 200
angle = 180
angle_speed = player1ship.accel/400
move_speed = player1ship.speed/400
if player1ship.ship_type == 'X-Wing':
    sprite = pg.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\X-Wing Mini.png")
if player1ship.ship_type == 'A-Wing':
    sprite = pg.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\A-Wing Mini.png")

# load p2 sprite
x_move2, y_move2 = GUI_X//2,850
angle2 = 0
angle_speed2 = player2ship.accel/400 
move_speed2 = player2ship.speed/400
if player2ship.ship_type == 'X-Wing':
    sprite2 = pg.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\X-Wing Mini.png")
if player2ship.ship_type == 'A-Wing':
    sprite2 = pg.image.load(r"C:\Users\1\OneDrive\Desktop\Python Stuff\Pocket Squadrons\A-Wing Mini.png")
def projectile(window, x, y):
    pygame.draw.circle(window, (255, 0, 0), (x,y), 3)
def projectile2(window, x, y):
    pygame.draw.circle(window, (50, 205, 50), (x,y), 3)
    
# bullet[x,y,sin,cos,time]
bullets = []
bullets2 = []
start_bullets = False
start_bullets2 = False
hull_damage = 0
hull_damage2 = 0
shield_damage = 0
shield_damage2 = 0
shield_recharge = 1
shield_recharge2 = 1
if player1ship.shield_type == 'reinforced':
    shield_recharge = 2
if player2ship.shield_type == 'reinforced':
    shield_recharge2 = 2
    
while True:
    window.fill((BLACK))
    # Player 1
    keys = pg.key.get_pressed()
    if keys[pg.K_a]: #works
        x_move -= move_speed
        if 0 <= angle < 90 or 270 < angle <= 360:
            angle += angle_speed
        if 90 < angle <= 270:
            angle -= angle_speed
        if 88 < angle < 92:
            x_move -= move_speed
    if keys[pg.K_d]: # works
        x_move += move_speed
        if 90 < angle < 270:
            angle += angle_speed
        if 270 < angle <= 360 or 90 > angle >= 0:
            angle -= angle_speed
        if 268 < angle < 272:
            x_move += move_speed
    if keys[pg.K_w]: #works
        y_move -= move_speed
        if 0 < angle < 180:
            angle -= angle_speed
        if 180 < angle <= 359.9:
            angle += angle_speed
        if 0 < angle < 2 or 358 < angle < 362:
            y_move -= move_speed
    if keys[pg.K_s]:    
        y_move += move_speed
        if 180 > angle >= 0:
            angle += angle_speed
        if 180 < angle <= 360:
            angle -= angle_speed
        if 178 < angle < 182:
            y_move += move_speed 
    while angle > 360:
        angle -=360
    while angle < 0:
        angle +=360
    rotated_sprite = pg.transform.rotate(sprite,angle)
    sprite_rect = sprite.get_rect(center=(x_move, y_move))
    rotated_sprite_rect = rotated_sprite.get_rect(center=sprite_rect.center)
    window.blit(rotated_sprite, rotated_sprite_rect)
    check_quit()
    
    # Player 2
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]: #works
        x_move2 -= move_speed2
        if 0 <= angle2 < 90 or 270 < angle2 <= 360:
            angle2 += angle_speed2
        if 90 < angle2 <= 270:
            angle2 -= angle_speed2
        if 88 < angle2 < 92:
            x_move2 -= move_speed2
    if keys[pg.K_RIGHT]: # works
        x_move2 += move_speed2
        if 90 < angle2 < 270:
            angle2 += angle_speed2
        if 270 < angle2 <= 360 or 90 > angle2 >= 0:
            angle2 -= angle_speed2
        if 268 < angle2 < 272:
            x_move2 += move_speed2
    if keys[pg.K_UP]: #works
        y_move2 -= move_speed2
        if 0 < angle2 < 180:
            angle2 -= angle_speed2
        if 180 < angle2 <= 359.9:
            angle2 += angle_speed2
        if 0 < angle2 < 2 or 358 < angle2 < 362:
            y_move2 -= move_speed2
    if keys[pg.K_DOWN]:
        y_move2 += move_speed2
        if 180 > angle2 >= 0:
            angle2 += angle_speed2
        if 180 < angle2 <= 360:
            angle2 -= move_speed2
        if 178 < angle2 < 182:
            y_move2 += move_speed2
    while angle2 > 360:
        angle2 -=360
    while angle2 < 0:
        angle2 +=360
    rotated_sprite2 = pg.transform.rotate(sprite2,angle2)
    sprite_rect2 = sprite2.get_rect(center=(x_move2, y_move2))
    rotated_sprite_rect2 = rotated_sprite2.get_rect(center=sprite_rect2.center)
    window.blit(rotated_sprite2, rotated_sprite_rect2)
    
    # bullets for p1
    if keys[pg.K_q] and len(bullets) < 250:
        radians = math.radians(angle)
        sin = math.sin(radians)
        cos = math.cos(radians)
        #print(sin,cos)
        bullets.append([x_move,y_move,sin,cos])
        # test for triple shot
        if player1ship.primary_weapon == 'BURST LASER CANNON':
            bullets.append([x_move-(20*cos),y_move-(20*sin),.5*sin,2*cos])
            bullets.append([x_move+(20*cos),y_move+(20*sin),2*sin,.5*cos])
        start_bullets = True
    if start_bullets == True:
        for bullet in bullets:
            bullet[0] -= bullet[2]
            bullet[1] -= bullet[3]
            projectile(window,bullet[0],bullet[1])
            if bullet[0] > 1900 or bullet[1] > 1000 or bullet[0] < 0 or bullet[1] <  0:
                bullets.remove(bullet)
            # shield damage on p2
            if x_move2-30 < bullet[0] < x_move2+30 and y_move2-30 < bullet[1] < y_move2+30:
                shield_damage2 += .1 
            # hull damage on p2
            if x_move2-20 < bullet[0] < x_move2+20 and y_move2-20 < bullet[1] < y_move2+20 and player2ship.shield - shield_damage2 < 0:
                hull_damage2 += .1
                if player1ship.engine == 'experimental':
                    hull_damage2 += .05
            if player2ship.hull - hull_damage2 < 0:
                win_txt = pressplay_font.render('Player 1 Wins', True, WHITE)
                window.blit(win_txt, (GUI_X/2.1, GUI_Y/2.5))
                
    # bullets for p2
    if keys[pg.K_SLASH] and len(bullets2) < 250:
        radians = math.radians(angle2)
        sin = math.sin(radians)
        cos = math.cos(radians)
        #print(sin,cos)
        bullets2.append([x_move2,y_move2,sin,cos])
        # test for triple shot
        if player2ship.primary_weapon == 'BURST LASER CANNON':
            bullets2.append([x_move2-(20*cos),y_move2-(20*sin),.5*sin,2*cos])
            bullets2.append([x_move2+(20*cos),y_move2+(20*sin),2*sin,.5*cos])
        start_bullets2 = True
    if start_bullets2 == True:
        for bullet in bullets2:
            bullet[0] -= bullet[2]
            bullet[1] -= bullet[3]
            projectile2(window,bullet[0],bullet[1])
            if bullet[0] > 1900 or bullet[1] > 1000 or bullet[0] < 0 or bullet[1] <  0:
                bullets2.remove(bullet)
            # shield damage on p2
            if x_move-30 < bullet[0] < x_move+30 and y_move-30 < bullet[1] < y_move+30:
                shield_damage += .1 
            # hull damage on p1
            if x_move-20 < bullet[0] < x_move+20 and y_move-20 < bullet[1] < y_move+20 and player1ship.shield - shield_damage < 0:
                hull_damage += .1
                if player2ship.engine == 'experimental':
                    hull_damage += .05
            if player1ship.hull - hull_damage < 0:
                win_txt = pressplay_font.render('Player 2 Wins', True, WHITE)
                window.blit(win_txt, (GUI_X/2.1, GUI_Y/2.5))
                
    # health bar p1
    bar1 = (250,150),((player1ship.hull - hull_damage)//2,20)
    pygame.draw.rect(window, (255, 0, 0), (bar1))
    health_txt = pressplay_font.render('P1', True, WHITE)
    window.blit(health_txt, (200,150))
    # health bar p2
    bar2 = (250,200),((player2ship.hull - hull_damage2)//2,20)
    pygame.draw.rect(window, (50, 205, 50), (bar2)) 
    health_txt2 = pressplay_font.render('P2', True, WHITE)
    window.blit(health_txt2, (200,200))
    
    # shield bar p1
    bar1 = (250,175),((player1ship.shield - shield_damage)//2,5)
    pygame.draw.rect(window, (173, 216, 230), (bar1))
    # shield bar p2
    bar2 = (250,225),((player2ship.shield - shield_damage2)//2,5)
    pygame.draw.rect(window, (173, 216, 230), (bar2))
    
    # ship tag p1
    tag1 = pressplay_font.render('P1', True, WHITE)
    window.blit(tag1, (x_move-12,y_move-52))
    # ship tag p2
    tag2 = pressplay_font.render('P2', True, WHITE)
    window.blit(tag2, (x_move2-12,y_move2-52))
  
    # shield p1
    if player1ship.shield - shield_damage > 0:
        pygame.draw.circle(window, (173, 216, 230), (x_move,y_move), 35, 3)
    # shield p2
    if player2ship.shield - shield_damage2 > 0:
        pygame.draw.circle(window, (173, 216, 230), (x_move2,y_move2), 35, 3)
    
    # shield recharge p1
    if shield_damage > 0:
        shield_damage -= .2/shield_recharge
    # shield recharge p2
    if shield_damage2 > 0:
        shield_damage2 -= .2/shield_recharge2
    
    pg.display.flip()
    pg.display.update()
    check_quit()

# Quit Pygame
pygame.quit()