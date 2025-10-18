import streamlit as st

def show_about_page():
    st.markdown("<h1 style='color:#5B2C6F; text-align:center;'>🌟 About Tarot</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        """
        Tarot cards have been used for centuries as tools of reflection and insight.<br>
        Originating in the 15th century as playing cards, they evolved into a mirror of the soul —
        offering guidance through symbolic imagery and archetypes.<br><br>
        This simulator reimagines that ancient tradition through modern technology,<br>
        letting intuition flow through code and card alike.<br><br>
        """,
        unsafe_allow_html=True
    )
    st.image(
        "https://www.thevintagenews.com/wp-content/uploads/sites/65/2016/10/lead-tarot6.jpg",
        caption="The Visconti-Sforza Tarot Deck, one of the oldest known tarot decks.",
        use_container_width=False,
        width=700
    )

    st.markdown(
        """
        <br>
        <i>“The tarot is a mirror that reflects the inner workings of the mind and soul.”</i> — Paul Foster Case<br><br>
        May your journey through these cards bring clarity, wisdom, and transformation.
        """,
        unsafe_allow_html=True
    )       

    st.markdown("---")
