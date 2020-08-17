# -*- coding: utf-8 -*-

import qbittorrentapi as qbit
import rarbgapi
import putiopy
from MovieFinder import config as cfg
from MovieFinder import putiokey as pkey
from datetime import datetime

'''
CATEGORY_ADULT
CATEGORY_MOVIE_XVID
CATEGORY_MOVIE_XVID_720P
CATEGORY_MOVIE_H264
CATEGORY_MOVIE_H264_1080P
CATEGORY_MOVIE_H264_720P
CATEGORY_MOVIE_H264_3D
CATEGORY_MOVIE_H264_4K
CATEGORY_MOVIE_H265_4K
CATEGORY_MOVIE_H265_4K_HDRmul
CATEGORY_MOVIE_FULL_BD
CATEGORY_MOVIE_BD_REMUX
CATEGORY_TV_EPISODES
CATEGORY_TV_EPISODES_HD
CATEGORY_TV_EPISODES_UHD
CATEGORY_MUSIC_MP3
CATEGORY_MUSIC_FLAC
CATEGORY_GAMES_PC_ISO
CATEGORY_GAMES_PC_RIP
CATEGORY_GAMES_PS3
CATEGORY_GAMES_PS4
CATEGORY_GAMES_XBOX
CATEGORY_SOFTWARE
CATEGORY_EBOOK
'''

qbt_auth = {'host': cfg.qbt["host"],
            'username': cfg.qbt['username'],
            'password': cfg.qbt['password']}

path_to_save = '/Users/PargAsh/Downloads/Offline/Film'


def MovieSearch(moviename):
    rarbgclient = rarbgapi.RarbgAPI()

    Qs = ['CATEGORY_MOVIE_H265_4K_HDR', 'CATEGORY_MOVIE_H265_4K', 'CATEGORY_MOVIE_H264_4K', 'CATEGORY_MOVIE_H264_1080P']
    Qualities = []
    for q in Qs:
        cat = eval('rarbgapi.RarbgAPI.' + q)
        Qualities.append(cat)

    movienamealt = moviename.replace(' ', '.')
    alts = [movienamealt, moviename]
    counter = 0
    for q in Qualities:
        # print(q)
        for x in alts:
            searchresult = rarbgclient.search(limit=10, search_string=x, category=q)
            if len(searchresult) != 0:
                # for torrent in searchresult:
                #     print(torrent.download)
                firsthit = searchresult[0]
                torrent = firsthit.download
                return torrent
            else:
                counter += 1
                if counter == len(Qualities)*len(alts):
                    response = 'No results found'
                    return response


def MovieFinder(moviename):

    response = ''
    link = MovieSearch(moviename)

    if link == 'No results found':
        response = 'No results found for' + moviename
    elif "1080p" in link:
        try:
            client = putiopy.Client(pkey.OAUTH_KEY)
            client.Transfer.add_url(link)
            response = "You'll be able to watch "+moviename+" on Put IO soon..."
        except Exception:
            return 'Something went wrong adding file to Put IO.'
    else:
        # instantiate a Client using the appropriate WebUI configuration
        qbt_client = qbit.Client(host=qbt_auth['host'], username=qbt_auth['username'], password=qbt_auth['password'])

        # the Client will automatically acquire/maintain a logged in state in line with any request.
        # therefore, this is not necessary; however, you many want to test the provided login credentials.
        try:
            qbt_client.auth_log_in()
        except qbit.LoginFailed:
            return 'Could not authenticate. Qbt is probably down.'

        # add download link to qbt client
        # help(qbt_client.torrents_add)
        try:
            qbt_client.torrents_add(urls=link, save_path=path_to_save, is_paused=False)
            response = "You'll be able to watch "+moviename+" in 4K soon..."
        except Exception:
            return 'Something went wrong adding file to Qbt.'

    try:
        with open("/var/www/piAppSwitcher/MovieFinder/MFResponses.txt", mode='a+') as txtfile:
            txtfile.write('On ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' MovieFinder sent response "' + response + '".\n')
    except IOError:
        print("Couldn't write to file!")

    return response
