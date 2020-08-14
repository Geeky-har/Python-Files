from win32com.client import Dispatch
from newsapi import NewsApiClient

speak = Dispatch("SAPI.SpVoice")


def bhokon(strs):

    speak.Speak(strs)


if __name__ == '__main__':

    newsapi = NewsApiClient(api_key='2e32ad57b7334bb8a8b85b3a84a1648c')

    top_headlines_india = newsapi.get_top_headlines(sources='the-hindu')

    top_headlines_sports = newsapi.get_top_headlines(sources='bbc-sport')

    top_headlines_inter = newsapi.get_top_headlines(sources='bbc-news')

    top_headlines_business = newsapi.get_top_headlines(sources='business-insider')

    head_str = 'Todays headlines for'

    print('Select an option from the list below: ')

    print('1. For International News (Headlines)')
    print('2. For News From India (Headlines)')
    print('3. For News from the world of sports (Headlines)')
    print('4. For Business related Headlines')
    option = int(input())

    if option == 1:

        print(f'{head_str} International news are:  ')
        bhokon(f'{head_str} International news are:  ')

        for i in range(10):
            print(f'{i+1}. ' + top_headlines_inter['articles'][i]['title'])
            bhokon(top_headlines_inter['articles'][i]['title'])

    elif option == 2:

        print(f'{head_str} India are: ')
        bhokon(f'{head_str} India are: ')

        for i in range(10):
            print(f'{i+1}. ' + top_headlines_india['articles'][i]['title'])
            bhokon(top_headlines_india['articles'][i]['title'])

    elif option == 3:

        print(f'{head_str} sports news are: ')
        bhokon(f'{head_str} sports news are: ')

        for i in range(10):
            print(f'{i+1}. ' + top_headlines_sports['articles'][i]['title'])
            bhokon(top_headlines_sports['articles'][i]['title'])

    elif option == 4:

        print(f'{head_str} Business news are: ')
        bhokon(f'{head_str} Business news are: ')

        for i in range(10):
            print(f'{i+1}. ' + top_headlines_business['articles'][i]['title'])
            bhokon(top_headlines_business['articles'][i]['title'])
