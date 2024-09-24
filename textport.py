# Installations
# !pip install streamlit-scrollable-textbox


# Import statements
import streamlit as st # for UI
import streamlit_scrollable_textbox as stx # for scrollable text areas



# ------------------------------------ DATA ------------------------------------
@st.cache_data
def load_data():
    """
    Locates and loads all chat data files. Uses st.cache_data decorator to cache the dataframes.

    Parameters
    ----------
    name : datatype
        description.

    Returns
    -------
    name : datatype
        description.
    """
    print('loading data...g')


# ------------------------------------ HELPER FUNCTIONS ------------------------------------



# ------------------------------------ STYLING FUNCTIONS ------------------------------------



# ------------------------------------ APP ------------------------------------
def main():
    st.title('TEXTPORT :rocket:')

    st.divider()
    
    st.subheader('Previous Export History:')
    # TESTING contact names & previous export info - to be extracted from chat files
    contact_names = "Hilary Pepperly, Jason Liu, Frederick Montag, Erin Cameron, Elliot Harding, Yuval Penn, Ishtar Lurig, Travis Dent, Reba Thickett, Perry Farhan, Ophelia Nguyen, Leanne Pepperly, Jason Harding, Frederick Montag, Pheobe Cannon, Primrose Lillian, Thierry Oldfield, Rebecca Grant, Whittaker Dent, Liam Ingrid, Willow Fable, Keesha Plum"
    contact_names = contact_names.split(sep=',')
    previous_export = f"""Dates: 06/04/2023 - 05/01/2024
                        Contacts: {', '.join(contact_names)}"""
    stx.scrollableTextbox(previous_export, height=70)
    
    with st.form('new_export'):
        st.subheader('New Export:')
        st.write('**Reminder: perform an unencrypted backup of your device on your machine prior to exporting**')
        
        st.date_input('Start Date')
        st.date_input('End Date')
        st.checkbox('All dates')

        st.multiselect('Contacts to Download:', contact_names)
        st.checkbox('All contacts')
        
        st.selectbox('Filetype:', ('PDF', 'CSV', 'Excel', 'HTML'))
    
        submitted = st.form_submit_button()
    
    if submitted:
        st.write('Form submitted!')



# ------------------------------------ RUN THE APP ------------------------------------
if __name__ == "__main__":
    main()