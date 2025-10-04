import streamlit as st
from rembg import remove
from PIL import Image

def removebg(img):
    input = Image.open(img)
    return remove(input)

def main():
    st.title("QuantWeb Background Remover")
    st.header("Developed by Codidioter")
    st.write("\n" * 70)  # Add empty lines to push the footer to the bottom
    
    st.write("Upload correct format!")
    st.markdown("---")  # Horizontal line
    uploaded = st.file_uploader("Choose an Image...", type=["jpeg","jpg","png"])

    if uploaded is not None:
        st.image(uploaded, caption="uploaded image")
        st.write("Processing Image..")
        result=removebg(uploaded)
        st.image(result, caption="Result")


if __name__ == '__main__':

    main()
