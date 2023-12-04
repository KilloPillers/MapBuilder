import pygame
import sys
from ButtonClass import ButtonClass

Grid_Width = 20
Grid_Height = 20
ButtonGrid = [0 for _ in range(Grid_Width*Grid_Height)]

pygame.init()

BACKGROUND_COLOR = (49, 51, 55)
DEFAULT_BUTTON_COLOR = (30, 31, 34)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

for x in range(Grid_Width):
    for y in range(Grid_Height):
        ButtonGrid[(y*Grid_Height)+x] = ButtonClass(75*x, 75*y, 75, 75, DEFAULT_BUTTON_COLOR, "5")

dragging = False
selecting = False
start_pos = None
end_pos = None
camera_offset = [0,0]
dragging_camera = False
zoom_factor = 1.0
selection_surface = pygame.Surface((800, 600), pygame.SRCALPHA)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 = left mouse button, 2 = middle, 3 = right
                dragging = True
                selecting = True
                start_pos = event.pos
                for button in ButtonGrid:
                    if button.zoom_rect.collidepoint(event.pos):
                        button.color = (0, 255, 0)
            if event.button == 3:
                dragging = True
                selecting = False
                start_pos = event.pos
                for button in ButtonGrid:
                    if button.zoom_rect.collidepoint(event.pos):
                        button.color = DEFAULT_BUTTON_COLOR
            if event.button == 2: # moving camera_pos
                dragging_camera = True
                prev_mouse_pos = pygame.mouse.get_pos()
            # Zooming
            if event.button == 4:  # Scroll up
                zoom_factor *= 1.01  # Increase zoom
                for x in range(Grid_Width):
                    for y in range(Grid_Height):
                        ButtonGrid[(y*Grid_Height)+x].zoom(zoom_factor, pygame.mouse.get_pos())
            elif event.button == 5:  # Scroll down
                zoom_factor /= 1.01  # Decrease zoom
                for x in range(Grid_Width):
                    for y in range(Grid_Height):
                        ButtonGrid[(y*Grid_Height)+x].zoom(zoom_factor, pygame.mouse.get_pos())
                
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                start_pos = None
                end_pos = None
            if event.button == 2:
                dragging_camera = False
            if event.button == 3:
                dragging = False
                start_pos = None
                end_pos = None

        if event.type == pygame.MOUSEMOTION:
            # Code for highlighting buttons on hover
            #for button in ButtonGrid:
            #    if button.isOver(event.pos):
            #        button.color = (0, 0, 255)
            #    else:
            #        button.color = (255, 0, 0)
            if dragging:
               end_pos = event.pos
            if dragging_camera:
                current_mouse_pos = pygame.mouse.get_pos()
                dx = current_mouse_pos[0] - prev_mouse_pos[0]
                dy = current_mouse_pos[1] - prev_mouse_pos[1]
                camera_offset[0] += dx
                camera_offset[1] += dy
                prev_mouse_pos = current_mouse_pos
                for x in range(Grid_Width):
                    for y in range(Grid_Height):
                        #adjut position of button based on camera_pos
                        ButtonGrid[(y*Grid_Height)+x].zoom_rect.move_ip(dx, dy)
                        ButtonGrid[(y*Grid_Height)+x].rect.move_ip(dx, dy)
                # Update button position
    
    screen.fill(BACKGROUND_COLOR)  # Fill the screen with white
    for x in range(Grid_Width):
        for y in range(Grid_Height):
            ButtonGrid[(y*Grid_Height)+x].draw(screen)

    if dragging and start_pos and end_pos:
        selection_surface.fill((0, 0, 0, 0)) # Clear previous rectangle
        
        top_left_x = min(start_pos[0], end_pos[0])
        top_left_y = min(start_pos[1], end_pos[1])
        width = abs(end_pos[0] - start_pos[0])
        height = abs(end_pos[1] - start_pos[1])
        
        selection_rect = pygame.Rect(top_left_x, top_left_y, width, height) 
        pygame.draw.rect(selection_surface, (0, 128, 255, 100), selection_rect)  # RGBA, 100 alpha for transparency
        screen.blit(selection_surface, (0, 0))
        
        for button in ButtonGrid:
            if selection_rect.colliderect(button.zoom_rect):
                #change color of button
                button.color = (0, 255, 0) if selecting else DEFAULT_BUTTON_COLOR

    pygame.display.flip()
