
import curses


def display_rankings(stdscr, students, source_label=""):
    stdscr.clear()
    curses.curs_set(0)
    
    header = f"=== STUDENT RANKING BY GPA (DESCENDING) [{source_label}] ===" if source_label else "=== STUDENT RANKING BY GPA (DESCENDING) ==="
    
    try:
        stdscr.addstr(1, 2, header, curses.A_BOLD)
        stdscr.addstr(3, 2, f"{'Rank':<5} {'ID':<10} | {'Name':<20} | {'DoB':<12} | {'GPA':<5}")
        stdscr.addstr(4, 2, "-" * 62)

        line = 5
        for rank, s in enumerate(students, start=1):
            stdscr.addstr(line, 2, f"{rank:<5} {s}")
            line += 1

        stdscr.addstr(line, 2, "Press any key to exit...", curses.A_DIM)
    except curses.error:
        pass

    stdscr.refresh()
    stdscr.getch()