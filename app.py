
import streamlit as st
import random
import time

st.set_page_config(page_title="Aviator Bet Predictor", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        color: #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 Aviator Predictor (Educational)")
st.write("এই অ্যাপটি পূর্ববর্তী বেট বিশ্লেষণ করে সম্ভাব্য পরবর্তী বেট অনুমান করে।")

user_input = st.text_input("শেষ ১০টি বেট দিন (কমা দিয়ে আলাদা করুন)", "1.2, 1.5, 1.8, 2.0, 1.1, 1.4, 2.3, 1.9, 1.6, 2.1")

# ফাংশন: ভবিষ্যদ্বাণী তৈরি
@st.cache_data
def predict_next_bets(previous_bets, count=5):
    avg = sum(previous_bets[-5:]) / min(5, len(previous_bets))
    predictions = []
    for _ in range(count):
        variation = random.uniform(-0.3, 0.3)
        next_value = round(max(1.0, avg + variation), 2)
        predictions.append(next_value)
        previous_bets.append(next_value)
    return predictions

# ইনপুট যাচাই ও প্রেডিকশন
try:
    bets = [float(x.strip()) for x in user_input.split(",") if x.strip()]
    if len(bets) < 3:
        st.warning("অনুগ্রহ করে কমপক্ষে ৩টি ইনপুট দিন।")
    else:
        if st.button("Predict করুন"):
            with st.spinner("ভবিষ্যদ্বাণী করা হচ্ছে..."):
                time.sleep(1.5)
                predicted = predict_next_bets(bets.copy())
            st.success("পরবর্তী ৫টি সম্ভাব্য বেট:")
            st.write(predicted)
except:
    st.error("দয়া করে ইনপুট সঠিকভাবে দিন। উদাহরণ: 1.2, 1.5, 2.0")

st.markdown("""
---
**দ্রষ্টব্য:** এই অ্যাপটি শুধুমাত্র শিক্ষামূলক উদ্দেশ্যে তৈরি। প্রকৃত Aviator গেম পূর্বানুমানযোগ্য নয়।
""")
