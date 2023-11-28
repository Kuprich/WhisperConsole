## whisper_console

Standalone executables of [Open AI / Whisper](https://github.com/openai/whisper)

![whisper_console](https://github.com/Kuprich/WhisperConsole/assets/23151696/9b56b336-f571-4066-a680-9a19344dc5ea)

if you **don't want to install Python**, use the following standalone executable for your purposes

There are two standalone applications:

1. whisper_console.exe without ffmpeg. (It needs to be installed manually)

    >   ``📝``If you run the application without ffmpeg preinstalled , the execution will be interrupted with the following error: *"FFmpeg is required! Please, install it to continue. More info: https://ffmpeg.org/"*

2. whisper_console.exe which contains ffmpeg

### Requirements

+ Microsoft Visual C++ Redistributable latest supported - [more details]((https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170))

+ NET 6.0 runtime - [more deatils](https://dotnet.microsoft.com/en-us/download/dotnet/6.0)

### Usage Examples

 <ol>
 <li> Show help to show all arguments (Perharps, some arguments don't working correctly, I'm not sure):
 
 ```.\whisper_console.exe --help```
 </li>
 <li> Recognizes audio using *"base"* whisper model by default:
 
 ```.\whisper_console.exe audio.mp3```
 </li>

  <li> Set whisper model:
 
 ```.\whisper_console.exe audio.mp3 --model large-v3```
 </li>

 <li> Set whisper model and show all transcribe info:
 
 ```.\whisper_console.exe audio.mp3 --model large-v3 --verbose true```
 </li>

  <li> Set whisper model(--model), show all transcribe info(--verbose), set language(--language), set output file format(output_format) and set output_text_only option, which saves all recognition info to output file (result.json):
 
 ```.\whisper_console.exe audio.mp3 --model large-v3 --verbose true --language en --output_format json --output_text_only false```
 </li>
 </ol>



 

