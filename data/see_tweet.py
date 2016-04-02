import json
 
with open('stream_Rome.json', 'r') as f:
    line = f.readline() # read the first tweet
    tweet = json.loads(line) # load it as Python dict
    print(json.dumps(tweet, indent=4)) # print