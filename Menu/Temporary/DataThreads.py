# buat edukasi aja
# Zoraa Dev/Dev Knowing

from Menu.Data.data import *

class Penyimpanan:
    def __init__(self) -> None:
        pass
        
    def data_profiles_threads(self, cookies, url = 'https://www.threads.com'):
        with requests.Session() as r:
            try:
                response = r.get(url, cookies = {'cookie':cookies}).text
                data = {
                    "av": re.search('{"actorID":"(\d+)"', str(response)).group(1),
                    "__user": re.search('{"actorID":"(\d+)"', str(response)).group(1),
                    "__a": "1",
                    "__req": "a",
                    "__hs": re.search('"haste_session":"(.*?)"', str(response)).group(1),
                    "dpr": "3",
                    "__ccg": re.search('"connectionClass":"(.*?)"',str(response)).group(1),
                    "__rev": "1025731959",
                    "__s": "h21p0t:2ugba4:bs6w13",
                    "__hsi": re.search('"hsi":"(\d+)"', str(response)).group(1),
                    "__dyn": "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awgo9oO0n24oaEd82lwv89k2C1Fwc60D85m1mzXwae4UaEW0Loco5G0zK5o4q0HU1IEGdwtU2ewbS1LwTwKG0hq1Iwqo9Epxq261bg5q2-2K7E4u48jgbVE-19xW1Vwn85SU7y",
                    "__csr": "iMYxA-AgBOROnNfTEN-AoBHWWnIyAGqchkvByFVauWAADoSmi5UnwzACXw05-_Ki9x2i09AIM7m0ol6J0bq1l5P0PwuQ1WUy1Y30K9go6o5vUbo6C0kG0pl6xq2F04FiGWy8B01B-Unw1d-0BooOyAu9yl2E9o5O2e2O7o0yC0OAA1Vo1dUrwJU3awHAzjG5k4VcMgxyku3632tN8qxx7kwdEaU2Hzqm0u2kIi0tb4xG2W6e4QcwXy8yiEy9kaxy0A8kooQ",
                    "__hsdp": "i84Q4G8x41q5cErcba6xA4isiwWMqR2wRtA0wF7qxmqBAl2hp8cpFML2Y-SgQAv84qwBhUCycNjE4Eqgui70AxldyCd83Fnfhu3KTKbxGcAABXwn9E3FU2lwoUd8aonwiE8k0SEeE88fm6Edouw7Yw",
                    "__hblp": "0Mg1jU8qwmd0HwlkcxW0DUp-cwIG2S10wwyoK7EKaByXz8pwBx62q2a5onCK485O14w7swFxujG68O4bBXxJ4wLzEa898rG7EG9UbE88aotxai2Z1W0vO",
                    "__sjsp": "i84Q4G8Dq0mxyG6P2OxEp14D4EeI6JgE4dwhUB1y9glw",
                    "__comet_req": re.search('__comet_req=(\d+)', str(response)).group(1),
                    "fb_dtsg": re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(response)).group(1),
                    "jazoest": re.search('jazoest=(\d+)', str(response)).group(1),
                    "lsd": re.search('"LSD",\[\],{"token":"(.*?)"',str(response)).group(1),
                    "__spin_r": re.search('"__spin_r":(\d+)', str(response)).group(1),
                    "__spin_b": re.search('"__spin_b":"(.*?)"',str(response)).group(1),
                    "__spin_t": re.search('"__spin_t":(\d+)', str(response)).group(1),
                    "__jssesw": "2",
                    "__crn": "comet.threads.BarcelonaProfileThreadsColumnRoute",
                    "fb_api_caller_class": "RelayModern",
                    "fb_api_req_friendly_name": "BarcelonaProfileEditDialogQuery",
                    "variables": json.dumps({
                        "__relay_internal__pv__BarcelonaIsShowIGBadgeSettingEnabledrelayprovider":True,
                        "__relay_internal__pv__BarcelonaIsShowRepliesTabSettingEnabledrelayprovider":False,
                        "__relay_internal__pv__BarcelonaHasEventBadgerelayprovider":False,
                        "__relay_internal__pv__BarcelonaHasDisplayNamesrelayprovider":False,
                        "__relay_internal__pv__BarcelonaHasProfileTagsrelayprovider":False,
                    }),
                    "server_timestamps": "true",
                    "doc_id": "9939980839447308"
                }
                headers = {
                    "authority": "www.threads.com",
                    "content-length": "336185",
                    "sec-ch-ua": "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
                    "offset": "0",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                    "sec-ch-ua-platform-version": "",
                    "x-entity-length": "336185",
                     "sec-ch-ua-full-version-list": "\"Chromium\";v=\"107.0.5304.74\", \"Not=A?Brand\";v=\"24.0.0.0\"",
                     "sec-ch-ua-model": "",
                     "sec-ch-prefers-color-scheme": "light",
                     "sec-ch-ua-platform": "\"Linux\"",
                     "accept": "*/*",
                     "origin": "https://www.threads.com",
                     "sec-fetch-site": "same-origin",
                     "sec-fetch-mode": "cors",
                     "sec-fetch-dest": "empty",
                     "referer": "https://www.threads.com/",
                     "accept-encoding": "gzip, deflate",
                     "accept-language": "id-ID,id;q=0.9",
                    "x-fb-friendly-name": "BarcelonaProfileEditDialogQuery",
                    "x-csrftoken": re.search(r'csrftoken=(.*?);', str(cookies)).group(1),
                    "x-bloks-version-id": "52fc1652455c0b437eef96decb69daa97f8db556a0db2cab5cd842c2accea603",
                    "x-ig-app-id": "238260118697367",
                    "x-fb-lsd": data.get('fb_dtsg'),
                    "x-asbd-id": "359341"
                }
                response2 = r.post('https://www.threads.com/graphql/query',data=data, headers=headers, cookies={'cookie':cookies})
                if response2.status_code == 200:
                    try:
                        return (response2.json()['data']['viewer']['user']['full_name'], response2.json()['data']['viewer']['user']['username'])
                    except (Exception) as e:
                        return None
                else:
                    return None
            except (Exception) as e:
                return None
                
    def edit_bio_profile_threads(self, cookies, biography, url = 'https://www.threads.com'):
        with requests.Session() as r:
            try:
                response = r.get(url, cookies = {'cookie':cookies}).text
                data = {
                    "av": re.search('{"actorID":"(\d+)"', str(response)).group(1),
                    "__user": re.search('{"actorID":"(\d+)"', str(response)).group(1),
                    "__a": "1",
                    "__req": "a",
                    "__hs": re.search('"haste_session":"(.*?)"', str(response)).group(1),
                    "dpr": "3",
                    "__ccg": re.search('"connectionClass":"(.*?)"',str(response)).group(1),
                    "__rev": "1025731959",
                    "__s": "h21p0t:2ugba4:bs6w13",
                    "__hsi": re.search('"hsi":"(\d+)"', str(response)).group(1),
                    "__dyn": "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awgo9oO0n24oaEd82lwv89k2C1Fwc60D85m1mzXwae4UaEW0Loco5G0zK5o4q0HU1IEGdwtU2ewbS1LwTwKG0hq1Iwqo9Epxq261bg5q2-2K7E4u48jgbVE-19xW1Vwn85SU7y",
                    "__csr": "iMYxA-AgBOROnNfTEN-AoBHWWnIyAGqchkvByFVauWAADoSmi5UnwzACXw05-_Ki9x2i09AIM7m0ol6J0bq1l5P0PwuQ1WUy1Y30K9go6o5vUbo6C0kG0pl6xq2F04FiGWy8B01B-Unw1d-0BooOyAu9yl2E9o5O2e2O7o0yC0OAA1Vo1dUrwJU3awHAzjG5k4VcMgxyku3632tN8qxx7kwdEaU2Hzqm0u2kIi0tb4xG2W6e4QcwXy8yiEy9kaxy0A8kooQ",
                    "__hsdp": "i84Q4G8x41q5cErcba6xA4isiwWMqR2wRtA0wF7qxmqBAl2hp8cpFML2Y-SgQAv84qwBhUCycNjE4Eqgui70AxldyCd83Fnfhu3KTKbxGcAABXwn9E3FU2lwoUd8aonwiE8k0SEeE88fm6Edouw7Yw",
                    "__hblp": "0Mg1jU8qwmd0HwlkcxW0DUp-cwIG2S10wwyoK7EKaByXz8pwBx62q2a5onCK485O14w7swFxujG68O4bBXxJ4wLzEa898rG7EG9UbE88aotxai2Z1W0vO",
                    "__sjsp": "i84Q4G8Dq0mxyG6P2OxEp14D4EeI6JgE4dwhUB1y9glw",
                    "__comet_req": re.search('__comet_req=(\d+)', str(response)).group(1),
                    "fb_dtsg": re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(response)).group(1),
                    "jazoest": re.search('jazoest=(\d+)', str(response)).group(1),
                    "lsd": re.search('"LSD",\[\],{"token":"(.*?)"',str(response)).group(1),
                    "__spin_r": re.search('"__spin_r":(\d+)', str(response)).group(1),
                    "__spin_b": re.search('"__spin_b":"(.*?)"',str(response)).group(1),
                    "__spin_t": re.search('"__spin_t":(\d+)', str(response)).group(1),
                    "__jssesw": "2",
                    "__crn": "comet.threads.BarcelonaProfileThreadsColumnRoute",
                    "fb_api_caller_class": "RelayModern",
                    "fb_api_req_friendly_name": "useBarcelonaEditProfileMutation",
                    "variables": json.dumps({
                        "external_url":"",
                        "biography": biography,
                        "username":"",
                        "name":"",
                        "is_private":True,
                        "profile_picture_upload_id": "null",
                        "remove_profile_picture":False,
                        "copy_ig_profile_picture_to_text_post_app":False,
                        "__relay_internal__pv__BarcelonaHasSpoilerStylingInforelayprovider":True
                    }),
                    "server_timestamps": "true",
                    "doc_id": "24130671149877999"
                }
                headers = {
                    "authority": "www.threads.com",
                    "content-length": "336185",
                    "sec-ch-ua": "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
                    "offset": "0",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                    "sec-ch-ua-platform-version": "",
                    "x-entity-length": "336185",
                     "sec-ch-ua-full-version-list": "\"Chromium\";v=\"107.0.5304.74\", \"Not=A?Brand\";v=\"24.0.0.0\"",
                     "sec-ch-ua-model": "",
                     "sec-ch-prefers-color-scheme": "light",
                     "sec-ch-ua-platform": "\"Linux\"",
                     "accept": "*/*",
                     "origin": "https://www.threads.com",
                     "sec-fetch-site": "same-origin",
                     "sec-fetch-mode": "cors",
                     "sec-fetch-dest": "empty",
                     "referer": "https://www.threads.com/",
                     "accept-encoding": "gzip, deflate",
                     "accept-language": "id-ID,id;q=0.9",
                    "x-fb-friendly-name": "useBarcelonaEditProfileMutation",
                    "x-csrftoken": re.search(r'csrftoken=(.*?);', str(cookies)).group(1),
                    "x-bloks-version-id": "52fc1652455c0b437eef96decb69daa97f8db556a0db2cab5cd842c2accea603",
                    "x-ig-app-id": "238260118697367",
                    "x-fb-lsd": data.get('fb_dtsg'),
                    "x-asbd-id": "359341"
                }
                response2 = r.post('https://www.threads.com/graphql/query',data=data, headers=headers, cookies={'cookie':cookies})
                if response2.status_code == 200:
                    try:
                        print(f'\n[•] Bio Berhasil Di Tambahkan\n[•] Teks: {biography}')
                        exit()
                    except (Exception) as e:
                        exit(f'[•] Bio Error: {str(e).title()}')
                else:
                    return False
            except (Exception) as e:
                exit(f'[•] Error: {str(e).title()}')
                
    def posting_utas_threads(self, cookies, text, url = 'https://www.threads.com'):
        with requests.Session() as r:
            try:
                response = r.get(url, cookies = {'cookie':cookies}).text
                data = {
                    "av": re.search('{"actorID":"(\d+)"', str(response)).group(1),
                    "__user": re.search('{"actorID":"(\d+)"', str(response)).group(1),
                    "__a": "1",
                    "__req": "a",
                    "__hs": re.search('"haste_session":"(.*?)"', str(response)).group(1),
                    "dpr": "3",
                    "__ccg": re.search('"connectionClass":"(.*?)"',str(response)).group(1),
                    "__rev": "1025731959",
                    "__s": "h21p0t:2ugba4:bs6w13",
                    "__hsi": re.search('"hsi":"(\d+)"', str(response)).group(1),
                    "__dyn": "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awgo9oO0n24oaEd82lwv89k2C1Fwc60D85m1mzXwae4UaEW0Loco5G0zK5o4q0HU1IEGdwtU2ewbS1LwTwKG0hq1Iwqo9Epxq261bg5q2-2K7E4u48jgbVE-19xW1Vwn85SU7y",
                    "__csr": "iMYxA-AgBOROnNfTEN-AoBHWWnIyAGqchkvByFVauWAADoSmi5UnwzACXw05-_Ki9x2i09AIM7m0ol6J0bq1l5P0PwuQ1WUy1Y30K9go6o5vUbo6C0kG0pl6xq2F04FiGWy8B01B-Unw1d-0BooOyAu9yl2E9o5O2e2O7o0yC0OAA1Vo1dUrwJU3awHAzjG5k4VcMgxyku3632tN8qxx7kwdEaU2Hzqm0u2kIi0tb4xG2W6e4QcwXy8yiEy9kaxy0A8kooQ",
                    "__hsdp": "i84Q4G8x41q5cErcba6xA4isiwWMqR2wRtA0wF7qxmqBAl2hp8cpFML2Y-SgQAv84qwBhUCycNjE4Eqgui70AxldyCd83Fnfhu3KTKbxGcAABXwn9E3FU2lwoUd8aonwiE8k0SEeE88fm6Edouw7Yw",
                    "__hblp": "0Mg1jU8qwmd0HwlkcxW0DUp-cwIG2S10wwyoK7EKaByXz8pwBx62q2a5onCK485O14w7swFxujG68O4bBXxJ4wLzEa898rG7EG9UbE88aotxai2Z1W0vO",
                    "__sjsp": "i84Q4G8Dq0mxyG6P2OxEp14D4EeI6JgE4dwhUB1y9glw",
                    "__comet_req": re.search('__comet_req=(\d+)', str(response)).group(1),
                    "fb_dtsg": re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(response)).group(1),
                    "jazoest": re.search('jazoest=(\d+)', str(response)).group(1),
                    "lsd": re.search('"LSD",\[\],{"token":"(.*?)"',str(response)).group(1),
                    "__spin_r": re.search('"__spin_r":(\d+)', str(response)).group(1),
                    "__spin_b": re.search('"__spin_b":"(.*?)"',str(response)).group(1),
                    "__spin_t": re.search('"__spin_t":(\d+)', str(response)).group(1),
                    "audience": "default",
                    "barcelona_source_reply_id": "",
                    "caption": text,
                    "creator_geo_gating_info": json.dumps({"whitelist_country_codes":[]}),
                    "custom_accessibility_caption": "",
                    "gen_ai_detection_method": "",
                    "internal_features": "",
                    "is_meta_only_post": "",
                    "is_paid_partnership": "",
                    "is_upload_type_override_allowed": "1",
                    "publish_mode": "text_post",
                    "text_post_app_info": "{\"entry_point\":\"top_of_profile\",\"excluded_inline_media_ids\":\"[]\",\"fediverse_composer_enabled\":true,\"is_spoiler_media\":false,\"link_attachment_url\":null,\"reply_control\":0,\"self_thread_context_id\":\"b3566216-9d48-433e-abf6-f0012d0f31d5\",\"snippet_attachment\":null,\"special_effects_enabled_str\":null,\"tag_header\":null,\"text_with_entities\":{\"entities\":[],\"text\":\"'"+text+"'\"}}",
                    "upload_id": re.search('{"actorID":"(\d+)"', str(response)).group(1)
                }
                
                headers = {
                    "authority": "www.threads.com",
                    "content-length": "336185",
                    "sec-ch-ua": "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
                    "offset": "0",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                    "sec-ch-ua-platform-version": "",
                    "x-entity-length": "336185",
                     "sec-ch-ua-full-version-list": "\"Chromium\";v=\"107.0.5304.74\", \"Not=A?Brand\";v=\"24.0.0.0\"",
                     "sec-ch-ua-model": "",
                     "sec-ch-prefers-color-scheme": "light",
                     "sec-ch-ua-platform": "\"Linux\"",
                     "accept": "*/*",
                     "origin": "https://www.threads.com",
                     "sec-fetch-site": "same-origin",
                     "sec-fetch-mode": "cors",
                     "sec-fetch-dest": "empty",
                     "referer": "https://www.threads.com/",
                     "accept-encoding": "gzip, deflate",
                     "accept-language": "id-ID,id;q=0.9",
                    "x-ig-app-id": "238260118697367",                   
                    "x-csrftoken": re.search(r'csrftoken=(.*?);', str(cookies)).group(1),
                    "x-bloks-version-id": "52fc1652455c0b437eef96decb69daa97f8db556a0db2cab5cd842c2accea603",
                    "x-fb-lsd": data.get('fb_dtsg'),
                    "x-asbd-id": "359341"
                }
                response2 = r.post('https://www.threads.com/api/v1/media/configure_text_only_post/', data=data, headers=headers, cookies={'cookie':cookies})
                if response2.status_code == 200:
                    try:
                        print(f'\n [•] Berhasil Mengunggah Postingan\n [•] Teks: {text}')
                        exit()
                    except (Exception) as e:
                        exit(f' [•] Postingan Error: {str(e).title()}')
                else:
                    return False
            except (Exception) as e:
                exit(f'[•] Error: {str(e).title()}')
     
        