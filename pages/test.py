import streamlit as st

@st.cache_data
def long_running_function(param1, param2):
    # Perform time-consuming computations or data retrieval here
    # ...
    # Return the result
    return result

def main():
    st.title("Long-Running Function Example")
    
    # Input parameters
    param1 = st.slider("Parameter 1", 0, 10)
    param2 = st.text_input("Parameter 2", "")

    # Call the long-running function
    result = long_running_function(param1, param2)

    # Display the result
    st.write("Result:", result)

if __name__ == "__main__":
    main() 


