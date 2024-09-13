# import pygame
# # Initialize Pygame
# pygame.init()
# # Set up display (required for Pygame window to appear)
# screen = pygame.display.set_mode((400, 300))
# # Main game loop
# running = True
# while running:
#     # Check for events (like quitting the window)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     # Get the current state of the keyboard
#     keys = pygame.key.get_pressed()
#     # Check if spacebar is pressed
#     if keys[pygame.K_SPACE]:
#         print("Spacebar is pressed")
#     # Update the display (required for changes to be shown)
#     pygame.display.flip()
# # Quit Pygame
# pygame.quit()

# import pygame
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the display
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Mouse Events Example")
#
# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print(f"Mouse Button Down at {event.pos} with button {event.button}")
#         elif event.type == pygame.MOUSEBUTTONUP:
#             print(f"Mouse Button Up at {event.pos} with button {event.button}")
#         elif event.type == pygame.MOUSEMOTION:
#             print(f"Mouse Moved to {event.pos}")
#
#     # Fill the screen with a color
#     screen.fill((255, 255, 255))
#
#     # Update the display
#     pygame.display.flip()
#
# # Quit Pygame
# pygame.quit()

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Events Example")

# Define custom event types
CUSTOM_EVENT = pygame.USEREVENT + 1
ANOTHER_CUSTOM_EVENT = pygame.USEREVENT + 2

# Post a custom event to the event queue
pygame.event.post(pygame.event.Event(CUSTOM_EVENT, {"info": "Custom Event Triggered!"}))
pygame.event.post(pygame.event.Event(ANOTHER_CUSTOM_EVENT, {"data": 123}))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CUSTOM_EVENT:
            print(f"Custom Event: {event.dict['info']}")
        elif event.type == ANOTHER_CUSTOM_EVENT:
            print(f"Another Custom Event: {event.dict['data']}")

    # Fill the screen with a color
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
