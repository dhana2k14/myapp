import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.write("""# First App
Below is pairplot of the famous Iris dataset!""")

rows_to_display = st.text_input('Enter a name of a Iris Species')

df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target_class']

# display data in its raw form
# st.table(df)

if st.button('Submit'):
    # plot corr

    df = df.iloc[0:int(rows_to_display)]
    plt = sns.pairplot(df, hue = 'target_class')
    st.pyplot(plt)

# st.write('Listen to my talk at Data Innovation Summit 2020!')
# video_file = open('C:\\Users\\dhanasekaranp\\Documents\\Zoom\\zoom_1.mp4', 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes)