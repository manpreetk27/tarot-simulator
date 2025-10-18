import streamlit as st
import time
from src.models.deck import Deck
from src.utils.persistence import create_reading_entry, save_readings

def show_custom_spread_page():
    st.markdown("<h1 style='color:#5B2C6F; text-align:center;'>🃏 Custom Tarot Spread</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    Create your own tarot spread by choosing how many cards to draw (up to 7).<br>
    This option is perfect for when you want to explore your intuition freely.<br><br>
    <i>Let your heart choose the number that feels right.</i>
    """, unsafe_allow_html=True)

    num_cards = st.slider("Select the number of cards to draw:", 1, 7, 3)
    reading_type = st.selectbox("Choose your reading type:", ["General", "Love", "Career"])

    # Initialize session state
    if "custom_drawn_cards" not in st.session_state:
        st.session_state.custom_drawn_cards = []
        st.session_state.custom_reflection = ""
        st.session_state.custom_reading_type = None

    if st.button("🔮 Draw Cards"):
        with st.spinner("Shuffling your custom spread..."):
            time.sleep(2)
        deck = Deck()
        deck.shuffle()
        st.session_state.custom_drawn_cards = [deck.draw_card() for _ in range(num_cards)]
        st.session_state.custom_reading_type = reading_type
        st.session_state.custom_reflection = ""

    if st.session_state.custom_drawn_cards:
        st.success("✨ Your custom spread is ready! ✨")

        for i, card in enumerate(st.session_state.custom_drawn_cards, start=1):
            st.subheader(f"Card {i}: {card}")
            st.write(card.get_meaning(st.session_state.custom_reading_type.lower()))

        st.markdown("---")
        st.markdown("Would you like to save this reading to your Reflection Journal?")

        save_option = st.radio(
            "Choose an option:",
            ["💾 Yes, save this reading", "❌ No, don't save"],
            index=0
        )

        if save_option == "💾 Yes, save this reading":
            st.session_state.reflection = st.text_area(
                "Write a short reflection about this reading: (If you wish)",
                value=st.session_state.reflection,
                height=150
            )

            if st.button("Save Reading"):
                entry = create_reading_entry(
                    "Past-Present-Future",
                    st.session_state.drawn_cards,
                    st.session_state.reading_type,
                    st.session_state.reflection
                )
                save_readings(entry)
                st.success("🌙 Reading saved successfully! You can view it later in your Reflection Journal.")

                # Optional: reset after saving
                st.session_state.drawn_cards = []
                st.session_state.reflection = ""
        elif save_option == "❌ No, don't save":
            st.info("Okay, not saving! You can draw new cards or navigate away.")