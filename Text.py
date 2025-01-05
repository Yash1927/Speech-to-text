import speech_recognition as sr
import pyttsx3
import streamlit as st

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Streamlit App
st.title("Speech-to-Text and Text-to-Speech App")
st.write("Speak into your microphone, and the app will transcribe it and read it back to you.")

# Button to start the speech recognition
if st.button("Start Recording"):
    try:
        with sr.Microphone() as source2:
            st.write("Adjusting for ambient noise...")
            r.adjust_for_ambient_noise(source2, duration=0.5)

            st.write("Listening...")
            audio2 = r.listen(source2)

            st.write("Processing your speech...")
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            # Display the transcribed text
            st.success(f"You said: {MyText}")

            # Speak the recognized text
            SpeakText(MyText)
            st.info("The app is speaking the transcribed text.")

    except sr.RequestError as e:
        st.error(f"Could not request results; {e}")

    except sr.UnknownValueError:
        st.error("Could not understand the audio. Please try again.")

