import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
  try:
    
    abs_working_directory = os.path.realpath(working_directory)
      
    target_file = os.path.realpath(os.path.join(abs_working_directory, file_path))
    
    valid_target_file_path = (
        os.path.commonpath([abs_working_directory, target_file]) == abs_working_directory
        )
    
    if not valid_target_file_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file):
      return f'Error: File not found or is not a regular file: "{file_path}"'
    
    
    contents = ""
    
    with open(target_file, "r") as f:
      contents = f.read(MAX_CHARS)
      
      if f.read(1):
          contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return contents
  except Exception as e:
    return f'Error: get_files_content: {e}'
  
  
  
  
 