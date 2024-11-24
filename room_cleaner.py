import os
from openai import OpenAI
from PIL import Image
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def analyze_room_image(image):
    """Analyze the room image and generate cleaning recommendations"""
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Analyze this messy room and provide a prioritized, step-by-step cleaning guide. Focus on breaking down the tasks into manageable chunks to prevent overwhelm. Include estimated time for each task."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image,
                            "detail": "auto"
                        }
                    }
                ]
            }
        ],
        max_tokens=1000
    )
    
    return response.choices[0].message.content

def create_streamlit_app():
    st.title("Room Cleaning Assistant")
    st.write("Upload a photo of your messy room to get a personalized cleaning guide!")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Your room", use_container_width=True)
        
        # Add a button to analyze the image
        if st.button("Get Cleaning Guide"):
            with st.spinner("Analyzing your room..."):
                # Convert image to base64 for API
                import base64
                from io import BytesIO
                
                buffered = BytesIO()
                image.save(buffered, format="JPEG")
                image_base64 = base64.b64encode(buffered.getvalue()).decode()
                image_url = f"data:image/jpeg;base64,{image_base64}"
                
                # Get cleaning recommendations
                cleaning_guide = analyze_room_image(image_url)
                
                # Display the cleaning guide
                st.subheader("Your Personalized Cleaning Guide:")
                st.write(cleaning_guide)

if __name__ == "__main__":
    create_streamlit_app()