import re
from TTS.api import TTS

# Function to handle acronyms (split them into individual characters with hyphens)
def handle_acronyms(text):
    """
    Convert acronyms like 'TP HYD' into 'T-P, H-Y-D'.
    """
    text = re.sub(r'\b([A-Z]{2,})(?:\s+([A-Z]{2,}))*\b', lambda match: '-'.join([word for word in match.group(0).split()]), text)
    return text

# Slash handling in TTS (e.g., "A/20" becomes "A slash 20")
def handle_slashes(text):
    """
    Converts text with slashes into a more readable form for TTS,
    like 'A/20' to 'A slash 20'.
    """
    return re.sub(r'(\w)/(\w+)', r'\1 slash \2', text)

# Function to process text by handling acronyms and slashes
def process_text(text):
    """
    Process text to ensure acronyms are split, slashes are converted, and abbreviations are left as-is.
    """
    # Handle acronyms
    text = handle_acronyms(text)
    # Handle slashes
    text = handle_slashes(text)
    return text

# Function to convert text to speech
def tts(text):
    """
    Converts text to speech using a TTS model and saves the output to a file.
    """
    # Pre-process the text for acronyms and slashes
    processed_text = process_text(text)
    print(f"Processed text: {processed_text}")
    
    # Use the TTS model to generate speech
    tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC_ph", progress_bar=False)
    tts_model.tts_to_file(text=processed_text, file_path="output.wav")
    print("Audio saved to output.wav")

# Example input
input_text = "Check the card A/20 in the TXC panel and RAM/B setup."
tts(input_text)  
