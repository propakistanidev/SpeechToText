import gradio as gr
import requests
import os
from dotenv import load_dotenv
import anthropic

# Load environment variables from .env file
load_dotenv()

# ============ CONFIG ============
HF_API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

# ============ FUNCTIONS ============
def transcribe_audio(audio_path: str) -> str:
    """Send audio to Hugging Face Whisper for transcription."""
    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
        "Content-Type": "audio/wav"
    }
    with open(audio_path, "rb") as f:
        response = requests.post(HF_API_URL, headers=headers, data=f)

    if response.status_code != 200:
        return f"[Error from Whisper]: {response.status_code} {response.text}"

    result = response.json()
    return result.get("text", "")

#####################################################################
############## ENABLE THIS FUNCTION TO USE CLAUDE ###################
# def refine_with_claude(text: str, user_prompt: str = None) -> str:
#     """Send transcription to Claude for refinement, with adjustable prompt."""
#     try:
#         # Default behavior if no custom prompt
#         if not user_prompt or user_prompt.strip() == "":
#             user_prompt = "Summarize this transcription in 3 concise sentences:"

#         message = client.messages.create(
#             model="claude-3-5-sonnet-20240620",
#             max_tokens=500,  # shorter response
#             messages=[
#                 {
#                     "role": "user",
#                     "content": f"{user_prompt}\n\n{text}"
#                 }
#             ]
#         )
#         return message.content[0].text
#     except Exception as e:
#         return f"[Error from Claude]: {e}"
######################################################################

def process_audio(audio, custom_prompt):
    if audio is None:
        return "", ""


    raw_text = transcribe_audio(audio)

    refined_text = "" #refine_with_claude(raw_text, custom_prompt) <= Enable this and fucntion above to use Claude

    return raw_text, refined_text

# ============ GRADIO UI ============
with gr.Blocks() as demo:
    gr.Markdown("##  Real-time Transcription with Whisper (HF) + Claude")

    with gr.Row():
        audio_input = gr.Audio(
            sources=["microphone", "upload"],
            type="filepath",
            streaming=False,
            label=" Record or Upload Audio"
        )

    with gr.Row():
        custom_prompt = gr.Textbox(
            label="Claude Prompt (optional)",
            placeholder="e.g., Summarize in 3 sentences, make it concise, extract key points..."
        )

    with gr.Row():
        raw_output = gr.Textbox(label="Whisper Transcription")
        refined_output = gr.Textbox(label="Claude Refined Output")

    # Bind function
    audio_input.change(
        process_audio,
        inputs=[audio_input, custom_prompt],
        outputs=[raw_output, refined_output]
    )

# Launch the Gradio app
demo.launch()