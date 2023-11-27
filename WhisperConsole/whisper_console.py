from argparser.parser import CustomArgumentParser
import argparse
from whisper_console.methods import load_model, transcribe
from whisper_console.output import output_result


parser = CustomArgumentParser(
    prog='Whisper-console. Source code is awailble here: https://github.com/Kuprich/WhisperConsole',
    description='This is a wrapper on a very cool project: https://github.com/openai/whisper',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

args = parser.parse_all_args()

model = load_model(args)

result = transcribe(model, args)

out_file = output_result(result, args)


