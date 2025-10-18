import streamlit as st 

def show_dashboard():
    st.markdown("<h1 style='text-align: center; color: #5B2C6F;'>🔮 Tarot Reading Simulator 🔮</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; color: #333; font-size: 1.2em;'>
            Welcome to your digital tarot sanctuary.<br>
            Here, ancient wisdom meets modern technology.<br><br>
            Select a spread, focus on your question, and let the cards guide your journey.<br>
            <i>May insight and clarity be yours.</i>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Choose your path...</h3>", unsafe_allow_html=True)

    # Three navigation buttons in one row
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💫 Past, Present, Future"):
            st.session_state.page = "Past, Present, Future Reading"
            st.rerun()
    with col2:
        if st.button("🪞 Reflection Journal"):
            st.session_state.page = "Reflection Journal"
            st.rerun()
    with col3:
        if st.button("📌 Journal Insights"):
            st.session_state.page = "Journal Insights"
            st.rerun()

    # Optionally, add another row for more buttons
    st.write("")  # Spacer
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("🔍 Learn About Tarot"):
            st.session_state.page = "The History"
            st.rerun()
    with col5:
        if st.button("✨ Custom Spread"):
            st.session_state.page = "Custom Spread"
            st.rerun()
    with col6:
        if st.button("🌟 Card of the Day"):
            st.session_state.page = "Card of the Day"
            st.rerun()

    st.write("")  # Spacer
    col7, col8, col9 = st.columns(3)
    with col8:
        if st.button("🔍 Tarot Card Search"):
            st.session_state.page = "Tarot Card Search"
            st.rerun()

