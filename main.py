import pygame
import sys
import random
pygame.init()
pygame.mixer.init()
pygame.font.init()

screen_width = 800
screen_height = 607
image_buf = 1200
player_height = 220
player_width = 220
white = (255, 255, 255)
black = (0, 0, 0)

pygame.mixer.music.load("Assets/Sounds/music2.mp3")
pygame.mixer.music.set_volume(0.5)         # Volume (0.0 to 1.0)
pygame.mixer.music.play(-1)
ui_sound=pygame.mixer.Sound("Assets/Sounds/ui.mp3")
fruit_sound=pygame.mixer.Sound("Assets/Sounds/boing.mp3")
textfont = pygame.font.Font("Assets/Fonts&Icons/80s-retro-future.ttf", 48)
textfont1 = pygame.font.Font("Assets/Fonts&Icons/80s-retro-future.ttf", 80)

game_icon = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/09.png")
tree_bg = pygame.image.load("Assets/Scene_BG/tree_bg.PNG")
tree_bg = pygame.transform.scale(tree_bg, (image_buf, screen_height))
tittle_bg = pygame.image.load("Assets/Scene_BG/Start_bg.jpg")

box_surface = pygame.Surface((400, 400))
box_surface.fill((0, 0, 0))  # Fill the surface with black
box_surface.set_alpha(180)
box_surface1 = pygame.Surface((1080, 607))
box_surface1.fill((0, 0, 0))  # Fill the surface with black
box_surface1.set_alpha(180)
right_arrow1 = pygame.image.load("Assets/Fonts&Icons/Lucid-V1.2/Lucid V1.2/PNG/Shadow/64/Chevron-Arrow-Right.png")
right_arrow1_rect = right_arrow1.get_rect()
right_arrow1_rect.topleft = (screen_width / 2 + 150, 280)
right_arrow2 = pygame.image.load("Assets/Fonts&Icons/Lucid-V1.2/Lucid V1.2/PNG/Shadow/64/Chevron-Arrow-Right.png")
right_arrow2_rect = right_arrow2.get_rect()
right_arrow2_rect.topleft = (screen_width / 2 + 150, 350)

left_arrow1 = pygame.image.load("Assets/Fonts&Icons/Lucid-V1.2/Lucid V1.2/PNG/Shadow/64/Chevron-Arrow-Left.png")
left_arrow1_rect = left_arrow1.get_rect()
left_arrow1_rect.topleft = (screen_width / 2 - 150, 280)
left_arrow2 = pygame.image.load("Assets/Fonts&Icons/Lucid-V1.2/Lucid V1.2/PNG/Shadow/64/Chevron-Arrow-Left.png")
left_arrow2_rect = left_arrow2.get_rect()
left_arrow2_rect.topleft = (screen_width / 2 - 150, 350)

ai_icon_on = pygame.image.load("Assets/Fonts&Icons/Lucid-V1.2/Lucid V1.2/PNG/Shadow/64/Cursor-4.png")
ai_icon_on_rect = ai_icon_on.get_rect()
ai_icon_on_rect.topleft = (screen_width / 2 + 80, 420)
ai_icon_off = pygame.image.load("Assets/Fonts&Icons/Lucid-V1.2/Lucid V1.2/PNG/Shadow/64/Cursor-3.png")

