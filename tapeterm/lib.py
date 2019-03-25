import json, os, signal, zipfile, datetime, selenium, subprocess, time, re, requests, shutil
from six.moves.urllib.request import urlretrieve
from selenium import webdriver
from tqdm import tqdm

HOME = os.environ['HOME']
BASE_URL_EN = 'http://www.casetophono.com/'
BASE_URL_EL = 'http://www.kasetophono.com/'
CONFIG_FOLDER = os.path.join(HOME, '.tapeterm')
CHROMEDRIVER = os.path.join(CONFIG_FOLDER, 'chromedriver')


class TapeLib(object):
    """
    This Class will retrieve the playlists from the kasetophono website
    """
    def __init__(self, lang='en'):
        """
        Constructo
        :param lang: language version
        """
        assert lang in ('en', 'el'), 'Given language is not supported'
        self.lang = lang
        self.JSON = os.path.join(CONFIG_FOLDER, 'config_{}.json'.format(lang))
        self.dr = None
        if not (os.path.exists(CHROMEDRIVER) and os.path.exists(self.JSON)):
            self.set_up()
        if not (os.path.exists(CHROMEDRIVER) and os.path.exists(self.JSON)):
            raise RuntimeError('''
            chromedriver: {}
            config json: {}
            '''.format(
                'OK' if os.path.exists(CHROMEDRIVER) else 'MISSING',
                'OK' if os.path.exists(self.JSON) else 'MISSING',
            ))
        if self.lang == 'EL':
            self.BASE_URL = BASE_URL_EL[:]
        else:
            self.BASE_URL = BASE_URL_EN[:]

    def set_up(self):
        """
        Set up scraping dependencies like selenium
        :return: nada
        """
        latest = None
        if not os.path.exists(CONFIG_FOLDER):
            os.mkdir(CONFIG_FOLDER)
        if not os.path.exists(os.path.join(CONFIG_FOLDER, 'chromedriver')):
            r = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE')
            latest = r.text.strip()

            file_n = os.path.join(CONFIG_FOLDER, 'chromedriver.zip')
            dest_dir = CONFIG_FOLDER
            urlretrieve('https://chromedriver.storage.googleapis.com/%s/chromedriver_linux64.zip' % latest, file_n)
            with zipfile.ZipFile(file_n) as z:
                z.extractall(dest_dir)
            os.remove(file_n)
            subprocess.call(['chmod', 'u+x', CHROMEDRIVER])
        if not os.path.exists(
            os.path.join(
                CONFIG_FOLDER,
                'config_en.json'
            )
        ):
            shutil.copy('config_en.json', os.path.join(CONFIG_FOLDER, 'config_en.json'))
        if not os.path.exists(
            os.path.join(
                CONFIG_FOLDER,
                'config_el.json'
            )
        ):
            shutil.copy('config_el.json', os.path.join(CONFIG_FOLDER, 'config_el.json'))
        with open(self.JSON, 'w') as f:
            json.dump({
                'meta': {
                    'last_update': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'chromedriver_v': latest,
                    'os': 'Linux',
                }
            }, f)

    def set_driver(self):
        """
        Set up headless brwoser
        :return: nada
        """
        assert self.dr is None
        assert os.path.exists(CHROMEDRIVER)
        self.opts = webdriver.ChromeOptions()
        self.opts.add_argument('--headless')
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.opts.add_experimental_option("prefs", prefs)
        self.dr = webdriver.Chrome(CHROMEDRIVER, chrome_options=self.opts)

    def write_json(self, data={}, filename=None):
        """
        Write json file in the config directory
        :param data: json data
        :param filename: filename
        :return: nada
        """
        if filename is None:
            filename = self.JSON[:]
        else:
            pass
        assert len(data)>0
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def read_json(self):
        """
        Read Config JSON FILE
        :return: nada
        """
        assert os.path.exists(self.JSON)
        with open(self.JSON, 'r') as f:
            self.data = json.load(f)

    def close_driver(self):
        self.dr.close()
        self.dr.service.process.send_signal(signal.SIGTERM)
        self.dr.quit()

    def get_home(self):
        if not isinstance(self.dr, selenium.webdriver.chrome.webdriver.WebDriver):
            self.set_driver()
        assert isinstance(self.dr, selenium.webdriver.chrome.webdriver.WebDriver)

        self.dr.get(self.BASE_URL)

        cat_x = '//*[@id="nav2"]/li'
        cat_elems = self.dr.find_elements_by_xpath(cat_x)

        struct_url = {}


        for cat_elem in cat_elems[:]:
            master_name = cat_elem.find_element_by_xpath('./a').get_attribute('text')
            struct_url[master_name] = {}

            sub = cat_elem.find_elements_by_xpath('./ul/li/a')


            for _ in sub[:]:
                struct_url[master_name][_.get_attribute('text')] = _.get_attribute('href')


        all_urls = {}

        for cat, subs in tqdm(struct_url.items()):
            all_urls[cat] = {}
            for sub, subsub in tqdm(struct_url.items()):
                for name, url in subsub.items():

                    all_urls[cat][sub] = {}
                    self.dr.get(url)

                    self.dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(1)
                    next = self.dr.find_elements_by_xpath('//*/div[@class="morepost bounce"]/a')
                    while next:
                        try:
                            next[0].click()
                            time.sleep(1.5)
                        except:
                            break
                    for _ in self.dr.find_elements_by_xpath('//*/h2[@class="related-posts-title"]/a'):
                        all_urls[cat][sub][_.get_attribute('text').strip()] = _.get_attribute('href')

        for cat, subs in tqdm(all_urls.items()):
            for sub, subsub in tqdm(subs.items()):
                for name, url in tqdm(subsub.items()):

                    if url:
                        self.dr.get(url)
                        pl_el = self.dr.find_element_by_xpath('//iframe[contains(@src, "youtube")]')

                        all_urls[cat][sub][name] = self.get_plid_from_url(pl_el.get_attribute('src'))
                        self.write_json(all_urls)
        self.close_driver()

    @staticmethod
    def get_plid_from_url(url):
        """
        Get youtube playlist id from url
        :param url: kasetophono url
        :return: youtube playlist url
        """
        for _ in re.findall('list=([\w\-_]+)', url):
            return _