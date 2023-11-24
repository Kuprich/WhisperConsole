from argparse import ArgumentParser

SAMPLE_RATE = 16_000


def _load_audio_arguments(parser:ArgumentParser):
    
    audio_arguments = parser.add_argument_group("Load Audio Arguments")
        
    audio_arguments.add_argument(
        "--file",
        help="""The audio file to open""")
    
    audio_arguments.add_argument(
        "--sr",
        type=int,
        default=SAMPLE_RATE,
        help="""The sample rate to resample the audio if necessary""")
    