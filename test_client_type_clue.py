import requests

def main():
    try:
       
        response = requests.get("http://127.0.0.1:5000/type_clue")

       
        if response.status_code == 200:
            data = response.json()
            print("Received response from microservice:")
            print(f"Clue 1 - First Type: {data['FirstType']}")
            print(f"Clue 2 - Second Type: {data['SecondType']}")
            print(f"Clue 3 - First Letter of Name: {data['FirstLetter']}")
            print(f"(For testing) Correct Answer: {data['CorrectAnswer']}")
        else:
            print(f"Error: Received status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    main()
