import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

letest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    letest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'










left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ１')
expander.write('問い合わせ１の回答')
expander = st.expander('問い合わせ２')
expander.write('問い合わせ２の回答')
expander = st.expander('問い合わせ３')
expander.write('問い合わせ３の回答')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味：', text
# 'コンディション：', condition

# if st.checkbox('Show Image'):

#     img = Image.open('IMG_2748.JPEG')

#     st.image(img,caption='Kohei Imanishi',use_column_width=True)

