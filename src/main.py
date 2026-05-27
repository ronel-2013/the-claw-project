from agent import ClawAgent

def main():
    backend = input("Choose backend ('ollama', 'deepseek', or 'gemini'): ").strip().lower()
    api_key = None
    model_name = None

    if backend == "deepseek":
        api_key = input("Enter your DeepSeek API key: ").strip()
        model_name = input("DeepSeek model name [deepseek-coder]: ").strip() or "deepseek-coder"
    elif backend == "ollama":
        model_name = input("Ollama model name [deepseek-coder:latest]: ").strip() or "deepseek-coder:latest"
    elif backend == "gemini":
        api_key = input("Enter your Gemini API key: ").strip()
        model_name = input("Gemini model name [gemini-pro]: ").strip() or "gemini-pro"
    else:
        print("Unknown backend.")
        return

    agent = ClawAgent(backend=backend, model_name=model_name, api_key=api_key)

    print(f"Chatting with The Claw Agent using {backend.title()} ({model_name})! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        reply = agent.chat(user_input)
        print("Claw:", reply)

if __name__ == "__main__":
    main()
