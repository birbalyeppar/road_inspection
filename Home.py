import streamlit as st

st.set_page_config(
    page_title="Road Damage Apps",
    page_icon="🛣️",
)

st.title("Road Damage Detection")

st.markdown(
    """
    This application is designed to enhance road safety and infrastructure maintenance by swiftly identifying and categorizing various forms of road damage, such as potholes and cracks.

    The model can detect four types of road damages:
    - Longitudinal Crack
    - Transverse Crack
    - Alligator Crack
    - Potholes

    It is trained using the YOLOv8-small model on a combination of Japanese and Indian road datasets (CRDDC2022).

    ---
    ### 📥 Test It Yourself!
    👉 Download sample images from the **"Download Sample Images"** page (available in the sidebar), and test them using the **Image Upload** section.

    🔧 You can also try adjusting the **Confidence Threshold** manually to control the sensitivity of detection results.

    ---
    🚀 **Supported Modes:**
    - Realtime Webcam Capture *(coming soon)*  
    - Video Upload *(coming soon)*  
    - 📷 Image Upload (**currently available** ✅)

    👉 Select the available mode from the sidebar. Currently, only **Image Upload** is active and working.
    """
)

st.divider()
