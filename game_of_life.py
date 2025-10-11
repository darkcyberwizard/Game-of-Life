
import pygame
import random
import pygameMenu
from pygameMenu.locals import *
import os

# *****************************************************************************
# Info text for the About Menu
# *****************************************************************************

ABOUT = ['Game of Life:',
         'Cellular Automaton devised by John Conway',
         PYGAMEMENU_TEXT_NEWLINE,
         'Author: Nipuna Weeratunge',
         PYGAMEMENU_TEXT_NEWLINE,
         'Email: nipunaw1@gmail.com']

# *****************************************************************************
# Info text for the Help Menu
# *****************************************************************************

HELP = ['Controls:',
         'Select the initial pattern. The default pattern is Glider.',
         PYGAMEMENU_TEXT_NEWLINE,
         'Select cell update rate in ms. ']


# *****************************************************************************
# Window and PyGame values  for initialization
# *****************************************************************************
WINDOW_START_POSITION_X = 200
WINDOW_START_POSITION_Y = 50 

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0,255, 0)
RED = (255, 0, 0)
GREY = (128,128,128)
BLUE = (0, 0, 250) 

# Width & Height of each cell
WIDTH = 10
HEIGHT = 10

# Set start position of window on screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WINDOW_START_POSITION_X,WINDOW_START_POSITION_Y) 

# Margin between each cell
MARGIN = 2

# Width & Height of window
WINDOW_SIZE = [1020, 768]

# PyGame Initialization
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set window title
pygame.display.set_caption("Game of Life")

# Set size & font for generation info
generation_info_text = pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30)

# Game loop execution variable
is_done = False
 
# Clock to update screen periodically
clock = pygame.time.Clock()

# Timing counters
current_time = 0
erase_time = 0

# Set Game speed
GAME_SPEED = 500

# Set Start Pattern
START_PATTERN = ['Glider']

# Start Pattern Selection
start_pattern_selected=False

# Row and Column count
row_count = WINDOW_SIZE[1]//(WIDTH + MARGIN)
col_count = WINDOW_SIZE[0]//(WIDTH + MARGIN)

# Cell count on grid
cell_count = row_count*col_count

# List to hold relative distance to 8 neighbouring cells
neighbour_cell_offset_list = [-86,-85,-84,-1, +1, +84, +85 , +86]

# Draw initial pattern on screen
draw_initial_pattern = True

# List to hold cell status Active/Inactive/Operation
cell_status_list = []

# Initialize all cell status to Inactive (0)
for cell in range(cell_count):
    cell_status_list.append(0)
    
# Iteration Counter
generation_no=0

# *****************************************************************************
# Define clear grid methods
# *****************************************************************************

def clear_grid():

    global cell_count

    # Clear all cells to zero
    for cell in range(cell_count):
        cell_status_list[cell]=0

# *****************************************************************************
# Define pattern methods
# *****************************************************************************

# Randomly animate 3000 cells on screen
def random_pattern():

    for cell in random.sample(range(0, cell_count), 3000):
        cell_status_list[cell] = 1    

# Draw glider
def glider():

    cell_status_list[4629] = 1
    cell_status_list[4714] = 1
    cell_status_list[4799] = 1
    cell_status_list[4628] = 1
    cell_status_list[4712] = 1

# Draw beacon
def beacon():

    cell_status_list[2675] = 1
    cell_status_list[2676] = 1
    cell_status_list[2760] = 1
    cell_status_list[2761] = 1
    cell_status_list[2847] = 1
    cell_status_list[2848] = 1
    cell_status_list[2932] = 1
    cell_status_list[2933] = 1

# Draw toad
def toad():

    cell_status_list[2675] = 1
    cell_status_list[2760] = 1
    cell_status_list[2846] = 1
    cell_status_list[2678] = 1
    cell_status_list[2763] = 1
    cell_status_list[2592] = 1

# Draw blinker
def blinker():

    cell_status_list[2675] = 1
    cell_status_list[2760] = 1
    cell_status_list[2845] = 1

# Draw tetromino
def tetromino():

    cell_status_list[2675] = 1
    cell_status_list[2674] = 1
    cell_status_list[2676] = 1
    cell_status_list[2590] = 1

