import streamlit as st
import time
from src.models.deck import Deck
from src.utils.persistence import create_reading_entry, save_readings

def show_custom_spread_page():
    """Displays the Custom Spread page in the Streamlit app."""
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
        st.session_state.custom_drawn_cards = [] # store drawn cards
        st.session_state.custom_reflection = "" # store reflection
        st.session_state.custom_reading_type = None # store reading type

    if st.button("🔮 Draw Cards"):
        with st.spinner("Shuffling your custom spread..."): 
            time.sleep(2) # simulate shuffling delay
        deck = Deck() # create new deck
        deck.shuffle() # shuffle deck
        st.session_state.custom_drawn_cards = [deck.draw_card() for _ in range(num_cards)] # draw specified number of cards
        st.session_state.custom_reading_type = reading_type # set reading type
        st.session_state.custom_reflection = "" # reset reflection

    if st.session_state.custom_drawn_cards:
        st.success("✨ Your custom spread is ready! ✨")

        for i, card in enumerate(st.session_state.custom_drawn_cards, start=1): # display drawn cards
            st.subheader(f"Card {i}: {card}") # display card
            st.write(card.get_meaning(st.session_state.custom_reading_type.lower())) # display meaning

        st.markdown("---")
        st.markdown("Would you like to save this reading to your Reflection Journal?")

        save_option = st.radio(
            "Choose an option:",
            ["💾 Yes, save this reading", "❌ No, don't save"],
            index=0 # default to saving
        )

        if save_option == "💾 Yes, save this reading":
            st.session_state.custom_reflection = st.text_area(
                "Write a short reflection about this reading: (If you wish)",
                value=st.session_state.custom_reflection, # current reflection
                height=150
            )

            if st.button("Save Reading"):
                entry = create_reading_entry(
                    "Custom Spread",
                    st.session_state.custom_drawn_cards, 
                    st.session_state.custom_reading_type,
                    st.session_state.custom_reflection
                )
                save_readings(entry)
                st.success("🌙 Reading saved successfully! You can view it later in your Reflection Journal.")

                # Optional: reset after saving
                st.session_state.custom_drawn_cards = [] # reset drawn cards
                st.session_state.custom_reflection = "" # reset reflection
        elif save_option == "❌ No, don't save":
            st.info("Okay, not saving! You can draw new cards or navigate away.")

        st.markdown("---")
        # Reset Deck Button
        if st.button("🔄 Reset Deck?"):
            st.session_state.custom_drawn_cards = []  # reset drawn cards
            st.success("Deck has been reset!")