player1_i0 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Male/Character 1/Clothes 3/Character1M_3_idle_0.png")
player1_i0 = pygame.transform.scale(player1_i0, (player_width, player_height))
player1_i1 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Male/Character 1/Clothes 3/Character1M_3_idle_1.png")
player1_i1 = pygame.transform.scale(player1_i1, (player_width, player_height))
player1_i2 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Male/Character 1/Clothes 3/Character1M_3_idle_2.png")
player1_i2 = pygame.transform.scale(player1_i2, (player_width, player_height))
player1_i3 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Male/Character 1/Clothes 3/Character1M_3_idle_3.png")
player1_i3 = pygame.transform.scale(player1_i3, (player_width, player_height))
player1_i4 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Male/Character 1/Clothes 3/Character1M_3_idle_4.png")
player1_i4 = pygame.transform.scale(player1_i4, (player_width, player_height))
player1_i5 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Male/Character 1/Clothes 3/Character1M_3_idle_5.png")
player1_i5 = pygame.transform.scale(player1_i5, (player_width, player_height))
player1_i6 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Male/Character 1/Clothes 3/Character1M_3_idle_6.png")
player1_i6 = pygame.transform.scale(player1_i6, (player_width, player_height))
player1_i7 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Male/Character 1/Clothes 3/Character1M_3_idle_7.png")
player1_i7 = pygame.transform.scale(player1_i7, (player_width, player_height))


player1_animation = [player1_i0,
                     player1_i1,
                     player1_i2,
                     player1_i3,
                     player1_i4,
                     player1_i5,
                     player1_i6,
                     player1_i7
                     ]

player2_i0 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Female/Character 3/Clothes 3/Character3F_3_idle_0.png")
player2_i1 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Female/Character 3/Clothes 3/Character3F_3_idle_1.png")
player2_i2 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Female/Character 3/Clothes 3/Character3F_3_idle_2.png")
player2_i3 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Female/Character 3/Clothes 3/Character3F_3_idle_3.png")
player2_i4 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Female/Character 3/Clothes 3/Character3F_3_idle_4.png")
player2_i5 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Female/Character 3/Clothes 3/Character3F_3_idle_5.png")
player2_i6 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Female/Character 3/Clothes 3/Character3F_3_idle_6.png")
player2_i7 = pygame.image.load(
    "Assets/sprites/mp_character_animation_asset_pack_v1.0/mp_character_animation_asset_pack_v1.0/Exported PNGs/Female/Character 3/Clothes 3/Character3F_3_idle_7.png")

player2_i0 = pygame.transform.scale(player2_i0, (player_width, player_height))
player2_i1 = pygame.transform.scale(player2_i1, (player_width, player_height))
player2_i2 = pygame.transform.scale(player2_i2, (player_width, player_height))
player2_i3 = pygame.transform.scale(player2_i3, (player_width, player_height))
player2_i4 = pygame.transform.scale(player2_i4, (player_width, player_height))
player2_i5 = pygame.transform.scale(player2_i5, (player_width, player_height))
player2_i6 = pygame.transform.scale(player2_i6, (player_width, player_height))
player2_i7 = pygame.transform.scale(player2_i7, (player_width, player_height))

player2_i0 = pygame.transform.flip(player2_i0, 1, 0)
player2_i1 = pygame.transform.flip(player2_i1, 1, 0)
player2_i2 = pygame.transform.flip(player2_i2, 1, 0)
player2_i3 = pygame.transform.flip(player2_i3, 1, 0)
player2_i4 = pygame.transform.flip(player2_i4, 1, 0)
player2_i5 = pygame.transform.flip(player2_i5, 1, 0)
player2_i6 = pygame.transform.flip(player2_i6, 1, 0)
player2_i7 = pygame.transform.flip(player2_i7, 1, 0)

player2_i_animation = [player2_i0,
                       player2_i1,
                       player2_i2,
                       player2_i3,
                       player2_i4,
                       player2_i5,
                       player2_i6,
                       player2_i7,
                       ]

one = pygame.image.load("Assets/Fonts&Icons/one.png")
one = pygame.transform.scale(one, (80, 80))
one_rect = one.get_rect()
one_rect.topleft = (screen_width / 2 - 150, 520)
two = pygame.image.load("Assets/Fonts&Icons/two.png")
two = pygame.transform.scale(two, (80, 80))
two_rect = two.get_rect()
two_rect.topleft = (screen_width / 2 + 80, 520)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fruit Fall")
pygame.display.set_icon(game_icon)

