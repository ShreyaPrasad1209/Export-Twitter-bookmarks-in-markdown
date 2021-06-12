import json
import glob

all_bookmarks = []
md_file = open("bookmarks.md", "w+")        # saving in markdown file, if no file exists  using '+' creates one

files = [file for file in glob.glob("bookmark.json")]     # using glob to read all files from the folder
for file_name in files:
    print(file_name)
    with open(file_name) as bk:
	    data = json.load(bk)        # reads json data
    all_bookmarks.append(data)


# Function to get profile pic if you need
def getAuthorProfilePic(id):
	return response["users"][id]["profile_image_url_https"]

# Function to get username
def getUserName(id):
	return response["users"][id]["screen_name"]

# Function to construct bookmarked tweet url
def constructUrl(tweet_id, username):
	return "https://twitter.com/" + username + "/status/" + tweet_id

# Function to format the text to write in file
def formatText(text):
	text = text.replace("\n-", " ")
	text = text.replace("\n", " ")
	text = text[:100] + "..."
	return text

# Run a loop through all_bookmarks
for data in all_bookmarks:
    response = data["data"]
    print(response)
    for tweet_id in response["entries"]:
        tweet = response["entries"][tweet_id]
        text = tweet["full_text"]
        text = formatText(text)
        url = constructUrl(tweet_id, getUserName(tweet["user_id_str"]))
        bookmarked_tweet = "\n- " + text + "\n" + "\t - " + url
        md_file.write(bookmarked_tweet)
