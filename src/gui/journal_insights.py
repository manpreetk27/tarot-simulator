import streamlit as st
from src.utils.persistence import load_readings

def show_insights_page():
    """Displays the Journal Insights page in the Streamlit app."""
    st.markdown("<h1 style='text-align: center; color: #5B2C6F;'>📌 Journal Insights</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""Analyze patterns in your past tarot readings.<br> 
    Discover your most drawn cards and common reading types.<br><br>
    <i>Reflect on your journey through the cards.</i>
    """, unsafe_allow_html=True)

    # Load readings
    readings = load_readings() # List of reading entries
    if not readings:
        st.warning("No readings found yet.")
        return

    # Count cards
    card_counts = {} # dictionary to count card occurrences
    for reading in readings: # iterate through readings
        for card in reading["cards"]: # iterate through cards in each reading
            name = card["name"] # get card name
            if name in card_counts: # increment count
                card_counts[name] += 1 # increment count
            else:
                card_counts[name] = 1 # initialize count

    # Show most frequent cards
    st.subheader("Most Frequently Drawn Cards")
    if card_counts:
        sorted_cards = sorted(card_counts.items(), key=lambda x: x[1], reverse=True) # sort by count, lambda is used to specify sorting by count, .items() returns (key, value) pairs
        medals = ["🥇", "🥈", "🥉"]
        for i, (name, count) in enumerate(sorted_cards[:3]): # enumerate is used to get index
            st.write(f"{medals[i]} {name} — {count} time{'s' if count > 1 else ''}") # this formats the output string
    else:
        st.write("No cards recorded yet.")

    # Count reading types
    type_counts = {} # dictionary to count reading types
    for reading in readings: # iterate through readings
        rtype = reading["reading_type"] # get reading type
        if rtype in type_counts: # increment count
            type_counts[rtype] += 1 # increment count
        else:
            type_counts[rtype] = 1 # initialize count

    # Show most common reading type
    st.subheader("Most Common Reading Type")
    if type_counts:
        sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True) # sort by count
        reading, count = sorted_types[0]
        st.write(f"✨ {reading} — {count} reading{'s' if count > 1 else ''}") # display most common reading type
    else:
        st.write("No readings yet.")

    # Simple major arcana insight
    majors_list = ["The Fool", "The Magician", "The High Priestess", "The Tower", "Death"]
    majors = 0
    total = 0
    for reading in readings:
        for card in reading["cards"]:
            total += 1
            if card["name"] in majors_list:
                majors += 1
    if total > 0 and majors > total / 2: # if more than half are major arcana
        st.info("You've been drawing a lot of Major Arcana — big life changes or themes may be unfolding.")

