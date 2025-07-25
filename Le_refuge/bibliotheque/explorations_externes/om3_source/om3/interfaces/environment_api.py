# interfaces/environment_api.py

import pygame

class OM3Environment:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("OM3 Virtual Desktop")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)

        # Internal state
        self.text_buffer = ""
        self.mouse_x = width // 2
        self.mouse_y = height // 2
        self.running = True

    def apply_actions(self, action_tokens):
        for token in action_tokens:
            if token.startswith("KEY_PRESS_"):
                char = token.split("_")[-1].lower()
                self.text_buffer += char
            elif token == "MOUSE_MOVE_LEFT":
                self.mouse_x -= 10
            elif token == "MOUSE_MOVE_RIGHT":
                self.mouse_x += 10
            elif token == "MOUSE_MOVE_UP":
                self.mouse_y -= 10
            elif token == "MOUSE_MOVE_DOWN":
                self.mouse_y += 10

        # Clamp mouse within window
        self.mouse_x = max(0, min(self.width, self.mouse_x))
        self.mouse_y = max(0, min(self.height, self.mouse_y))

    def update(self):
        # Handle pygame quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Draw background
        self.screen.fill((30, 30, 30))

        # Draw text field (top 100px)
        pygame.draw.rect(self.screen, (50, 50, 50), (0, 0, self.width, 100))
        text_surface = self.font.render(self.text_buffer[-80:], True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 40))

        # Draw mouse cursor (circle)
        pygame.draw.circle(self.screen, (0, 255, 0), (self.mouse_x, self.mouse_y), 10)

        pygame.display.flip()
        self.clock.tick(30)  # Limit to 30 FPS

    def is_running(self):
        return self.running

    def close(self):
        pygame.quit()

if __name__ == "__main__":
    env = OM3Environment()
    while env.is_running():
        # Example test action: move right + type 'a'
        env.apply_actions(["MOUSE_MOVE_RIGHT", "KEY_PRESS_A"])
        env.update()
