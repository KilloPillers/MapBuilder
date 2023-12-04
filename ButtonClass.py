import pygame

class ButtonClass:
    def __init__(self, x, y, width, height, color, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.zoom_rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = (145, 150, 159)
        self.border_color = (145, 150, 159)
        self.border_thickness = 2
        self.font_size = 30
        self.zoom_font_size = 30

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, self.zoom_rect, 0)
        pygame.draw.rect(win, self.border_color, self.zoom_rect.inflate(self.border_thickness * 2, self.border_thickness * 2))
        pygame.draw.rect(win, self.color, self.zoom_rect, 0)
        
        if self.text != '':
            font = pygame.font.SysFont('arial', self.zoom_font_size)
            text = font.render(self.text, 1, self.text_color)
            win.blit(text, (self.zoom_rect.x + (self.zoom_rect.width / 2 - text.get_width() / 2),
                            self.zoom_rect.y + (self.zoom_rect.height / 2 - text.get_height() / 2)))

    def zoom(self, zoom, focus):
        self.zoom_rect = pygame.Rect(
                round((self.rect.x - focus[0]) * zoom + focus[0]),
                round((self.rect.y - focus[1]) * zoom + focus[1]),
                round(self.rect.width * zoom),
                round(self.rect.height * zoom))
        if self.text != '':
            self.zoom_font_size = int(self.font_size * zoom)


    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.rect.x < pos[0] < self.rect.x + self.rect.width:
            if self.rect.y < pos[1] < self.rect.y + self.rect.height:
                return True
        return False