# Draw pulsar
def pulsar():

    cell_status_list[2675] = 1
    cell_status_list[2676] = 1
    cell_status_list[2677] = 1
    cell_status_list[2681] = 1
    cell_status_list[2682] = 1
    cell_status_list[2683] = 1
    cell_status_list[2843] = 1
    cell_status_list[2928] = 1
    cell_status_list[3013] = 1
    cell_status_list[2848] = 1
    cell_status_list[2933] = 1
    cell_status_list[3018] = 1
    cell_status_list[3100] = 1
    cell_status_list[3101] = 1
    cell_status_list[3102] = 1
    cell_status_list[2850] = 1
    cell_status_list[2935] = 1
    cell_status_list[3020] = 1
    cell_status_list[3106] = 1
    cell_status_list[3107] = 1
    cell_status_list[3108] = 1
    cell_status_list[2855] = 1
    cell_status_list[2940] = 1
    cell_status_list[3025] = 1
    cell_status_list[3270] = 1
    cell_status_list[3271] = 1
    cell_status_list[3272] = 1
    cell_status_list[3276] = 1
    cell_status_list[3277] = 1
    cell_status_list[3278] = 1
    cell_status_list[3358] = 1
    cell_status_list[3443] = 1
    cell_status_list[3528] = 1
    cell_status_list[3360] = 1
    cell_status_list[3445] = 1
    cell_status_list[3530] = 1
    cell_status_list[3353] = 1
    cell_status_list[3438] = 1
    cell_status_list[3523] = 1
    cell_status_list[3695] = 1
    cell_status_list[3696] = 1
    cell_status_list[3697] = 1
    cell_status_list[3701] = 1
    cell_status_list[3702] = 1
    cell_status_list[3703] = 1
    cell_status_list[3365] = 1
    cell_status_list[3450] = 1
    cell_status_list[3535] = 1

# Draw light weight spacechip
def light_weight_spaceship():

    cell_status_list[2675] = 1
    cell_status_list[2678] = 1
    cell_status_list[2764] = 1
    cell_status_list[2849] = 1
    cell_status_list[2934] = 1
    cell_status_list[2933] = 1
    cell_status_list[2932] = 1
    cell_status_list[2931] = 1
    cell_status_list[2845] = 1 

# Draw copperhead spaceship
def copperhead_spaceship():

    cell_status_list[3438] = 1
    cell_status_list[3439] = 1
    cell_status_list[3442] = 1
    cell_status_list[3443] = 1
    cell_status_list[3525] = 1
    cell_status_list[3526] = 1
    cell_status_list[3610] = 1
    cell_status_list[3611] = 1
    cell_status_list[3692] = 1
    cell_status_list[3694] = 1
    cell_status_list[3697] = 1
    cell_status_list[3699] = 1
    cell_status_list[3777] = 1
    cell_status_list[3784] = 1
    cell_status_list[3947] = 1
    cell_status_list[3954] = 1
    cell_status_list[4033] = 1
    cell_status_list[4034] = 1
    cell_status_list[4037] = 1
    cell_status_list[4038] = 1
    cell_status_list[4119] = 1
    cell_status_list[4120] = 1
    cell_status_list[4121] = 1
    cell_status_list[4122] = 1
    cell_status_list[4290] = 1
    cell_status_list[4291] = 1
    cell_status_list[4375] = 1
    cell_status_list[4376] = 1

# Draw weekender
def weekender():

    cell_status_list[5308] = 1
    cell_status_list[5309] = 1
    cell_status_list[5312] = 1
    cell_status_list[5313] = 1
    cell_status_list[5222] = 1
    cell_status_list[5229] = 1
    cell_status_list[5050] = 1
    cell_status_list[5051] = 1
    cell_status_list[5052] = 1
    cell_status_list[5053] = 1
    cell_status_list[5058] = 1
    cell_status_list[5059] = 1
    cell_status_list[5060] = 1
    cell_status_list[5061] = 1
    cell_status_list[4969] = 1
    cell_status_list[4970] = 1
    cell_status_list[4971] = 1
    cell_status_list[4972] = 1
    cell_status_list[4884] = 1
    cell_status_list[4885] = 1
    cell_status_list[4886] = 1
    cell_status_list[4887] = 1
    cell_status_list[4880] = 1
    cell_status_list[4891] = 1
    cell_status_list[4794] = 1
    cell_status_list[4807] = 1
    cell_status_list[4709] = 1
    cell_status_list[4722] = 1
    cell_status_list[4623] = 1
    cell_status_list[4625] = 1
    cell_status_list[4636] = 1
    cell_status_list[4638] = 1
    cell_status_list[4539] = 1
    cell_status_list[4552] = 1
    cell_status_list[4454] = 1
    cell_status_list[4467] = 1

