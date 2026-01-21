import gradio as gr

def chat(msg, history):
    return "Hello! Your Space is connected to GitHub."

gr.ChatInterface(chat).launch()
