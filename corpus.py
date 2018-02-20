import sys
import io
import string
import praw

def download(name):
    print('downloading...')
    reddit = praw.Reddit(client_id='k1TRpvZvtwdO0A',
                client_secret='nhXP4m3w-lYq_jvzuvz7SxXgc1A',
                user_agent='python:praw (by /u/sq42na)')
    subreddit = reddit.subreddit(name)
    printable = set(string.printable)
    with io.open(name + '.txt', 'w') as f:
        print('saving...')
        for submission in subreddit.top('all', limit=1000):
            title = ''.join(filter(lambda x: x in printable, submission.title))
            f.write(title + '\n')
        print('done.')

if __name__ == '__main__':
    cmd = sys.argv[1]
    name = sys.argv[2]
    if cmd == 'download':
        download(name)
