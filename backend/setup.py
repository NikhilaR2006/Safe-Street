from setuptools import setup, find_packages

setup(
    name="safe_street_backend",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask==3.1.0",
        "flask-cors==5.0.1",
        "numpy<1.23.0,>=1.22.0",
        "opencv-python==4.11.0.86",
        "joblib==1.4.2",
        "pandas==2.2.2",
        "matplotlib==3.9.1",
        "gunicorn==22.0.0"
    ],
    entry_points={
        "console_scripts": [
            "safe_street_backend=app:app",
        ],
    },
)
