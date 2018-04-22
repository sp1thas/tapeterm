import json, os, signal, requests, zipfile, datetime, selenium, subprocess, time
from urllib import urlretrieve
from tempfile import mktemp
from selenium import webdriver
from pprint import pprint
from tqdm import tqdm

HOME = os.environ['HOME']
BASE_URL_EN = 'http://www.casetophono.com/'
BASE_URL_GR = 'http://www.kasetophono.com/'
CONFIG_FOLDER = os.path.join(HOME, '.tapeterm')
JSON = os.path.join(CONFIG_FOLDER, 'config.json')
CHROMEDRIVER = os.path.join(CONFIG_FOLDER, 'chromedriver')


class TapeLib():

    def __init__(self):
        self.dr = None
        if not (os.path.exists(CHROMEDRIVER) and os.path.exists(JSON)):
            self.set_up()

    def set_up(self):
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


        with open(JSON, 'w') as f:
            json.dump({
                'meta': {
                    'last_update': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'chromedriver_v': latest,
                    'os': 'Linux',
                }
            }, f)

    def set_driver(self):
        assert self.dr is None
        assert os.path.exists(CHROMEDRIVER)
        self.dr = webdriver.Chrome(CHROMEDRIVER)

    def write_json(self, data={}):
        assert len(data)>0
        with open(JSON, 'w') as f:
            json.dump(data, f)

    def read_json(self):
        """
        Read Config JSON FILE
        :param filepath:
        :return:
        """
        assert os.path.exists(JSON)
        with open(JSON, 'r') as f:
            return json.load(f)

    def close_driver(self):
        self.dr.close()
        self.dr.service.process.send_signal(signal.SIGTERM)
        self.dr.quit()

    def get_home(self):
        assert isinstance(self.dr, selenium.webdriver.chrome.webdriver.WebDriver)

        self.dr.get(BASE_URL_EN)

        cat_x = '//*[@id="nav2"]/li'
        cat_elems = self.dr.find_elements_by_xpath(cat_x)

        struct_url = {}


        for cat_elem in cat_elems[1:-1]:
            master_name = cat_elem.find_element_by_xpath('./a').get_attribute('text')
            struct_url[master_name] = {}

            sub = cat_elem.find_elements_by_xpath('./ul/li/a')


            for _ in sub:
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
                    while(next):
                        try:
                            next[0].click()
                            time.sleep(1.5)
                        except:
                            break
                    for _ in self.dr.find_elements_by_xpath('//*/h2[@class="related-posts-title"]/a'):
                        all_urls[cat][sub][_.get_attribute('text').strip()] = _.get_attribute('href')


        print('lets got get playlist urls')

        for cat, subs in tqdm(all_urls.items()):
            for sub, subsub in tqdm(subs.items()):
                for name, url in tqdm(subsub.items()):

                    if url:
                        self.dr.get(url)
                        pl_el = self.dr.find_element_by_xpath('//*/div[@class="post-body entry-content"]/div/div[2]/iframe')

                        all_urls[cat][sub][name] = pl_el.get_attribute('src')
                        self.write_json(all_urls)
                        return
        pprint(all_urls)