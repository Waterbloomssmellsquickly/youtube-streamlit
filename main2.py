import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title('Streamlit 超入門')
# st.write('DataFrame')
st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_colomn = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_colomn.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
# st.sidebar.write("Interactive Widgets")
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：', text, 'です。'

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition
# option = st.selectbox(
#     'あなたの数字を教えてください。',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'

# ctrl + / で選択行をコメント化できる。
# if (st.checkbox('Show Image')):
#     img = Image.open('fuji.jpg')
#     st.image(img, caption = "富士山", use_column_width=True)
