from argparser.extensions import str2bool

from argparse import ArgumentParser

def _load_model_arguments(parser:ArgumentParser):
    
    model_arguments = parser.add_argument_group("Load Model")
        
    model_arguments.add_argument(
        "--model",
        default="base",
        help="""one of the official model names listed by `whisper.available_models()`, or
    path to a model checkpoint containing the model dimensions and the model state_dict.""")
        
    model_arguments.add_argument(
        "--model_dir",
        default="~/.cache/whisper",
        help="""path to download the model files""")
        
    model_arguments.add_argument(
        "--in_memory",
        type=str2bool,
        default="False",
        help="""whether to preload the model weights into host memory""")
    
    #TODO:
    # device : Union[str, torch.device]
    #     the PyTorch device to put the model into