import streamlit as st
from dotenv import load_dotenv
import os
from bluesky_bot import BlueskyBot

load_dotenv()
bot = BlueskyBot(os.getenv("BSKY_HANDLE"), os.getenv("BSKY_APP_PASSWORD"))

st.title("Bluesky Bot Interface")

# --- Post section ---
st.header("Post a Message")
post_text = st.text_area("Write your post")
if st.button("Post"):
    bot.post_message(post_text)
    st.success("Post sent.")

# --- Search + Follow section ---
st.header("Search and Follow Users")
keyword = st.text_input("Enter keyword (e.g., 'python', 'AI', 'cybersecurity')")
limit = st.slider("Number of results", 1, 20, 5)

if st.button("Search"):
    users = bot.search_users_by_keyword(keyword, limit=limit)
    if not users:
        st.warning("No users found.")
    else:
        for user in users:
            st.markdown(f"**{user['display_name']}** ({user['handle']})  \n{user['description']}")
            if st.button(f"Follow {user['handle']}", key=user['did']):
                bot.follow_user(user['did'])
                st.success(f"Followed {user['handle']}")
                st.balloons()
