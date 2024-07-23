import Openai
Openai.api_key= 'YOUR_API_KEY'
messages=[{"role": "system","contect":"you are intelligent assistant"}]

while True:
    message =input("user:")
    if messages:
        messages.append({"role":"user","content":messages},)
        chat=Openai.chatcompletion.create(
          model="gpt-3.5-turbo",
          messages=messages
      )

reply=chat.choices[0].message.content

print(f"chatgpt:{reply}")
messages.append({"role":"assistent","content":reply})
 
