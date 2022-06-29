import numpy as np
import cv2
# pip install streamlit
# pip install streamlit_drawable_canvas
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model('digit_recognizer.h5')


st.title('Digit Recognizer Streamlit App')


SIZE = 200 # size of the box where users can draw images (numbers from 1 ot 9)
mode = st.checkbox('Draw or Delete',True) 
canvas_res = st_canvas(
    fill_color='#000000',  # black
    stroke_width = 10,
    stroke_color = "#FFFFFF",  # white
    background_color = '#000000', # black
    width = SIZE,
    height = SIZE,
    drawing_mode = 'freedraw' if mode else 'transform',
    key = 'canvas')

if canvas_res.image_data is not None:
    img = cv2.resize(canvas_res.image_data.astype('uint8'),(28,28))
    rescaled = cv2.resize(img,(SIZE,SIZE),interpolation=cv2.INTER_NEAREST)
    st.write('This image will be used as Model imput')
    st.image(rescaled)


if st.button('Predict'):
    test_x = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    res = model.predict(test_x.reshape(1,28,28,1))
    st.write(f'Result is {np.argmax(res[0])}')
    st.write(res)
    st.bar_chart(res[0])


# To run this app:  streamlit run app.py 
# in the terminal



