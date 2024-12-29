import yt_dlp
import streamlit as st


url = input("Enter video url: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

st.write("Video downloaded successfully!")
