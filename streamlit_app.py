import streamlit as st

# Example keyword-abbreviation dictionary
keyword_dict = {
    "Adas": "Adas",
    "Vehicle": "Veh",
    "Speed": "Speed",
    # Add more keywords and abbreviations as needed
}

# Function to split compound word using UpperCamelCase pattern


def split_upper_camel_case(word):
    import re
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', word)

    # Function to get abbreviation for each keyword
    def get_abbreviations(words):
        return [keyword_dict.get(word, "") for word in words]

        # Title of the app
        st.title("Naming Convention Checker")

        # Input section for entering a compound word
        compound_word = st.text_input(
            "Enter a compound word (e.g., AdasVehicleSpeed):")

        if compound_word:
            parts = split_upper_camel_case(compound_word)
            abbreviations = get_abbreviations(parts)

            st.write("### Split Words:")
            st.write(parts)

            st.write("### Abbreviations:")
            st.write(abbreviations)

            # Dropdown selectors to compose a compound word
            st.write("### Select Keywords from Dropdowns:")
            selected_parts = []
            # Assuming max 3 parts for simplicity, adjust as needed
            for i in range(3):
                selected_parts.append(st.selectbox(
                    f"Part {i+1}", [""] + list(keyword_dict.keys()), key=f"part_{i+1}"))

                if all(selected_parts):
                    composed_word = ''.join(
                        selected_parts)
                    composed_abbreviations = get_abbreviations(
                        selected_parts)

                    st.write("### Composed Word:")
                    st.write(composed_word)

                    st.write("### Abbreviations:")
                    st.write(composed_abbreviations)

                    # Ensure synchronization between text input and dropdowns
                    if compound_word:
                        st.write(
                            "### Corresponding Dropdown Selections:")
                        for i, part in enumerate(parts):
                            st.write(f"Part {i+1}: {part}")

                            st.write(
                                "### Abbreviations for Dropdown Selections:")
                            for i, abbreviation in enumerate(abbreviations):
                                st.write(f"Part {i+1}: {abbreviation}")

                    elif all(selected_parts):
                        st.write(
                            "### Corresponding Compound Word:")
                        st.write(composed_word)

                        st.write(
                            "### Abbreviations for Selected Parts:")
                        for i, abbreviation in enumerate(composed_abbreviations):
                            st.write(f"Part {i+1}: {abbreviation}")


# Running the app with `streamlit run app.py`
