from agent import ClawAgent

def main():
    backend = input("Choose backend ('ollama' or 'deepseek'): ").strip().lower()
    api_key = None
    if backend == "deepseek":
        api_key = input("Enter your DeepSeek API key: ").strip()
    agent = ClawAgent(backend=backend, api_key=api_key)

    print(f"Chatting with The Claw Agent using {backend.title()}! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        reply = agent.chat(user_input)
        print("Claw:", reply)

if __name__ == "__main__":
    main()
