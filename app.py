# 그래프 그리기
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DataFrame 생성
data = pd.DataFrame({
    '이름': ['kim', 'lee', 'park'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})

st.subheader('서브헤더')
st.dataframe(data, use_container_width=True)

# 캔버스 만들기
# 맷플랏립
# 데이터로 그림 bar chart 그리기
fig= plt.figure()
plt.bar(data['이름'], data['나이'])
st.pyplot(fig)# 생성된 figure를 그리기

# seaborn 으로 그래프 그리기
barplot = sns.barplot(x='이름', y='나이', data=data, palette='Set2')
fig = barplot.get_figure()
st.pyplot(fig)

#############

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

# plt.show() 대신에 스트림릿으로 출력
st.pyplot(fig)
