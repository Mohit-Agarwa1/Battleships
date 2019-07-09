#!Python3 Battlehsips Game

print('USERNOTICE: Ignore any SyntaxWarning')

import pygame
import pygame_textinput
import random

a = pygame.image.load('square.png')
pygame.display.set_icon(a)
BLACK = (30, 30, 30)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
black = BLACK
white = WHITE
red = RED

DIFF_LIST = []

# CHANGE DIFFICULTY, from 0 to 8
DIFF_SET = 5

if DIFF_SET == -1:
    DIFF_LIST = [1]
if DIFF_SET == 0:
    DIFF_LIST = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if DIFF_SET == 1:
    DIFF_LIST = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if DIFF_SET == 2:
    DIFF_LIST = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if DIFF_SET == 3:
    DIFF_LIST = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if DIFF_SET == 4:
    DIFF_LIST = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if DIFF_SET == 5:
    DIFF_LIST = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if DIFF_SET == 6:
    DIFF_LIST = [0, 1, 1, 1, 1, 1, 1]
if DIFF_SET == 7:
    DIFF_LIST = [0, 1, 1]
if DIFF_SET == 8:
    DIFF_LIST = [0, 1]
if DIFF_SET == -2:
    DIFF_LIST = [0]

print('Diffset{}'.format(DIFF_SET))
WIDTH = 45
HEIGHT = 45
MARGIN = 5
bot_hitlist = []
bot_list_possible = []
for i in range(0, 5):
    for q in range(0, 9):
        list_cir = [[q, i], [q, i + 1], [q, i + 2], [q, i + 3]]
        bot_list_possible.append(list_cir)
for q in range(0, 5):
    for i in range(0, 9):
        list_cir = [[q, i], [q, i + 1], [q, i + 2], [q, i + 3]]
        bot_list_possible.append(list_cir)
bot_list_possible_l = []
# print(bot_list_possible)
listpotplay = []
grid = []
for row in range(10):

    grid.append([])
    for column in range(10):
        grid[row].append(0)

pygame.init()
upgrid = []
for row in range(10):

    upgrid.append([])
    for column in range(10):
        upgrid[row].append(0)

bpgrid = []
for row in range(10):

    bpgrid.append([])
    for column in range(10):
        bpgrid[row].append(0)

