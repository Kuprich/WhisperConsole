import sys
from argparser.parser import CustomArgumentParser
import argparse
from whisper_console.methods import load_model, transcribe, ffmpeg_is_installed



parser = CustomArgumentParser(
    description='This is a wrapper on a very cool project: https://github.com/openai/whisper\n',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

if not ffmpeg_is_installed():
    print("""FFmpeg is required! Please, install it to continue. More info: https://ffmpeg.org/""")
    sys.exit(1)


args = parser.parse_all_args()
args.verbose = True
args.model = "medium"

model = load_model(args)

result = transcribe(model, args)

print(result["text"])



