import streamlit as st
import os
import subprocess

st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube URL:")

def download_video(url):
    if st.button("Download"):
    download_video(url)
    try:
        command = f"yt-dlp -x --audio-format mp3 {url}"
        os.system(command)
        st.write(f"Downloaded video: {url.split('/')[-1]}.mp3")
    except Exception as e:
        st.write(f"Error: {e}")
