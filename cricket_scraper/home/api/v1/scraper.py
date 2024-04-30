import requests
from bs4 import BeautifulSoup
from django.conf import settings


def get_single_blog(url):
    base_url = settings.CRICBUZZ_BASE_URL
    blog_url = base_url + url
    response = requests.get(blog_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # title = soup.select_one('//h1[@class="nws-dtl-hdln" and @itemprop="headline"]')
        title = soup.select_one('h1.nws-dtl-hdln[itemprop="headline"]')
        img_tag = soup.select_one('img.cursor-pointer')
        src_value = img_tag.get('src')

        content_text = ""

        p_tags = soup.select('p.cb-nws-para')

        for p_tag in p_tags:
            print("Text is : ", p_tag.text)
            content_text += p_tag.text


        print('src value of image is : ', src_value)
        resp = {
            'title': title.text.strip() if title.text else '',
            'content': content_text,
            'title_image': base_url + src_value
        }
        return resp
    


def get_t20_wc_blogs():
    base_url = settings.CRICBUZZ_BASE_URL
    wc_page_url = base_url + "/cricket-series/7476/icc-mens-t20-world-cup-2024"
    
    response = requests.get(wc_page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        divs = soup.find_all('div', class_='cb-col cb-col-100 cb-lst-itm cb-pos-rel cb-lst-itm-lg')
        blogs = []
        print("No of divs are : ", len(divs))
        for div in divs:
            a_tags = div.find_all('a')
            href_value = a_tags[0].get('href') if len(a_tags) > 0 else None
            data = get_single_blog(href_value)
            if data is not None:
                blogs.append(data)
            print("---------------------------")    
        return blogs
    else:
        print("Failed to fetch the page:", response.status_code)
