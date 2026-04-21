from tkinter import Tk
from initialize_database import initialize_database
from ui.ui import UI

def main():
    initialize_database()

    window = Tk()
    window.title("Movie Watchlist")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
