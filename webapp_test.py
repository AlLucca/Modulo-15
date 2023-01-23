import streamlit as st
import pandas as pd
import numpy as np
import time

st.write('Bem Vindo!')
#1----------------------------------------------------------------------------------------
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

#2----------------------------------------------------------------------------------------
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))

#3----------------------------------------------------------------------------------------
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#4----------------------------------------------------------------------------------------
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

#5----------------------------------------------------------------------------------------
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

    df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

#6----------------------------------------------------------------------------------------
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

#7----------------------------------------------------------------------------------------
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

#8----------------------------------------------------------------------------------------
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

#9----------------------------------------------------------------------------------------
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")