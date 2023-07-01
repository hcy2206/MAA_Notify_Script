if not exist venv (
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
)

call venv\Scripts\activate.bat

python main.py