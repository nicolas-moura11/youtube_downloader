import tkinter as tk
from tkinter import ttk, filedialog
from download_functions import download_video, download_video_with_resolution
import sv_ttk

root = tk.Tk()
root.title("Downloader de Vídeos")
sv_ttk.set_theme("dark")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

for i in range(8):
    root.grid_rowconfigure(i, weight=1)

title_label = ttk.Label(root, text="Download de Vídeo", font=("Helvetica", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=4, pady=(10,5))

instruction_label = ttk.Label(root, text="Insira o link do vídeo abaixo e personalize o download:", font=("Helvetica", 10))
instruction_label.grid(row=1, column=0, columnspan=4, pady=(0,10))

link_label = ttk.Label(root, text="Link do Vídeo:")
link_label.grid(row=2, column=0, sticky="w", padx=5)
link_entry = ttk.Entry(root, width=40)
link_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=3, sticky="w")

download_button = ttk.Button(root, text="Baixar Vídeo Completo", command=lambda: download_video(link_entry, status_label))
download_button.grid(row=3, column=0, columnspan=4, pady=5)

customize_label = ttk.Label(root, text="Personalize seu download:", font=("Helvetica", 12, "bold"))
customize_label.grid(row=4, column=0, columnspan=4, pady=(15,5))

start_time_label = ttk.Label(root, text="Início (HH:MM:SS):")
start_time_label.grid(row=5, column=0, sticky="w", padx=5)
start_time_entry = ttk.Entry(root, width=12)
start_time_entry.grid(row=5, column=1, pady=5, sticky="w")

end_time_label = ttk.Label(root, text="Fim (HH:MM:SS):")
end_time_label.grid(row=5, column=2, sticky="w", padx=5)
end_time_entry = ttk.Entry(root, width=12)
end_time_entry.grid(row=5, column=3, pady=5, sticky="w")

filename_label = ttk.Label(root, text="Nome do Corte:")
filename_label.grid(row=6, column=0, sticky="w", padx=5)
filename_entry = ttk.Entry(root, width=20)
filename_entry.grid(row=6, column=1, pady=5, columnspan=3, sticky="w")

resolution_label = ttk.Label(root, text="Resolução:")
resolution_label.grid(row=7, column=0, sticky="w", padx=5)
resolutions = ["360p", "480p", "720p", "1080p"]
resolution_combobox = ttk.Combobox(root, values=resolutions, width=12)
resolution_combobox.grid(row=7, column=1, pady=5, sticky="w")
resolution_combobox.current(2) 

download_cut_button = ttk.Button(root, text="Baixar Corte de Vídeo", command=lambda: download_video_with_resolution(link_entry, start_time_entry, end_time_entry, filename_entry, resolution_combobox, status_label))
download_cut_button.grid(row=8, column=0, columnspan=4, pady=15)

status_label = ttk.Label(root, text="", font=("Helvetica", 10, "italic"))
status_label.grid(row=9, column=0, columnspan=4, pady=(0,10))

root.mainloop()
