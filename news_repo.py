import requests
import time


def pyNewsIndia():
    main_url = "https://newsapi.org/v2/everything?q=python&apiKey=YOUR_API_KEY"
    # main_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY"
    open_google_page = requests.get(main_url).json()

    articles = open_google_page["articles"]
    result = [a["title"] for a in articles]

    print(f"Total articles fetched: {len(result)}")  # see how many came back

    for i in range(min(10, len(result))):  # don't exceed what's available
        time.sleep(5)
        Headline = i + 1, result[i]
        print(Headline)


pyNewsIndia()