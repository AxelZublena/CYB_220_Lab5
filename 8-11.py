# 8.11
sent_messages = []

def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["My first message.", "This is a second message.", "The next message.", "Maybe the final message."]

send_messages(messages[:])

print(messages)
print(sent_messages)
