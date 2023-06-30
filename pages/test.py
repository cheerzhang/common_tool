import streamlit as st

@st.cache(allow_output_mutation=True)
def get_cached_values():
    return []

def main():
    st.title("Caching Selected Values")

    # Retrieve the cached values
    selected_values = get_cached_values()

    options = ['a', 'b', 'c', 'd', 'e']

    selected_indices = st.multiselect("Select values", options, default=selected_values)
    selected_values = [options[i] for i in selected_indices]

    # Update the cached values
    get_cached_values().clear()
    get_cached_values().extend(selected_values)

    if st.button("Print Cached Values"):
        st.write("Cached Values:", selected_values)

if __name__ == "__main__":
    main()


