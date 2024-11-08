import streamlit as st
import os
import sys

# Add the parent directory to the path so we can import program_config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from backend.git import git_handler

st.title("Code management Installation Manager")

st.markdown("This page will install the following programs on your system:")
programs = [
    git_handler
]

st.write("---")
for program in programs:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(program.name)
    
    with col2:
        status_placeholder = st.empty()
        status_placeholder.write(program.status)
    
    with col3:
        if program.status == "Not installed":
            if st.button(f"Install {program.name}", key=program.name):
                status_placeholder.write("Installing...")
                if program.install(status_placeholder):
                    status_placeholder.write("Installed")
                    st.success(f"{program.name} installed successfully!")
                else:
                    status_placeholder.write("Failed")
                    st.error(f"Failed to install {program.name}")
        else:
            st.write("✓")

    st.write("---")