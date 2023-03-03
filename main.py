import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def convert_video():
    file_path = filedialog.askopenfilename(title="Select MOV file", filetypes=(("MOV files", "*.mov"), ("all files", "*.*")))
    if not file_path:
        return
    clip = VideoFileClip(file_path)
    mp4_path = file_path.replace(".mov", ".mp4")
    clip.write_videofile(mp4_path)
    clip.close()
    status_label.config(text="Conversion complete!")

root = tk.Tk()
root.title("MOV to MP4 Converter")

# Create the GUI
tk.Label(root, text="Click 'Convert' to select a MOV file for conversion to MP4").grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, text="Convert", command=convert_video).grid(row=1, column=0, padx=10, pady=10)
status_label = tk.Label(root, text="")
status_label.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()