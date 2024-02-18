import requests
import pandas as pd

url = "https://api.usaspending.gov"
TOPTIER_AGENCY_CODE = '020'
endpoint = "/api/v2/agency/{TOPTIER_AGENCY_CODE}/awards/"
payload = {"toptier_code": '020'}

def get_awards(CGAC=None):

    # initialization
    has_next_page = True
    page = 1
    output = []

    while has_next_page:
        try:
            # run the request
            response = requests.get(f"{url}{endpoint}", params=payload).json()
            print(payload)
            response.raise_for_status()
            response_data = response
            
            # add response data to output
            output += response['results']

            # handle pagination
            has_next_page = response['page_metadata']['has_next_page']
            page += 1
        except requests.exceptions.RequestException as e:
            print(f"Error during API call: {e}")
            break  # Exit the loop in case of an error

    return output

data = get_awards(CGAC='097')

if data:
    df = pd.DataFrame(data)
    print(df)
else:
    print("No data retrieved due to an error.")

    

# import pandas as pd
# import requests

# url = "https://api.usaspending.gov"
# endpoint = "/api/v2/agency/awards/count/"
# payload = {}

# response = requests.get(f"{url}{endpoint}", params=payload)
# data = response.json()

# df = pd.DataFrame(data["results"])

# print(df)