from argparser.extensions import str2bool
from argparse import ArgumentParser

def _decode_options_arguments(parser:ArgumentParser):
    
    decode_arguments = parser.add_argument_group("Decode Options")
        
    decode_arguments.add_argument(
        "--task",
        default="transcribe",
        help="""whether to perform X->X "transcribe" or X->English "translate""")
    
    decode_arguments.add_argument(
        "--language",
        help="""language that the audio is in; uses detected language if None""")
    
    decode_arguments.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="""language that the audio is in; uses detected language if None""")

    decode_arguments.add_argument(
        "--sample_len",
        type=int,
        default=None,
        help="""Maximum number of tokens to sample""")
    
    decode_arguments.add_argument(
        "--best_of",
        type=int,
        default=None,
        help="""Number of independent sample trajectories, if t > 0""")
    
    decode_arguments.add_argument(
        "--beam_size",
        type=int,
        default=None,
        help="""Number of beams in beam search, if t == 0""")
    
    decode_arguments.add_argument(
        "--patience",
        type=int,
        default=None,
        help="""Patience in beam search (arxiv:2204.05424)""")
    
    decode_arguments.add_argument(
        "--length_penalty",
        type=float,
        default=None,
        help=""""Alpha" in Google NMT, or None for length norm, when ranking generations
        to select which to return among the beams or best-of-N samples""")
    
    decode_arguments.add_argument(
        "--without_timestamps",
        type=str2bool,
        default="False",
        help="""Use <|notimestamps|> to sample text tokens only""")
    
    decode_arguments.add_argument(
        "--max_initial_timestamp",
        type=float,
        default=1.0)
    
    decode_arguments.add_argument(
        "--fp16",
        type=str2bool,
        default="True",
        help="""Use fp16 for most of the calculation""")
    
    
    #TODO:
    # prompt: Optional[Union[str, List[int]]] = None  # for the previous context
    # prefix: Optional[Union[str, List[int]]] = None  # to prefix the current context
    # suppress_tokens: Optional[Union[str, Iterable[int]]] = "-1"
    # suppress_blank: bool = True  # this will suppress blank outputs
