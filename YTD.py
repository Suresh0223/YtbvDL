import streamlit as st
import os
import subprocess

st.title("Youtube downloader")

url = st.text_input("Enter YouTube URL: ")

def download_video(url):
  st.button(Download_Video)
  if st.button("Download_Video"):
    download_video(url)
  st.success("Video downloaded successfully")
  try:
    command = f"yt-dlp -x --audio-format mp3 {url}"
    os.system(command)
    st.write(f"Downl;oaded video: {url.split('/')[-1]}.mp3")    
  except Exception as e:
    st.error(f"Error downloading video: {e}") 
