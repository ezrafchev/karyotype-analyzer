
import tkinter as tk
from gui import KaryotypeAnalyzerGUI
import os

def main():
    root = tk.Tk()
    root.title("Karyotype Analyzer")
    root.geometry("400x500")  # Set a default window size
    
    # Ensure the samples directory exists
    samples_dir = os.path.join(os.path.dirname(__file__), 'samples')
    if not os.path.exists(samples_dir):
        os.makedirs(samples_dir)
    
    app = KaryotypeAnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
