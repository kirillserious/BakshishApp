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
            'About': "Bahşiş App is an app for multicurrency FX convertation rate monitoring."
        }
    )

    st.write("## Merhaba!")

    col1, _ = st.columns([1, 3])
    button1 = col1.button(label="Push me, my friend!", key="test_button")
    if button1:
        st.write("Give me 50 TRY, brother!")

    button2 = col1.button(label="Push me again, please!", key="test_button2")
    if button2:
        st.write("Oooops... Bahşiş 100 TRY!")
    # Bahşiş
