import streamlit as st
def main():
    st.title('Subtraction Of Two Numbers')
    number1 = st.number_input('Insert Number1')
    number2 = st.number_input('Insert Number2')
    subtraction=number2-number1
    st.write('The subtraction of above numbers is  Number2-Number1 ', subtraction)
    
if __name__ == "__main__":
    main()
