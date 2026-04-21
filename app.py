from agent import load_knowledge, retrieve_answer
from tools import mock_lead_capture
from memory import ConversationState

state = ConversationState()
kb = load_knowledge()

def classify_intent(user_input):
    user_input = user_input.lower()

    # Greeting
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    # Pricing
    elif any(word in user_input for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"

    # Lead intent
    elif any(word in user_input for word in ["buy", "subscribe", "start", "try", "want"]):
        return "lead"

    return "unknown"

def chatbot(user_input):
    global state

    if state.intent != "lead":
        state.intent = classify_intent(user_input)

    if state.intent == "greeting":
        return "Hi! 👋 Welcome to AutoStream. Ask me about pricing or features."

    elif state.intent == "pricing":
        return retrieve_answer(user_input, kb)

    elif state.intent == "lead":

        if not state.name:
            state.name = user_input
            return "Great! What's your email?"

        elif not state.email:
            state.email = user_input

            if "@" not in state.email:
                state.email = None
                return "Please enter a valid email."

            return "Which platform do you create content on?"

        elif not state.platform:
            state.platform = user_input

            result = mock_lead_capture(
                state.name,
                state.email,
                state.platform
            )

            return result

    return "Can you rephrase that?"

if __name__ == "__main__":
    print("AutoStream AI Agent 🤖")

    while True:
        user = input("You: ")

        if user.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye 👋")
            break

        response = chatbot(user)
        print("Bot:", response)
        