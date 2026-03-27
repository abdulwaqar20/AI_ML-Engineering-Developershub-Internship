import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load model (will work after training completes)
model_path = "news_classifier"

tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)

labels = ["World", "Sports", "Business", "Sci/Tech"]

st.title("📰 News Topic Classifier")

text = st.text_area("Enter News Headline")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter text")
    else:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits).item()
        st.success(f"Category: {labels[prediction]}")