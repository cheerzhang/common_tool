import streamlit as st

def main():
    st.title("Multi-Select Example")

    options = ['a', 'b', 'c', 'd', 'e']

    selected_indices = st.multiselect("Select values", options)
    selected_values = [options[i] for i in selected_indices]

    if st.button("Print Logs"):
        logs = []
        for i, value in enumerate(selected_values, start=1):
            logs.append(f"{i}st: {value}")
        st.write("Logs:")
        for log in logs:
            st.write(log)

if __name__ == "__main__":
    main()

