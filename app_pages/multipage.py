class MultiPage:
    def __init__(self, app_name):
        self.pages = []
        self.app_name = app_name

    def add_page(self, title, func):
        self.pages.append({"title": title, "function": func})

    def run(self):
        import streamlit as st

        page = st.sidebar.selectbox(
            "Navigation", self.pages, format_func=lambda p: p["title"]
        )
        page["function"]()
