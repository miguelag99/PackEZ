import streamlit as st
import os
import sys

# Add the parent directory to the path so we can import program_config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from backend.htop import htop_handler

st.title("System monitoring Installation Manager")

st.markdown("This page will install the following programs on your system:")
programs = [
    htop_handler
]


st.write("---")
# Display each program in the list
for program in programs:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(program.name)
    
    with col2:
        status_placeholder = st.empty()
        status_placeholder.write(program.status)
    
    with col3:
        if program.status == "Not installed":
            if st.button(f"Install {program.name}",
                         key=program.name,
                         icon=":material/enable:"):
                status_placeholder.write("Installing...")
                st.session_state[f"{program.name}_disabled"] = True
                st.session_state[f"{program.name}_icon"] = ":material/build:"
                if program.install(status_placeholder):
                    status_placeholder.write("Installed")
                    st.success(f"{program.name} installed successfully!")
                else:
                    status_placeholder.write("Failed")
                    st.error(f"Failed to install {program.name}")
        else:
            st.write(":material/check:")

    st.write("---")
    
# Display the refresh button at the bottom
if st.button("Refresh state", key="refresh_states", icon=":material/refresh:"):
    # Refresh all programs
    for program in programs:
        program.get_state()
    st.rerun()
