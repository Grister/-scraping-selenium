from services import SocialNetworkScraper

if __name__ == '__main__':
    title = "new title from test scraping344"
    context = "text from test scraping44444"
    service = SocialNetworkScraper()
    service.social_network_add_post(title, context)
    print('done')
