messages = ['LISA: "Hi Jim!"', 'JIM: "Hi Lisa!"', 'LISA: "How are you?"', 'JIM: "Good."']
sent_messages = []

def show_messages(messages):
    while messages:
        sending = messages.pop(0)
        print(sending)
        sent_messages.append(sending)

show_messages(messages[:],)

print(f"\n{sent_messages}\n{messages}")
