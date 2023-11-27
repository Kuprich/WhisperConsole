
import json
import os
from pathlib import Path

FILE_NAME = "result"


def output_result(result:dict[str,str|list], args):
    
    out_result = result["text"] if args.output_text_only else result
    
    match args.output_format.lower():
        
        case "console":
            print("\n"+out_result)
        
        case "txt" | "json":
            return _write_to_file(out_result, args)
            
            
def _write_to_file(result, args):
    
    out_dir = Path.cwd() if args.output_dir == "." else args.output_dir
    out_file = os.path.join(out_dir, FILE_NAME+"."+args.output_format)
    
    os.remove(out_file) if os.path.exists(out_file) else None
    
    try:
        with open(out_file , "w", encoding="utf-8") as file:
            if args.output_format.lower()=="json":
                json.dump(result , file, ensure_ascii=False, indent=4, )
            else:
                file.write(result)
                
        return out_file
    
    except:
        print(f"An error occurred while writing file {out_file}. the result will be printed to the console:")
        print(result)