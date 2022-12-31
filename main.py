import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('DataFrame')

df = pd.DataFrame(
    {'1列目':[1, 2, 3, 4],
     '2列目':[10, 20, 30, 40]
     }
)


st.write(df)
st.dataframe(df, width = 100, height = 100)
st.dataframe(df.style.highlight_max(axis = 0))
st.table(df.style.highlight_max(axis = 0))

#コメント
#マジックコマンド
#マークダウン記法
#章　節　項
#Display text  Latexもかける
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

#チャート
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.write(df)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)
st.write("画像のImage")

img = Image.open('fuji.jpg')
st.image(img, caption = "富士山", use_column_width=True)
