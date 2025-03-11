# Importing Libraries

import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
# list of timezones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "Pacific/Auckland",
    "Africa/Cairo",
    "America/Los_Angeles",
    "Europe/Paris",
    "Asia/Dubai",
    "Asia/Singapore"

]

# app title
st.title("Time Zone App")
# select timezones
selected_timezones = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["Asia/Karachi"])

# display current time for selected timezones
st.subheader("Selected Timezones")
for tz in selected_timezones:

    current_time = datetime.now(ZoneInfo(tz)).strftime(
        "%Y-%m-%d %I %H:%M:%S %p")

    st.write(f"**{tz}**: {current_time}")

# convert time between timezones
st.subheader("Convet Time between Timezones")

# select current time
current_time = st.time_input("Current Time", value=datetime.now().time())

# select from timezone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

# select to timezone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# convert time
if st.button("Convert Time"):

    dt = datetime.combine(datetime.today(), current_time,
                          tzinfo=ZoneInfo(from_tz))

    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime(
        "%Y-%m-%d %I %H:%M:%S %p")

    st.success(f"Converted Time in {to_tz}: {converted_time}")
