import streamlit as st 
import matplotlib.pyplot as plt

# Plan project Hypotesis visualization page

def page_project_hypothesis_body():
    st.write('## Hypothesis and Validation')
    st.write('### Hypothesis:')

    st.info(
        f"Plants which are infected with powdery mildew show distinct, "
        f"markings on their leaves which indicate infection. "
        f"The markings on an infected leaf are usually light powdery stripes and spots.\n"
        )

    st.success(
        f"### Validation:\n\n"
        f"By displaying images of infected and healthy leaves we can visually "
        f"compare them in order to establish differences in the leaves.\n"
        f"This is done by creating an image montage to conduct the comparison of "
        f"infected and healthy leaves.\n"
        f'From analysis of the montage it can be seen that infected leaves '
        f"show distinct white markings that the healthy leaves dont."
    )