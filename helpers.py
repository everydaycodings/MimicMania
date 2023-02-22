import json
from TTS.api import TTS
import os
from pydub import AudioSegment
import librosa
import soundfile as sf
import streamlit as st
import datetime
import zipfile
import requests
from tqdm import tqdm


clonner_file_path = "clonner_output/voice_clonning_audio.wav"


def download_audio_file(audio, file_name):
    st.download_button(
        label="Download The Audio File",
        data=audio,
        file_name="{}-{}.wav".format(file_name, datetime.datetime.now()),
        mime="audio/wav")



class DownloadModels():

    def __init__(self):
        pass


    def download_models(self):


        # Set the URL of the ZIP file on Google Drive
        url = "https://drive.google.com/u/0/uc?id=1iltFKo48DctOzF8Sm4Bcn3GS9GEXgYvg&export=download&confirm=t&uuid=dc3156e7-054a-43ff-82c0-ab96eb98f433&at=ALgDtszFJkCFJTfums9pB4SaqwMC:1677095101169"
        temp_path = 'temp.zip'
        model_path = "language_model"

        dict_list = os.listdir(path=model_path)

        if len(dict_list) == 1:

            # Download the ZIP file to a temporary folder
            response = requests.get(url, stream=True)
            total_size_in_bytes = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

            with open(temp_path, 'wb') as f:

                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    f.write(data)

            progress_bar.close()
            print("Downloading Of Models Completed!")
            print("Starting The Extraction Process to {} Folder...".format(model_path))

            # Extract the contents of the ZIP file to a specific folder
            extract_folder = model_path
            with zipfile.ZipFile(temp_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)

            # Delete the ZIP file
            os.remove(temp_path)
            print("Extraction Completed!")
        
        else:
            print("Models already exists, skipping download and extraction.")



@st.cache_resource
class ProcessModelList():


    def __init__(self) -> None:
        pass


    def read_file(self):

        f = open("model_list.json", "r")
        data = json.load(f)

        return data
    

    def get_langauge_labels(self):

        data = self.read_file()

        return data["labels"]
    

    def get_popular_voice_list(self, model_name):
        data = self.read_file()

        if model_name in  data["custom_voice"]:
            return True
        else:
            return False
    

    def get_popular_voice_path(self, selected_language, selected_model):

        data = self.read_file()

        model_names = data["data"][selected_language]

        for i in range(len(model_names)):
             
             model_name = model_names[i]["name"]

             if model_name == selected_model:
                model_voice = model_names[i]["model_voice"]

                return model_voice
    


    def get_model_name(self, selected_language):
        
        model_name_list = []

        data = self.read_file()

        model_names = data["data"][selected_language]

        for i in range(len(model_names)):
             
             model_name = model_names[i]["name"]
             model_name_list.append(model_name)
        
        return model_name_list
    

    def get_model_path(self, selected_language, selected_model):

        data = self.read_file()

        model_names = data["data"][selected_language]

        for i in range(len(model_names)):
             
             model_name = model_names[i]["name"]

             if model_name == selected_model:
                model_path = model_names[i]["model_path"]

                return model_path

    
    def multi_language_selected(self, model_path):

        tts = TTS(model_path="language_model/{}/model_file.pth".format(str(model_path)), config_path="language_model/{}/config.json".format(str(model_path)))
        return tts.speakers, tts.languages

    
    def get_multi_speaker_model(self, model_path):

        search_model_path = "language_model/{}".format(str(model_path))
        subdirectories = os.listdir(path=search_model_path)

        if "speaker_ids.json" in subdirectories:
            tts = TTS(model_path="language_model/{}/model_file.pth".format(str(model_path)), config_path="language_model/{}/config.json".format(str(model_path)))
            return True, tts.speakers
        
        else:
            return False, None

