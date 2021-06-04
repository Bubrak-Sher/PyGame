import time
import pygame
import random
from pygame import mixer
from pygame.locals import *
import math

pygame.init()


def main_menu_1():
	WIDTH = 500
	HEIGHT = 500

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	icon = pygame.image.load("data/Ayra0.png")
	pygame.display.set_caption("MAIN MENU")
	pygame.display.set_icon(icon)
	white = (255, 255, 255)
	blue = (0, 0, 255)
	# AUDIO


	playsound = False

	mixer.music.load("data/backgmain.wav")
	mixer.music.play(-1)

	menu_sound = mixer.Sound("data/mainmenu.wav")
	selecSound = mixer.Sound("data/pop.wav")


	font1 = pygame.font.SysFont(None, 40)
	font2 = pygame.font.SysFont(None, 37)
	font = pygame.font.SysFont(None, 60)

	# Functions 
	def coll_obj(obj1, obj2, action=None):
		if obj1[0] > obj2[0] and obj1[0] < obj2[0] + obj2[2] or obj1[0] + obj1[2] > obj2[0] and obj1[0] + obj1[2] < obj2[0] + obj2[2]:
			if obj1[1] < obj2[1] + obj2[3]:
				if obj1[1] + obj1[3] > obj2[1]:
					return True
					gravity = False
		return False



	def draw_screen(color):
		screen.fill((color))


	def draw_rec(color,x, y, width, height, action=None):
		pygame.draw.rect(screen, color, (x, y, width, height))

	def draw_text(text, value, fontty, color, window, x, y, action=None):
		txt = text + str(value)
		img = fontty.render(txt, True, color)
		window.blit(img, (x, y))

	color_1 = random.randint(0, 255) 
	color_2 = random.randint(0, 255)
	color_3 = random.randint(0, 255)

	counter = 0
	run = True
	while run:
		
		color_1 = random.randint(0, 255) 
		color_2 = random.randint(0, 255)
		color_3 = random.randint(0, 255)
		screen.fill((0, 0, 0))
		draw_text("Bubrak  &  ","Shahik " , font1, (color_1, color_2, color_3), screen, 0, 70)
		draw_text("For: Asfand, Ayra, Muhammad & Mehak", "", font2, (color_1, color_2, color_3), screen, 0, 460)
		# draw_text(text, value, fontty, color, window, x, y, action=None)
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		# print(mouse)
		draw_rec((0, 0, 50), 300, 300, 50, 50)
		pygame.draw.rect(screen , (255, 0, 0), (298, 298, 53, 53), 2)

		game_1 = draw_rec((255, 0, 0), 0, 100, 500, 350, 5)

		draw_text("MAIN MENU", " ", font, blue, screen, 0, 5)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quit()

		if  80 + 400 > mouse[0] > 80 and 150 + 50 > mouse[1] > 150:
			draw_text("   Snake Game", " ", font, (0, 0 , 0), screen, 80, 150)
			
			if playsound == True:
				menu_sound.play()
				playsound = False
			if click[0] == 1:
				mixer.music.stop()
				play_snake()
	
		else:
			draw_text("    Snake Game", " ", font, white, screen, 55, 153)		

		if  80 + 400 > mouse[0] > 80 and 250 + 50 > mouse[1] > 250:	
			draw_text("   Space Invader", " ", font, (0, 0 , 0), screen, 80, 250)
			
			if playsound == True:
				menu_sound.play()
				playsound = False
					
			if click[0] == 1:
				mixer.music.stop()
				import space

		
		else:
			draw_text("   Space Invader", " ", font, white, screen, 55, 253)									
			
		if  80 + 400 > mouse[0] > 80 and 350 + 50 > mouse[1] > 350:	
			draw_text("   Space Shooter", " ", font, (0, 0 , 0), screen, 80, 350)
			if playsound == True:
				menu_sound.play()
				playsound = False
			if click[0] == 1:
				mixer.music.stop()
				space_shooter()
		else:
			draw_text("   Space Shooter", " ", font, white, screen, 55, 353)
		
		if  80 + 400 > mouse[0] > 80 and 150 + 50 > mouse[1] > 150 or 80 + 400 > mouse[0] > 80 and 250 + 50 > mouse[1] > 250 or 80 + 400 > mouse[0] > 80 and 350 + 50 > mouse[1] > 350:
			playsound = False
		else:
			playsound = True			
		
		pygame.display.update()		
	pygame.quit()

