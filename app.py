import streamlit as st 
from PIL import Image 
from rembg import remove 

def main():
    st.title("AI Background Removal")
    uploaded_files = st.file_uploader("Upload an image",type=['png','jpg','jpeg'])
    if st.button("Generate"):
        if uploaded_files:
            img = Image.open(uploaded_files)
            res = remove(img)
            st.balloons()
            col1,col2 = st.columns(2,gap="medium")
            with col1:
                st.write("### Original Image")
                st.image(img)
            with col2:
                st.write("### Result Image")
                st.image(res)
        else:
            st.error("Please upload a valid image")



if __name__=="__main__":
    main()