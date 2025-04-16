import streamlit as st
from PIL import Image

image = Image.open('chapt02/test_image.jpg')
st.image(image, caption='サンプルイメージ')

st.write('---')

video_file = open('chapt02/test_movie.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)