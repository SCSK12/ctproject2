import streamlit as st
import streamlit.components.v1 as htmlviewer
st.set_page_config(layout='wide', page_title='CT문제!!!')
# Title Msg#1
st.title('This is NAM Webapp!!')

with open('index1.html', 'r', encoding='utf-8') as f:
    html1 = f.read()

with open('index2.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

with open('index3.html', 'r', encoding='utf-8') as f:
    html3 = f.read()

# html = '''
# <html>
#     <head>
#         <title> this is my html </title>
#     </head>
#     <body>
#         <h1>Topic</h1>
#         <h2>SubTopic</h2>
#     </body>
# </html>
# '''
# Box#1(4), Box#2(1)

col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content #1...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content..')
        st.video(url)

    with st.expander('Image ...'):
        imgfilepath = './images/물분자.jpg'
        st.image(imgfilepath)

    with st.expander('Content #2...'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html1,height=920)

    with st.expander('Content #3...'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html2,height=900)

    with st.expander('Content #4...'):
        #st.write(html, unsafe_allow_html=True)
        htmlviewer.html(html3,height=740)
    
with col2:
    with st.expander('Tips..'):
        st.info('Tips..')
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by skykang', unsafe_allow_html=True)

