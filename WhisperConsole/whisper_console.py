from argparser.parser import CustomArgumentParser
import argparse
import whisper

parser = CustomArgumentParser(
     formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
args = parser.parse_all_args()

args.name="medium"

model = whisper.load_model(
    name=args.name,
    download_root=args.download_root,
    in_memory=args.in_memory,
)


# result = model.transcribe("audio.mp3", verbose=True)

args.audio = "audio.mp3"
args.verbose = True

result = model.transcribe(
    audio = args.audio,
    verbose=args.verbose,               
    temperature=args.temperature,               
    compression_ratio_threshold=args.compression_ratio_threshold,              
    logprob_threshold=args.logprob_threshold,               
    no_speech_threshold=args.no_speech_threshold,               
    condition_on_previous_text=args.condition_on_previous_text,               
    initial_prompt=args.initial_prompt,               
    word_timestamps=args.word_timestamps,              
    prepend_punctuations=args.prepend_punctuations,               
    append_punctuations=args.append_punctuations,
    )

print(result["text"])




