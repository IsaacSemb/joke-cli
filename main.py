import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke = response.json()
    print(f"{joke['setup']}\n{joke['punchline']}")

if __name__ == "__main__":
    get_joke()
