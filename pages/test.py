import streamlit as st


def get_translate(word):
    translate = word + '_translate'
    return translate

def main():
    st.title("Option Selection")

    options = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5',
               'Option 6', 'Option 7', 'Option 8', 'Option 9', 'Option 10']
    selected_options = []

    selected = st.multiselect("Select options", options)
    selected_options.extend(selected)

    if st.button("Print Selection"):
        st.write("Selected Options:")
        for i, option in enumerate(selected_options, start=1):
            t = get_translate(option)
            st.write(f"{i}. {option}.")

if __name__ == "__main__":
    main()




