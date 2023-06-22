# Retrieve the data from the pagination to calculate the number of transactionds done by user. 
import requests
import pandas as pd

def count_transactions(url):    
    total_pages = None
    page = 1
    
    total_data = []
    while total_pages is None or page<=total_pages:
        
        response = requests.get(f"{url}/{page}")
        
        print(f" Processing page : {page} {response.status_code}") 
        if response.status_code == 200:
            respons_data = response.json()
            total_data.append(respons_data)        
            page +=1 
        else:
            break
        
        if page==30:
            total_pages=30
    print(" ")
    df = pd.DataFrame(total_data)
    # print(f" Json ddf \n : {df}")
    user_id = df.groupby('userId')
    # print(f" User group \n : {list(user_id.items())}")
    print(f" Group data : {list(user_id.size().iteritems())}")
    
    print(f" Group data : {list(df['userId'].value_counts().items())}")
    # print(df.value_counts())
    
url = 'https://jsonplaceholder.typicode.com/posts'
print(count_transactions(url))
        