WINDOW_SIZE = [1250, 800]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Battleships by Mohit")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def button(msg, x, y, w, h, ic, ac, action=None, tyl=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            if tyl != None:
                action(tyl)
            else:
                action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("arial", 20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [i, x.index(v)]


def text_objects(text, font, color):
    white = (255, 255, 255)

    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    red = (200, 0, 0)
    bright_red = (255, 0, 0)
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def find(searchList, elem):
    return [[i for i, x in enumerate(searchList) if x == e] for e in elem]


def check_pg_one(a):
    al = a[1]
    count_a_1 = sum(x.count(1) for x in al)

    if count_a_1 != 13:
        page_one('Incorrect number selected')
    elif count_a_1 == 13:
        check_two_pg_one(a[1], [False, False, False, False])
        #                       4     4     4     1      2       1


def check_surround(x, y, ak, shipsused):
    h = False
    v = False
    E = False
    if ak[x][y] == 1:
        if ak[x + 1][y] == 1 or ak[x - 1][y] == 1:
            h = True
        elif ak[x][y + 1] == 1 or ak[x][y - 1] == 1:
            v = True
        if ak[x + 1][y + 1] == 1 or ak[x - 1][y - 1] == 1 or ak[x + 1][y - 1] == 1 or ak[x - 1][y + 1] == 1:
            E = True

    if E == True:
        page_one('error in placement')
    if v == True and h == True:
        page_one('error  in placement')
    if h != True and v != True and E != True:
        if shipsused[3] == True:
            page_one('error  in placement')
        shipsused[3] = True
        ak[x][y] = 0
        check_two_pg_one(ak, shipsused)

    elif h == True and v == False:
        s = ak[x]
        if s.count(1) == 4:
            if shipsused[0] == False:
                shipsused[0] = True
            elif shipsused[1] == False:
                shipsused[1] = True
            elif shipsused[2] == False:
                shipsused[2] = True
            elif shipsused[1] == True and shipsused[0] == True and shipsused[2] == True:
                page_one('error  in placement')
    elif h == False and v == True:
        s = []
        for i in ak:
            s.append(i[y])
        if s.count(1) == 4:
            if shipsused[0] == False:
                shipsused[0] = True
            elif shipsused[1] == False:
                shipsused[1] = True
            elif shipsused[2] == False:
                shipsused[2] = True
            elif shipsused[1] == True and shipsused[0] == True and shipsused[2] == True:
                page_one('error  in placement')


def gen_bot():
    gridbot = []
    for row in range(10):

        gridbot.append([])
        for column in range(10):
            gridbot[row].append(0)

    list_used = []

    count_oscar = 0
    while count_oscar == 0:
        count_oscar = 1
        r_i = random.randint(0, 9)
        r_i_h = random.randint(0, 6)
        list_curr = [[r_i, r_i_h], [r_i, r_i_h + 1], [r_i, r_i_h + 2], [r_i, r_i_h + 3]]
        for i in list_curr:
            if i in list_used:
                count_oscar = 0
    for i in list_curr:
        gridbot[i[0]][i[1]] = 1
        list_used.append(i)

    count_oscar = 0
    while count_oscar == 0:
        count_oscar = 1
        r_i = random.randint(0, 9)
        r_i_h = random.randint(0, 6)
        list_curr = [[r_i, r_i_h], [r_i, r_i_h + 1], [r_i, r_i_h + 2], [r_i, r_i_h + 3]]
        for i in list_curr:
            if i in list_used:
                count_oscar = 0
    for i in list_curr:
        gridbot[i[0]][i[1]] = 1
        list_used.append(i)

    count_oscar = 0
    while count_oscar == 0:
        count_oscar = 1
        r_i_h = random.randint(0, 9)
        r_i = random.randint(0, 6)
        list_curr = [[r_i, r_i_h], [r_i + 1, r_i_h], [r_i + 2, r_i_h], [r_i + 3, r_i_h]]
        for i in list_curr:
            if i in list_used:
                count_oscar = 0
    for i in list_curr:
        gridbot[i[0]][i[1]] = 1
        list_used.append(i)

    count_oscar = 0
    while count_oscar == 0:
        count_oscar = 1
        r_i_h = random.randint(0, 9)
        r_i = random.randint(0, 6)
        list_curr = [[r_i, r_i_h], [r_i + 1, r_i_h], [r_i + 2, r_i_h], [r_i + 3, r_i_h]]
        for i in list_curr:
            if i in list_used:
                count_oscar = 0
    for i in list_curr:
        gridbot[i[0]][i[1]] = 1
        list_used.append(i)

    count_oscar = 0
    while count_oscar == 0:
        count_oscar = 1
        r_i = random.randint(0, 9)
        r_i_h = random.randint(0, 9)
        if [r_i, r_i_h] in list_curr:
            count_oscar = 0

    gridbot[r_i][r_i_h] = 1
    ak = gridbot

    global gridbot, list_curr
    page_two('')


def page_two(msg):
    global usergrid
    global gridbot
    global upgrid
    global bpgrid
    global counter_c

    counter_c = 0
    a = pygame.image.load('square.png')
    pygame.display.set_icon(a)
    BLACK = (30, 30, 30)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    d_red = (190, 0, 0)
    black = BLACK
    white = WHITE
    red = RED

    WIDTH = 45
    HEIGHT = 45
    MARGIN = 5

    grid = []
    for row in range(10):

        grid.append([])
        for column in range(10):
            grid[row].append(0)

    pygame.init()

    WINDOW_SIZE = [1250, 800]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Battleships by Mohit")

    done = False

    clock = pygame.time.Clock()

    while done == False:
        textinput = pygame_textinput.TextInput()

        try:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    if upgrid[row][column] == 0:
                        if gridbot[row][column] == 1:
                            upgrid[row][column] = 2
                        if gridbot[row][column] == 0:
                            upgrid[row][column] = 3
                        bot_play(bpgrid)

            screen.fill(black)

            # Draw the grid
            for row in range(10):
                for column in range(10):
                    color = white

                    if upgrid[row][column] == 2:
                        color = RED
                    if upgrid[row][column] == 3:
                        color = BLUE

                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
            for row in range(10):
                for column in range(10):
                    color = white
                    if usergrid[row][column] == 1:
                        color = GREEN
                    if usergrid[row][column] == 2:
                        color = RED
                    if usergrid[row][column] == 3:
                        color = BLUE

                    pygame.draw.rect(screen,
                                     color,
                                     [650 + (MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])

            clock.tick(60)

            largeText = pygame.font.SysFont("arial", 35)
            TextSurf, TextRect = text_objects("Your ships are on the right, red indicates a hit, blue a miss",
                                              largeText, white)
            TextRect.center = (625, 600)
            screen.blit(TextSurf, TextRect)

            largeTextB = pygame.font.SysFont("arial", 35)
            TextSurfB, TextRectB = text_objects("The grid you attack is on the left, click a square to fire.",
                                                largeTextB, white)
            TextRectB.center = (625, 700)
            screen.blit(TextSurfB, TextRectB)

            largeTextB = pygame.font.SysFont("arial", 35)
            TextSurfB, TextRectB = text_objects("Red = HIT, Blue = MISS, White = NOTHING", largeTextB, white)
            TextRectB.center = (625, 650)
            screen.blit(TextSurfB, TextRectB)

            largeTextB = pygame.font.SysFont("arial", 35)
            TextSurfB, TextRectB = text_objects(str(msg), largeTextB, white)
            TextRectB.center = (625, 550)
            screen.blit(TextSurfB, TextRectB)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        except Exception as e:
            pass


def page_three(msg):
    global usergrid, gridbot, upgrid, bpgrid
    a = pygame.image.load('square.png')
    pygame.display.set_icon(a)
    BLACK = (30, 30, 30)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    d_red = (190, 0, 0)
    black = BLACK
    white = WHITE
    red = RED

    # print('\n\n\nusergrid')
    # print(usergrid)
    # print('\n\n\ngridbot')
    # print(gridbot)
    # print('\n\n\nupgrid')
    # print(upgrid)
    # print('\n\n\nbpgrid')
    # print(bpgrid)
    WIDTH = 45
    HEIGHT = 45
    MARGIN = 5

    grid = []
    for row in range(10):

        grid.append([])
        for column in range(10):
            grid[row].append(0)

    pygame.init()

    WINDOW_SIZE = [1250, 800]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Battleships by Mohit")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    example_image = pygame.image.load('example.png')
    # -------- Main Program Loop -----------
    while not done:
        textinput = pygame_textinput.TextInput()

        try:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
            # Set the screen background
            screen.fill(black)

            # Limit to 60 frames per second
            clock.tick(60)

            button("Exit", 625, 400, 100, 50, d_red, red, quit)

            largeTextB = pygame.font.SysFont("arial", 35)
            TextSurfB, TextRectB = text_objects(str(msg), largeTextB, white)
            TextRectB.center = (550, 425)
            screen.blit(TextSurfB, TextRectB)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        except Exception as e:
            pass


def bot_play(bpgrid):
    indexer = 0
    global listpotplay
    global usergrid
    global counter_c
    global DIFF_LIST
    global bot_hitlist

    while indexer == 0:
        counter_c += 1
        # print('run')

        i = random.randint(0, 9)
        i_h = random.randint(0, 9)

        if len(listpotplay) > 0:

            g = random.choice(listpotplay)
            counter_a = 0
            counter_d = 0
            index_d = [0, 0, 0]
            choicer = 1

            if choicer == 1:
                # print('routeB')
                try:
                    item = random.choice(bot_list_possible_l)
                    g = random.choice(item)
                    list_diff = []

                    if random.choice(DIFF_LIST) == 0:
                        g = index_2d(usergrid, 1)
                    for i in range(0, 30):
                        if 1 in list:
                            g = [random.randint(0, 9), random.randint(0, 9)]
                    i = g[0]
                    i_h = g[1]

                except:
                    i = random.randint(0, 9)
                    i_h = random.randint(0, 9)
                    if random.choice(DIFF_LIST) == 0:
                        g = index_2d(usergrid, 1)
                        i = g[0]
                        i_h = g[1]

        indexer = 1
        if i > 9 or i < 0 or i_h > 9 or i_h < 0:
            # print('outgrid')
            indexer = 0

        for rest in listpotplay:
            if [rest[0], rest[1]] == [i, i_h]:
                indexer = 0
        # print(len(bot_list_possible_l))

    if usergrid[i][i_h] == 1:
        bpgrid[i][i_h] = 2
        usergrid[i][i_h] = 2
        index_a = sum(x.count(2) for x in upgrid)
        # print('user{}'.format(index_a))
        # print(usergrid)
        if index_a == 13:
            page_three('You win.')

        index_b = sum(x.count(2) for x in usergrid)
        # print('bot{}'.format(index_b))
        index_usergrid = (sum(x.count(2) for x in usergrid)) + (sum(x.count(1) for x in usergrid))
        if index_usergrid != 13:
            page_three('error.')

        if index_b == 13:
            page_three('You lose.')

        for d in bot_list_possible:
            if [i, i_h] in d:
                bot_list_possible_l.append(d)
        listpotplay.append([i, i_h, 1])
        page_two('CPU hit one of your ships')

    if usergrid[i][i_h] == 0:
        bpgrid[i][i_h] = 3
        usergrid[i][i_h] = 3
        index_a = sum(x.count(2) for x in upgrid)
        # print('user{}'.format(index_a))
        if index_a == 13:
            page_three('You win.')

        index_b = sum(x.count(2) for x in usergrid)
        # print('bot{}'.format(index_b))
        if index_b == 13:
            page_three('You lose.')
        for d in bot_list_possible:
            if [i, i_h] in d:
                bot_list_possible.remove(d)
        for d in bot_list_possible_l:
            if [i, i_h] in d:
                bot_list_possible_l.remove(d)
        bot_hitlist.append([[i], [i_h]])
        listpotplay.append([i, i_h, 0])
        page_two('CPU missed your ships')


def check_two_pg_one(ak, shipsused):
    global usergrid
    count_alice = 0
    for i in ak:
        if 1 in i:
            count_alice = 1

    if count_alice != 0:
        x = index_2d(ak, 1)
        x_co = x[0]
        y_co = x[1]
        check_surround(x_co, y_co, ak, shipsused)

    gen_bot()


def check_two_pg_one_bot(shipsused_bot):
    global gridbot
    count_alice = 0
    ak = gridbot
    for i in ak:
        if 1 in i:
            count_alice = 1

    if count_alice != 0:
        x = index_2d(ak, 1)
        x_co = x[0]
        y_co = x[1]
        check_surround_bot(x_co, y_co, ak, shipsused_bot)


def check_surround_bot(x, y, ak, shipsused):
    h = False
    v = False
    E = False
    if ak[x][y] == 1:
        if ak[x + 1][y] == 1 or ak[x - 1][y] == 1:
            h = True
        elif ak[x][y + 1] == 1 or ak[x][y - 1] == 1:
            v = True
        if ak[x + 1][y + 1] == 1 or ak[x - 1][y - 1] == 1 or ak[x + 1][y - 1] == 1 or ak[x - 1][y + 1] == 1:
            E = True

    if E == True:
        gen_bot()
    if v == True and h == True:
        gen_bot()
    if h != True and v != True and E != True:
        if shipsused[3] == True:
            gen_bot()
        shipsused[3] = True
        ak[x][y] = 0
        check_two_pg_one_bot(shipsused)

    elif h == True and v == False:
        s = ak[x]
        if s.count(1) == 4:
            if shipsused[0] == False:
                shipsused[0] = True
            elif shipsused[1] == False:
                shipsused[1] = True
            elif shipsused[2] == False:
                shipsused[2] = True
            elif shipsused[1] == True and shipsused[0] == True and shipsused[2] == True:
                gen_bot()
    elif h == False and v == True:
        s = []
        for i in ak:
            s.append(i[y])
        if s.count(1) == 4:
            if shipsused[0] == False:
                shipsused[0] = True
            elif shipsused[1] == False:
                shipsused[1] = True
            elif shipsused[2] == False:
                shipsused[2] = True
            elif shipsused[1] == True and shipsused[0] == True and shipsused[2] == True:
                gen_bot()


def page_one(msg):
    global usergrid
    a = pygame.image.load('square.png')
    pygame.display.set_icon(a)
    BLACK = (30, 30, 30)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    d_red = (190, 0, 0)
    black = BLACK
    white = WHITE
    red = RED
    WIDTH = 45
    HEIGHT = 45
    MARGIN = 5
    grid = []
    for row in range(10):

        grid.append([])
        for column in range(10):
            grid[row].append(0)

    pygame.init()

    WINDOW_SIZE = [1250, 800]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Battleships by Mohit")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    example_image = pygame.image.load('example.png')
    # -------- Main Program Loop -----------
    while not done:
        textinput = pygame_textinput.TextInput()

        try:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    if grid[row][column] == 1:
                        grid[row][column] = 0
                    else:
                        grid[row][column] = 1

            # Set the screen background
            screen.fill(black)

            # Draw the grid
            for row in range(10):
                for column in range(10):
                    color = white
                    if grid[row][column] == 1:
                        color = GREEN

                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])

            # Limit to 60 frames per second
            clock.tick(60)
            listitems = [0, grid]
            usergrid = grid
            button("Submit", 550, 450, 100, 50, d_red, red, check_pg_one, listitems)

            largeText = pygame.font.SysFont("arial", 35)
            TextSurf, TextRect = text_objects("Welcome, draw one of each ship above then hit 'submit'", largeText,
                                              white)
            TextRect.center = (870, 400)
            screen.blit(TextSurf, TextRect)

            largeTextB = pygame.font.SysFont("arial", 35)
            TextSurfB, TextRectB = text_objects("Ships cannot be diagonal and cannot be positioned next to each other",
                                                largeTextB, white)
            TextRectB.center = (625, 700)
            screen.blit(TextSurfB, TextRectB)

            largeTextB = pygame.font.SysFont("arial", 35)
            TextSurfB, TextRectB = text_objects("Placment at edges can cause issues. Do not place 1 ship last.",
                                                largeTextB, white)
            TextRectB.center = (625, 725)
            screen.blit(TextSurfB, TextRectB)

            largeTextB = pygame.font.SysFont("arial", 35)
            TextSurfB, TextRectB = text_objects(str(msg), largeTextB, white)
            TextRectB.center = (625, 600)
            screen.blit(TextSurfB, TextRectB)

            screen.blit(example_image, (650, 150))

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        except Exception as e:
            pass


page_one('')
