import sys
from argparser.parser import CustomArgumentParser
import argparse
from whisper_console.methods import load_model, transcribe, ffmpeg_is_installed
from whisper_console.output import output_result


parser = CustomArgumentParser(
    description='This is a wrapper on a very cool project: https://github.com/openai/whisper\n',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

if not ffmpeg_is_installed():
    print("""FFmpeg is required! Please, install it to continue. More info: https://ffmpeg.org/""")
    sys.exit(1)

args = parser.parse_all_args()

model = load_model(args)

result = transcribe(model, args)

out_file = output_result(result, args)

if out_file is not None:
    print(f"\nResult saved to the file:{out_file}")