# Draw Gosper Glider Gun
def gosper_glider_gun():

    cell_status_list[2470] = 1
    cell_status_list[2471] = 1
    cell_status_list[2555] = 1
    cell_status_list[2556] = 1
    cell_status_list[2480] = 1
    cell_status_list[2565] = 1
    cell_status_list[2650] = 1
    cell_status_list[2396] = 1
    cell_status_list[2736] = 1
    cell_status_list[2312] = 1
    cell_status_list[2313] = 1
    cell_status_list[2822] = 1
    cell_status_list[2823] = 1
    cell_status_list[2400] = 1
    cell_status_list[2486] = 1
    cell_status_list[2569] = 1
    cell_status_list[2571] = 1
    cell_status_list[2572] = 1
    cell_status_list[2656] = 1
    cell_status_list[2740] = 1
    cell_status_list[2320] = 1
    cell_status_list[2321] = 1
    cell_status_list[2405] = 1
    cell_status_list[2406] = 1
    cell_status_list[2490] = 1
    cell_status_list[2491] = 1
    cell_status_list[2237] = 1
    cell_status_list[2239] = 1
    cell_status_list[2154] = 1
    cell_status_list[2577] = 1
    cell_status_list[2579] = 1
    cell_status_list[2664] = 1
    cell_status_list[2334] = 1
    cell_status_list[2335] = 1
    cell_status_list[2419] = 1
    cell_status_list[2420] = 1

# *****************************************************************************
# Define method to draw start screen
# *****************************************************************************
def draw_initial_screen():

    # Fill screen with Grey
    screen.fill(GREY) 
    

# *****************************************************************************
# Define method to select start pattern
# *****************************************************************************
def change_start_pattern(d):

    # Initialize grid
    clear_grid()

    # Call global variables
    global START_PATTERN
    global start_pattern_selected

    START_PATTERN[0] = d

    if START_PATTERN[0] == 'Glider':
        glider()

    elif START_PATTERN[0] == 'Beacon':
        beacon()
    
    elif START_PATTERN[0] == 'Toad':
        toad()
    
    elif START_PATTERN[0] == 'Blinker':
        blinker()
    
    elif START_PATTERN[0] == 'Tetromino':
        tetromino()
    
    elif START_PATTERN[0] == 'Pulsar':
        pulsar()

    elif START_PATTERN[0] == 'Light Weight Spaceship':
        light_weight_spaceship()

    elif START_PATTERN[0] == 'Copperhead Spaceship':
        copperhead_spaceship()
    
    elif START_PATTERN[0] == 'Weekender':
        weekender()

    elif START_PATTERN[0] == 'Gosper Glider Gun':
        gosper_glider_gun()

    elif START_PATTERN[0] == 'Random':
        random_pattern()

    else:
        random_pattern()

    # Set variable to draw start pattern
    start_pattern_selected = True

# *****************************************************************************
# Define method to select game speed
# *****************************************************************************
def change_game_speed(d):

    # Call global speed variable
    global GAME_SPEED
    
    GAME_SPEED = d


