import json
import os
from pathlib import Path
import shutil


class ResultSaver:
    
    _segment_num = 0
    segment_dir_name = "segments"
    text_file_basename = "text.json"
    
    def segment_filepath(self):
        return os.path.join(self.segments_dir,
                            "segment_"+ str(self._segment_num) + ".json")
    
    def text_filepath(self):
        return os.path.join(self.output_dir,
                            self.text_file_basename)

        
    def __init__(self, audio_file):
        self.output_dir = os.path.splitext(os.path.basename(Path(audio_file)))[0]
        self.segments_dir = os.path.join(self.output_dir, self.segment_dir_name)
    
    def prepare_output(self):
        
        if Path.exists(Path(self.output_dir)):
            self._delete_everythong_in_folder(self.output_dir)
        
        os.mkdir(self.output_dir)
        os.mkdir(self.segments_dir)
        
    def _delete_everythong_in_folder(self, folder_path):
        shutil.rmtree(folder_path)    
    
        
    def segments_to_file(self, segment):
        with open(self.segment_filepath(), "w", encoding="utf-8") as json_file:
            json_file.write(json.dumps(segment, ensure_ascii=False, indent=4))
        self._segment_num+=1
        
    def text_to_file(self, text):
        with open(self.text_filepath(), "w", encoding="utf-8") as json_file:
            json_file.write(json.dumps(dict(text=text), ensure_ascii=False, indent=4))
        