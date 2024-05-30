cd MAA_Notify_Script
if exist MAA_Notify_Script (
    cd MAA_Notify_Script
) else (
    if exist MAA_Notify_Script-master (
        cd MAA_Notify_Script-master
    )
)

if not exist venv (
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
)

call venv\Scripts\activate.bat

python main.py