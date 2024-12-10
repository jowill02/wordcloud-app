import streamlit as st
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Real-Time Word Cloud")
st.write("Submit words using the form on the left, and watch the word cloud update live!")

# Sidebar for User Input
st.sidebar.header("Submit Your Word")
word_input = st.sidebar.text_input("Enter a word or phrase:")
if st.sidebar.button("Submit"):
    # Append the input to the word list
    with open("word_list.txt", "a") as file:
        file.write(f"{word_input}\n")

# Read the Submitted Words
try:
    with open("word_list.txt", "r") as file:
        words = file.readlines()
except FileNotFoundError:
    words = []

# Generate the Word Cloud if Words Exist
if words:
    wordcloud_text = " ".join([word.strip() for word in words])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(wordcloud_text)
    # Display the Word Cloud
    st.image(wordcloud.to_array(), use_column_width=True)
else:
    st.write("No words submitted yet! Add your words to create the cloud.")

# Clear Words Option
if st.button("Clear All Words"):
    open("word_list.txt", "w").close()  # Clear the word list
    st.experimental_rerun()

from matplotlib.colors import ListedColormap

# Define a custom colormap
custom_colormap = ListedColormap(["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FFC300"])

# Generate the Word Cloud with the custom colormap
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    colormap=custom_colormap
).generate(wordcloud_text)

# Display the word cloud
st.image(wordcloud.to_array(), use_column_width=True)

import matplotlib.pyplot as plt

# Generate gradient background
def plot_with_gradient(wordcloud):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.set_axis_off()

    # Create a gradient
    ax.imshow(
        np.linspace(0, 1, wordcloud.width).reshape(1, -1),
        aspect="auto",
        cmap="coolwarm",
        alpha=0.5,
        extent=ax.get_xlim() + ax.get_ylim()
    )
    st.pyplot(fig)

plot_with_gradient(wordcloud)
