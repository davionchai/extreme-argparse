import sys
import warnings
from pathlib import Path
from setuptools import setup


package_version: str = "0.0.1"
min_required_python_version: str = "3.9"
max_supported_python_version: str = "3.12"

package_name: str = "extreme-argparse"
package_description: str = "next level argparse designed for python apps running in kubernetes"

# check python compatible version
detected_python_version: tuple = sys.version_info
if detected_python_version < (3, 9):
    raise OSError(
        f"Error: [{package_name}] version [{package_version}] that you are trying to install does not meet"
        f" the minimum required python runtime version [{min_required_python_version}]"
        f" that you are using ([{detected_python_version}])."
    )
elif detected_python_version >= (3, 12):
    warnings.warn(
        f"Warning: Your detected python runtime version [{detected_python_version}] is detected to"
        f" be greater our maximum supported python version [{max_supported_python_version}],"
        " please be warned that you might face unknown issue.",
        RuntimeWarning,
    )

try:
    from setuptools import find_namespace_packages
except ImportError:
    raise ImportError(
        f"Error: [{package_name}] version [{package_version}] requires setuptools with mininum v40.1.0.\n"
        f"Please upgrade setuptools with `pip install --upgarde setuptools` and try again."
    )

this_directory: Path = Path(__file__).resolve().parent
with open(Path(f"{this_directory}/README.md")) as readme:
    package_long_description: str = readme.read()

setup(
    name=package_name,
    version=package_version,
    description=package_description,
    long_description=package_long_description,
    long_description_content_type="text/markdown",
    author="nearjer poor engineers",
    author_email="dchai@nearjer.com",
    url="https://github.com/NearJer/extreme-argparse",
    packages=find_namespace_packages(include=["eargparse", "eargparse.*"]),
    include_package_data=True,
    python_requires=f">={min_required_python_version}",
    install_requires=[],
    extras_require={
        "dev": [
            "black~=24.4.0",  # annually update unless security issue
            "flake8",
            "mypy",
            "pre-commit",
            "pytest",
        ]
    },
    zip_safe=False,
    classifiers=[
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
