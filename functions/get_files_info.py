import os

schema_get_files_info = {
      "type": "function",
      "function": {
        "name": "get_files_info",
        "description": "List files in a specified directory relative to the working directory, providing the file size and directory status",
        "parameters": {
          "type": "object",
          "properties": {
            "directory": {
              "type": "string",
              "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
            },
          },
        },
      },
      
    }

def get_files_info(working_directory: str, directory: str=".") -> str:
  
  try:
    
    
    
    abs_working_directory = os.path.abspath(working_directory)
    
    
    target_dir = os.path.normpath(os.path.join(abs_working_directory, directory))
    
    valid_target_dir = os.path.commonpath([abs_working_directory, target_dir]) == abs_working_directory
    
    if not valid_target_dir:
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
      return f'Error: "{directory}" is not a directory'
    
    
    target_directory_list = os.listdir(target_dir)
    
    string_list = []
    for item in target_directory_list:
      abs_path_item = os.path.join(target_dir, item)
      file_name = item
      file_size = os.path.getsize(abs_path_item)
      is_dir = os.path.isdir(abs_path_item)
      
      finished_string = f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}"
      string_list.append(finished_string)
    
    
    return "\n".join(string_list)
    
  except Exception as e:
    return f"Error -> listing files:  {e}"

    
  
  
  
  