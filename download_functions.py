from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
from tkinter import filedialog

def download_video(link_entry, status_label):
    link = link_entry.get()
    folder_selected = filedialog.askdirectory()  
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=folder_selected)  
    status_label.config(text="Download completo.")
import traceback

def download_video_with_resolution(link_entry, start_time_entry, end_time_entry, filename_entry, resolution_combobox, status_label):
    link = link_entry.get()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    filename = filename_entry.get()
    resolution = resolution_combobox.get()
    folder_selected = filedialog.askdirectory()  

    try:
        yt = YouTube(link)
        stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=resolution).first()

        if stream is not None:
            stream.download(output_path=folder_selected, filename=f"{filename}_temp.mp4")  

            video_clip = VideoFileClip(f"{folder_selected}/{filename}_temp.mp4")
            video_clip = video_clip.subclip(start_time, end_time)
            video_clip.write_videofile(f"{folder_selected}/{filename}.mp4", codec='libx264')  
            video_clip.close()

            os.remove(f"{folder_selected}/{filename}_temp.mp4")
            status_label.config(text="Download do corte do vídeo concluído.")
        else:
            status_label.config(text="Erro: Não foi possível encontrar uma stream de vídeo com a resolução especificada.")
    except Exception as e:
        error_message = traceback.format_exc()
        print(error_message)
        status_label.config(text=f"Erro: {str(e)}")
