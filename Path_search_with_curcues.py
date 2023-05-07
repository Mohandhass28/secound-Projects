import curses
from curses import wrapper

import Path_Search_Algo


def main(stdscr):
    max = Path_Search_Algo.maze
    s = Path_Search_Algo.path(max)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    c1 = curses.color_pair(1)
    c2 = curses.color_pair(2)
    s.find_path(stdscr,c1,c2,K=True)
    # stdscr.clear()
    # stdscr.addstr('jj')
    stdscr.getch()
if __name__ == '__main__':
    wrapper(main)
