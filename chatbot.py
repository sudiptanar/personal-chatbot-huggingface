import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


exit_words = ["exit", "close", "quit", "bye", "leave me alone",
              "goodbye", "please go", "stop", "good bye", "leave now"]


if __name__ == "__main__":
    past_user_inputs = []
    generated_responses = []

    while True:
        input_response = input("Your Response : ").lower()
        if input_response in exit_words or input_response=='':
            break

        output = query({
            "inputs": {
                "past_user_inputs": past_user_inputs,
                "generated_responses": generated_responses,
                "text": input_response
            },
        })
        # Output
        print("Chatbot Response : " + output.get('generated_text'))

        # Store data
        past_user_inputs.append(input_response)
        generated_responses.append(output.get('generated_text'))

    print("Chatbot Response : Ok. Good Bye. Take care :)")
