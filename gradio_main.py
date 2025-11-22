import gradio as gr

# Define a function to simulate a chatbot response
def chatbot_response(user_input):
    # For simplicity, echo the user input with a prefix
    return f"Chatbot: I heard you say '{user_input}'"

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## ChatGPT-like Interface")
    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(label="Your Message", placeholder="Type your message here...")
            submit_button = gr.Button("Send")
        with gr.Column():
            chatbot_output = gr.Textbox(label="Chatbot Response", interactive=False)
    
    submit_button.click(chatbot_response, inputs=user_input, outputs=chatbot_output)

# Launch the app
if __name__ == "__main__":
    demo.launch()