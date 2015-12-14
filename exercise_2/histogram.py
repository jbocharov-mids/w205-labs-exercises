import psycopg2
import sys

def print_bounded_histogram(lower, upper):
  select = 'SELECT word, count FROM Tweetwordcount '
  where = 'WHERE count >= %s AND count <= %s';

  conn = get_connection()
  cur = conn.cursor()
  cur.execute(select + where, (lower, upper))
  records = cur.fetchall()

  for rec in records:
    word = rec[0]
    count = rec[1]
    print( '%s: %d' % ( word, count ) )

  conn.close()


def print_usage():
  print ('''
    Usage: python histogram.py <lower>,<upper>
      Where <lower> and <upper> are integers
      Prints words and counts with counts between lower and upper, inclusive
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
    span_arg = sys.argv[1]
    span_array = span_arg.split(',')
    lower, upper = ( int(span_array[0]), int(span_array[1]) )
    print_bounded_histogram(lower, upper)


  else:
    print_usage() 