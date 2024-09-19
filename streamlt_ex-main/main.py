import streamlit as st

st.title('나의 첫 웹 서비스 만들기!!')

# 사용자 입력 받기
name = st.text_input('엄준식을 입력해주세요 : ')
mbti = st.selectbox('MBTI를 선택해주세요:', [
    'INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP'
])

# MBTI 설명 데이터 (더 자세히)
mbti_data = {
    'INTJ': {
        '특징': ' 전략적 사고와 높은 독립성을 가진 유형으로, 계획적이며 체계적입니다. '
               '논리적이고 분석적인 사고를 통해 문제를 해결하며, 목표 달성을 위해 끊임없이 노력합니다. '
               '독립적이고 자기주도적인 성향이 강해, 혼자서 일하는 것을 선호합니다.',
        '직업': '과학자, 엔지니어, 교수, 전략기획자, 데이터 분석가',
        '잘 맞는 MBTI': ['ENFP', 'ENTP']
    },
    'INFP': {
        '특징': '이상주의적이고 감정적인 유형으로, 예술적 감각이 뛰어납니다. '
               '강한 내면의 가치를 지니고 있으며, 다른 사람의 감정을 잘 이해하고 공감합니다. '
               '창의적이고 독창적인 아이디어를 많이 가지고 있으며, 예술이나 문학 분야에서 두각을 나타냅니다.',
        '직업': '작가, 예술가, 상담사, 교사, 음악가',
        '잘 맞는 MBTI': ['ENFJ', 'ESFJ']
    },
    'ENTJ': {
        '특징': '천부적인 리더십을 지닌 유형으로, 목표 지향적이고 결정력이 뛰어납니다. '
               '논리적이고 분석적인 사고를 통해 문제를 해결하며, 조직을 효율적으로 운영하는 능력이 탁월합니다. '
               '자기주장이 강하고 경쟁을 즐기며, 도전적인 환경에서 최고의 성과를 냅니다.',
        '직업': '경영자, 사업가, 변호사, 관리자, 정치인',
        '잘 맞는 MBTI': ['INFP', 'ISFP']
    },
    'ENTP': {
        '특징': '창의적이고 혁신적인 유형으로, 새로운 아이디어와 도전에 열정적입니다. '
               '논리적이고 분석적인 사고를 통해 문제를 해결하며, 다양한 분야에 관심이 많습니다. '
               '사교적이고 에너지가 넘치며, 토론을 즐기고 다른 사람과의 상호작용을 통해 발전합니다.',
        '직업': '발명가, 변호사, 마케팅 전문가, 컨설턴트, 기업가',
        '잘 맞는 MBTI': ['INFJ', 'INTJ']
    },
    'INFJ': {
        '특징': '직관적이고 감정적인 유형으로, 깊은 통찰력과 공감 능력을 지니고 있습니다. '
               '이상주의적이며, 다른 사람을 돕고자 하는 마음이 강합니다. '
               '창의적이고 독창적인 아이디어를 많이 가지고 있으며, 예술이나 문학 분야에서 두각을 나타냅니다.',
        '직업': '상담사, 심리학자, 작가, 예술가, 교사',
        '잘 맞는 MBTI': ['ENFP', 'ENTP']
    },
    'INFP': {
        '특징': '이상주의적이고 감정적인 유형으로, 예술적 감각이 뛰어납니다. '
               '강한 내면의 가치를 지니고 있으며, 다른 사람의 감정을 잘 이해하고 공감합니다. '
               '창의적이고 독창적인 아이디어를 많이 가지고 있으며, 예술이나 문학 분야에서 두각을 나타냅니다.',
        '직업': '작가, 예술가, 상담사, 교사, 음악가',
        '잘 맞는 MBTI': ['ENFJ', 'ESFJ']
    },
    'ENFJ': {
        '특징': '카리스마 있고 사교적인 유형으로, 타인을 돕고자 하는 마음이 강합니다. '
               '높은 감정 지능을 지니고 있으며, 다른 사람의 감정을 잘 이해하고 공감합니다. '
               '조직을 이끄는 능력이 탁월하며, 팀워크를 중시하고 협력적인 환경에서 최고의 성과를 냅니다.',
        '직업': '교사, 상담사, 사회복지사, 인사 전문가, 코치',
        '잘 맞는 MBTI': ['INFP', 'ISFP']
    },
    'ENFP': {
        '특징': '창의적이고 활기찬 유형으로, 새로운 아이디어와 도전에 열정적입니다. '
               '사교적이고 에너지가 넘치며, 다양한 사람과의 상호작용을 즐깁니다. '
               '높은 감정 지능을 지니고 있으며, 다른 사람의 감정을 잘 이해하고 공감합니다.',
        '직업': '마케팅 전문가, 작가, 예술가, 상담사, 교사',
        '잘 맞는 MBTI': ['INFJ', 'INTJ']
    },
    'ISTJ': {
        '특징': '현실적이고 신뢰할 수 있는 유형으로, 책임감이 강합니다. '
               '논리적이고 분석적인 사고를 통해 문제를 해결하며, 체계적이고 조직적인 접근을 선호합니다. '
               '전통과 규칙을 중시하며, 안정적인 환경에서 최고의 성과를 냅니다.',
        '직업': '회계사, 관리자, 변호사, 공무원, 엔지니어',
        '잘 맞는 MBTI': ['ESFP', 'ESTP']
    },
    'ISFJ': {
        '특징': '친절하고 사려 깊은 유형으로, 타인을 돕고자 하는 마음이 강합니다. '
               '높은 감정 지능을 지니고 있으며, 다른 사람의 감정을 잘 이해하고 공감합니다. '
               '조직적이고 책임감이 강하며, 세부 사항에 주의를 기울입니다.',
        '직업': '간호사, 교사, 상담사, 사회복지사, 관리자',
        '잘 맞는 MBTI': ['ESFP', 'ESTP']
    },
    'ESTJ': {
        '특징': '현실적이고 체계적인 유형으로, 책임감이 강합니다. '
               '논리적이고 분석적인 사고를 통해 문제를 해결하며, 조직을 효율적으로 운영하는 능력이 탁월합니다. '
               '전통과 규칙을 중시하며, 안정적인 환경에서 최고의 성과를 냅니다.',
        '직업': '경영자, 관리자, 변호사, 공무원, 엔지니어',
        '잘 맞는 MBTI': ['ISTP', 'ISFP']
    },
    'ESFJ': {
        '특징': '사교적이고 친절한 유형으로, 타인을 돕고자 하는 마음이 강합니다. '
               '높은 감정 지능을 지니고 있으며, 다른 사람의 감정을 잘 이해하고 공감합니다. '
               '조직적이고 책임감이 강하며, 세부 사항에 주의를 기울입니다.',
        '직업': '간호사, 교사, 상담사, 사회복지사, 관리자',
        '잘 맞는 MBTI': ['ISFP', 'ISTP']
    },
    'ISTP': {
        '특징': '현실적이고 독립적인 유형으로, 문제 해결에 뛰어납니다. '
               '논리적이고 분석적인 사고를 통해 문제를 해결하며, 실용적인 접근을 선호합니다. '
               '혼자서 일하는 것을 선호하며, 새로운 도전과 모험을 즐깁니다.',
        '직업': '엔지니어, 기술자, 파일럿, 탐험가, 스포츠 선수',
        '잘 맞는 MBTI': ['ESFJ', 'ESTJ']
    },
    'ISFP': {
        '특징': '감정적이고 예술적인 유형으로, 높은 감정 지능을 지니고 있습니다. '
               '강한 내면의 가치를 지니고 있으며, 다른 사람의 감정을 잘 이해하고 공감합니다. '
               '창의적이고 독창적인 아이디어를 많이 가지고 있으며, 예술이나 문학 분야에서 두각을 나타냅니다.',
        '직업': '예술가, 음악가, 디자이너, 상담사, 교사',
        '잘 맞는 MBTI': ['ENFJ', 'ESFJ']
    },
    'ESTP': {
        '특징': '활기차고 사교적인 유형으로, 새로운 도전과 모험을 즐깁니다. '
               '현실적이고 실용적인 접근을 통해 문제를 해결하며, 타고난 협상가입니다. '
               '다양한 사람과의 상호작용을 즐기며, 즉각적인 피드백을 선호합니다.',
        '직업': '기업가, 마케팅 전문가, 판매 전문가, 운동 선수, 파일럿',
        '잘 맞는 MBTI': ['ISFJ', 'ISTJ']
    },
    'ESFP': {
        '특징': '사교적이고 활기찬 유형으로, 타인을 돕고자 하는 마음이 강합니다. '
               '높은 감정 지능을 지니고 있으며, 다른 사람의 감정을 잘 이해하고 공감합니다. '
               '다양한 사람과의 상호작용을 즐기며, 즉각적인 피드백을 선호합니다.',
        '직업': '간호사, 사회복지사, 상담사, 교사, 마케팅 전문가',
        '잘 맞는 MBTI': ['ISFJ', 'ISTJ']
    },
}

if st.button('특징 생성'):
    if mbti in mbti_data:
        특징 = mbti_data[mbti]['특징']
        직업 = mbti_data[mbti]['직업']
        잘_맞는_mbti = ', '.join(mbti_data[mbti]['잘 맞는 MBTI'])

        st.write(f"{name}님! 당신의 MBTI 유형은 {mbti}입니다!")
        st.write(f"**특징**: {특징}")
        st.write(f"**어울리는 직업**: {직업}")
        st.write(f"**잘 맞는 MBTI 유형**: {잘_맞는_mbti}")
    else:
        st.write(f"{name}님! 아직 {mbti} 유형에 대한 정보가 없습니다.")
