import pygame
from pygame.draw import *

def main():
	x,y = 100,100
	width,height = 200,200

	draw_house(x,y,width,height)
def	draw_sky(y,color,):
	'''

	:param y: отступ линии горизонта от верха рисунка, в пикселях
	:return: None
	'''
	pass

def draw_house(x,y,width,height):
	"""
	Нарисовать домик ширины width и высоты height от опорной точки (x,y),
	:param x: координата x середины домика
	:param y: координата y низа фундамента
	:param width: полная ширина домика
	:param height: полная высота домика
	:return: None
	"""
	print('Типа рисую домик2', x,y,width,height)


def draw_house_foundation(x, y, width, height):
	"""
	Нарисовать основание домика ширины width и высоты height от опорной точки (x,y),
	которая находитсяв середине нижней точки фундамента.
	:param x: координата x середины фундамента
	:param y: координата y  середины фундамента
	:param width: полная ширина фундамента
	:param height: полная высота фундамента
	:return:
	"""
	pass
def	draw_house_walls(x, y - foundation_height, walls_width, walls_height):
	pass
def	draw_house_roof(x, y - foundation_height - walls_height, width, roof_height):
	pass

main()

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))
screen.fill('black')
color = (229,43,80)
#draw sky

grey_sky = rect(screen, (102,102,102), (0,0,794,470))
moon = circle(screen, '#A1A1A1', (719,95), 70,0)
pipe_1 = rect(screen, (18,18,18), (95,145,12,75))
pipe_3 = rect(screen, (18,18,18), (288,153,12,75))

top2_cloud = ellipse(screen, (36,36,36), [36, 106, 661-36, 177-106], 0)
pipe_2 = rect(screen, (18,18,18), (120,100,30,130))
pipe_4 = rect(screen, (18,18,18), (385,138,15,88))
top1_cloud = ellipse(screen, (54,54,54), [348, 75, 810-348, 152-75], 0)
top3_cloud = ellipse(screen, (54,54,54), [469, 165, (793-469)*2, 232-165], 0)
top4_cloud = ellipse(screen, (18,18,18), [401, 238, 390+60, 70], 0)
#draw house
roof = polygon(screen, 'black', [(0,246),(62,200),(423,201),(495,246)])
house_main = rect(screen, (43,34,0), (41,246,456-41,816-246))
window_1 = rect(screen, (30,12,0), (88,649,168-88,748-649))
window_2 = rect(screen, (30,12,0), (214,647,168-88,748-649))
window_2 = rect(screen, (148,119,0), (331,648,411-331,749-648))
#columns, left to right
column_1 = rect(screen, (72,62,55), (72,248,115-72,458-248))
column_2 = rect(screen, (72,62,55), (145,248,46,217))
column_3 = rect(screen, (72,62,55), (253,248,46,217))
column_4 = rect(screen, (72,62,55), (360,248,46,217))

railing_bar_bottom = rect(screen, (26,26,26), (0,470,500,527-470))
railing_column_1 = rect(screen, (26,26,26), (9,417,13,55))
railing_column_2 = rect(screen, (26,26,26), (60,417,25,55))
railing_column_3 = rect(screen, (26,26,26), (135,417,25,55))
railing_column_4 = rect(screen, (26,26,26), (215,417,25,55))
railing_column_5 = rect(screen, (26,26,26), (305,417,25,55))
railing_column_6 = rect(screen, (26,26,26), (395,417,25,55))
railing_column_7 = rect(screen, (26,26,26), (475,417,13,55))
railing_bar_top = rect(screen, (26,26,26), (22,417,475-22,25))


# 9+13=22 22,392 (22,417,475-22,25) 
# face = circle(screen, 'yellow', (400,400), 200)

# left_eye = circle(screen, 'red', (320,350), 40)

# right_eye = circle(screen, 'red', (480,350), 30)

# left_pupil = circle(screen, 'black', (320,350), 15)

# right_pupil = circle(screen, 'black', (480,350), 15)

# delta = 14

# left_brow = polygon(screen, 'black', [(196,225-delta),(211,205-delta),(404,351-delta),(390,371-delta)])

# right_brow = polygon(screen, 'black', [(431,338-delta),(575,265-delta),(583,281-delta),(439,353-delta)])

# mouth = rect(screen, 'black', (319,500,490-319,537-500))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
