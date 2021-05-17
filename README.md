<div style="display: flex; justify-content:space-between; max-height: 300px;">
    <div>
        <h1>Andraste</h1>
        <p style="margin-right: 20px;text-align: justify">Andraste is know as the base for the creation, her teaching were used for leading and defining how everything would be. In Octopus, Andraste is the base for the crawlers, it controls and define where all the collected data goes. It is created wrapping the scrapy framework, her purpose is to get the inputs, pass to the crawlers, follow the data and send it to Blackwall</p>
    </div>
    <img style="max-width: 200px; max-height: 1000px" src="https://i.pinimg.com/originals/cb/38/8a/cb388adbbb7ed5b190e06903491b82ed.jpg">
</div>

<hr>
<br><br>

##  1. Usage
##### 1.1 Using the base class:<br>
```
from andraste.base import Spider

class Crawler(Spider):
   ...  
```
<br>


##### 1.2 Running the crawler:<br>
<p style="opacity: 0.6">Assuming that the crawler's file is in 'bot' module, and the file's name is bot.py, we can run the crawler by doing:<p>

```
python3 andraste.py bot.bot.Crawler
```
<p style="opacity: 0.6">python3 andraste.py module.filename.classname<p>

<br>

##### 1.3 Running tests:<br>
```
python3 -m unittest tests/file_name.py
```