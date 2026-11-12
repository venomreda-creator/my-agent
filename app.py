import streamlit as st


page_1  = st.Page("page_1.py", title="home")
page_2  = st.Page("page_2.py", title="chat")
page_3  = st.Page("page_3.py", title="login")

pages = st.navigation([page_1, page_2, page_3], position="top")

pages.run()

# st.title("My First Streamlit App")

# st.write("dd")
# st.write("Hello, Streamlit!")

# st.markdown("안녕하세요 *Streamlit* 입니다.")

# st.badge("Success", icon=":material/check:", color="green")

# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code, language="python")

# st.text("This is text\n[and x](that's not a Markdown link).")


# from datetime import datetime
# import streamlit as st

# event_time = st.datetime_input(
#     "Schedule your event",
#     datetime(2025, 11, 19, 16, 45),
# )
# st.write("Event scheduled for", event_time)

# from datetime import date
# import streamlit as st

# d = st.date_input("When's your birthday", date(2019, 7, 6))
# st.write("Your birthday is:", d)