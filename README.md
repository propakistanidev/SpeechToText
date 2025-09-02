# Real-time Transcription with Whisper (HF) + Claude

This project provides a **speech-to-text pipeline** using [Hugging Face Whisper](https://huggingface.co/models?search=whisper) for transcription and optionally [Claude](https://www.anthropic.com/claude) for refinement/summarization.  
It also comes with a simple **Gradio UI** for recording/uploading audio and getting real-time transcripts.  

---

##  Features
- Record or upload audio and transcribe it using **Whisper Large v3 Turbo** (Hugging Face Inference API).  
- (Optional) Refine or summarize transcriptions using **Claude 3.5 Sonnet**.  
-  Easy-to-use **Gradio web interface**.  
- Supports **custom prompts** for Claude refinement (e.g., summarize, extract key points, rewrite).  

---

## Installation

Clone this repo:

```bash
git clone https://github.com/your-username/whisper-claude-transcriber.git
cd whisper-claude-transcriber
```

``` bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### Requirements
```bash
pip install -r requirements.txt
```

### Environment Variables

Create a .env file in the root directory and add the following keys:
```bash
HF_API_TOKEN=your_huggingface_api_token
CLAUDE_API_KEY=your_claude_api_key   # Only required if using Claude
```

### Usage

Run the app:
``` bash
python3 main.py
```

###  Project Structure
``` bash
.
├── main.py            # Main application file
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## How Claude Integration Works

By default, Claude is disabled.
To enable it:
	1.	Uncomment the refine_with_claude function in main.py.
	2.	Uncomment the line in process_audio where it calls refine_with_claude.
	3.	Ensure your .env contains CLAUDE_API_KEY.

Example:
```bash
refined_text = refine_with_claude(raw_text, custom_prompt)
```

### Example Prompts for Claude
	•	Summarize in 3 concise sentences
	•	Extract key decisions and action items
	•	Rewrite this as a professional email

# License

This project is licensed under the MIT License.
