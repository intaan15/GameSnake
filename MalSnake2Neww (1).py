from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import sys
import random
import math

 
pygame.init()

 
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

 
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE

 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

 
snake = [(5, 5)]
snake_direction = (1, 0)

 
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

 
score = 0

 
speed = 2

 
font = pygame.font.SysFont("TimesNewRoman", 30)

 
high_score = 0

 
def draw_snake(snake):
    for i, segment in enumerate(snake):
        if i == 0:   
            pygame.draw.circle(screen, (255, 255, 255), ((segment[0] * GRID_SIZE) + GRID_SIZE // 2, (segment[1] * GRID_SIZE) + GRID_SIZE // 2), GRID_SIZE // 2)
        elif i == len(snake) - 1:   
            draw_tail_triangle(segment)

        else:
            pygame.draw.rect(screen, (255, 255, 255), (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

 
def draw_tail_triangle(tail_segment):
    tail_rect = pygame.Rect(tail_segment[0] * GRID_SIZE, tail_segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)

     
    tail_direction = (tail_segment[0] - snake[-2][0], tail_segment[1] - snake[-2][1])

     
    if tail_direction[0] == 0:
        if tail_direction[1] > 0:
            tail_direction = (0, -1)
        else:
            tail_direction = (0, 1)

     
    if tail_direction[0] < 0:   
        pygame.draw.polygon(screen, (255, 255, 255), [(tail_rect.right, tail_rect.top),
                                                   (tail_rect.right, tail_rect.bottom),
                                                   (tail_rect.left, tail_rect.centery)])
    elif tail_direction[0] > 0:  
        pygame.draw.polygon(screen, (255, 255, 255), [(tail_rect.left, tail_rect.top),
                                                   (tail_rect.left, tail_rect.bottom),
                                                   (tail_rect.right, tail_rect.centery)])
    elif tail_direction[1] < 0:   
        pygame.draw.polygon(screen, (255, 255, 255), [(tail_rect.left, tail_rect.top),
                                                          (tail_rect.right, tail_rect.top),
                                                          (tail_rect.left + GRID_SIZE // 2, tail_rect.bottom)])
    elif tail_direction[1] > 0:   
        pygame.draw.polygon(screen, (255, 255, 255), [(tail_rect.left, tail_rect.bottom),
                                                          (tail_rect.right, tail_rect.bottom),
                                                          (tail_rect.left + GRID_SIZE // 2, tail_rect.top)])
                    
 
def draw_food(food):
    pygame.draw.rect(screen, WHITE, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

 
def check_wall_collision(snake_head):
    return snake_head[0] < 0 or snake_head[0] >= GRID_WIDTH or snake_head[1] < 0 or snake_head[1] >= GRID_HEIGHT

def load_texture(file_path):
    image = pygame.image.load(file_path)
    image_data = pygame.image.tostring(image, "RGBA", 1)

    width, height = image.get_size()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    return texture_id

 
def draw_image(texture_id, x, y, width, height):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(x, y)

    glTexCoord2f(1, 0)
    glVertex2f(x + width, y)

    glTexCoord2f(1, 1)
    glVertex2f(x + width, y + height)

    glTexCoord2f(0, 1)
    glVertex2f(x, y + height)
    glEnd()

    glDisable(GL_TEXTURE_2D)

def start_screen():
    pygame.init()
     
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
     
    image = pygame.image.load(r"Start.png") 
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if 260 <= x <= 380 and 330 <= y <= 380:
                        return
         
        screen.blit(image, (0,0))
         
        pygame.display.flip()

def Game_over():
    pygame.init()
     
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
     
    image = pygame.image.load(r"game over.png") 
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                     
                    if 490 <= x <= 610 and 390 <= y <= 450:
                        pygame.quit()
                        sys.exit()
                         
        screen.blit(image, (0, 0))
         
        pygame.display.flip()

def message_win():
    pygame.init()
     
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
     
    image = pygame.image.load(r"winner.png") 
    image = pygame.transform.scale(image, (WIDTH, HEIGHT))
     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                     
                    if 440 <= x <= 560 and 360 <= y <= 420:
                        pygame.quit()
                        sys.exit()
                         
        screen.blit(image, (0, 0))
         
        pygame.display.flip()

 
def main():
    global snake, snake_direction, food, score, speed

    start_screen()

    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        snake_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

        if check_wall_collision(snake_head):
            game_over = True

        if snake_head == food:
            snake.insert(0, food)
            score += 1
            if score >= 5:
                speed += 2
            if score >= 10:
                speed += 4
            if score >= 15:
                speed += 6
            if score >= 20:
                speed += 8
            if score >= 25:
                speed += 10
            if score >= 30:
                speed += 12
            if score >= 35:
                speed += 14
            if score >= 40:
                speed += 16
            if score >= 45:
                speed += 18
            if score >= 50:
                speed += 20
            if score >= 55:
                speed += 22
            if score >= 60:
                speed += 24
            if score >= 65:
                speed += 26
            if score >= 70:
                speed += 28
            if score >= 75:
                speed += 30
            if score >= 80:
                speed += 32
            if score >= 85:
                speed += 34
            if score >= 90:
                speed += 36
            if score >= 95:
                speed += 38
            if score >= 100:
                speed += 40          

            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            if snake_head in snake[1:]:
                game_over = True
            else:
                snake.insert(0, snake_head)
                snake.pop()
                
         
        if len(snake) > 1:
            snake_tail = snake[-1]
            prev_tail = snake[-2]
            tail_rect = pygame.Rect(snake_tail[0] * GRID_SIZE, snake_tail[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)

            if prev_tail[0] < snake_tail[0]:   
                pygame.draw.polygon(screen, (0, 0, 0), [(tail_rect.left, tail_rect.top),
                                                          (tail_rect.right, tail_rect.centery),
                                                          (tail_rect.left, tail_rect.bottom)])
            elif prev_tail[0] > snake_tail[0]:   
                pygame.draw.polygon(screen, (0, 0, 0), [(tail_rect.left, tail_rect.top),
                                                        (tail_rect.right, tail_rect.centery),
                                                        (tail_rect.left, tail_rect.bottom)])
            elif prev_tail[1] < snake_tail[1]:   
                pygame.draw.polygon(screen, (0, 0, 0), [(tail_rect.left, tail_rect.top),
                                                          (tail_rect.right, tail_rect.top),
                                                          (tail_rect.left + GRID_SIZE // 2, tail_rect.bottom)])
            elif prev_tail[1] > snake_tail[1]:   
                pygame.draw.polygon(screen, (0, 0, 0), [(tail_rect.left, tail_rect.bottom),
                                                          (tail_rect.right, tail_rect.bottom),
                                                          (tail_rect.left + GRID_SIZE // 2, tail_rect.top)])

        screen.fill((255,70,190))
        draw_snake(snake)
        draw_food(food)

         
        if 0 <= score < 5:
            score_text = font.render("Level 1 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 5 <= score < 10:
            score_text = font.render("Level 2 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 10 <= score < 15:
            score_text = font.render("Level 3 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 15 <= score < 20:    
            score_text = font.render("Level 4 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 20 <= score < 25:
            score_text = font.render("Level 5 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 25 <= score < 30:
            score_text = font.render("Level 6 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 30 <= score < 35:    
            score_text = font.render("Level 7 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))    
        if 35 <= score < 40:    
            score_text = font.render("Level 8 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 40 <= score < 45:
            score_text = font.render("Level 9 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 45 <= score < 50:
            score_text = font.render("Level 10 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 50 <= score < 55:    
            score_text = font.render("Level 11 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 55 <= score < 60:
            score_text = font.render("Level 12 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 60 <= score < 65:
            score_text = font.render("Level 13 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 65 <= score < 70:
            score_text = font.render("Level 14 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 70 <= score < 75:    
            score_text = font.render("Level 15 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 75 <= score < 80:
            score_text = font.render("Level 16 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 80 <= score < 85:
            score_text = font.render("Level 17 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 85 <= score < 90:    
            score_text = font.render("Level 18 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))    
        if 90 <= score < 95:    
            score_text = font.render("Level 19 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 95 <= score < 100:
            score_text = font.render("Level 20 - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10))
        if 100 <= score  :
            score_text = font.render("Level ∞ - Score: " + str(score), True, WHITE)
            screen.blit(score_text, (10, 10)) 

        pygame.display.update()
        clock.tick(speed)

     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((255,70,190))
        if score >= 100:
            message_win() 
                
            return   
        else:
            Game_over()
             
        pygame.display.update()
 

if __name__ == "__main__":
    main()