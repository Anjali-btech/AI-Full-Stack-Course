import streamlit as st
st.set_page_config(page_title = "Streamlit Demo", page_icon = ".")

st.title("Streamlit demo")
st.write("This is plain text")
st.markdown("This is **Bold**, this is *italic*, this is blue[coloured] ")
st.write("You can also include a divider")
st.divider()