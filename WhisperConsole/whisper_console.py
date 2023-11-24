from pathlib import Path
from argparser.parser import CustomArgumentParser
import argparse
import whisper

parser = CustomArgumentParser(
     formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
args = parser.parse_all_args()

print("")

args.name="tiny"

model = whisper.load_model(
    name=args.name,
    download_root=args.download_root,
    in_memory=args.in_memory,
)

# # load audio and pad/trim it to fit 30 seconds

args.file="audio.mp3"

audio = whisper.load_audio(
    file=args.file,
    sr=args.sr
)
audio = whisper.pad_or_trim(audio)

# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)

# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)

# # print the recognized text
# print(result.text)