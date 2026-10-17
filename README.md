# AI Agent (Boot.dev Project)

[View on GitHub](https://github.com/JimmyJimenez2400/AI_Agent)

A simple command-line AI agent built in Python, powered by Google's Gemini API. 
The agent can read files, write files, list directory contents, and execute 
Python files within a restricted working directory.

> **Warning:** This is an educational project. It does not include the 
> security hardening required for production use. Do not expose this to 
> untrusted input or run it outside of a safe, isolated environment.

## Features

- **get_files_info** — Lists files and subdirectories within the working directory.
- **get_file_content** — Reads and returns the content of a specified file.
- **write_file** — Writes content to a specified file.
- **run_python_file** — Executes a Python file with optional arguments, 
  restricted to the working directory, with a 30-second timeout.

All file operations are sandboxed to a `working_directory` to prevent access 
outside the intended scope.

## Known Limitations

- Code execution is restricted to a single working directory, but the LLM 
  can still run arbitrary Python code within that directory.
- There is no sandboxing beyond directory restriction and a 30-second timeout.
- This project should only be used for learning purposes, not in production 
  or with untrusted input.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/JimmyJimenez2400/AI_Agent.git
   cd AI_Agent
   ```

2. Install dependencies with [uv](https://docs.astral.sh/uv/):
   ```bash
   uv sync
   ```

3. Create a `.env` file in the project root with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the agent with a prompt:
```bash
uv run main.py "your prompt here"
```

Add the `--verbose` flag to see detailed function call information:
```bash
uv run main.py "your prompt here" --verbose
```

## Running Tests

Each function has a corresponding test file at the project root:
```bash
uv run test_get_files_info.py
uv run test_get_file_content.py
uv run test_write_file.py
uv run test_run_python_file.py
```

## Project Structure

```
.
├── calculator/        # Sample project used to test agent capabilities
├── functions/         # Agent function implementations
├── config.py          # Configuration constants (e.g., working directory, limits)
├── main.py            # Entry point for running the agent
└── test_*.py          # Test suites for each function
```

## License

MIT