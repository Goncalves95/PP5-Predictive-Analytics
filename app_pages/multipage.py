import streamlit as st

class MultiPage:
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title="My App",
            page_icon=":smiley:",
            layout="wide"
        )

        # Set the background color
        st.write("<style>body { background-color: #262730; }</style>", unsafe_allow_html=True)

        # Set the font
        st.write("<style>body { font-family: Helvetica; }</style>", unsafe_allow_html=True)

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()



#############      #############      #############
#############      #############      #############
###                ###                ###       ###
###                ###                ###       ###
########           ########           #############
########           ########           #############
###                ###                ###       ###           #########
###                ###                ###        ###          ###   ###
###                #############      ###         ###         ###   ###
###                #############      ###         ###         #########