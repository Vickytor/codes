import pyglet
import random
from pyglet.window import mouse

window = pyglet.window.Window(1024, 768, resizable=True)

blue = pyglet.image.load('blue.png')
blue.width = 162
blue.height = 162

yellow = pyglet.image.load('red.png')
yellow.width = 162
yellow.height = 162

red = pyglet.image.load('yellow.png')
red.width = 162
red.height = 162

batch = pyglet.graphics.Batch()
color_bubbles = [blue, yellow, red]
direction = [-100, 100]
bubble_list = []
counter = 0
counter_update = 0

def new_bubble(x, y):
	bubble = pyglet.sprite.Sprite(random.choice(color_bubbles), batch=batch)
	bubble.position = (x - 81, y - 81)
	bubble_list.append(bubble)
	
def update(dt):
	for bubble in bubble_list:
		bubble.x += 100*dt
		bubble.y += 100*dt
		
class Bubbles: 
	

	

@window.event()
def on_mouse_press(x, y, button, modifiers):
	if button == mouse.LEFT:
		new_bubble(x, y)


@window.event()
def on_draw():
	window.clear()
	batch.draw()


pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()
