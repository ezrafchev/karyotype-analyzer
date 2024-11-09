
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
from karyotype_analyzer import main as analyze_karyotype, SAMPLES_DIR

class KaryotypeAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Karyotype Analyzer")

        self.label = tk.Label(master, text="Select Sample Image:")
        self.label.pack()

        self.sample_listbox = tk.Listbox(master)
        self.sample_listbox.pack()

        self.refresh_button = tk.Button(master, text="Refresh Samples", command=self.refresh_samples)
        self.refresh_button.pack()

        self.analyze_button = tk.Button(master, text="Analyze Sample", command=self.analyze_sample)
        self.analyze_button.pack()

        self.output_text = scrolledtext.ScrolledText(master, height=10)
        self.output_text.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        self.refresh_samples()

    def refresh_samples(self):
        self.sample_listbox.delete(0, tk.END)
        for file in os.listdir(SAMPLES_DIR):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                self.sample_listbox.insert(tk.END, file)

    def analyze_sample(self):
        selection = self.sample_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a sample image")
            return

        sample_file = self.sample_listbox.get(selection[0])
        sample_id = sample_file  # Use the full filename as sample_id

        output_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not output_path:
            return

        try:
            self.output_text.delete(1.0, tk.END)  # Clear previous output
            self.output_text.insert(tk.END, f"Analyzing {sample_file}...
")
            self.master.update()  # Update GUI to show new text immediately

            analyze_karyotype(sample_id, output_path)

            self.output_text.insert(tk.END, f"Analysis complete. Results saved to {output_path}
")
            self.output_text.insert(tk.END, f"Segmented image saved to {output_path.replace('.json', '_segmented.png')}
")
            messagebox.showinfo("Success", f"Analysis complete. Results saved to {output_path}")
        except Exception as e:
            error_message = str(e)
            self.output_text.insert(tk.END, f"Error: {error_message}
")
            messagebox.showerror("Error", error_message)

if __name__ == "__main__":
    root = tk.Tk()
    gui = KaryotypeAnalyzerGUI(root)
    root.mainloop()
