import streamlit as st
def main():
    number1 = st.number_input('Insert NUmber1')
    st.write('The current number is ', number1)
    number2 = st.number_input('Insert NUmber2')
    st.write('The current number is ', number2)
    subtraction=number2-number1
    st.write('The current number is ', subtraction)
    
if __name__ == "__main__":
    main()
