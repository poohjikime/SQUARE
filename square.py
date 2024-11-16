import streamlit as st
import math

st.title('양의 제곱근과 음의 제곱근 계산기')

number = st.number_input('제곱근을 구할 양수를 입력하세요:', min_value=0.0, value=0.0)

if st.button('계산하기'):
    if number > 0:
        positive_sqrt = math.sqrt(number)
        negative_sqrt = -math.sqrt(number)
        st.write(f'입력하신 {number}의 양의 제곱근은 {positive_sqrt:.3f} 입니다.')
        st.write(f'입력하신 {number}의 음의 제곱근은 {negative_sqrt:.3f} 입니다.')
    else:
        st.error('양수를 입력해주세요.')
