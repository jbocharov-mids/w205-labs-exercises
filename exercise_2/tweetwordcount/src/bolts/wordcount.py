from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.create_connection()
        self.create_cursor()
       

    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        self.ensure_connection()
        self.ensure_cursor()
        
        self.ensure_database_word_entry(word)
        self.increment_database_count(word)

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

    def ensure_connection(self):
        if not self.conn:
            self.create_connection()

    def ensure_cursor(self):
        if not self.cur:
            self.create_cursor()

    def ensure_database_word_entry(self, word):
        # This query will insert (word, 0) but no-op if word already exists
        insert = 'INSERT INTO Tweetwordcount (word, count) '
        select = 'SELECT %s AS word, 0 AS count '
        where = 'WHERE %s NOT IN (SELECT word FROM Tweetwordcount)'
        query = insert + select + where

        self.cur.execute(query, (word, word))
        self.conn.commit()

    def increment_database_count(self, word):
        increment = 'UPDATE Tweetwordcount SET count = count+1 WHERE word = %s'
        self.cur.execute(increment, (word, ))
        self.conn.commit()
        

    def create_connection(self):
        self.conn = psycopg2.connect(
            database = "Tcount", 
            user = "postgres", 
            password = "pass", 
            host = "localhost", 
            port = "5432"
        )
        self.log('Created connection: %s' % str(self.conn))

    def create_cursor(self):
        self.cur = self.conn.cursor()
        self.log('Created cursor: %s' % str(self.cur))