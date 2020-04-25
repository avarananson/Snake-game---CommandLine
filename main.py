import curses  # For windows, use  'pip install window-curses'
import random
from curses import wrapper


def main(scr):

    scr.clear()
    curses.curs_set(0)
    y, x = scr.getmaxyx()
    initpos = [y / 2, x / 2]
    initfood = [random.randint(1, y - 1), random.randint(1, x - 1)]
    scr.timeout(120)
    scr.addch(int(initpos[0]), int(initpos[1]), curses.ACS_CKBOARD)
    scr.addch(int(initpos[0]), int(initpos[1] - 1), curses.ACS_CKBOARD)
    scr.addch(int(initfood[0]), int(initfood[1]), "*")
    head = initpos
    tail = [initpos[0], initpos[1] - 1]
    i, l, j, m = 0, 0, 1, 1
    pivot = []
    while True:
        k = scr.getch()
        if(k == curses.KEY_UP):
            i, j = -1, 0
            pivot.insert(len(pivot), [[head[0], head[1]], [i, j]])
        elif(k == curses.KEY_DOWN):
            i, j = 1, 0
            pivot.insert(len(pivot), [[head[0], head[1]], [i, j]])
        elif(k == curses.KEY_LEFT):
            i, j = 0, -1
            pivot.insert(len(pivot), [[head[0], head[1]], [i, j]])
        elif(k == curses.KEY_RIGHT):
            i, j = 0, 1
            pivot.insert(len(pivot), [[head[0], head[1]], [i, j]])

        if(head[0] == initfood[0] and head[1] == initfood[1]):
            tail[0] = tail[0] - l
            tail[1] = tail[1] - m
            scr.addch(int(tail[0]), int(tail[1]), curses.ACS_CKBOARD)
            scr.refresh()
            initfood = [random.randint(1, y - 1), random.randint(1, x - 1)]
            scr.addch(int(initfood[0]), int(initfood[1]), "*")

        head[0] = head[0] + i
        head[1] = head[1] + j
        if((scr.inch(int(head[0]), int(head[1])) == curses.ACS_CKBOARD) or
                (int(head[0] == y or int(head[1]) == x)) or
                (int(head[0] == 0 or int(head[1]) == 0))):
            scr.erase()
            scr.addstr(int(y / 2), int(x / 2), "GAME OVER")
            scr.addstr(int(y / 1.5), int(x / 2), "Press 'q' for exit")
            scr.timeout(100000)
            if scr.getch() == ord('q'):
                break

        else:
            scr.addch(int(head[0]), int(head[1]), curses.ACS_CKBOARD)

        if(len(pivot) > 0 and tail == pivot[0][0]):
            scr.addch(int(tail[0]), int(tail[1]), " ")
            l = pivot[0][1][0]
            m = pivot[0][1][1]
            tail[0] = tail[0] + l
            tail[1] = tail[1] + m
            pivot.pop(0)
        else:
            scr.addch(int(tail[0]), int(tail[1]), " ")
            tail[0] = tail[0] + l
            tail[1] = tail[1] + m

        scr.refresh()


wrapper(main)
