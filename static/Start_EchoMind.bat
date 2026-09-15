@echo off
cd /d "C:\Users\HP\OneDrive\Desktop\ecomind\ecomind"
call venv\Scripts\activate
python -m uvicorn main:app --host 127.0.0.1 --port 8000
pause