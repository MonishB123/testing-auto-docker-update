import pygame
import sys

def main():

    # Initialize pygame
    pygame.init()

    # Set up the display
    window_size = (400, 300)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Hello World Window")

    # Set up font
    font = pygame.font.Font(None, 36)  # Default font, size 36
    text = font.render("Hello, World!", True, (255, 255, 255))  # White text
    text_rect = text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the window with a color (e.g., black)
        window.fill((0, 0, 0))

        # Blit the text onto the window
        window.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()