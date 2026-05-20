import wikipedia


def mywiki(topic):
    info = wikipedia.summary(topic, sentences=2)
    url = wikipedia.page(topic).url
    print(
        f"Here's the information about {topic} : {info}"
        f"\n\nRead more about {topic} : \n{url}"
    )


user_input = input("Which topic's information do you want? : ")

if __name__ == "__main__":
    mywiki(user_input)
