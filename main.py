import pandas as pd
import numpy as np
import streamlit as st


if __name__ == "__main__":
    st.set_page_config(
        page_title="Bahşiş App",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )

    st.write("Merhaba!")
    col1, _ = st.columns([1, 3])
    button1 = col1.button(label="Push me, my friend!", key="test_button")
    if button1:
        st.write("Give me 50 TRY, brother!")

    button1 = col1.button(label="Push me again!", key="test_button")
    if button1:
        st.write("Bahşiş 100 TRY!")
    # Bahşiş
