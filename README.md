# Loan Approval Project - Two Stage ML Application

## Overview :
Two stage model :
1. Classify applicant as Approved / Rejected.
2. If Approved, predict the loan amount.

## Quickstack (local) 
1. Create venv :
- uv venv
- uv pip install -r requirements.txt
2. Put your trained `stage_1...pkl` and `stage_2...pkl` files in `models\`.
3. Run locally :
- Interface/UI : `uv run streamlit run streamlit_app.py`
- CLI : `uv run python main.py`

## Config
- See `config.yaml` for runtime parameters (models paths)

## Note :
- Make sure the version used to create the model is same as your local environment where you are testing the main.py and streamlit app.
- We are using python 13.5 for our virtual environment.