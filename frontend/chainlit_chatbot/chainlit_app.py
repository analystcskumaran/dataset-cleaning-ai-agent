import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain import hub
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# LLM Setup
llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

# Memory for conversation
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    k=10
)

@cl.on_chat_start
async def start():
    """Called when a new chat session starts"""
    await cl.Message(
        content="""🧹 Welcome to Dataset Cleaning AI Agent!\n\nI can help you clean various types of datasets:\n• CSV/Excel files - missing values, duplicates, outliers\n• Images - corrupted files, quality issues, format standardization\n• Videos - frame quality, resolution, codec validation\n• JSON/XML - schema validation, formatting\n\nHow can I assist you today?"""
    ).send()

@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages"""
    msg = cl.Message(content="")
    await msg.send()
    
    try:
        # Process message through agent
        response = f"Processing your request: {message.content}"
        msg.content = response
    except Exception as e:
        msg.content = f"❌ Error: {str(e)}"
    
    await msg.update()

@cl.on_file_upload
async def on_file_upload(files: list[cl.File]):
    """Handle file uploads in chat"""
    for file in files:
        cl.user_session.set(f"uploaded_file_{file.name}", file)
        await cl.Message(
            content=f"✅ File uploaded: {file.name}\n\nAnalyzing file... Please wait."
        ).send()

@cl.on_stop
async def stop():
    """Called when chat session ends"""
    print("Chat session ended")
