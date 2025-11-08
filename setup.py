from setuptools import setup, find_packages

setup(
    name="batterynotifier",
    version="0.0.1",
    description="Battery notifier utility that notifies when below 25 and 20%",
    author="Keandre Rafael",
    author_email="keandre.imposter@gmail.com",
    url="https://github.com/keandrake-24/battery-notifier",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    license="MIT",
    python_requires=">=3.8",
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "battery-notifier=batterynotifier.batterynotifier:main",
        ]
    }
)