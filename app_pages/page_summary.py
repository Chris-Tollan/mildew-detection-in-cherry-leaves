import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew is a fungal disease that commonly "
        f"affects cherry trees. It appears as a white or gray  "
        f"powdery substance on the leaves, stems, "
        f"and sometimes fruit of the tree.\n"
        f"The fungus responsible for powdery mildew "
        f"thrives in warm, humid conditions and is spread through "
        f"spores being carried by the wind.\n\n "
        f"The risk of infection with powdery mildew is relatively high  "
        f"in cherry trees, especially during periods of warm, humid weather."
        f"Once infected, the fungus can spread rapidly throughout the tree and "
        f"cause damage to the leaves, reducing the "
        f"trees ability to photosynthesize and eventually impacting fruit production.")


    st.write(
        f"**Dataset**\n\n"
        f"The dataset was provided by the client.\n "
        f"It contains 4208 images of cherry leaves, "
        f"2104 healthy leaves and 2104 powdery mildew infected leaves.")


    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Chris-Tollan/mildew-detection-in-cherry-leaves).")


    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from "
        f"one that contains powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is "
        f"healthy or contains powdery mildew."
        )

