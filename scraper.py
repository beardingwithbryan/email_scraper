import re
from requests_html import HTMLSession
import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", required=True,  help="Input URL File")
parser.add_argument("-d", "--domain", required=True,  help="Domain of Emails to Look for")

args = parser.parse_args()



f = open(args.input, "r")
a = open("emails.txt", "a+")

def write_email(email, file):
    file.seek(0)

    # print(site)

    if email in file.read():
        return

    file.write(email + "\n")

for url in f:
  session = HTMLSession()
  if url.endswith('\n'):
    #have to drop the /n off the end of each URL
    r = session.get(url[:len(url)-1])
  else:
    r = session.get(url)
  # for JAVA-Script driven websites use the following line instead
  #r.html.render()
  mailto = re.findall('\S+@\S+', str(r.content))
  for links in mailto:
    email_list = links.replace('href="mailto:', '').rsplit(args.domain+'">')
    write_email(email_list[0]+args.domain, a)
