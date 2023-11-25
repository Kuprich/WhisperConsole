import argparse
from argparser.methods.load_model import _load_model_arguments
from argparser.methods.transcribe import _transcribe_arguments


class CustomArgumentParser(argparse.ArgumentParser):
    
    def parse_all_args(self):
        
        _load_model_arguments(self)
        _transcribe_arguments(self)
        
        return self.parse_args()
      
        