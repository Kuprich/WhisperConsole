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

args.fp16=False

decode_options = {
    "task": args.task,
    "language": args.language,
    "temperature": args.temperature,
    "sample_len": args.sample_len,
    "best_of": args.best_of,
    "beam_size": args.beam_size,
    "patience": args.patience,
    "length_penalty": args.length_penalty,
    "without_timestamps": args.without_timestamps,
    "max_initial_timestamp": args.max_initial_timestamp,
    "fp16": args.fp16,
}
    

args.audio = "audio.mp3"
args.verbose = True

result = model.transcribe(
    audio = args.audio,
    verbose=args.verbose,                         
    compression_ratio_threshold=args.compression_ratio_threshold,              
    logprob_threshold=args.logprob_threshold,               
    no_speech_threshold=args.no_speech_threshold,               
    condition_on_previous_text=args.condition_on_previous_text,               
    initial_prompt=args.initial_prompt,               
    word_timestamps=args.word_timestamps,              
    prepend_punctuations=args.prepend_punctuations,               
    append_punctuations=args.append_punctuations,
    **decode_options,
    )


print(result["text"])


