import time
from random import choice
import json
from flask import Flask, request

app = Flask(__name__)

blob = {'tracks': [
        {
          'name': 'I Forgot That You Existed',
          'length': '2:51'
        },
        {
          'name': 'Cruel Summer',
          'length': '2:58'
        },
        {
          'name': 'Lover',
          'length': '3:41'
        },
        {
          'name': 'The Man',
          'length': '3:10'
        },
        {
          'name': 'The Archer',
          'length': '3:31'
        },
        {
          'name': 'I Think He Knows',
          'length': '2:53'
        },
        {
          'name': 'Miss Americana & The Heartbreak Prince',
          'length': '3:54'
        },
        {
          'name': 'Paper Rings',
          'length': '3:42'
        },
        {
          'name': 'Cornelia Street',
          'length': '4:47'
        },
        {
          'name': 'Death By A Thousand Cuts',
          'length': '3:19'
        },
        {
          'name': 'London Boy',
          'length': '3:10'
        },
        {
          'name': 'Soon You’ll Get Better (feat. Dixie Chicks)',
          'length': '3:22'
        },
        {
          'name': 'False God',
          'length': '3:20'
        },
        {
          'name': 'You Need To Calm Down',
          'length': '2:51'
        },
        {
          'name': 'Afterglow',
          'length': '3:43'
        },
        {
          'name': 'ME! (feat. Brendon Urie of Panic! At The Disco)',
          'length': '3:13'
        },
        {
          'name': 'It’s Nice To Have A Friend',
          'length': '2:30'
        },
        {
          'name': 'Daylight',
          'length': '4:53'
        },
        {
          'name': 'Fearless',
          'length': '4:02'
        },
        {
          'name': 'Fifteen',
          'length': '4:54'
        },
        {
          'name': 'Love Story',
          'length': '3:55'
        },
        {
          'name': 'Hey Stephen',
          'length': '4:14'
        },
        {
          'name': 'White Horse',
          'length': '3:54'
        },
        {
          'name': 'You Belong With Me',
          'length': '3:51'
        },
        {
          'name': 'Breathe',
          'length': '4:24'
        },
        {
          'name': 'Tell Me Why',
          'length': '3:21'
        },
        {
          'name': 'You\'re Not Sorry',
          'length': '4:22'
        },
        {
          'name': 'The Way I Loved You',
          'length': '4:04'
        },
        {
          'name': 'Forever & Always',
          'length': '3:45'
        },
        {
          'name': 'The Best Day',
          'length': '4:05'
        },
        {
          'name': 'Change',
          'length': '4:40'
        },
        {
          'name': 'State Of Grace',
          'length': '4:55'
        },
        {
          'name': 'Red',
          'length': '3:41'
        },
        {
          'name': 'Treacherous',
          'length': '4:01'
        },
        {
          'name': 'I Knew You Were Trouble.',
          'length': '3:38'
        },
        {
          'name': 'All Too Well',
          'length': '5:28'
        },
        {
          'name': '22',
          'length': '3:50'
        },
        {
          'name': 'I Almost Do',
          'length': '4:03'
        },
        {
          'name': 'We Are Never Ever Getting Back Together',
          'length': '3:12'
        },
        {
          'name': 'Stay Stay Stay',
          'length': '3:25'
        },
        {
          'name': 'The Last Time',
          'length': '4:58'
        },
        {
          'name': 'Holy Ground',
          'length': '3:22'
        },
        {
          'name': 'Sad Beautiful Tragic',
          'length': '4:44'
        },
        {
          'name': 'The Lucky One',
          'length': '4:00'
        },
        {
          'name': 'Everything Has Changed',
          'length': '4:04'
        },
        {
          'name': 'Starlight',
          'length': '3:38'
        },
        {
          'name': 'Begin Again',
          'length': '3:58'
        },
        {
          'name': '...Ready For It?',
          'length': '3:28'
        },
        {
          'name': 'End Game',
          'length': '4:05'
        },
        {
          'name': 'I Did Something Bad',
          'length': '3:58'
        },
        {
          'name': 'Don’t Blame Me',
          'length': '3:56'
        },
        {
          'name': 'Delicate',
          'length': '3:52'
        },
        {
          'name': 'Look What You Made Me Do',
          'length': '3:32'
        },
        {
          'name': 'So It Goes...',
          'length': '3:48'
        },
        {
          'name': 'Gorgeous',
          'length': '3:30'
        },
        {
          'name': 'Getaway Car',
          'length': '3:54'
        },
        {
          'name': 'King Of My Heart',
          'length': '3:34'
        },
        {
          'name': 'Dancing With Our Hands Tied',
          'length': '3:32'
        },
        {
          'name': 'Dress',
          'length': '3:50'
        },
        {
          'name': 'This Is Why We Can\'t Have Nice Things',
          'length': '3:27'
        },
        {
          'name': 'Call It What You Want',
          'length': '3:24'
        },
        {
          'name': 'New Year\'s Day',
          'length': '3:55'
        },
        {
          'name': 'Mine',
          'length': '3:51'
        },
        {
          'name': 'Sparks Fly',
          'length': '4:21'
        },
        {
          'name': 'Back To December',
          'length': '4:53'
        },
        {
          'name': 'Speak Now',
          'length': '4:01'
        },
        {
          'name': 'Dear John',
          'length': '6:44'
        },
        {
          'name': 'Mean',
          'length': '3:58'
        },
        {
          'name': 'The Story Of Us',
          'length': '4:26'
        },
        {
          'name': 'Never Grow Up',
          'length': '4:50'
        },
        {
          'name': 'Enchanted',
          'length': '5:52'
        },
        {
          'name': 'Better Than Revenge',
          'length': '3:37'
        },
        {
          'name': 'Innocent',
          'length': '5:02'
        },
        {
          'name': 'Haunted',
          'length': '4:02'
        },
        {
          'name': 'Last Kiss',
          'length': '6:07'
        },
        {
          'name': 'Long Live',
          'length': '5:18'
        },
        {
          'name': 'Tim McGraw',
          'length': '3:52'
        },
        {
          'name': 'Picture To Burn',
          'length': '2:53'
        },
        {
          'name': 'Teardrops On My Guitar - Radio Single Remix',
          'length': '3:23'
        },
        {
          'name': 'A Place in this World',
          'length': '3:19'
        },
        {
          'name': 'Cold As You',
          'length': '3:59'
        },
        {
          'name': 'The Outside',
          'length': '3:27'
        },
        {
          'name': 'Tied Together with a Smile',
          'length': '4:08'
        },
        {
          'name': 'Stay Beautiful',
          'length': '3:56'
        },
        {
          'name': 'Should\'ve Said No',
          'length': '4:02'
        },
        {
          'name': 'Mary\'s Song (Oh My My My)',
          'length': '3:33'
        },
        {
          'name': 'Our Song',
          'length': '3:21'
        },
        {
          'name': 'I\'m Only Me When I\'m With You',
          'length': '3:33'
        },
        {
          'name': 'Invisible',
          'length': '3:23'
        },
        {
          'name': 'A Perfectly Good Heart',
          'length': '3:40'
        },
        {
          'name': 'Teardrops on My Guitar - Pop Version',
          'length': '2:59'
        },
        {
          'name': 'Welcome To New York',
          'length': '3:33'
        },
        {
          'name': 'Blank Space',
          'length': '3:52'
        },
        {
          'name': 'Style',
          'length': '3:51'
        },
        {
          'name': 'Out Of The Woods',
          'length': '3:56'
        },
        {
          'name': 'All You Had To Do Was Stay',
          'length': '3:13'
        },
        {
          'name': 'Shake It Off',
          'length': '3:39'
        },
        {
          'name': 'I Wish You Would',
          'length': '3:27'
        },
        {
          'name': 'Bad Blood',
          'length': '3:32'
        },
        {
          'name': 'Wildest Dreams',
          'length': '3:40'
        },
        {
          'name': 'How You Get The Girl',
          'length': '4:08'
        },
        {
          'name': 'This Love',
          'length': '4:10'
        },
        {
          'name': 'I Know Places',
          'length': '3:16'
        },
        {
          'name': 'Clean',
          'length': '4:31'
        },
        {
          'name': 'State Of Grace',
          'length': '4:55'
        },
        {
          'name': 'Red',
          'length': '3:41'
        },
        {
          'name': 'Treacherous',
          'length': '4:01'
        },
        {
          'name': 'I Knew You Were Trouble.',
          'length': '3:38'
        },
        {
          'name': 'All Too Well',
          'length': '5:28'
        },
        {
          'name': '22',
          'length': '3:50'
        },
        {
          'name': 'I Almost Do',
          'length': '4:03'
        },
        {
          'name': 'We Are Never Ever Getting Back Together',
          'length': '3:12'
        },
        {
          'name': 'Stay Stay Stay',
          'length': '3:25'
        },
        {
          'name': 'The Last Time',
          'length': '4:58'
        },
        {
          'name': 'Holy Ground',
          'length': '3:22'
        },
        {
          'name': 'Sad Beautiful Tragic',
          'length': '4:44'
        },
        {
          'name': 'The Lucky One',
          'length': '4:00'
        },
        {
          'name': 'Everything Has Changed',
          'length': '4:04'
        },
        {
          'name': 'Starlight',
          'length': '3:38'
        },
        {
          'name': 'Begin Again',
          'length': '3:58'
        },
        {
          'name': 'The Moment I Knew',
          'length': '4:46'
        },
        {
          'name': 'Come Back...Be Here',
          'length': '3:43'
        },
        {
          'name': 'Girl At Home',
          'length': '3:40'
        },
        {
          'name': 'Treacherous - Original Demo Recording',
          'length': '3:60'
        },
        {
          'name': 'Red - Original Demo Recording',
          'length': '3:46'
        },
        {
          'name': 'State Of Grace - Acoustic Version',
          'length': '5:23'
        },
        {
          'name': 'The 1',
          'length': '3:30'
        },
        {
          'name': 'Cardigan',
          'length': '3:59'
        },
        {
          'name': 'The Last Great American Dynasty',
          'length': '3:51'
        },
        {
          'name': 'Exile (featuring Bon Iver)',
          'length': '4:45'
        },
        {
          'name': 'My Tears Ricochet',
          'length': '4:15'
        },
        {
          'name': 'Mirrorball',
          'length': '3:29'
        },
        {
          'name': 'Seven',
          'length': '3:28'
        },
        {
          'name': 'August',
          'length': '4:21'
        },
        {
          'name': 'This Is Me Trying',
          'length': '3:15'
        },
        {
          'name': 'Illicit Affairs',
          'length': '3:10'
        },
        {
          'name': 'Invisible String',
          'length': '4:12'
        },
        {
          'name': 'Mad Woman',
          'length': '3:57'
        },
        {
          'name': 'Epiphany',
          'length': '4:49'
        },
        {
          'name': 'Betty',
          'length': '4:54'
        },
        {
          'name': 'Peace',
          'length': '3:54'
        },
        {
          'name': 'Hoax',
          'length': '3:40'
        },
      ]
    }

@app.route('/', methods=['GET'])
def serve():
  songlist = []
  for i in range(5):
    track = choice(blob['tracks'])
    songlist.append(track['name'])

  time.sleep(5)
  return json.dumps(songlist)