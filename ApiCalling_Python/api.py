#learnt how request library is used and got good grip on API Handling in python


import requests

def Person_Data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data: # to check in recived json format which has success key returned and data: contain user data. if any error then error will be thrown and printed
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        city = user_data["location"]["city"]
        return user_name, city, country
    else:
        raise Exception("failure in getting API")



def main():
    try:
        name, city, country = Person_Data()
        print(f"the username is: {name}, city: {city}, country: {country}")

    except Exception as e:
        print(e)  

if __name__ == "__main__":
    main()