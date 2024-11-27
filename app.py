import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
# 애플 사용자 
# plt.rcParams['font.family'] = "AppleGothic"
# Windows, 리눅스 사용자
plt.rcParams['font.family'] = "NanumGothic"
plt.rcParams['axes.unicode_minus'] = False
# import matplotlib.font_manager as fm
# import os
# # os.getcwd() #프로젝트 경로 
# fpath = os.path.join(os.getcwd(), 'Nanum_Gothic/NanumGothic-Bold.ttf')
# prop = fm.FontProperties(fname=fpath)


# DataFrame 생성
data = pd.DataFrame({
    'name': ['김', 'lee', 'park'],
    'age': [22, 31, 25],
    'weight': [75.5, 80.2, 55.1]
})

st.dataframe(data, use_container_width=True)

# 캔버스 만들기 
# 맷플랏립
fig, ax = plt.subplots()
# 데이터로 그림 bar chart 그리기
ax.bar(data['name'], data['age'])
# 생성된 figure를 그리기 
st.pyplot(fig)

# seaborn 으로 그래프 그리기 
barplot = sns.barplot(x='name', y='age', data=data, ax=ax, palette='Set2')

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
