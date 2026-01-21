import os
import requests
import gradio as gr

HF_TOKEN = os.environ.get("hftoken")
MODEL = "HuggingFaceH4/zephyr-7b-beta"

def chat(message, history):
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                *[
                    {"role": "user", "content": h[0]} if i % 2 == 0
                    else {"role": "assistant", "content": h[1]}
                    for i, h in enumerate(history)
                ],
                {"role": "user", "content": message}
            ]
        }
    }

    r = requests.post(
        f"https://api.openai-inference.huggingface.co/models/{MODEL}",
        headers=headers,
        json=payload,
        timeout=60
    )

    return r.json()[0]["generated_text"]

gr.ChatInterface(
    chat,
    title="LLM Chatbot (GitHub + Hugging Face)",
    description="Python-only chatbot hosted on Hugging Face Spaces"
).launch()
