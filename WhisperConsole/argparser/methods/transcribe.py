from argparser.extensions import str2bool
from argparse import ArgumentParser

def _transcribe_arguments(parser:ArgumentParser):
    
    transcribe_arguments = parser.add_argument_group("Transcribe")
        
    transcribe_arguments.add_argument(
        "audio",
        help="""The path to the audio file to open""")
        #TODO:
        # audio: Union[str, np.ndarray, torch.Tensor]
        
    transcribe_arguments.add_argument(
        "--verbose",
        type=str2bool,
        help="""Whether to display the text being decoded to the console. If True, displays all the details,
        If False, displays minimal details. If None, does not display anything""")
    
    transcribe_arguments.add_argument(
        "--compression_ratio_threshold",
        type=float,
        default=2.4,
        help="""If the gzip compression ratio is above this value, treat as failed""")
    
    transcribe_arguments.add_argument(
        "--logprob_threshold",
        type=float,
        default=-1.0,
        help="""If the average log probability over sampled tokens is below this value, treat as failed""")
        
    transcribe_arguments.add_argument(
        "--no_speech_threshold",
        type=float,
        default=0.6,
        help="""If the no_speech probability is higher than this value AND the average log probability
        over sampled tokens is below `logprob_threshold`, consider the segment as silent""")
    
    transcribe_arguments.add_argument(
        "--condition_on_previous_text",
        type=str2bool,
        default="True",
        help="""if True, the previous output of the model is provided as a prompt for the next window;
        disabling may make the text inconsistent across windows, but the model becomes less prone to
        getting stuck in a failure loop, such as repetition looping or timestamps going out of sync.""")
    
    transcribe_arguments.add_argument(
        "--initial_prompt",
        help="""Optional text to provide as a prompt for the first window. This can be used to provide, or
        "prompt-engineer" a context for transcription, e.g. custom vocabularies or proper nouns
        to make it more likely to predict those word correctly.""")
    
    transcribe_arguments.add_argument(
        "--word_timestamps",
        type=str2bool,
        default="False",
        help="""Extract word-level timestamps using the cross-attention pattern and dynamic time warping,
        and include the timestamps for each word in each segment.""")
    
    transcribe_arguments.add_argument(
        "--prepend_punctuations",
        default="\"'“¿([{-",
        help="""Extract word-level timestamps using the cross-attention pattern and dynamic time warping,
        and include the timestamps for each word in each segment.""")
    
    transcribe_arguments.add_argument(
        "--append_punctuations",
        default="\"'.。,，!！?？:：”)]}、",
        help="""If word_timestamps is True, merge these punctuation symbols with the previous word""")
    
    
    