# *****************************************************************************
# Define method to draw grid
# *****************************************************************************
def draw_grid():

    # Call global draw_initial_pattern 
    global draw_initial_pattern

    # Call global cell count
    global cell_count

    # Call global generation info 
    global generation_no

    # Increment generation no
    generation_no += 1

    # Render generation info 
    generation_info_count = generation_info_text.render('Generation No: '+str(generation_no), 1, WHITE)
    
    # Iterate for each cell on grid
    for cell in range(cell_count):

        # Calculate row and column no from cell no
        row_no = int(cell/85)
        col_no = cell%85

        # Counter for no of active neighbours
        active_neighbour_count = 0
        
        # Set color as Green for Active cells
        if cell_status_list[cell] == 1:
            color = GREEN
        
        # Set color as Grey for Inactive cells
        elif cell_status_list[cell] == 0:
            color = GREY

        # Iterate for each cell neighbour
        for offset in neighbour_cell_offset_list:

            # Check active neighbour count for each cell
            # And increase count
            if (cell+offset >= 0 and cell+offset < cell_count and (cell_status_list[cell+offset] == 1 or cell_status_list[cell+offset] >= 3 )):
                active_neighbour_count += 1

        # *****************************************************************************
        # Define rules for Game of Life
        # *****************************************************************************  
        
        # Continue if initial pattern on screen has been drawn  
        if draw_initial_pattern == False:
            
            # Reproduction
            # Mark cell as active for next iteration
            if active_neighbour_count == 3 and cell_status_list[cell] == 0:
                color = GREEN
                cell_status_list[cell] = 2

            # Isolation
            # Mark cell as inactive for next iteration
            elif active_neighbour_count <= 1 and cell_status_list[cell] == 1:
                color = GREY
                cell_status_list[cell] = 3
  
            # Survival
            # Mark cell as active for next iteration
            elif active_neighbour_count >= 2 and active_neighbour_count <= 3 and cell_status_list[cell] == 1:
                color = GREEN
                cell_status_list[cell] = 4
                    
            # Overpopulation
            # Mark cell as inactive for next iteration
            elif active_neighbour_count >= 4 and cell_status_list[cell] == 1:
                color = GREY
                cell_status_list[cell] = 5

        # Draw cell according to above rules
        pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * col_no + MARGIN,
                                (MARGIN + HEIGHT) * row_no + MARGIN,
                                WIDTH,
                                HEIGHT])

    # Display generation info
    screen.blit(generation_info_count, (800, 30))

    # Update PyGame display
    pygame.display.flip()

    # Update any cell operation status 
    # As Active or Inactive for next iteration
    for cell in range(cell_count):

        # Set cell operation status Survival & Reproduction to Active
        if cell_status_list[cell] == 2 or cell_status_list[cell] == 4:
            cell_status_list[cell] = 1

        # Set cell operation status Isolation & Overpopulation to Inactive
        elif cell_status_list[cell] == 3 or cell_status_list[cell] == 5:
            cell_status_list[cell] = 0
   

def Game_Loop():

    # Call global draw_initial_pattern 
    global draw_initial_pattern

    # Call global game speed
    global GAME_SPEED

    # Call global loop execution varibale
    global is_done

    # Call global timing counters
    global current_time
    global erase_time

    # Call global start pattern variable
    global start_pattern_selected

    # Call global generation info
    global generation_no
 
    # Draw Glider pattern if a start pattern is not selected
    if not start_pattern_selected:
        clear_grid
        glider()
        start_pattern_selected=True

    # Disable and reset Main Menu
    main_menu.disable()
    main_menu.reset(1)

    # Reset generation no if game loop restarts
    generation_no =0

    # Run loop until user event
    while not is_done:

        # Check for Pygame events
        events = pygame.event.get()

        
        # Check for user events
        for event in events:  

            # If user closes window
            if event.type == pygame.QUIT: 
                
                # Disable execution loop
                is_done = True

                # Exit Main Loop
                exit()

            # If user presses Esc key
            elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE and main_menu.is_disabled():

                # Enable main menu
                main_menu.enable() 

        # Pass Pygame event to Main Menu
        main_menu.mainloop(events) 

        # Set screen background to Black and draw grid every 50 ms
        if pygame.time.get_ticks() - current_time >= GAME_SPEED:
            screen.fill(BLACK) 
            current_time = pygame.time.get_ticks()
            draw_grid()

        # Set initial pattern as drawn after 1 second 
        elif pygame.time.get_ticks() - erase_time >= 1000 and draw_initial_pattern == True:
            draw_initial_pattern = False

        # Limit screen update speed to 60 fps
        clock.tick(60)
    
    # Call PyGame exit routines and exit program
    pygame.quit()


# Main Menu of the game
main_menu = pygameMenu.Menu(screen,
                            bgfun = draw_initial_screen,
                            color_selected = RED,
                            font = pygameMenu.fonts.FONT_BEBAS,
                            font_color = BLACK,
                            font_size = 30,
                            menu_alpha = 50,
                            menu_color = BLACK,
                            menu_color_title = BLUE,
                            menu_height = int(WINDOW_SIZE[1] * 0.7),
                            menu_width = int(WINDOW_SIZE[0] * 0.7),
                            onclose = PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow = False,
                            title = 'Main menu',
                            window_height = WINDOW_SIZE[1],
                            window_width = WINDOW_SIZE[0]
                            )

