import argparse
from argparser.methods.load_model import _load_model_arguments
from argparser.methods.load_audio import _load_audio_arguments


class CustomArgumentParser(argparse.ArgumentParser):
    
    def parse_all_args(self):
        _load_model_arguments(self)
        _load_audio_arguments(self)
        return self.parse_args()
      
        