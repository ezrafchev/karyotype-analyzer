
import tkinter as tk
from gui import KaryotypeAnalyzerGUI

def main():
    root = tk.Tk()
    app = KaryotypeAnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
