from argparser.parser import CustomArgumentParser
import argparse
from whisper_console.methods import load_model, transcribe


parser = CustomArgumentParser(
     formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

args = parser.parse_all_args()

args.name="medium"

model = load_model(args)

result = transcribe(model, args)

print(result["text"])


