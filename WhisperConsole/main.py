from argparser.parser import CustomArgumentParser
import argparse
from whisper_console.methods import load_model, transcribe
from whisper_console.output import output_result


parser = CustomArgumentParser(
     formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

args = parser.parse_all_args()

model = load_model(args)

result = transcribe(model, args)

output_result(result, args)



