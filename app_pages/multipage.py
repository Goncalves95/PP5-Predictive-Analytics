import streamlit as st

class MultiPage:
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.markdown("""
        <style>
        streamlit-app, streamlit-app-header, streamlit-app-content {
            background-color: #000000;
            color: #FFFFFF;
            font-family: Helvetica Neue;
        }
        streamlit-app-header {
            border-bottom: 1px solid #FFFFFF;
        }
        streamlit-app-content {
            padding: 1rem;
        }
        </style>
        """, unsafe_allow_html=True)

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()