import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

st.set_page_config(page_title="AI Travel Planner")
st.title("Ai Travel Itinerary Planner")
st.write("Plan your day trip itinerary by entering your city and interests")

load_dotenv()

with st.form("planner_form"):
    city = st.text_input("Enter the city name for your trip")
    interest = st.text_input("Enter your interests(comma separated)")
    submitted = st.form_submit_button("Generated itinerary")

    if submitted:
        if city and interest:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interest)
            itinerary = planner.create_itinerary()

            st.subheader("📃: Your Itinerary")
            st.markdown(itinerary)
        else:
            st.warning("Please fill the city and interest to move forward")
