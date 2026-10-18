import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
  try:
   abs_working_directory = os.path.realpath(working_directory)
   
   target_file_path = os.path.realpath(os.path.join(abs_working_directory, file_path))
   
   validate_target_file_path = os.path.commonpath([abs_working_directory, target_file_path]) == abs_working_directory
   
   if not validate_target_file_path:
     return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
   
   if not os.path.isfile(target_file_path):
     return f'Error: "{file_path}" does not exist or is not a regular file'
   
   if not file_path.endswith('.py'):
     return f'Error: "{file_path}" is not a Python file'
   
   command = ["python", target_file_path]
   
   if args: 
     command.extend(args)
   
   command_completed = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=abs_working_directory,)
   
   output_string = []
   
   if command_completed.returncode != 0:
     output_string.append(f"Process exited with code {command_completed.returncode}")
   if not command_completed.stdout and not command_completed.stderr:
     output_string.append("No output produced")
   if command_completed.stdout:
     output_string.append(f'STDOUT: {command_completed.stdout}')
   if command_completed.stderr:
     output_string.append(f'\nSTDERR: {command_completed.stderr}')
   
   
   return "\n".join(output_string)
  except Exception as e:
    return f'Error: executing Python file: {e}'
  