import pandas as pd
import requests

def query_api(tag, query1, query2, page, from_date, api_key):
    """
    Function to query the API for a particular tag
    returns: a response from API
    """
    response = requests.get(f'https://content.guardianapis.com/search?q={query1}%20AND%20{query2}&tag={tag}/{tag}&from-date={from_date}&page={page}&page-size=200&api-key={api_key}')
    return response

def get_results_for_tag(tag, query1, query2, from_date, api_key):
    """
    Function to run a for loop for results greater than 200. 
    Calls the query_api function accordingly
    returns: a list of JSON results
    """
    json_responses = []
    response = query_api(tag, query1, query2, 1, from_date, api_key).json()
    json_responses.append(response)
    number_of_results = response['response']['total']
    print(number_of_results)
    if number_of_results > 200:
        for page in range(2, (round(number_of_results/200))+1):
            response = query_api(tag, query1, query2, page, from_date, api_key).json()
            json_responses.append(response)
    return json_responses

def convert_json_responses_to_df(json_responses):
    """
    Function to convert the list of json responses to a dataframe
    """
    df_results = []
    for json in json_responses:
        df = pd.json_normalize(json['response']['results'])
        df_results.append(df)
    all_df = pd.concat(df_results)
    return all_df


json_responses = get_results_for_tag('environment', 'bangladesh', ' ', '2012-01-01', '1997b4cf-fab9-4990-9a04-3e4722c6bd79')
df = convert_json_responses_to_df(json_responses)
