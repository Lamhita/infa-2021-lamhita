
def main():
	x,y = 100,100
	width,height = 200,200

	draw_house(x,y,width,height)

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
	foundation_height = 0.05 * height
	walls_height = 0.5 * height
	walls_width = 0.9 * width
	roof_height = height - foundation_height - walls_height

	draw_house_foundation(x, y, width, foundation_height)
	draw_house_walls(x, y - foundation_height, walls_width, walls_height)
	draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)

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

