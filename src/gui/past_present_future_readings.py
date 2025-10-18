import streamlit as st
from src.models.deck import Deck
import time
from src.utils.persistence import create_reading_entry, save_readings

def show_reading_page():
    st.markdown("<h1 style='color:#5B2C6F; text-align:center;'>📯 Past, Present, Future Tarot Reading</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    Explore the influences of your past, the realities of your present, and the possibilities of your future through a three-card tarot spread.<br>
    This spread offers insight into how your history shapes your current situation and what outcomes may lie ahead.<br><br>
    <i>Focus on your question and trust what the cards reveal.</i>
    """, unsafe_allow_html=True)

    reading_type = st.selectbox("Choose your reading type:", ["General", "Love", "Career"])

    # Initialize session state to store current reading
    if "drawn_cards" not in st.session_state:
        st.session_state.drawn_cards = []
        st.session_state.reading_type = None
        st.session_state.reflection = ""

    # Button to draw cards
    if st.button("🔮 Draw Cards"):
        with st.spinner("Shuffling the deck..."):
            time.sleep(2)
        deck = Deck()
        deck.shuffle()
        positions = ["Past", "Present", "Future"]
        st.session_state.drawn_cards = [deck.draw_card() for _ in positions]
        st.session_state.reading_type = reading_type
        st.session_state.reflection = ""

    # If we already have cards in session, display them
    if st.session_state.drawn_cards:
        st.success("✨ Your cards are ready! ✨")

        positions = ["Past", "Present", "Future"]
        for position, card in zip(positions, st.session_state.drawn_cards):
            st.subheader(f"{position}: {card}")
            st.write(card.get_meaning(st.session_state.reading_type.lower()))

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