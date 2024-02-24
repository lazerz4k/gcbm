from openai import OpenAI

client = OpenAI(
    api_key="YOUR OPENAI API KEY HERE"
)

conversation1 = [{"role": "system", "content": "AI PROMPT 1"}]
conversation2 = [{"role": "system", "content": "AI PROMPT 2"}]

def fetch_reply_1(input: str):
    conversation1.append({"role": "user", "content": input})
    reply_stream = client.chat.completions.create(
        messages=conversation1,
        model="gpt-4",
        stream=True
    )
    global reply1
    reply1 = ""
    print(f"\n\nA.I 1:\n")
    for i in reply_stream:
        print(i.choices[0].delta.content or "", end="")
        reply1+=(i.choices[0].delta.content or "")
    conversation1.append({"role": "assistant", "content":  reply1})
    wait_for_user()
    fetch_reply_2(reply1)

def fetch_reply_2(input: str):
    conversation2.append({"role": "user", "content": input})
    reply_stream = client.chat.completions.create(
        messages=conversation2,
        model="gpt-4",
        stream=True
    )
    global reply2
    reply2 = ""
    print(f"\n\nA.I 2:\n")
    for i in reply_stream:
        print(i.choices[0].delta.content or "", end="")
        reply2+=(i.choices[0].delta.content or "")
    conversation2.append({"role": "assistant", "content":  reply2})
    wait_for_user()
    fetch_reply_1(reply2)

def wait_for_user():
    input("\nPress enter to continue...")

start = False
while start == False:
    request = input(f"\n\nStart the conversation: ")
    fetch_reply_1(request)
    start = True
