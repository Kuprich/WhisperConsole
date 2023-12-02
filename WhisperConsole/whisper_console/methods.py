import os
from pathlib import Path
import whisper
from whisper import Whisper 

from whisper_console.transcribe import transcribe as transcribe_fucntion


def _decode_options(args):
    return {
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

def load_model(args):
    
    download_root = Path(args.model_dir).expanduser()
    
    print(f"Path to download model files: {download_root}")
    
    return whisper.load_model(
        name=args.model,
        download_root=download_root,
        in_memory=args.in_memory,
    )
    
def transcribe(model:Whisper, args):
    return transcribe_fucntion(
        model= model,
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
        result_to_file=args.result_to_file,
        **_decode_options(args),
    )
    
    
def ffmpeg_is_installed():
    try:
        os.startfile(r'ffmpeg')
        return True
    except:
        return False
        
    