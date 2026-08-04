def two_stage_predict(cls, reg, applicant_df):

    prova = cls.predict_proba(applicant_df)
    preds = cls.predict(applicant_df)

    result = []
    i = 0
    approved_idx = 1

    approved = int(preds[i])
    approved_prob = float(prova[i, approved_idx])
    reg_pred = None

    if approved == 1:
        applicant_reg_df = applicant_df.copy()
        applicant_reg_df['loan_status'] = 'Approve'
        reg_pred = float(reg.predict(applicant_reg_df)[0])

    result.append({
        "Approved" : approved,
        "Approval_probability" : approved_prob,
        "Approval_amount" : reg_pred
    })  

    return result      
