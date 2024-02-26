import requests
from bs4 import BeautifulSoup

url = "https://www.vlr.gg/295610/loud-vs-sentinels-champions-tour-2024-americas-kickoff-opening-b/?game=153737&tab=overview"

def scrape_table(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table element using its tag name
    table = soup.find('table')
    
    # Initialize an empty list to store the table data
    data = []
    
    # Iterate over each row in the table
    for row in table.find_all('tr'):
        # Initialize an empty list to store the row data
        row_data = []
        
        # Iterate over each cell in the row
        for cell in row.find_all('td'):
            # Append the cell text to the row data list
            row_data.append(cell.text.strip())
        
        # Append the row data to the table data list
        data.append(row_data)
    
    # Return the table data
    return data

print(scrape_table(url))