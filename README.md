# BoxNovel_Scraper
Simple script to scrape a complete novel from BoxNovel

You will need to run using the following: python main.py "URL of the novel"

Ex. python main.py https://boxnovel.com/novel/top-tier-providence-secretly-cultivate-for-a-thousand-years/

The script will automatically attach the chapter-number to the end of the URL. 

The script does use a Google Chrome driver to run Selenium, so be aware that you'll need a Chromedriver to run this script 
(or you can modify the script to work with other drivers).

Once the script is running, it will grab the novel's name and generate a folder based of the name (folder will be generated in working directory).
From there, it will generate a pdf for every chapter in the novel (starting from 1 and going to newest) storing them in the created/existing directory. If you run the script after already running it once (with the same novel name) the script will just get the newest chapters released since the last time it was ran. 
