# MimicMania

MiniMania is a web application that provides text-to-speech (TTS) and voice cloning capabilities. The application utilizes deep learning models to generate high-quality speech output in multiple languages, with options to customize the pitch, speed, and volume of the generated audio. MiniMania's TTS engine is built on top of the Tacotron 2 and WaveGlow models, while its voice cloning capabilities are based on the FastSpeech and MelGAN models.

## Features

- Easy-to-use interface: MimicMania has a user-friendly interface that allows users to quickly    generate speech in their desired language and voice.
- Multiple languages: MimicMania supports multiple languages, including English, Spanish, French, and more.
- Multiple voices: MimicMania provides a range of voices for each language, giving users a wide variety of options to choose from.
- Customizable parameters: Users can adjust the speed, pitch, and volume of the generated speech to fit their specific needs.
- Voice cloning: MimicMania's voice cloning technology allows users to clone their own voice, making it easier than ever to create personalized voiceovers.

## Things to Be Downloaded

Before you can install and use MimicMania, you will need to download and install the following:

- **ffmpeg:** MimicMania requires the ffmpeg library for audio encoding and decoding. To install ffmpeg, execute the command `apt-get install ffmpeg` in your terminal.
- **espeak-ng:** MimicMania uses the espeak-ng text-to-speech engine for generating speech in various languages. To install espeak-ng, execute the command `sudo apt-get install espeak-ng` in your terminal. 
- **espeak:** MimicMania uses the espeak-ng text-to-speech engine for generating speech in various languages. To install espeak-ng, execute the command `sudo apt-get install espeak` in your terminal.

Additionally, you will also need to download the required module and Python dependencies as described in the next section.

## Installation

To install and run MimicMania, follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/YourUserName/MimicMania.git`
2. Navigate to the project directory using `cd MimicMania`
3. Run the command `python setup.py` to download the required modules. This process may take some time, as the required module is around 6 GB.
4. Run the command `pip install -r requirements.txt` to download all the Python dependencies.
5. Type the command `streamlit run app.py` to start the web application.



## Contributing

If you'd like to contribute to MimicMania, please fork the repository and create a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## Credits

MimicMania was developed by [Kumar Saksham(everydaycodings)] with the help of various open source resources. 

We would like to extend a special thank you to [coqui-ai/TTS](https://github.com/coqui-ai/TTS) for providing their text-to-speech model as a resource for our project.

MimicMania is licensed under the [MIT License](https://opensource.org/licenses/MIT). 

## Support

If you have any questions or issues with MimicMania, please contact us at [everydaycodings@gmail.com](mailto:everydaycodings@gmail.com) or reach out to us on Twitter [@everydaycodings](https://twitter.com/everydaycodings) or Medium [@everydaycodings](https://medium.com/@everydaycodings).

We're always happy to help!
