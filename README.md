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

## To install/freeze additional libraries using UV :
```bash
uv pip install -r requirements.txt
uv pip freeze > requirements.txt
```

## git Instructions :
```bash
git init
git add .
git commit -m "message"
git remote add origin http://url_of_your_git_repo.git
git pull origin main --allow-unrelated-histories
git push -u origin main
```

## Note :
- Make sure the version used to create the model is same as your local environment where you are testing the main.py and streamlit app.
- We are using python 3.13.5 for our virtual environment.

