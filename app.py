import streamlit as st

st.set_page_config(page_title="Stroke Risk Calculator", page_icon="🧠", layout="centered")

st.title("🧠 Interactive Stroke Risk Calculator")

st.markdown(
    """
    Welcome! This short questionnaire will help you estimate your **relative risk of stroke** based on
    several well-known lifestyle and health factors. It is **not** a medical diagnosis—always consult a
    qualified professional about your personal health.
    """
)

st.markdown("---")

# 1. Age
age = st.slider("1️⃣  How old are you?", 18, 100, 30)
if age < 55:
    age_score = 0
elif age < 65:
    age_score = 1
else:
    age_score = 2

# 2. Hypertension
htn = st.radio(
    "2️⃣  Have you **ever** been told you have high blood pressure (hypertension)?",
    ["No / Unknown / Normal", "Yes – Diagnosed"],
)
htn_score = 0 if htn == "No / Unknown / Normal" else 2

# 3. Smoking
smoke = st.radio(
    "3️⃣  What best describes your smoking status?",
    ["Never smoked ❌", "Stopped smoking > 5 years ago ✅", "Currently smoking", "Stopped within last 5 years"],
    index=0,
)
smoke_score = 0 if smoke in ("Never smoked ❌", "Stopped smoking > 5 years ago ✅") else 2

# 4. Diabetes
dm = st.radio("4️⃣  Have you **ever** been diagnosed with diabetes?", ["No", "Yes"], index=0)
dm_score = 0 if dm == "No" else 2

# 5. Family History of Stroke
fh = st.radio("5️⃣  Do you have a **family history** of stroke (parent or sibling)?", ["No", "Yes"], index=0)
fh_score = 0 if fh == "No" else 1

# 6. Physical Activity
pa = st.radio(
    "6️⃣  How would you describe your weekly physical activity?",
    ["Active – ≥30 min per day, ≥5 days/week", "Sedentary"],
    index=0,
)
pa_score = 0 if pa.startswith("Active") else 1

# 7. Obesity (visual estimate)
ob = st.radio("7️⃣  Do you consider yourself **visually** obese?", ["No", "Yes"], index=0)
ob_score = 0 if ob == "No" else 1

# Utility mapping: numeric → qualitative level
risk_map = {0: "Low", 1: "Moderate", 2: "High"}

# Calculate total when button pressed
if st.button("✨ Calculate My Risk"):
    total_score = age_score + htn_score + smoke_score + dm_score + fh_score + pa_score + ob_score

    if total_score <= 2:
        risk_level, color, emoji = "Low Risk", "#4caf50", "😊"
    elif total_score <= 5:
        risk_level, color, emoji = "Moderate Risk", "#ff9800", "😐"
    else:
        risk_level, color, emoji = "High Risk", "#f44336", "😟"

    st.markdown("---")
    st.subheader("Your Results")

    st.markdown(
        f"""
        <div style='text-align:center;'>
            <span style='font-size:60px;'>{emoji}</span><br>
            <span style='font-size:32px; font-weight:bold; color:{color};'>{risk_level}</span><br>
            <span style='font-size:20px;'>Total Score: {total_score}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown(
        """
        **What next?**

        - Even a **low score** doesn’t guarantee you’re risk-free—maintain healthy habits.  
        - If you scored **moderate or high**, consider consulting a healthcare professional for personalized advice.  
        - Everyone can benefit from regular physical activity, balanced nutrition, and routine health check-ups.
        """
    )

st.markdown("---")