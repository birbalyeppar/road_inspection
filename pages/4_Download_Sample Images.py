import streamlit as st
import os
from io import BytesIO
from zipfile import ZipFile
from PIL import Image

# -- Settings --
st.set_page_config(page_title="Sample Images", page_icon="🖼️")

SAMPLE_IMAGE_DIR = "sample_images"

st.title("🖼️ Download Sample Images")
st.write("You can download individual images or all of them as a ZIP file to test the system.")

# -- Helper: Load all images from sample folder --
def load_images():
    image_files = [f for f in os.listdir(SAMPLE_IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    return image_files

# -- Load image files --
image_files = load_images()

if not image_files:
    st.warning("No sample images found. Please add images to the 'sample_images' folder.")
else:
    # -- Download All as ZIP on Top --
    def get_zip_buffer():
        zip_buffer = BytesIO()
        with ZipFile(zip_buffer, "w") as zip_file:
            for image_file in image_files:
                file_path = os.path.join(SAMPLE_IMAGE_DIR, image_file)
                zip_file.write(file_path, arcname=image_file)
        zip_buffer.seek(0)
        return zip_buffer

    st.subheader("📦 Download All")
    st.download_button(
        label="⬇️ Download All Images as ZIP",
        data=get_zip_buffer(),
        file_name="sample_images.zip",
        mime="application/zip"
    )

    st.divider()

    # -- Show images with download buttons --
    cols = st.columns(5)  # 5 images per row
    for idx, image_file in enumerate(image_files):
        image_path = os.path.join(SAMPLE_IMAGE_DIR, image_file)
        image = Image.open(image_path)

        with cols[idx % 5]:
            st.image(image, caption=image_file, use_column_width=True)
            with open(image_path, "rb") as img_file:
                st.download_button(
                    label="Download",
                    data=img_file,
                    file_name=image_file,
                    mime="image/jpeg"
                )
