
import tkinter as tk
from tkinter import filedialog, messagebox
from karyotype_analyzer import main as analyze_karyotype

class KaryotypeAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Karyotype Analyzer")

        self.label = tk.Label(master, text="Enter Sample ID:")
        self.label.pack()

        self.sample_id_entry = tk.Entry(master)
        self.sample_id_entry.pack()

        self.analyze_button = tk.Button(master, text="Analyze Sample", command=self.analyze_sample)
        self.analyze_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def analyze_sample(self):
        sample_id = self.sample_id_entry.get()
        if not sample_id:
            messagebox.showerror("Error", "Please enter a Sample ID")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not output_path:
            return

        try:
            analyze_karyotype(sample_id, output_path)
            messagebox.showinfo("Success", f"Analysis complete. Results saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    gui = KaryotypeAnalyzerGUI(root)
    root.mainloop()