f1 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/01.png")
f2 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/02.png")
f3 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/03.png")
f4 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/04.png")
f5 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/05.png")
f6 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/06.png")
f7 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/07.png")
f8 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/08.png")
f9 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/09.png")
f10 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/10.png")
f11 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/11.png")
f12 = pygame.image.load("Assets/sprites/Fruits Asset/Fruits Asset/Black Outline/12.png")

f1 = pygame.transform.scale(f1, (50, 50))
f2 = pygame.transform.scale(f2, (50, 50))
f3 = pygame.transform.scale(f3, (50, 50))
f4 = pygame.transform.scale(f4, (50, 50))
f5 = pygame.transform.scale(f5, (50, 50))
f6 = pygame.transform.scale(f6, (50, 50))
f7 = pygame.transform.scale(f7, (50, 50))
f8 = pygame.transform.scale(f8, (50, 50))
f9 = pygame.transform.scale(f9, (50, 50))
f10 = pygame.transform.scale(f10, (50, 50))
f11 = pygame.transform.scale(f11, (50, 50))
f12 = pygame.transform.scale(f12, (50, 50))

fruits = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

bee = pygame.image.load("Assets/sprites/bee.png")
bee = pygame.transform.scale(bee, (50, 50))
state = "Start"
No_Fruits = 10
No_honey = 3
AI_on = True
start_text = textfont.render("START", True, (0, 255, 0))
start_rect = start_text.get_rect()
start_rect.topleft = (screen_width / 2 - 50, 520)

center_pos = screen_width / 2 - 100
p1_pos = screen_width / 2 - 360
p2_pos = screen_width / 2 + 180

seq = []
player_score = 0
ai_score = 0
running = True
on_screen = []
fruit_pos = [(372, 451), (320, 430), (404, 402), (469, 378), (412, 354), (347, 326), (295, 297), (355, 276), (413, 259),
             (470, 235), (415, 216), (357, 199), (307, 175), (389, 144), (461, 124)]
max_fruit_on_screen = 15
game_over = False
is_player_turn = False


def draw_seq(seq):
    on_screen = seq[:15]
    fruits_left = len(seq)
    if fruits_left <= 15:
        for x in range(fruits_left):
            screen.blit(seq[x], fruit_pos[x])
    else:
        for x in range(15):
            screen.blit(seq[x], fruit_pos[x])




def minimax(s, is_maximizing):
    if not s:
        return 0
    best_score = float('-inf') if is_maximizing else float('inf')
    for take in [1, 2]:
        if len(s) >= take:
            picked = s[:take]
            rest = s[take:]
            score = sum(2 if f in fruits else -1 for f in picked)
            future_score = minimax(rest, not is_maximizing)
            total_score = score + future_score if is_maximizing else -score + future_score
            if is_maximizing:
                best_score = max(best_score, total_score)
            else:
                best_score = min(best_score, total_score)
    return best_score

def ai_move(s):
    best_value = float('-inf')
    best_pick = 1
    for take in [1, 2]:
        if len(s) >= take:
            picked = s[:take]
            rest = s[take:]
            score = sum(2 if f in fruits else -1 for f in picked)
            value = score + minimax(rest, False)
            if value > best_value:
                best_value = value
                best_pick = take
    return best_pick

p1_frame = 0
p2_frame = 0
frame=15
cooldown=80

