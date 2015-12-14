import psycopg2
import sys

def print_specific_word_count(word):
  query = 'SELECT count FROM Tweetwordcount WHERE word = %s';

  conn = get_connection()
  cur = conn.cursor()
  cur.execute(query, (word, ))
  records = cur.fetchall()

  try:
    # take the first cell of the first row
    count = records.__iter__().next()[0]
    print ( 'Total number of occurences of "%s": %d' % ( word, count ) )

  except StopIteration:
    print ( 'The word %s was not found in the data set' % ( word, ) )

  conn.close()

def print_ascending_word_counts():
  query = 'SELECT word, count FROM Tweetwordcount ORDER BY word ASC, count ASC';
  
  conn = get_connection()
  cur = conn.cursor()
  cur.execute(query)
  records = cur.fetchall()
  
  for rec in records:
    word = rec[0]
    count = rec[1]
    print( '(%s, %d)' % ( word, count ) )

  conn.close()

def print_usage():
  print ('''
    Usage: python finalresults.py [word]
      if [word] is supplied, prints the count for that word
      otherwise, prints all word counts in ascending order 
  ''')

def get_connection():
  return psycopg2.connect(
    database = "Tcount", 
    user = "postgres", 
    password = "pass", 
    host = "localhost", 
    port = "5432"
  )

if __name__ == '__main__':

  if len(sys.argv) == 2:
    word = sys.argv[1]
    print_specific_word_count(word)

  elif len(sys.argv) == 1:
    print_ascending_word_counts()

  else:
    print_usage() 


