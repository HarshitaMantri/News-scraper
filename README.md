# News-scraper
<h3>Objective</h3><br> Scrape top news headlines from a major news website (e.g., BBC News) and save them to a .txt file for offline reading or analysis.

🛠️ Tools Used
- Python 3
- requests – for fetching HTML content
- BeautifulSoup (bs4) – for parsing and extracting headlines

📁 Project Structure
news_scraper/
├── news_scraper.py         # Main Python script
├── headlines.txt           # Output file with scraped headlines
└── README.md               # Project documentation



🚀 How to Run
1. Install dependencies
   pip install requests beautifulsoup4
2. Run the script
python news_scraper.py


3. View the results
Open headlines.txt to see the list of scraped headlines.

🔍 How It Works
- Sends a GET request to the news site.
- Parses the HTML using BeautifulSoup.
- Extracts headlines from <h2> tags (can be customized).
- Saves each headline to a text file, one per line.

🧪 Sample Output
1. Ukraine war: Russia launches new wave of missile attacks
2. Climate crisis: UN calls for urgent action
3. Tech giants face new regulations
...





