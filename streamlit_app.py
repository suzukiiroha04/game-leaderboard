import streamlit as st
import pandas as pd

st.set_page_config(page_title="게임 대회 리더보드", layout="centered")

st.title("🏆 2025 게임 챔피언십 리더보드")
st.markdown("4라운드 점수를 입력하면 자동으로 순위가 매겨집니다.")

teams = ['팀 A', '팀 B', '팀 C', '팀 D', '팀 E', '팀 F', '팀 G', '팀 H']
rounds = ['라운드 1', '라운드 2', '라운드 3', '라운드 4']

scores = []

st.subheader("🎯 점수 입력")

for team in teams:
    with st.expander(f"{team} 점수 입력"):
        team_scores = []
        for rnd in rounds:
            score = st.number_input(f"{team} - {rnd}", min_value=0, key=f"{team}_{rnd}")
            team_scores.append(score)
        total = sum(team_scores)
        scores.append({'팀': team, '총점': total, **{rnd: s for rnd, s in zip(rounds, team_scores)}})

# 데이터프레임 생성 및 정렬
df = pd.DataFrame(scores)
df = df.sort_values(by='총점', ascending=False).reset_index(drop=True)
df.index += 1  # 순위로 사용

# 🥇 이모지 추가
medals = ['🥇', '🥈', '🥉'] + [''] * (len(df) - 3)
df.insert(0, '순위', medals[:len(df)])

st.subheader("📋 현재 리더보드")
st.dataframe(df.style.highlight_max(axis=0, subset=['총점'], color='lightgreen'), use_container_width=True)
