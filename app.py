import streamlit as st
from helpers import ProcessModelList, ConvertTextToSpeech, AudioClonning, download_audio_file
import io



sidebar_options = ["Text To Speech", "Voice Clonning"]
choice = st.sidebar.selectbox(label="Select Your Usecase: ", options=sidebar_options)


if choice == sidebar_options[0]:
    model_list = ProcessModelList()

    selected_language = st.selectbox("Select The Language: ", options=model_list.get_langauge_labels())
    selected_model = st.selectbox("Select The Model: ", options=model_list.get_model_name(selected_language=selected_language))
    selected_model_path = model_list.get_model_path(selected_language=selected_language, selected_model=selected_model)
    multi_speaker, multi_speaker_list = model_list.get_multi_speaker_model(model_path=selected_model_path)

    if selected_language == "Multi Language":
        speakers, languages = model_list.multi_language_selected(model_path=selected_model_path)
        selected_speaker = st.selectbox("Select the voice: ", options=speakers) 
        selected_speaker_language = st.selectbox("Select the Speaker: ", options=languages)


    elif multi_speaker == True:
        selected_speaker = st.selectbox("Select the voice: ", options=multi_speaker_list)

    else:
        selected_speaker = None
        selected_speaker_language = None

    text = st.text_area("Enter Your Text which you want to convert to audio.")

    if st.button("Convert"):

        text_to_speech = ConvertTextToSpeech(model_name=selected_model, model_path=selected_model_path, text=text)
        
        if selected_language == "Multi Language" or selected_language == "Popular Person":
            text_to_speech.convert_text_to_speech_multi_langauge(speaker=selected_speaker, language=selected_speaker_language, model_name=selected_model, selected_langauge=selected_language)
        else:
            text_to_speech.convert_text_to_speech(speaker_id=selected_speaker)

        read_audio = text_to_speech.read_audio_file()
        st.audio(read_audio, format='audio/wav')
        download_audio_file(audio=read_audio, file_name="TTS")



elif choice == sidebar_options[1]:

    uploaded_music = st.file_uploader(label="Upload Your Audio File: ", type=["mp3", "wav"])
    text = st.text_area(label="Enter The text you want to convert: ")
    emotion = "Neutral"#st.selectbox(label="Select What will the voice emotion: ", options=["Neutral", "Happy", "Sad", "Angry", "Surprise", "Dull"])

    if st.button("Start Clonning"):
        if uploaded_music is not None:

            audio_filename = uploaded_music.name
            audio = io.BytesIO(uploaded_music.read())

            audio_clonning = AudioClonning(audio=audio, audio_filename=audio_filename, text=text, emotion=emotion)

            cloned_voice = audio_clonning.convert_text_to_speech()
            #cloned_voice = audio_clonning.emotion_modification()

            st.audio(cloned_voice, format="audio/wav")
            download_audio_file(audio=cloned_voice, file_name="Voice-Cloned")