import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the book elements on the page
        books = soup.find_all('div', class_='book')
        
        # Extract information for each book
        book_list = []
        for book in books:
            title = book.find('h2', class_='title').text.strip()
            author = book.find('p', class_='author').text.strip()
            rating = book.find('span', class_='rating').text.strip()
            
            book_list.append({'title': title, 'author': author, 'rating': rating})
        
        return book_list
    else:
        print("Failed to fetch data from the URL.")
        return []

if __name__ == "__main__":
    # URL of the webpage to scrape
    target_url = "https://www.example.com/books"
    
    # Call the function and get the list of books
    books_data = scrape_books(target_url)
    
    # Display the scraped data
    for book in books_data:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Rating: {book['rating']}")
        print("-" * 30)