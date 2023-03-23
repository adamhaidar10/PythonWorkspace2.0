import requests
import shutil # shell utilities
import random
# get 10 pics of kittens
for i in range(10):
    # get random size of pics
    x = random.randint(300, 800)
    y = random.randint(300, 800)
    print(x, y)



# call the service with the random size
    url = f"http://placekitten.com/{x}/{y}"
    res = requests.get(url, stream=True)
    print(res.status_code)
# save the file in memory to disk using the shutil library
    outfile = open(f"kitten{i}.png", "wb")
    shutil.copyfileobj(res.raw, outfile)
    outfile.close()

