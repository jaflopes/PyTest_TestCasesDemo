import pytest
import sys
import pathlib


cwd = pathlib.Path.cwd()
sys.path.append(str(cwd.parent.parent))

pytest.main()
