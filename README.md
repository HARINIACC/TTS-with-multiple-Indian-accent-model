# TTS-with-multiple-Indian-accent-model(OFFLINE)
This project is a Python script that preprocesses text and converts it into speech using a TTS model. The preprocessing ensures better clarity in spoken text by handling specific cases like acronyms and slashes.

Features

Acronym Handling: Acronyms like TP HYD are converted into T-P, H-Y-D for clearer pronunciation.

Slash Handling: Text with slashes, such as A/20, is converted to A slash 20.

Text-to-Speech Conversion: Converts processed text into speech and saves the output as an audio file (output.wav).

Prerequisites

Ensure you have the following installed:

Python 3.7 or later

Required libraries:

TTS (for text-to-speech processing)

re (for regular expressions, included in Python's standard library)

Installation

Install the TTS library using pip:

pip install TTS

Clone or download this repository.

Usage

Input Text: Provide the text you want to convert to speech. Example:

input_text = "Check the card A/20 in the TXC panel and RAM/B setup."

Run the Script: Execute the script to generate the speech:

python script_name.py

Processed Text: The script will preprocess the input text to handle acronyms and slashes. For example:

Input: Check the card A/20 in the TXC panel and RAM/B setup.

Processed: Check the card A slash 20 in the T-X-C panel and R-A-M slash B setup.

Audio Output: The speech is saved as output.wav in the current directory.

Code Overview

Key Functions

handle_acronyms(text):

Identifies acronyms (uppercase words) and converts them to a hyphen-separated format.

Example: TP HYD becomes T-P, H-Y-D.

handle_slashes(text):

Replaces slashes in text with the word "slash".

Example: A/20 becomes A slash 20.

process_text(text):

Calls the above functions to preprocess the text.

tts(text):

Preprocesses the input text.

Uses the TTS model (tts_models/en/ljspeech/tacotron2-DDC_ph) to generate speech.

Saves the audio as output.wav.

Example Workflow

input_text = "Check the card A/20 in the TXC panel and RAM/B setup."
tts(input_text)

Output

Processed text: Check the card A slash 20 in the T-X-C panel and R-A-M slash B setup.

Audio file: output.wav

Notes

The script is designed to enhance text clarity for TTS models.

You can extend the preprocessing functions to handle additional text formatting cases.

Troubleshooting

ModuleNotFoundError: Ensure you have installed the TTS library using:

pip install TTS

Text not processed correctly: Double-check the regular expressions in the handle_acronyms and handle_slashes functions for edge cases.

Author

Harini

For feedback or contributions, feel free to reach out!
