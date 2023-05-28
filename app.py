import streamlit as st

import requests

from PIL import Image

from io import BytesIO

def main():

    st.title("Image Downloader")

    st.write("Enter the URL of an image to download:")

    # User input

    url = st.text_input("URL", "")

    # Download and display the image

    if st.button("Download"):

        if url:

            try:

                response = requests.get(url)

                image = Image.open(BytesIO(response.content))

                st.image(image, caption='Downloaded Image', use_column_width=True)

                save_image(response.content)

                st.success("Image downloaded successfully!")

            except Exception as e:

                st.error(f"Error downloading the image: {str(e)}")

        else:

            st.warning("Please enter a valid URL.")

def save_image(image_content):

    with open("downloaded_image.jpg", "wb") as f:

        f.write(image_content)

if __name__ == "__main__":

    main()

