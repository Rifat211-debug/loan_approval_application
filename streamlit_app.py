import streamlit as st
import yaml

from app.loader import load_models
from app.utils import build_applicant_from_dict
from app.predict import two_stage_predict

with open("config.yaml") as f:
    config = yaml.safe_load(f)

st.set_page_config(page_title = "Loan Approval", layout = "centered")

st.title("Loan Approval - Two Stage Predictor")

cls, reg = load_models(config)

st.sidebar.header("Model Info")
try:
    st.sidebar.write("Classifier Expects : ", list(cls.feature_names_in_))
except Exception:
    st.sidebar.write("Classofoer feature names unavailable!")

st.header("Applicant Details")

default = config['ui']['default_inputs']

cols = st.columns(2)
with cols[0]:
    no_of_dependents = st.number_input("Number of Dependents", value = int(default['no_of_dependents']))
    education = st.selectbox("Education", options = ["Graduate", "Not Graduate"], index = 0 if default['education'] == "Graduate" else 1)
    self_employed = st.selectbox("Self Employed", options = ["Yes", "No"], index = 0 if default["self_employed"] == "Yes" else 1)
    income_annum = st.number_input("Annual Income", value = float(default["income_annum"]))
    loan_amount = st.number_input("Loand Amount Requested", value = float(default["loan_amount"]))
with cols[1]:
    loan_term = st.number_input("Loan Term (years)", value = int(default["loan_term"]))
    cibil_score = st.number_input("Cibil Score", value = int(default["cibil_score"]))
    residential_assets_value = st.number_input("Residential Assests", value = float(default['residential_assets_value']))
    commercial_assets_value = st.number_input("Commercial Assets", value = float(default["commercial_assets_value"]))
    luxury_assets_value = st.number_input("Luxury Assets", value = float(default['luxury_assets_value']))
    bank_asset_value = st.number_input("Bank Asset", value = float(default['bank_asset_value']))

applicant = {
    'no_of_dependents' : no_of_dependents,
    'education' : education,
    'self_employed' : self_employed,
    'income_annum' : income_annum,
    'loan_amount' : loan_amount,
    'loan_term' : loan_term,
    'cibil_score' : cibil_score,
    'residential_assets_value': residential_assets_value,
    'commercial_assets_value' : commercial_assets_value,
    'luxury_assets_value' : luxury_assets_value, 
    'bank_asset_value' : bank_asset_value
}

if st.button("Predict"):
    try:
        expected_cols = list(cls.feature_names_in_)
        applicant_df = build_applicant_from_dict(applicant, expected_cols)
        results = two_stage_predict(cls, reg, applicant_df)
        res = results[0] #final dictionary

        st.write("Approval Probability : {:2%}".format(res['Approval_probability']))
        if res['Approved'] == 1:
            st.success("✅ Approved")
            st.write(f"Predicted loan amount (or interest) : {res['Approval_amount']:.2f}")
        else:
            st.error("❌ Rejected")
    except Exception as e:
        st.error(f"Prediction failed : {e}")            
