from argparser.extensions import str2bool
from argparse import ArgumentParser

def _output_arguments(parser:ArgumentParser):
    decode_arguments = parser.add_argument_group("Result Output")  
    # decode_arguments.add_argument(
    #     "--output_dir",
    #     default=".",
    #     help="""Directory to save the outputs""")
    
    # decode_arguments.add_argument(
    #     "--output_format",
    #     choices=['txt', 'json', 'console'],
    #     default="console",
    #     help="""format of the output file or print result to console""")
    
    decode_arguments.add_argument(
        "--result_to_file",
        type= str2bool,
        default="True",
        help="""If true, result seved to output directory corresponding to the audio file name""")
    
    