# About Menu where players can see information about the game
about_menu = pygameMenu.TextMenu(screen,
                                 bgfun = draw_initial_screen,
                                 color_selected = RED,
                                 font = pygameMenu.fonts.FONT_BEBAS,
                                 font_color = BLACK,
                                 font_size_title = 30,
                                 font_title = pygameMenu.fonts.FONT_8BIT,
                                 menu_alpha = 50,
                                 menu_color = BLACK,
                                 menu_color_title = BLUE,
                                 menu_height = int(WINDOW_SIZE[1] * 0.7),
                                 menu_width = int(WINDOW_SIZE[0] * 0.7),
                                 onclose = PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow = False,
                                 text_color = BLACK,
                                 text_fontsize = 20,
                                 title = 'About',
                                 window_height = WINDOW_SIZE[1],
                                 window_width = WINDOW_SIZE[0]
                                 )

# Help Menu where players can see information about game controls
help_menu = pygameMenu.TextMenu(screen,
                                 bgfun = draw_initial_screen,
                                 color_selected = RED,
                                 font = pygameMenu.fonts.FONT_BEBAS,
                                 font_color = BLACK,
                                 font_size_title = 30,
                                 font_title = pygameMenu.fonts.FONT_8BIT,
                                 menu_alpha = 50,
                                 menu_color = BLACK,
                                 menu_color_title = BLUE,
                                 menu_height = int(WINDOW_SIZE[1] * 0.7),
                                 menu_width = int(WINDOW_SIZE[0] * 0.7),
                                 onclose = PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow = False,
                                 text_color = BLACK,
                                 text_fontsize = 20,
                                 title = 'Help',
                                 window_height = WINDOW_SIZE[1],
                                 window_width = WINDOW_SIZE[0]
                                 )

# Play Menu where players can change start pattern and game speed 
play_menu = pygameMenu.Menu(screen,
                            bgfun = draw_initial_screen,
                            color_selected = RED,
                            font = pygameMenu.fonts.FONT_BEBAS,
                            font_color = BLACK,
                            font_size = 30,
                            menu_alpha = 50,
                            menu_color = BLACK,
                            menu_color_title = BLUE,
                            menu_height = int(WINDOW_SIZE[1] * 0.7),
                            menu_width = int(WINDOW_SIZE[0] * 0.7),
                            onclose = PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow = False,
                            title = 'Play menu',
                            window_height = WINDOW_SIZE[1],
                            window_width = WINDOW_SIZE[0]
                            )

# Calls play_function when Start Game is pressed
play_menu.add_option('Start Game', Game_Loop)

# Selector to select start pattern
# On change calls change_start_pattern function
play_menu.add_selector('Select Start Pattern', [('Glider', 'Glider'),
                                             ('Beacon', 'Beacon'),
                                             ('Toad', 'Toad'),
                                             ('Blinker', 'Blinker'),
                                             ('Tetromino', 'Tetromino'),
                                             ('Pulsar', 'Pulsar'),
                                             ('Light Weight Spaceship', 'Light Weight Spaceship'),
                                             ('Copperhead Spaceship', 'Copperhead Spaceship'),
                                             ('Weekender', 'Weekender'),
                                             ('Gosper Glider Gun', 'Gosper Glider Gun'),
                                             ('Random', 'Random')],
                       onreturn = None,
                       onchange = change_start_pattern)

# Selector to select game update speed
# On change calls change_game_speed function
play_menu.add_selector('Select Update Speed in ms', [('500', 500),
                                             ('400', 400),
                                             ('300', 300),
                                             ('200', 200),
                                             ('100', 100),
                                             ('50', 50)],
                       onreturn = None,
                       onchange = change_game_speed)

# Return to Main Menu when this option is selected
play_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

# Adding options to the Main Menu
main_menu.add_option('Play Game', play_menu)
main_menu.add_option('Help', help_menu)
main_menu.add_option('About', about_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)

# Write the game info on About Menu
for line in ABOUT:
    about_menu.add_line(line)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)

# Return to Main Menu when this option is selected
about_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

# Write the game controls info on Help Menu
for line in HELP:
    help_menu.add_line(line)
help_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)

# Return to Main Menu when this option is selected
help_menu.add_option('Return to main menu', PYGAME_MENU_BACK) 

# *****************************************************************************
# Main Program Loop
# *****************************************************************************

while True:

    # Set Frame Rate to 60 FPS
    clock.tick(60)

    # Check for Pygame events
    events = pygame.event.get()

    # Exit game if window is closed
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Pass Pygame event to Main Menu
    main_menu.mainloop(event)

    # Update screen
    pygame.display.flip()
