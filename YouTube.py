from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import os

save_dir = os.path.join(os.getcwd(), 'my_saved_files')


def download_video (url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=true, file_extension="mp4") 
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Download complete!")
    except Exception as e :
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print ( f"Selected folder: {folder}")

        return folder
    
if __name__=="__main__":
    root= tk.Tk()
    root.withdraw()

video_url = input("Pleaser enter a YouTube url: ")
save_path = open_file_dialog()

if save_dir:
    print("Started download...")
    download_video(video_url, save_dir)
else:
    print("Invalid save location.")



