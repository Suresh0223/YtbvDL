import streamlit as st
import os
import subprocess

st.title("Youtube downloader")

url = st.text_input("Enter YouTube URL: ")
if st.button("Download"):
  download_video(url)
  st.success("Video downloaded successfully")

def download_video(url):
  try:
    command = f"yt-dlp -x --audio-format mp3 {url}"
    os.system(command)
    st.write(f"Downl;oaded video: {url.split('/')[-1]}.mp3")    
  except Exception as e:
    st.error(f"Error downloading video: {e}") 
