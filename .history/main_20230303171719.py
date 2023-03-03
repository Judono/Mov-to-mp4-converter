import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from moviepy.editor import VideoFileClip

def convert_video():
    file_path = filedialog.askopenfilename(title="Select MOV file", filetypes=(("MOV files", "*.mov"), ("all files", "*.*")))
    if not file_path:
        return
    clip = VideoFileClip(file_path)
    mp4_path = file_path.replace(".mov", ".mp4")
    status_label.config(text="Converting...")
    progress_bar.start()
    clip.write_videofile(mp4_path, fps=clip.fps, progress_bar=update_progress)
    clip.close()
    status_label.config(text="Conversion complete!")
    progress_bar.stop()

def update_progress(progress):
    progress_bar_var.set(progress)

root = tk.Tk()
root.title("MOV to MP4 Converter")

# Create the GUI
tk.Label(root, text="Click 'Convert' to select a MOV file for conversion to MP4").grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, text="Convert", command=convert_video).grid(row=1, column=0, padx=10, pady=10)
status_label = tk.Label(root, text="")
status_label.grid(row=2, column=0, padx=10, pady=10)
progress_bar_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_bar_var, maximum=100)
progress_bar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

root.mainloop()