## whisper_console

Standalone executables of [Open AI / Whisper](https://github.com/openai/whisper)

![whisper_console](https://github.com/Kuprich/WhisperConsole/assets/23151696/9b56b336-f571-4066-a680-9a19344dc5ea)

if you **don't want to install Python**, use the following standalone executable for your purposes


For [whisper_console.exe](https://github.com/Kuprich/WhisperConsole/releases/tag/whisper) required [FFMpeg](https://ffmpeg.org/). 

>   ``📝``If you run the application without ffmpeg preinstalled , the execution will be interrupted with the following error: *"FFmpeg is required! Please, install it to continue. More info: https://ffmpeg.org/"*


### Requirements

+ FFMpeg - [more details](https://ffmpeg.org/)

+ Microsoft Visual C++ Redistributable latest - [more details](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

+ NET 6.0 runtime - [more deatils](https://dotnet.microsoft.com/en-us/download/dotnet/6.0)

### Usage Examples

 <ol>
 <li> Use --help or -h command to show all arguments (Perharps, some arguments don't working correctly, I'm not sure):
 
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

### More Info

Please, for more info visit the General project page - [Whisper](https://github.com/openai/whisper)

Visit similar project page - [whisper-standalone-win](https://github.com/Purfview/whisper-standalone-win)





 

