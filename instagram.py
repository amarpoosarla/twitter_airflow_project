from instagram_private_api import Client

# Initialize a new Instagram API client
username = 'amarpoosarla'
password = 'Saroja@143'
api = Client(username, password)



def run_instagram_etl():
    # Get user information
    user_id = api.username_info('amarpoosarla')['user']['pk']
    user_info = api.user_info(user_id)

    # Print the user's full name and follower count
    print(user_info['user']['full_name'])
    print(user_info['user']['follower_count'])

    #print the above data in a dataframe
    import pandas as pd
    df = pd.DataFrame(user_info)
    df

    #print the dataframes in a csv file
    df.to_csv('instagram.csv')
    #save to s3
    df.to_csv(
        's3://amarpoosarla/instagram.csv',
        index=False
    )

