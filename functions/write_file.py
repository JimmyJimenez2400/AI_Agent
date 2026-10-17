import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
  
  try:
    abs_working_directory = os.path.realpath(working_directory)
      
    target_file_path = os.path.realpath(os.path.join(abs_working_directory, file_path))
    
    valid_target_file_path = os.path.commonpath([abs_working_directory, target_file_path]) == abs_working_directory
    
    if not valid_target_file_path:
      return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_file_path):
      return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        
    with open(target_file_path, "w") as f:
      f.write(content)
    
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
  except Exception as e:
    return f'Error: write_file: {e}'
  
  
    
  