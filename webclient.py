#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client that returns the title
of the free daily e-book from www.packtpub.com
Created on 3/1/2017
@author: amr1990
'''

import urllib2
import bs4


class Client(object):

    """Web Client, for www.packtpub.com
    Downloads www.packtpub.com/packt/offers/free-learning page to parse
    and get the title of the free book of the day"""

    def __init__(self):
        super(Client, self).__init__()

    def get_web_page(self, url):

        """
        Retrieves an HTML URL returns HTML
        """
        wp = urllib2.urlopen(url)
        html = wp.read()
        wp.close()

        return html

    def get_data(self, html):

        '''
        Parses an html page searching for the title of the book
        '''

        soup = bs4.BeautifulSoup(html, "lxml")
        booksummary = soup.find("div", "dotd-main-book-summary float-left")
        book = booksummary.find("div", "dotd-title").find("h2").text.strip()
        return book

    def print_data(self, book):

        '''
        Print the data retrieved
        '''

        print "The free book of the day is: " + book

    def run(self):

        '''
        Retrieves the title of the free book of the day
        '''

        html = self.get_web_page("https://www.packtpub.com/packt/offers/free-learning")
        book = self.get_data(html)
        self.print_data(book)


if __name__ == "__main__":
    client = Client()
    client.run()
