import os
import pygame
import sys
import tkinter as tk
from ButtonClass import ButtonClass
from pygame.locals import DOUBLEBUF

BACKGROUND_COLOR = (49, 51, 55)
DEFAULT_BUTTON_COLOR = (30, 31, 34)

class PygameInterface():
    def __init__(self, embed, width, height, grid_width, grid_height):
        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        os.environ['SDL_VIDEODRIVER'] = 'windib'
        pygame.init()
        self.grid_width = grid_width
        self.grid_height = grid_height
        
        self.ButtonGrid = [0 for _ in range(self.grid_width*self.grid_height)]
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                self.ButtonGrid[(y*self.grid_height)+x] = ButtonClass(75*x, 75*y, 75, 75, DEFAULT_BUTTON_COLOR, "5")
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF)
        
        self.dragging = False
        self.selecting = False
        
        self.start_pos = None
        self.end_pos = None
        
        self.camera_offset = [0,0]
        self.prev_mouse_pos = None
        self.dragging_camera = False
        self.zoom_factor = 1.0
        self.selection_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 = left mouse button, 2 = middle, 3 = right
                    self.dragging = True
                    self.selecting = True
                    self.start_pos = event.pos
                    for button in self.ButtonGrid:
                        if button.zoom_rect.collidepoint(event.pos):
                            button.color = (0, 255, 0)
                
                if event.button == 3:
                    self.dragging = True
                    self.selecting = False
                    self.start_pos = event.pos
                    for button in self.ButtonGrid:
                        if button.zoom_rect.collidepoint(event.pos):
                            button.color = DEFAULT_BUTTON_COLOR
                
                if event.button == 2: # moving camera_pos
                    self.dragging_camera = True
                    self.prev_mouse_pos = pygame.mouse.get_pos()
                
                # Zooming
                if event.button == 4:  # Scroll up
                    self.zoom_factor *= 1.01  # Increase zoom
                    for x in range(self.grid_width):
                        for y in range(self.grid_height):
                            self.ButtonGrid[(y*self.grid_height)+x].zoom(self.zoom_factor, pygame.mouse.get_pos())
                elif event.button == 5:  # Scroll down
                    self.zoom_factor /= 1.01  # Decrease zoom
                    for x in range(self.grid_width):
                        for y in range(self.grid_height):
                            self.ButtonGrid[(y*self.grid_height)+x].zoom(self.zoom_factor, pygame.mouse.get_pos())
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging = False
                    self.start_pos = None
                    self.end_pos = None
                if event.button == 2:
                    self.dragging_camera = False
                if event.button == 3:
                    self.dragging = False
                    self.start_pos = None
                    self.end_pos = None

            if event.type == pygame.MOUSEMOTION:
                # Code for highlighting buttons on hover
                #for button in ButtonGrid:
                #    if button.isOver(event.pos):
                #        button.color = (0, 0, 255)
                #    else:
                #        button.color = (255, 0, 0)
                if self.dragging:
                   self.end_pos = event.pos
                if self.dragging_camera:
                    current_mouse_pos = pygame.mouse.get_pos()
                    dx = current_mouse_pos[0] - self.prev_mouse_pos[0]
                    dy = current_mouse_pos[1] - self.prev_mouse_pos[1]
                    self.camera_offset[0] += dx
                    self.camera_offset[1] += dy
                    self.prev_mouse_pos = current_mouse_pos
                    for x in range(self.grid_width):
                        for y in range(self.grid_height):
                            #adjut position of button based on camera_pos
                            self.ButtonGrid[(y*self.grid_width)+x].zoom_rect.move_ip(dx, dy)
                            self.ButtonGrid[(y*self.grid_height)+x].rect.move_ip(dx, dy) 

    def update_screen(self):
        self.screen.fill(BACKGROUND_COLOR)  # Fill the screen with white
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                self.ButtonGrid[(y*self.grid_height)+x].draw(self.screen)
        if self.dragging and self.start_pos and self.end_pos:
            self.selection_surface.fill((0, 0, 0, 0)) # Clear previous rectangle
        
            top_left_x = min(self.start_pos[0], self.end_pos[0])
            top_left_y = min(self.start_pos[1], self.end_pos[1])
            width = abs(self.end_pos[0] - self.start_pos[0])
            height = abs(self.end_pos[1] - self.start_pos[1])
            
            selection_rect = pygame.Rect(top_left_x, top_left_y, width, height) 
            pygame.draw.rect(self.selection_surface, (0, 128, 255, 100), selection_rect)  # RGBA, 100 alpha for transparency
            self.screen.blit(self.selection_surface, (0, 0))
            
            for button in self.ButtonGrid:
                if selection_rect.colliderect(button.zoom_rect):
                    #change color of button
                    button.color = (0, 255, 0) if self.selecting else DEFAULT_BUTTON_COLOR
        pygame.display.flip()


def tkinter_update():
    pygame_interface.handle_events()
    pygame_interface.update_screen()
    root.after(5, tkinter_update)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Map Editor")
    embed = tk.Frame(root, width=500, height=500)
    embed.pack()
    pygame_interface = PygameInterface(embed, 800, 600, 10, 10)
    #while True:
    #    pygame_interface.handle_events()
    #    pygame_interface.update_screen()
    #    pygame.display.update()
    root.after(5, tkinter_update)
    root.mainloop()

