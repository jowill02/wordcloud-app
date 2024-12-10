from wordcloud import WordCloud
import streamlit as st
from PIL import Image
import numpy as np
from matplotlib.colors import ListedColormap

# App Title
st.title("Enhanced Word Cloud")
st.write("Submit words using the form on the left!")

# Sidebar Input
st.sidebar.header("Submit Your Word")
word_input = st.sidebar.text_input("Enter a word:")
if st.sidebar.button("Submit"):
    with open("word_list.txt", "a") as file:
        file.write(f"{word_input}\n")

# Read Words
try:
    with open("word_list.txt", "r") as file:
        words = file.readlines()
except FileNotFoundError:
    words = []

if words:
    wordcloud_text = " ".join([word.strip() for word in words])

    # Handle Missing Mask
    try:
        mask_image = np.array(Image.open("heart.png"))
    except FileNotFoundError:
        mask_image = None

    # Custom Colormap
    custom_colormap = ListedColormap(["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FFC300"])

    # Generate Word Cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        mask=mask_image,
        contour_color="black",
        contour_width=2,
        colormap=custom_colormap
    ).generate(wordcloud_text)

    # Display Word Cloud
    st.image(wordcloud.to_array(), use_column_width=True)
else:
    st.write("No words submitted yet! Please add words using the sidebar.")

# Clear Words Option
if st.button("Clear All Words"):
    open("word_list.txt", "w").close()
    st.experimental_rerun()
