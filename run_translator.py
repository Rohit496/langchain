#!/usr/bin/env python3
"""
Script to run the Language Translator Streamlit app
"""

import subprocess
import sys
import os


def main():
    # Get the path to the Streamlit app
    app_path = os.path.join("Langchain", "Prompts", "8_chat_prompt_template_UI.py")

    # Check if the file exists
    if not os.path.exists(app_path):
        print(f"Error: File {app_path} not found!")
        sys.exit(1)

    print("🚀 Starting Language Translator...")
    print(f"📁 Running: {app_path}")
    print("🌐 The app will open in your default web browser")
    print("⚠️  Make sure you have set your OPENAI_API_KEY in your .env file")
    print("-" * 50)

    try:
        # Run the Streamlit app
        subprocess.run(
            [
                sys.executable,
                "-m",
                "streamlit",
                "run",
                app_path,
                "--server.headless",
                "false",
                "--server.runOnSave",
                "true",
                "--browser.gatherUsageStats",
                "false",
            ]
        )
    except KeyboardInterrupt:
        print("\n👋 App stopped by user")
    except Exception as e:
        print(f"❌ Error running the app: {e}")


if __name__ == "__main__":
    main()
