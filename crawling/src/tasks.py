from __future__ import absolute_import, unicode_literals
import logging, sys, os, json
from typing import List, Tuple, Dict, TYPE_CHECKING
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from celery import Celery
# from celery.schedules import crontab
import billiard
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings

from .crawler.crawler.spiders import crawl_spider

spiders = [
    # crawl_spider에 게시판 크롤링 class 생성 후 이 곳에 추가.
    # 이 곳에 있는 게시판(class)을 대상으로 crawling됨.
    crawl_spider.MainSpider,
    crawl_spider.CseSpider,
    crawl_spider.CbaSpider,
    # crawl_spider.BizSpider, 
    crawl_spider.AccountSpider,
    crawl_spider.EconomicsSpider,
    # crawl_spider.StatisticsSpider,
    crawl_spider.TourismSpider,
    crawl_spider.ItbSpider,
    # crawl_spider.KnucalsSpider,
    # crawl_spider.CllSpider,
    crawl_spider.BseSpider,
    crawl_spider.FoodtechSpider,
    crawl_spider.AppliedplantSpider,
    crawl_spider.ApplybioSpider,
    crawl_spider.HortiSpider,
    crawl_spider.AgeconSpider,
    crawl_spider.AedSpider,
    crawl_spider.DbeSpider,
    # crawl_spider.EcoenvSpider,
    # crawl_spider.CalsSpider,
    # crawl_spider.AnimalSpider,
    crawl_spider.ApplanimalsciSpider,
    crawl_spider.AniscienceSpider,
    crawl_spider.AceSpider,
    # crawl_spider.ArchitectureSpider,
    crawl_spider.ArchiSpider,
    crawl_spider.CivilSpider,
    crawl_spider.EnvironSpider,
    crawl_spider.MechanicalSpider,
    crawl_spider.MechaSpider,
    crawl_spider.MaterialSpider,
    crawl_spider.EnreSpider,
    crawl_spider.SmeSpider,
    crawl_spider.ChemengSpider,
    crawl_spider.BioengSpider,
    crawl_spider.DesignSpider,
    crawl_spider.KangwonartSpider,
    crawl_spider.SportSpider,
    crawl_spider.VcultureSpider,
    # crawl_spider.EducatioSpider,
    # crawl_spider.HomecsSpider,
    # crawl_spider.ScieduSpider,
    # crawl_spider.EduSpider,
    # crawl_spider.KoreduSpider,
    # crawl_spider.MatheduSpider,
    crawl_spider.HistorySpider,
    # crawl_spider.EngeduSpider,
    # crawl_spider.EthicseduSpider,
    # crawl_spider.SseduSpider,
    # crawl_spider.GeoeduSpider,
    # crawl_spider.PhyeduSpider,
    # crawl_spider.CceduSpider,
    crawl_spider.SocialSpider,
    # crawl_spider.AnthroSpider,
    # crawl_spider.Re1978Spider,
    # crawl_spider.SociologySpider,
    # crawl_spider.MasscomSpider,
    crawl_spider.PoliticsSpider,
    crawl_spider.PadmSpider,
    crawl_spider.PsychSpider,
    crawl_spider.ForestSpider,
    crawl_spider.FmSpider,
    # crawl_spider.ForestrySpider,
    # crawl_spider.FepSpider,
    crawl_spider.WoodSpider,
    # crawl_spider.PaperSpider,
    crawl_spider.LandsSpider,
    # crawl_spider.VetmedSpider,
    crawl_spider.PharmacySpider,
    crawl_spider.NurseSpider,
    # crawl_spider.BmcollegeSpider,
    crawl_spider.MolscienSpider,
    crawl_spider.Bio_healthSpider,
    crawl_spider.BmeSpider,
    crawl_spider.SiSpider,
    crawl_spider.DmbtSpider,
    crawl_spider.ItSpider,
    # crawl_spider.KoreanSpider,
    crawl_spider.EnglishSpider,
    # crawl_spider.FranceSpider,
    crawl_spider.GermanSpider,
    # crawl_spider.ChineseSpider,
    # crawl_spider.JapanSpider,
    crawl_spider.KnuhistoSpider,
    crawl_spider.PhysicsSpider,
    crawl_spider.BiologySpider,
    crawl_spider.MathSpider,
    crawl_spider.GeologySpider,
    crawl_spider.GeophysicsSpider,
    crawl_spider.BiochemSpider,
    # crawl_spider.ChemisSpider,
    crawl_spider.EeeSpider,
    crawl_spider.EeSpider,
    crawl_spider.MultimajorSpider,
    crawl_spider.LiberalSpider,
]

class CustomCrawler:

    def __init__(self):
        self.output = None

    def _yield_output(self, data):
        self.output = data

    def _crawling_start(
            self, 
            scrapy_settings: Settings, 
            spider: object, 
            board_name: str, 
            return_dic:Dict) -> Dict:
        process = CrawlerProcess(scrapy_settings)
        crawler = process.create_crawler(spider)
        process.crawl(crawler, args={'callback': self._yield_output})
        process.start()
        return_dic[board_name] = self.output

        # stats = crawler.stats   # <class 'scrapy.statscollectors.MemoryStatsCollector'>
        stats = crawler.stats.get_stats()   # <class 'dict'>
        return stats

    def get_scrapy_settings(self):
        scrapy_settings = Settings()
        os.environ['SCRAPY_SETTINGS_MODULE'] = 'src.crawler.crawler.settings'
        settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
        scrapy_settings.setmodule(settings_module_path, priority='project')
        return scrapy_settings

    def crawl(self, board_name, page_num):
        invalid_board_name = True
        spider_arg = None
        if board_name:
            board = f"{board_name.capitalize()}Spider"
            for i in range(len(spiders)):
                if spiders[i].__name__ == board:
                    spider_arg = [spiders[i]]
                    invalid_board_name = False
                    break
        else:
            spider_arg = spiders

        self.manager = billiard.Manager()
        return_dic = self.manager.dict()
        if invalid_board_name and board_name:
            message = "Invalid board name. Request with correct board name to initialize Database."
            result_code = 1
            return_dic["empty"] = ""
        else:
            scrapy_settings = self.get_scrapy_settings()
            crawl_spider.page_num = page_num
            proc_list = []
            for spider in spider_arg:
                proc = billiard.context.Process(
                    target=self._crawling_start, 
                    args=(
                        scrapy_settings,
                        spider,
                        board_name,
                        return_dic,
                    )
                )
                proc.start()
                proc_list.append(proc)
            for proc in proc_list:
                proc.join()
            message = "Success."
            result_code = 0
        res = dict()
        res["result_code"] = result_code
        res["message"] = message
        res["output"] =  json.dumps(dict(return_dic))
        return res