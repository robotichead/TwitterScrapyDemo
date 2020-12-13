# TwitterScrapyDemo
I am just playing around with Scrapy


# How to install

Please use VirtualEnv to run this project

`virtualenv venv`

Once the virtual environment has been created, activate it. `source ./venv/bin/activate`

Install the required libraries using `pip install -r requirements.txt`

To run the program, use the following command `scrapy crawl twitter`


## What is not working

Sadly the loop for the 10 minute scheduled job causes a serious terminal crash. This code has been commented out.
