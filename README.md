# Web-Crawler


## Design Decisions

For keeping the code short I have created a webcrawler python script that firsts searches for some domains in the commoncrawler. It then gets the fileName, offset and lengths of all 2020 domains matching the domains given in the input.
Used - http://index.commoncrawl.org/ 

It then reads the html, parses and finds all htmls with covid and economy. And prints the domain names as outputs.

How to run
python3 webcrawler.py


## Challenges and Updates that can be done

This method is not efficient and scalable.A more scalable approach would be to use mapreduce.
Examples:
https://blog.stefan-koch.name/2016/05/01/analyzing-the-commoncrawl-using-mapreduce 

https://engineeringblog.yelp.com/2015/03/analyzing-the-web-for-the-price-of-a-sandwich.html
