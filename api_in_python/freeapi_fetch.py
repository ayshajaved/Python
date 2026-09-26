import requests

# def jokes_fetch(url):
#     url = url
#     response = requests.get(url) #response is collected
#     print(response)             #response is printed that is 200 (sucessfull)
#     print("------------------------")
#     data = response.json()     #json data is printed
#     print(data)
#     print("----------------")
#     if response.status_code == 200 and "data" in data:   #data is in data in key so condition is true
#         print(data["data"]["content"])    #in data key theres a key content that is printing the joke

# jokes_fetch("https://api.freeapi.app/api/v1/public/randomjokes/joke/random")        #api is present for the practise at api.freeapi.app
# print("")
# print("")
# jokes_fetch("https://api.freeapi.app/api/v1/public/quotes/quote/random")     #random quote


# url ="https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human" #this contains a huge data in json so we can use json formatter online to easily view andfetch
# response = requests.get(url)
# data = response.json()
# if response.status_code == 200 and "data" in data :              #response.content and response.text is also used
#     for i in range(len(data)):
#         print("Quote is  :-",data["data"]["data"][i]["content"])
#         print('')

#saving the quotes in a file
# with open("quotes.txt", "w") as f:
#     def jokes_fetch(url):
#         url = url
#         response = requests.get(url) #response is collected
#         data = response.json()     #json data is printed
#         if response.status_code == 200 and "data" in data:   #data is in data in key so condition is true
#             f.write((data["data"]["content"]))    #in data key theres a key con
#             f.write("\n")
#     for i in range(10):
#         jokes_fetch("https://api.freeapi.app/api/v1/public/quotes/quote/random")