@st.cache_resource
class ConvertTextToSpeech():

    def __init__(self, model_name, model_path, text):
        
        self.model_name = model_name
        self.model_path = model_path
        self.text = text
    
    
    def convert_text_to_speech(self, speaker_id=None):

        tts = TTS(model_path="language_model/{}/model_file.pth".format(str(self.model_path)), config_path="language_model/{}/config.json".format(str(self.model_path)))
        if speaker_id == None:
            tts.tts_to_file(text=self.text, file_path="output/output.wav")
        else:
            tts.tts_to_file(text=self.text, speaker=speaker_id, file_path="output/output.wav")

    
    def convert_text_to_speech_multi_langauge(self, speaker, language, model_name, selected_langauge):

        if ProcessModelList().get_popular_voice_list(model_name=model_name):
            tts = TTS(model_path="language_model/{}/model_file.pth".format(str(self.model_path)), config_path="language_model/{}/config.json".format(str(self.model_path)))
            tts.tts_to_file(text=self.text, speaker=tts.speakers[0], language=tts.languages[0], speaker_wav="language_model/{}".format(ProcessModelList().get_popular_voice_path(selected_model=model_name, selected_language=selected_langauge)), file_path="output/output.wav")

        else:
            tts = TTS(model_path="language_model/{}/model_file.pth".format(str(self.model_path)), config_path="language_model/{}/config.json".format(str(self.model_path)))
            tts.tts_to_file(text=self.text, speaker=speaker, language=language, file_path="output/output.wav")
        


    def read_audio_file(self):

        audio_file = open("output/output.wav", 'rb')
        audio_bytes = audio_file.read()
        return audio_bytes



@st.cache_resource
class AudioClonning():

    def __init__(self, audio, audio_filename, text, emotion):

        self.audio = audio
        self.audio_filename = audio_filename
        self.text = text
        self.emotion = emotion

    
    def convert_mp3_to_wav(self):

        input_file = self.audio

        # load the audio file using pydub
        audio = AudioSegment.from_file(input_file)

        # convert the audio to wav format
        audio.export(clonner_file_path, format='wav')
    

    def check_audio_file_format(self):


        audio_file_name = str(self.audio_filename).split(".")[-1]

        if audio_file_name == "mp3":
            self.convert_mp3_to_wav()

            return clonner_file_path
        
        else:
            audio = AudioSegment.from_file(self.audio)
            audio.export(clonner_file_path, format='wav')

            return clonner_file_path

    
    def convert_text_to_speech(self):

        clonner_audio = self.check_audio_file_format()

        tts = TTS(model_path="language_model/tts_models--multilingual--multi-dataset--your_tts/model_file.pth", config_path="language_model/tts_models--multilingual--multi-dataset--your_tts/config.json")
        tts.tts_to_file(text=self.text, speaker=tts.speakers[0], language=tts.languages[0], speaker_wav=clonner_audio, file_path="clonner_output/voice_clonning_audio.wav")
        
        audio_file = open(clonner_file_path, 'rb')
        
        return audio_file.read()
    

    def emotion_modification(self):

        emotion = str(self.emotion).lower()
        # load audio file
        y, sr = librosa.load(clonner_file_path)

        # modify audio file
        if emotion == 'happy':
            y_pitch = librosa.effects.pitch_shift(y, sr, n_steps=2)  # increase pitch by 2 semitones
            y_energy = y * 1.5  # increase energy level by 50%

        elif emotion == 'sad':
            y_pitch = librosa.effects.pitch_shift(y, sr, n_steps=-2)  # decrease pitch by 2 semitones
            y_energy = y * 0.5  # reduce energy level by 50%
        
        elif emotion == 'angry':
            y_pitch = librosa.effects.pitch_shift(y, sr, n_steps=-1)  # decrease pitch by 1 semitone
            y_energy = y * 2.0  # increase energy level by 100%
        
        elif emotion == 'surprise':
            y_pitch = librosa.effects.pitch_shift(y, sr, n_steps=3)  # increase pitch by 3 semitones
            y_energy = y * 2.5  # increase energy level by 150%
        
        elif emotion == 'neutral':
            y_pitch = y
            y_energy = y * 1.0  # no change in energy level
        
        elif emotion == 'dull':  # emotion is dull
            y_pitch = librosa.effects.pitch_shift(y, sr, n_steps=-3)  # decrease pitch by 3 semitones
            y_energy = y * 0.5  # reduce energy level by 50%

        # save modified audio file
        sf.write('clonner_output/voice_clonning_audio1.wav', y_pitch * y_energy, sr)

       
