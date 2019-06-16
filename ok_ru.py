from bs4 import BeautifulSoup
import requests

URL = 'https://ok.ru/mil'

def get_base_url(url):
    return url.rsplit('/', 1)[0]

def get_html(url):
    ok_ru = requests.get(url)
    html = BeautifulSoup(ok_ru.text, 'html.parser')
    return html

def get_posts(html):
    posts = html.find_all('div', attrs={"class": "feed-w"})
    return posts

def get_post_details(post):
    post_details = {}

    #group_name
    group_name = post.find('a', attrs={"class": "group-link o"}).text
    #content
    content = post.find('div', attrs={"class": "media-text_cnt"}).div.text
    #date_posted
    date_posted = post.find('div', attrs={"class": "feed_date"}).text
    #content_url
    content_details = post.find('div', attrs={"class": "media-text_cnt"})
    content_url = get_base_url(URL) + content_details.find('a', attrs={"class": "media-text_a"}).attrs["href"]

    widgets = post.find('ul', attrs={"class": "widget-list h-mod"})
    #comment_count
    comments = widgets.find('a', attrs={"data-module": "CommentWidgets"})
    comment_count = comments.find('span', attrs={"class": "widget_count"}).text
    #share_count
    shares = widgets.find('button', attrs={"data-module": "LikeComponent"})
    share_count = shares.find('span', attrs={"class": "widget_count"}).text
    #like_count
    likes = widgets.find('span', attrs={"class": "widget_cnt controls-list_lk"})
    like_count = likes.find('span', attrs={"class": "widget_count"}).text

    #build post_details dictionary
    post_details["group_name"] = group_name
    post_details["content"] = content
    post_details["date_posted"] = date_posted
    post_details["content_url"] = content_url
    post_details["comment_count"] = comment_count
    post_details["like_count"] = like_count
    post_details["share_count"] = share_count
    return post_details

def get_all_post_details(posts):
    post_details_list = []
    for post in posts:
        post_details_list.append(get_post_details(post))
    return post_details_list

#entry point for parsing details from url
def get_post_details_from_url(url):
    ok_html = get_html(URL)
    ok_posts = get_posts(ok_html)
    return get_all_post_details(ok_posts)

print(get_post_details_from_url(URL))