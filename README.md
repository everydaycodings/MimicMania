# MiniMania

MiniMania is a web application that allows you to generate speech and clone voices using text-to-speech technology. With MiniMania, you can create custom voices in a variety of languages and use them for a range of applications, from voiceovers to chatbots.

## Features

- Easy-to-use interface: MiniMania has a user-friendly interface that allows users to quickly    generate speech in their desired language and voice.
- Multiple languages: MiniMania supports multiple languages, including English, Spanish, French, and more.
- Multiple voices: MiniMania provides a range of voices for each language, giving users a wide variety of options to choose from.
- Customizable parameters: Users can adjust the speed, pitch, and volume of the generated speech to fit their specific needs.
- Voice cloning: MiniMania's voice cloning technology allows users to clone their own voice, making it easier than ever to create personalized voiceovers.

## Things to Be Downloaded

Before you can install and use MiniMania, you will need to download and install the following:

- **ffmpeg:** MiniMania requires the ffmpeg library for audio encoding and decoding. To install ffmpeg, execute the command `apt-get install ffmpeg` in your terminal.
- **espeak-ng:** MiniMania uses the espeak-ng text-to-speech engine for generating speech in various languages. To install espeak-ng, execute the command `sudo apt-get install espeak-ng` in your terminal. 
- **espeak:** MiniMania uses the espeak-ng text-to-speech engine for generating speech in various languages. To install espeak-ng, execute the command `sudo apt-get install espeak` in your terminal.

Additionally, you will also need to download the required module and Python dependencies as described in the next section.

## Installation

To install and run MiniMania, follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/YourUserName/MiniMania.git`
2. Navigate to the project directory using `cd MiniMania`
3. Run the command `python setup.py` to download the required modules. This process may take some time, as the required module is around 6 GB.
4. Run the command `pip install -r requirements.txt` to download all the Python dependencies.
5. Type the command `streamlit run app.py` to start the web application.



## Contributing

If you'd like to contribute to MiniMania, please fork the repository and create a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

## Credits

MiniMania was developed by [Kumar Saksham(everydaycodings)] with the help of various open source resources. 

We would like to extend a special thank you to [coqui-ai/TTS](https://github.com/coqui-ai/TTS) for providing their text-to-speech model as a resource for our project.

MiniMania is licensed under the [MIT License](https://opensource.org/licenses/MIT). 

## Support

If you have any questions or issues with MiniMania, please contact us at [everydaycodings@gmail.com](mailto:everydaycodings@gmail.com) or reach out to us on Twitter [@everydaycodings](https://twitter.com/everydaycodings) or Medium [@everydaycodings](https://medium.com/@everydaycodings).

We're always happy to help!