beepsound=pygame.mixer.Sound("Assets/Sounds/beep.mp3")
last_update = pygame.time.get_ticks()
hurt=False
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_click = True

    if state == "Start":
        fruit_text = textfont.render(f"FRUITS:{No_Fruits}", True, white)
        honey_text = textfont.render(f"COMBS:{No_honey}", True, white)
        AI_text = textfont.render(f"AI", True, white)

        screen.blit(tittle_bg, (0, 0))
        screen.blit(box_surface, (screen_width / 2 - 185, 250))
        screen.blit(right_arrow1, right_arrow1_rect)
        screen.blit(right_arrow2, right_arrow2_rect)
        screen.blit(left_arrow1, left_arrow1_rect)
        screen.blit(left_arrow2, left_arrow2_rect)
        screen.blit(fruit_text, (screen_width / 2 - 100, 350))
        screen.blit(honey_text, (screen_width / 2 - 80, 280))
        screen.blit(AI_text, (screen_width / 2 - 100, 420))
        screen.blit(start_text, start_rect)


        if AI_on:
            screen.blit(ai_icon_on, ai_icon_on_rect)
        elif not AI_on:
            screen.blit(ai_icon_off, ai_icon_on_rect)

        if left_arrow1_rect.collidepoint(mouse_pos) and mouse_click:
            ui_sound.play()
            No_honey -= 1
            if No_honey <= 0:
                No_honey = 1
        elif right_arrow1_rect.collidepoint(mouse_pos) and mouse_click:
            ui_sound.play()
            No_honey += 1
            if No_honey >= 11:
                No_honey = 10
        elif left_arrow2_rect.collidepoint(mouse_pos) and mouse_click:
            ui_sound.play()
            No_Fruits -= 1
            if No_Fruits <= 7:
                No_Fruits = 8
        elif right_arrow2_rect.collidepoint(mouse_pos) and mouse_click:
            ui_sound.play()
            No_Fruits += 1
            if No_Fruits >= 31:
                No_Fruits = 30
        elif ai_icon_on_rect.collidepoint(mouse_pos) and mouse_click:
            ui_sound.play()
            AI_on = not AI_on
        elif start_rect.collidepoint(mouse_pos) and mouse_click:
            ui_sound.play()
            for x in range(No_Fruits):
                seq.append(fruits[random.randint(0, 11)])
            seq = seq + [bee] * No_honey
            random.shuffle(seq)
            is_player_turn = not AI_on
            state = "RUN"

    elif state == "RUN":
        screen.blit(tree_bg, (-(image_buf - screen_width) / 2, 0))
        playerS_text = textfont.render(f"PLAYER:{player_score}", True, white)
        aiS_text = textfont.render(f"AI:{ai_score}", True, white)
        screen.blit(playerS_text, (0, 0))
        screen.blit(aiS_text, (screen_width -130, 0))


        take = 0
        # draw_seq(seq)
        if len(seq)<=0:game_over=True
        if game_over:

            screen.blit(box_surface1, (0, 0))
            if player_score>ai_score:
                winner_text=textfont1.render("YOU WIN",True,white)
            else:
                winner_text=textfont1.render("YOU LOSE",True,white)
            screen.blit(winner_text,(center_pos-100,250))

        else:
            if not is_player_turn:
                pygame.time.delay(1000)
                ai_take = ai_move(seq)
                picked = seq[:ai_take]
                seq = seq[ai_take:]
                ai_score += sum(2 if f in fruits else -1 for f in picked)
                for f in picked:
                    if f == bee:
                        hurt=True
                if ai_take==2:
                    beepsound.play()
                    pygame.time.delay(100)
                    beepsound.play()

                else:
                    beepsound.play()
                is_player_turn = True

            elif is_player_turn:
                screen.blit(one, one_rect)
                screen.blit(two, two_rect)
                if one_rect.collidepoint(mouse_pos) and mouse_click:
                    take = 1
                elif two_rect.collidepoint(mouse_pos) and mouse_click:
                    take = 2
                if take > len(seq):
                    take = len(seq)
                for t in range(take):
                    if seq[t] in fruits:
                        player_score += 2
                        fruit_sound.play()
                    elif seq[t] == bee:
                        player_score -= 1
                seq = seq[take:]
                if take != 0:
                    is_player_turn = False
                    take =0



            draw_seq(seq)
            p1_frame += 1
            if p1_frame > 7:
                p1_frame = 0
            screen.blit(player1_animation[p1_frame], (p1_pos, 400))
            screen.blit(player2_i_animation[p1_frame], (p2_pos, 400))
            pygame.time.delay(100)


    pygame.display.update()

pygame.quit()
sys.exit()
