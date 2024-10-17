import requests
import json
def main():
    date = "2024-06-01"
    subreddit = "Republican"
    search_term = "president"
    posts_comments = "comments"
    body_or_query = "body" if posts_comments == "comments" else "query"
    url = f"https://arctic-shift.photon-reddit.com/api/{posts_comments}/search?sort=asc&after={date}&subreddit={subreddit}&{body_or_query}={search_term}&limit=100"
    try:
        response = requests.get(url)
        response.raise_for_status()
        responsedata = response.json()["data"]
        with open(f'./data/{subreddit}_{posts_comments}_2024.jsonl', "w") as f:
            for comment in responsedata:
                f.write(json.dumps(comment) + '\n')
            f.close()
    except requests.exceptions.RequestException as errex:
        print(f"Invalid arguments for API query. Try again.")

if __name__ == "__main__":
    main()