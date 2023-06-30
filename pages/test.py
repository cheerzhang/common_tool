import streamlit as st

def main():
    st.title("Multi-Select Example")

    options = ['a', 'b', 'c', 'd', 'e']
    selected_indices = []

    selected_values = [options[i] for i in selected_indices]
    st.write("Selected Values:", selected_values)

    selected_values_logs = []

    selected = st.multiselect("Select values", options)
    selected_indices = [options.index(value) for value in selected]
    selected_values = [options[i] for i in selected_indices]

    selected_values_logs.append(selected_values)
    selected_values_logs_str = [', '.join(values) for values in selected_values_logs]
    st.write("Logs:")
    for i, log in enumerate(selected_values_logs_str):
        st.write(f"{i+1}st: {log}")

    if st.button("Print Logs"):
        for i, log in enumerate(selected_values_logs_str):
            st.write(f"{i+1}st: {log}")

if __name__ == "__main__":
    main()
