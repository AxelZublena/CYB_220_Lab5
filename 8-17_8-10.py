# 8.10 rewrite for 8.17
sent_messages = []

def send_messages(messages):
    """
    Simulate printing each message, until none are left.
    Move each message to sent_messages after printing.
    """
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["My first message.", "This is a second message.", "The next message.", "Maybe the final message."]

send_messages(messages)

print(messages)
print(sent_messages)
