from setuptools import setup, find_packages

setup(
    name="pysolarmanproxy",
    version="1.0.0",
    description="minimal proxy server which exposes a solarman device by rtu-over-tcp modbus",
    packages=find_packages(),
    install_requires=[
        "pysolarmanv5==3.0.5",
        "click==8.1.8"
    ],
    entry_points={"console_scripts": ["pysolarmanproxy = pysolarmanproxy.server:run"]}
)