##################################################################
##################################################################
##################################################################
####################        SNAKE GAME        ####################
##################################################################
##################################################################
##################################################################


def play_snake():
	
	WIDTH = 600
	HEIGHT = 600

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("SNAKE GAME")



	mixer.music.load("data/snake_music.wav")
	mixer.music.play(-1)
	snake_food = mixer.Sound("data/snake_food11.wav")
	collisionSound = mixer.Sound("data/alert.wav")


	color_1 = random.randint(0, 255) 
	color_2 = random.randint(0, 255)
	color_3 = random.randint(0, 255)

	name_font = pygame.font.SysFont(None, 30) 
	font1 = pygame.font.SysFont(None, 50)
	font = pygame.font.SysFont(None, 40)
	large_font = pygame.font.SysFont(None, 80)
	med_font = pygame.font.SysFont(None, 60)
	
	name_color = (240, 100, 0)


	clock = pygame.time.Clock()
	FPS = 30
	# Functions 

	def draw_screen(color):
		screen.fill((color))
		
		draw_text("Score: ", score, font, white, screen, 0, 0)
		draw_text("Stage: ", stage, font, white, screen, 480, 0)
		
		
	def draw_rec(color,x, y, width, height, action=None):
		pygame.draw.rect(screen, color, (x, y, width, height))

	def draw_text(text, value, fontty, color, window, x, y, action=None):
		txt = text + str(value)
		img = fontty.render(txt, True, color)
		window.blit(img, (x, y))

	def coll_obj(obj1, obj2, action=None):
		if obj1[0] > obj2[0] and obj1[0] < obj2[0] + obj2[2] or obj1[0] + obj1[2] > obj2[0] and obj1[0] + obj1[2] < obj2[0] + obj2[2]:
			if obj1[1] < obj2[1] + obj2[3]:
				if obj1[1] + obj1[3] > obj2[1]:
					return True
					gravity = False
		return False
	
	# variables
	r_width = 540
	r_height = 540
	x_r = 30
	y_r = 30
	stage = 1
	cell_size = 10
	score = 0
	food = [0, 0]
	new_piece = [0, 0]
	update_snake = 0
	clicked = False
	game_over = False
	
	inside = True
	
	# Colors
	bg = (21, 46, 18)
	bgg = (70, 170, 70)
	body_outer = (10, 10, 30)
	body_inner = (0, 43, 0)
	food_col = (200, 20, 20)
	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	white = (255, 255, 255)


	playsound_1 = True

	# Snake Variables
	snake_pos = [[int(100), int(300)]]
	snake_pos.append([100, 310])
	snake_pos.append([100, 320])
	snake_pos.append([100, 330])
	direction = 1
	new_food = True
	
	def check_game_over(game_over):
		
		head_count = 0
		for x in snake_pos:
			if snake_pos[0] == x and head_count > 0:
				game_over = True
			head_count += 1	
		if snake_pos[0][0] < x_r or snake_pos[0][0] > r_width + 20 or snake_pos[0][1] < y_r or snake_pos[0][1] > r_height + 20:
			game_over = True
		return game_over		

	run = True
	while run:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				main_menu_1()
				run = False
				quit()
		mouse = pygame.mouse.get_pos()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and direction != 2:	
			direction = 4
		if keys[pygame.K_RIGHT] and direction != 4:
			direction = 2
		if keys[pygame.K_UP] and direction != 3:
			direction = 1
		if keys[pygame.K_DOWN] and direction != 1:
			direction = 3

		draw_screen((bg))
		pygame.draw.rect(screen, bgg, (x_r, y_r, r_width, r_height))
		
		if score > 2 and score < 4:
			stage = 2
		if score >= 5:
			stage = 3
		
		if snake_pos[0] == food:
			new_food = True
			new_piece = list(snake_pos[-1])

			if direction == 1:
				new_piece[1] += cell_size
			if direction == 3:
				new_piece[1] -= cell_size
			if direction == 2:
				new_piece[0] -= cell_size	  
			if direction == 4:
				new_piece[0] += cell_size
			snake_pos.append(new_piece)
			snake_food.play()
			score += 1
			

		if new_food == True:
			new_food = False
			food[0] = cell_size * random.randint(3, (r_width / cell_size) - 1)	
			food[1] = cell_size * random.randint(3, (r_width / cell_size) - 1)
		
			

		if stage == 1:
			pygame.draw.rect(screen, (bgg), (x_r, y_r, r_width, r_height))
			body_inner = (255, 255, 255)
			food_col = (255, 255, 255)
			hit1 = pygame.draw.rect(screen, bg, (125, 275, 350, 50))
			draw_text("  S  C  O  R  P  I  O  ", "", med_font, white, screen, 118, 283)
			
			if food[1] < 270 or food[1] > 360:
				pygame.draw.rect(screen, food_col, (food[0], food[1], cell_size, cell_size))
			else:
				food = [0, 0]
				food[0] = cell_size * random.randrange(5, 6)
				food[1] = cell_size * random.randrange(30, 31)
				pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], cell_size, cell_size))	
				new_food = False
			if 125 + 350 > snake_pos[0][0] > 115 and 280 + 50 > snake_pos[0][1] > 265:
				game_over = True
				pygame.draw.rect(screen, red,(125, 275, 350, 50), 2)	
				draw_text("  S  C  O  R  P  I  O  ", "", med_font, (160, 90, 0), screen, 118, 283)
		
		if stage == 2:

			pygame.draw.rect(screen, (20, 120, 20), (x_r, y_r, r_width, r_height))
			body_inner = (0, 255, 255)
			food_col = (0, 255, 255)
			hit2 = pygame.draw.rect(screen, bg, (125, 275, 445, 50))
			
			if food[1] < 260 or food[1] > 360: 
				pygame.draw.rect(screen, food_col, (food[0], food[1], cell_size, cell_size))
			else:
				food = [0, 0]
				food[0] = cell_size * random.randrange(7, 8)
				food[1] = cell_size * random.randrange(30, 31)
				pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], cell_size, cell_size))
				new_food = False
			if 125 + 445 > snake_pos[0][0] > 115 and 280 + 50 > snake_pos[0][1] > 265:
				game_over = True
				pygame.draw.rect(screen, red,(125, 275, 445, 50), 2)
						
		if stage == 3:
			
			pygame.draw.rect(screen, (150, 150, 70), (x_r, y_r, r_width, r_height))
			body_inner = (255, 255, 0)
			food_col = (250, 250, 0)
			hit3 = pygame.draw.rect(screen, bg, (270, 30, 50, 220))
			hit3_1 = pygame.draw.rect(screen, bg, (270, 350, 50, 220))
			
			if food[0] < 270 or food[0] > 340: 
				pygame.draw.rect(screen, food_col, (food[0], food[1], cell_size, cell_size))
			else:
				food = [0, 0]
				food[0] = cell_size * random.randrange(10,11)
				food[1] = cell_size * random.randrange(30,31)
				pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], cell_size, cell_size))
				new_food = False
			if 270 + 50 > snake_pos[0][0] > 260 and 30 + 220 > snake_pos[0][1] > 25 or 270 + 50 > snake_pos[0][0] > 260 and 350 + 220 > snake_pos[0][1] > 340:
				game_over = True	
				pygame.draw.rect(screen, green,(270, 30, 50, 540), 2)							
			

		if game_over == False:
			if update_snake > 99:
				update_snake = 0
				snake_pos = snake_pos[-1:] + snake_pos[:-1]

				if direction == 1:
					snake_pos[0][0] = snake_pos[1][0]
					snake_pos[0][1] = snake_pos[1][1] - cell_size
				if direction == 3:
					snake_pos[0][0] = snake_pos[1][0]
					snake_pos[0][1] = snake_pos[1][1] + cell_size
				if direction == 2:
					snake_pos[0][1] = snake_pos[1][1]
					snake_pos[0][0] = snake_pos[1][0] + cell_size
				if direction == 4:
					snake_pos[0][1] = snake_pos[1][1]
					snake_pos[0][0] = snake_pos[1][0] - cell_size			

				game_over = check_game_over(game_over)

		if game_over == True:
			mixer.music.stop()
			if playsound_1 == True:
				collisionSound.play()
				playsound_1 = False
			again_rect = pygame.draw.rect(screen, green, (170, 350, 250, 50))
			if again_rect[0] + again_rect[2] > mouse[0] > again_rect[0] and again_rect[1] + again_rect[3] > mouse[1] > again_rect[1]:	
				pygame.draw.rect(screen, white, (170, 350, 250, 50))
				draw_text("Game Over", "", large_font, red, screen, 145, HEIGHT // 2 - 100)
				draw_text("Play Again", "", med_font, bg, screen, 185, 355)

			else:
				draw_text("Game Over", "", large_font, red, screen, 145, HEIGHT // 2 - 100)
				again_rect = pygame.draw.rect(screen, bg, (170, 350, 250, 50))
				draw_text("Play Again", "", med_font, white, screen, 185, 355)		

			if again_rect[0] + again_rect[2] > mouse[0] > again_rect[0] and again_rect[1] + again_rect[3] > mouse[1] > again_rect[1]:	
			
				if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
					clicked = True
				if event.type == pygame.MOUSEBUTTONUP and clicked == True:
					game_over = False
					clicked = False
					mixer.music.play()
					score = 0
					stage = 1
					update_snake = 0
					playsound_1 = True

					new_food = True
					new_piece = [0, 0]		
					snake_pos = [[int(100), int(300)]]
					snake_pos.append([100, 310])
					snake_pos.append([100, 320])
					snake_pos.append([100, 330])
					direction = 1


		head = 1
		for x in snake_pos:
			if head == 0:
				pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
				pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))	
			if head == 1:
				pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
				pygame.draw.rect(screen, red, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))	
				head = 0
			
		pygame.display.update()
		if stage == 1:
			update_snake += 1.4
		if stage == 2:
			update_snake += 1.6
		if stage == 3:
			update_snake += 1.8
		
					
	pygame.display.quit()



