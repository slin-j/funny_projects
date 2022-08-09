import os
import time
import folium

import comparis
import siteScraper

url = ""

GLOBAL_PATH = os.path.dirname(__file__)
OUTPUT_FILE = os.path.join(GLOBAL_PATH, 'out.html')

if __name__ == "__main__":
    t_start = time.time()
    # scrape given comparis-link for addresses and links to the adverts
    addresses, links = siteScraper.get_all_addresses(url)
    print(f'Found {len(addresses)} adverts on the site in {round(time.time() - t_start, 3)}s:')
    
    # create objects and also convert the addresses to geolocation (lat lon)
    adverts = []
    for adr, link in zip(addresses, links):
        adverts.append(comparis.advert(adr, link))

    print('generating map...')
    mapit = folium.Map()
    mapit.fit_bounds([ad.get_latlon() for ad in adverts]) # fit map that all pins are in view
    
    # create marker for every advert
    for ad in adverts:
        folium.Marker(
            location=ad.get_latlon(),
            popup=f'<a href={ad.get_link()}>Link</a>',
            tooltip=ad.get_address(),
            icon=folium.Icon(color='purple', prefix='fa', icon='home')
        ).add_to(mapit)
    
    mapit.save(OUTPUT_FILE)
    print(f'generation successful! saved as {OUTPUT_FILE}')
    print(f'script took {round(time.time() - t_start, 3)}s')