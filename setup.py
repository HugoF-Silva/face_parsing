from setuptools import setup, find_packages

setup(
    name="face_parsing",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "torch>=1.7.0",
        "opencv-python",
        "numpy>=1.19.5",
        "opencv-python>=4.5.3.56",
        "resnet=0.1"
        "tensorflow"
    ],
    author="zllrunning",
    description="BiSeNet face parsing",
)