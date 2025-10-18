import streamlit as st
from src.utils.persistence import load_readings

def show_insights_page():
    st.markdown("<h1 style='text-align: center; color: #5B2C6F;'>📌 Journal Insights</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""Analyze patterns in your past tarot readings.<br> 
    Discover your most drawn cards and common reading types.<br><br>
    <i>Reflect on your journey through the cards.</i>
    """, unsafe_allow_html=True)

    # Load readings
    readings = load_readings()
    if not readings:
        st.warning("No readings found yet.")
        return

    # Count cards
    card_counts = {}
    for reading in readings:
        for card in reading["cards"]:
            name = card["name"]
            if name in card_counts:
                card_counts[name] += 1
            else:
                card_counts[name] = 1

    # Show most frequent cards
    st.subheader("Most Frequently Drawn Cards")
    if card_counts:
        sorted_cards = sorted(card_counts.items(), key=lambda x: x[1], reverse=True)
        medals = ["🥇", "🥈", "🥉"]
        for i, (name, count) in enumerate(sorted_cards[:3]):
            st.write(f"{medals[i]} {name} — {count} time{'s' if count > 1 else ''}")
    else:
        st.write("No cards recorded yet.")

    # Count reading types
    type_counts = {}
    for reading in readings:
        rtype = reading["reading_type"]
        if rtype in type_counts:
            type_counts[rtype] += 1
        else:
            type_counts[rtype] = 1

    # Show most common reading type
    st.subheader("Most Common Reading Type")
    if type_counts:
        sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
        reading, count = sorted_types[0]
        st.write(f"✨ {reading} — {count} reading{'s' if count > 1 else ''}")
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
    if total > 0 and majors > total / 2:
        st.info("You've been drawing a lot of Major Arcana — big life changes or themes may be unfolding.")