##################################################################
##################################################################
##################################################################
####################       SPACE INVADER      ####################
##################################################################
##################################################################
##################################################################







##################################################################
##################################################################
##################################################################
####################      SPACE SHOOTER       ####################
##################################################################
##################################################################
##################################################################

def space_shooter():
	import pygame
	import os
	import time
	import random
	pygame.font.init()

	WIDTH, HEIGHT = 800, 700
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Space Shooter Tutorial")

	# Load images
	RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
	GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
	BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

	# Player player
	YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

	# Lasers
	RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
	GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
	BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
	YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

	# Background
	BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

	class Laser:
		def __init__(self, x, y, img):
			self.x = x
			self.y = y
			self.img = img
			self.mask = pygame.mask.from_surface(self.img)

		def draw(self, window):
			window.blit(self.img, (self.x, self.y))

		def move(self, vel):
			self.y += vel

		def off_screen(self, height):
			return not(self.y <= height and self.y >= 0)

		def collision(self, obj):
			return collide(self, obj)


	class Ship:
		COOLDOWN = 30

		def __init__(self, x, y, health=100):
			self.x = x
			self.y = y
			self.health = health
			self.ship_img = None
			self.laser_img = None
			self.lasers = []
			self.cool_down_counter = 0

		def draw(self, window):
			window.blit(self.ship_img, (self.x, self.y))
			for laser in self.lasers:
				laser.draw(window)

		def move_lasers(self, vel, obj):
			self.cooldown()
			for laser in self.lasers:
				laser.move(vel)
				if laser.off_screen(HEIGHT):
					self.lasers.remove(laser)
				elif laser.collision(obj):
					obj.health -= 10
					self.lasers.remove(laser)

		def cooldown(self):
			if self.cool_down_counter >= self.COOLDOWN:
				self.cool_down_counter = 0
			elif self.cool_down_counter > 0:
				self.cool_down_counter += 1

		def shoot(self):
			if self.cool_down_counter == 0:
				laser = Laser(self.x, self.y, self.laser_img)
				self.lasers.append(laser)
				self.cool_down_counter = 1

		def get_width(self):
			return self.ship_img.get_width()

		def get_height(self):
			return self.ship_img.get_height()


	class Player(Ship):
		def __init__(self, x, y, health=100):
			super().__init__(x, y, health)
			self.ship_img = YELLOW_SPACE_SHIP
			self.laser_img = YELLOW_LASER
			self.mask = pygame.mask.from_surface(self.ship_img)
			self.max_health = health

		def move_lasers(self, vel, objs):
			self.cooldown()
			for laser in self.lasers:
				laser.move(vel)
				if laser.off_screen(HEIGHT):
					self.lasers.remove(laser)
				else:
					for obj in objs:
						if laser.collision(obj):
							objs.remove(obj)
							if laser in self.lasers:
								self.lasers.remove(laser)

		def draw(self, window):
			super().draw(window)
			self.healthbar(window)

		def healthbar(self, window):
			pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
			pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


	class Enemy(Ship):
		COLOR_MAP = {
					"red": (RED_SPACE_SHIP, RED_LASER),
					"green": (GREEN_SPACE_SHIP, GREEN_LASER),
					"blue": (BLUE_SPACE_SHIP, BLUE_LASER)
					}

		def __init__(self, x, y, color, health=100):
			super().__init__(x, y, health)
			self.ship_img, self.laser_img = self.COLOR_MAP[color]
			self.mask = pygame.mask.from_surface(self.ship_img)

		def move(self, vel):
			self.y += vel

		def shoot(self):
			if self.cool_down_counter == 0:
				laser = Laser(self.x-20, self.y, self.laser_img)
				self.lasers.append(laser)
				self.cool_down_counter = 1


	def collide(obj1, obj2):
		offset_x = obj2.x - obj1.x
		offset_y = obj2.y - obj1.y
		return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

	def main():
		run = True
		FPS = 60
		level = 0
		lives = 5
		main_font = pygame.font.SysFont("comicsans", 50)
		lost_font = pygame.font.SysFont("comicsans", 60)

		enemies = []
		wave_length = 5
		enemy_vel = 1

		player_vel = 5
		laser_vel = 5

		player = Player(300, 580)

		clock = pygame.time.Clock()

		lost = False
		lost_count = 0

		def redraw_window():
			WIN.blit(BG, (0,0))
			# draw text
			lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
			level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

			WIN.blit(lives_label, (10, 10))
			WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

			for enemy in enemies:
				enemy.draw(WIN)

			player.draw(WIN)

			if lost:
				lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
				WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

			pygame.display.update()

		while run:
			clock.tick(FPS)
			redraw_window()

			if lives <= 0 or player.health <= 0:
				lost = True
				lost_count += 1

			if lost:
				if lost_count > FPS * 3:
					run = False
				else:
					continue

			if len(enemies) == 0:
				level += 1
				wave_length += 5
				for i in range(wave_length):
					enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
					enemies.append(enemy)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()

			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT] and player.x - player_vel > 0: # left
				player.x -= player_vel
			if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH: # right
				player.x += player_vel
			if keys[pygame.K_UP] and player.y - player_vel > 0: # up
				player.y -= player_vel
			if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
				player.y += player_vel
			if keys[pygame.K_SPACE]:
				player.shoot()

			for enemy in enemies[:]:
				enemy.move(enemy_vel)
				enemy.move_lasers(laser_vel, player)

				if random.randrange(0, 2*60) == 1:
					enemy.shoot()

				if collide(enemy, player):
					player.health -= 10
					enemies.remove(enemy)
				elif enemy.y + enemy.get_height() > HEIGHT:
					lives -= 1
					enemies.remove(enemy)

			player.move_lasers(-laser_vel, enemies)

	def main_menu():
		title_font = pygame.font.SysFont("comicsans", 70)
		run = True
		while run:
			WIN.blit(BG, (0,0))
			title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
			WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					main_menu_1()
					quit()
					
				if event.type == pygame.MOUSEBUTTONDOWN:
					main()
		pygame.quit()


	main_menu()



main_menu_1()
