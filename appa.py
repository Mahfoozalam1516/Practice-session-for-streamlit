import streamlit as st

def rate_yourself():
    with st.sidebar:
        st.title('Rate Yourself')
        languages = st.text_input('Enter the programming languagesa that you know with comma seperations', value = 'Python')
        languages = [i.strip() for i in languages.split(',')]
    st.subheader('How would you rate youself in specified programming language')
    for language in languages:
        st.write(language)
        st.slider(language, min_value = 0. , max_value = 10., step = .5)

        
def bmi_calculator():
    st.title ('BMI Calculator')

    with st.form('BMI Calculator'):
        col1, col2, col3 = st.columns ([3,2,1])
        with col1:
            weight = st.number_input('Enter your weights in KG')
        with col2:
            height = st.number_input('Enter your height in Meters')
        with col3:
            submit = st.form_submit_button ('Calculator')

        if submit:
            BMI = round((weight / (height**2)), 2)
            if BMI<= 18.5:
                st.error('Underweight')
            elif BMI > 18.5 and BMI <= 24.9:
                st.success('Healthy/Normal')
            elif BMI >= 25.0 and BMI <= 29.9:
                st.warning('Overweight')
            elif BMI >= 30.0:
                st.error('Obese')

choice = st.sidebar.selectbox('Menu', ['BMI','Rate Yourself'])

if choice == 'BMI':
    bmi_calculator()
elif choice == 'Rate Yourself':
    rate_yourself()