# Command-Line File Organizer & Test Suite

This project contains a simple Python command-line tool (`organizer.py`) to organize files based on their extension, and a comprehensive automated test suite (`test_organizer.py`) built with `pytest`.

The primary purpose of this project is to demonstrate best practices in testing command-line applications, including file system interaction, process management, and validation of outputs.

## Features

- **CLI Tool:** A simple file organizer written in Python using `argparse`.
- **Automated Testing:** A robust test suite using `pytest` and the `subprocess` module.
- **Test Fixtures:** Uses `pytest` fixtures to create and tear down a clean test environment for each test case.
- **Success & Error Validation:** Includes tests for both successful file organization and graceful error handling.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-link>
    cd <your-repo-name>
    ```
2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## How to Run the Tool

```bash
python organizer.py /path/to/your/folder