import streamlit as st
st.title('은경박의 첫 웹앱')
st.write('만나서 반가워요!!🤗')
import streamlit as st
import streamlit as st

# -------------------------------------------------
# 기본 설정
# -------------------------------------------------
st.set_page_config(
    page_title="MBTI 포켓몬 추천",
    page_icon="⚡",
    layout="centered"
)

# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>

.stApp{
    background:#FFF9E6;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#FFB300;
}

.subtitle{
    text-align:center;
    color:#666;
    font-size:18px;
    margin-bottom:25px;
}

.result-card{
    background:white;
    border-radius:20px;
    padding:25px;
    border:3px solid #FFD54F;
    box-shadow:0px 5px 15px rgba(0,0,0,.12);
}

.pokemon{
    font-size:42px;
    font-weight:bold;
    color:#1976D2;
}

.section{
    font-size:22px;
    font-weight:bold;
    margin-top:20px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# 제목
# -------------------------------------------------

st.markdown(
    '<div class="title">⚡ MBTI 포켓몬 추천 ⚡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">당신의 MBTI와 가장 잘 어울리는 포켓몬을 찾아드립니다.</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# MBTI 목록
# -------------------------------------------------

mbti_list = [
"INTJ","INTP","ENTJ","ENTP",
"INFJ","INFP","ENFJ","ENFP",
"ISTJ","ISFJ","ESTJ","ESFJ",
"ISTP","ISFP","ESTP","ESFP"
]

selected = st.selectbox(
    "MBTI를 선택하세요.",
    mbti_list
)

# -------------------------------------------------
# 데이터
# -------------------------------------------------

pokemon = {

"INTJ":{
"name":"뮤츠",
"type":"에스퍼",
"reason":"탁월한 전략과 분석 능력을 가진 지적인 리더.",
"strength":"계획성 · 논리성 · 통찰력",
"weakness":"감정 표현이 서툴 수 있음",
"job":"연구원, 전략기획, 개발자"
},

"INTP":{
"name":"후딘",
"type":"에스퍼",
"reason":"호기심과 탐구심이 뛰어난 천재형.",
"strength":"창의력 · 분석력",
"weakness":"실행력이 부족할 수 있음",
"job":"과학자, 교수, AI개발자"
},

"ENTJ":{
"name":"리자몽",
"type":"불꽃 / 비행",
"reason":"카리스마와 추진력이 강한 리더.",
"strength":"결단력 · 리더십",
"weakness":"독단적일 수 있음",
"job":"CEO, 팀장, 사업가"
},

"ENTP":{
"name":"조로아크",
"type":"악",
"reason":"아이디어가 풍부하고 새로운 도전을 즐김.",
"strength":"창의성 · 순발력",
"weakness":"끈기가 부족할 수 있음",
"job":"기획자, 마케터, 창업가"
},

"INFJ":{
"name":"가디안",
"type":"에스퍼 / 페어리",
"reason":"타인의 마음을 잘 이해하는 이상주의자.",
"strength":"공감 능력 · 통찰력",
"weakness":"혼자 고민을 많이 함",
"job":"상담사, 교육자"
},

"INFP":{
"name":"이브이",
"type":"노말",
"reason":"무한한 가능성을 가진 이상주의자.",
"strength":"창의성 · 배려심",
"weakness":"우유부단할 수 있음",
"job":"작가, 디자이너"
},

"ENFJ":{
"name":"루카리오",
"type":"격투 / 강철",
"reason":"정의감과 책임감이 강한 리더.",
"strength":"배려 · 리더십",
"weakness":"자신보다 남을 먼저 생각함",
"job":"교사, 리더, 코치"
},

"ENFP":{
"name":"피카츄",
"type":"전기",
"reason":"밝고 긍정적인 에너지의 소유자.",
"strength":"사교성 · 창의력",
"weakness":"충동적일 수 있음",
"job":"유튜버, 기획자, MC"
},

"ISTJ":{
"name":"거북왕",
"type":"물",
"reason":"책임감이 강하고 신뢰를 주는 유형.",
"strength":"성실함 · 책임감",
"weakness":"융통성이 부족할 수 있음",
"job":"공무원, 회계사"
},
"ISFJ":{
"name":"해피너스",
"type":"노말",
"reason":"헌신적이고 따뜻한 마음으로 주변 사람들을 돌봅니다.",
"strength":"배려심 · 책임감",
"weakness":"거절을 어려워함",
"job":"간호사, 사회복지사, 교사"
},

"ESTJ":{
"name":"보스로라",
"type":"강철 / 바위",
"reason":"원칙을 중요하게 생각하며 조직을 안정적으로 이끕니다.",
"strength":"실행력 · 조직력",
"weakness":"융통성이 부족할 수 있음",
"job":"관리자, 공무원, 군인"
},

"ESFJ":{
"name":"픽시",
"type":"페어리",
"reason":"사람들과 함께할 때 가장 큰 행복을 느낍니다.",
"strength":"친화력 · 배려",
"weakness":"타인의 평가에 민감",
"job":"서비스직, 상담사, 교사"
},

"ISTP":{
"name":"핫삼",
"type":"벌레 / 강철",
"reason":"조용하지만 뛰어난 문제 해결 능력을 갖춘 실용주의자.",
"strength":"분석력 · 적응력",
"weakness":"감정 표현 부족",
"job":"엔지니어, 정비사"
},

"ISFP":{
"name":"라프라스",
"type":"물 / 얼음",
"reason":"온화하고 감성이 풍부한 예술가형.",
"strength":"감수성 · 배려",
"weakness":"갈등을 피하려 함",
"job":"디자이너, 음악가, 사진작가"
},

"ESTP":{
"name":"초염몽",
"type":"에스퍼",
"reason":"도전을 즐기며 행동력이 뛰어난 해결사.",
"strength":"실행력 · 순발력",
"weakness":"계획성이 부족할 수 있음",
"job":"사업가, 영업직, 운동선수"
},

"ESFP":{
"name":"윈디",
"type":"불꽃",
"reason":"밝고 활기찬 분위기 메이커.",
"strength":"사교성 · 긍정성",
"weakness":"즉흥적인 선택",
"job":"배우, 방송인, 이벤트기획자"
}

}

# ---------------------------------------------
# 추천 결과
# ---------------------------------------------

st.divider()

if st.button("✨ 포켓몬 추천받기", use_container_width=True):

    data = pokemon[selected]

    st.markdown(
        f"""
<div class="result-card">

<div class="pokemon">
🎉 {data['name']}
</div>

### 🧬 타입
**{data['type']}**

### ⭐ 추천 이유
{data['reason']}

### 💪 강점
{data['strength']}

### ⚠️ 약점
{data['weakness']}

### 💼 잘 어울리는 직업
{data['job']}

</div>
""",
        unsafe_allow_html=True
    )

    st.success(
        f"{selected} 유형에게 가장 잘 어울리는 포켓몬은 **{data['name']}** 입니다!"
    )

st.markdown(
"""
<div class="footer">
Made with ❤️ using Streamlit
</div>
""",
unsafe_allow_html=True
)
