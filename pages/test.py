import streamlit as st

@st.cache_data
def long_running_function(param1, param2):
    # Perform time-consuming computations or data retrieval here
    # ...
    # Return the result
    result = int(param1) + int(param2)
    return result

@st.cache_data
def save_data(arr, result):
    arr.append(result)
    return arr

def main():
    arr = []
    st.title("Long-Running Function Example")
    
    # Input parameters
    param1 = st.slider("Parameter 1", 0, 10, 0)
    param2 = st.slider("Parameter 2", 0, 10, 0)

    # Call the long-running function
    result = long_running_function(param1, param2)
    arr = save_data(arr, result)

    # Display the result
    st.write("Result:", arr)

if __name__ == "__main__":
    main() 


