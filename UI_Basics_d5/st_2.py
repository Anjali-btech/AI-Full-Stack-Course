import streamlit as st
st.set_page_config(page_title = "Text Input Demo")
st.tite("Text Input Demo")
name = st.text_input("Enter your Name:", placeholder = "e.g.shanti")
st.write(f"Hello , {Name}!")
secret = st.text_input("Enter your password:", type = "Password")
st.write(f"Your password has {len(secret)} character.")

comment = st.text_area("Any additional commemts?",height = 150)
st.write(f"Your wrote {len(comment)} character.")

if st.button("Submit"):
    st.write("You clicked on submit!")

show_message = st.checkbox("Do you want an extra message")
if show_message:
    st.write("This is the message. Have a good day")

