#By github.com/tushar2704
import streamlit as st
from st_functions import st_button, load_css
from PIL import Image


custom_css = """
<style>
# .stApp > header {
#     background-color: transparent;
# }

.stApp {
    margin: auto;
    font-family: 'Roboto', sans-serif;
    overflow: auto;
    background: linear-gradient(#FDF8E1 38%);
    animation: gradient 15s ease infinite;
    background-size: 400% 400%;
    background-attachment: fixed;
}


</style>
"""

def main():
    # Inject the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    

if __name__ == "__main__":
    main()

load_css()

st.write("[![Star](https://img.shields.io/github/stars/tushar2704/Links_Application.svg?logo=github&style=social)](https://gitHub.com/tushar2704/Links_Application)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.jpg'))

st.header('Tushar Aggarwal, M.S.')

st.info('Data Scientist | Data Analyst | Business Analyst | Python, SQL | Medium Writer | MSc INSEEC, PARIS | RNCP Manager Level 7')

icon_size = 20

st_button('website', 'https://www.tushar-aggarwal.com/', 'Tushar-Aggarwal.com', icon_size)
st_button('medium', 'https://medium.com/@tushar_aggarwal', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/TaggData', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/tusharaggarwalinseec/', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://substack.com/@tusharaggarwal', 'Sign up for my Newsletter', icon_size)
st_button('youtube', 'https://www.youtube.com/channel/UCGCsCecaRR4ZSITB3Mqzqqg', 'YouTube channel', icon_size)
st_button('cup', 'https://ko-fi.com/tusharaggarwal', 'Buy me a Coffee', icon_size)