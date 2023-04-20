from services import SocialNetworkScraper

if __name__ == '__main__':
    service = SocialNetworkScraper()
    service.social_network_add_post('new post', 'content for test scraping')
    print('done')
