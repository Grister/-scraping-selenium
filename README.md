# -scraping-selenium

## Installation

Clone repository
```
git clone https://github.com/Grister/-scraping-selenium.git
```

Install dependencies
```
pip3 install -r requirements.txt 
```

Create `.env` from `env.example` file and update as needed
```
cp env.example .env
```

### Chromedriver
Download from official website proper version of chromedriver for your OS: https://chromedriver.chromium.org/downloads
- Update path to `chromedriver` executable in env variable

### Run application

Ensure, that `social-network` application is running
```
cd -scraping-selenium
python3 app.py
```
