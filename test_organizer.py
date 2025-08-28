import os
import shutil
import subprocess
import sys
import pytest

CLI_SCRIPT = "organizer.py"

@pytest.fixture
def setup_test_directory(tmp_path):
    """A pytest fixture to create a temporary test directory with dummy files."""
    src_dir = tmp_path / "test_source"
    src_dir.mkdir()

    #Create dummy files
    (src_dir / "img1.jpg").touch()
    (src_dir / "doc1.pdf").touch()
    (src_dir / "arch1.zip").touch()

    yield str(src_dir)

    #cleanup after test is done
    #shutil.rmtree(src_dir)

def test_successful_organization(setup_test_directory):
    """Tests that the CLI tool successfully organizes known file types."""
    src_dir= setup_test_directory

    #1. Running CLI tool as a subprocess
    result = subprocess.run(
        [sys.executable, CLI_SCRIPT, src_dir],
        capture_output=True,
        text=True
    )

    #2.  Asserting that the script ran without errors
    assert result.returncode == 0
    assert "Error" not in result.stderr

    #3. Asserting that files were moved to correct dirs
    assert os.path.exists(os.path.join(src_dir, "images", "img1.jpg"))
    assert os.path.exists(os.path.join(src_dir, "documents", "doc1.pdf"))

    #4. Asserting that files were removed from src dir
    assert not os.path.exists(os.path.join(src_dir,  "img1.jpg"))
    assert not os.path.exists(os.path.join(src_dir, "doc1.pdf"))

    #5. Asserting that skipped file is still there
    assert os.path.exists(os.path.join(src_dir, "arch1.zip"))

def test_nonexistent_directory():
    """Tests that the CLI tool handles a non-existent source directory gracefully."""
    src_dir = "doesNotExist101"

    result= subprocess.run(
        [sys.executable, CLI_SCRIPT, src_dir],
        capture_output=True,
        text=True
    )

    assert "Error: Source directory" in result.stdout
    assert "not found" in result.stdout