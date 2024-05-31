import gradio as gr
from gpt4all import GPT4All

# Initialize the GPT4All model
model = GPT4All('gpt4all-falcon-q4_0.gguf')

def assist_with_homework(prompt):
    # Use the GPT4ALL model to assist with homework
    response = model.generate(prompt=prompt, max_tokens=300)
    return response

# Define the Gradio interface
iface = gr.Interface(fn=assist_with_homework, inputs="text", outputs="text", title="Student Homework Helper")

# Launch the interface
iface.launch()

