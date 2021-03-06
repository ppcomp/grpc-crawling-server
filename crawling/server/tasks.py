from __future__ import absolute_import, unicode_literals
import logging, sys, os
from typing import List, Tuple, Dict, TYPE_CHECKING
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# from celery import Celery
# from celery.schedules import crontab
from billiard.context import Process
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.settings import Settings

from crawler.crawler.spiders import crawl_spider

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

def get_scrapy_settings():
    scrapy_settings = Settings()
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'crawler.crawler.settings'
    settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
    scrapy_settings.setmodule(settings_module_path, priority='project')
    return scrapy_settings

def crawling_start(scrapy_settings: Settings, spiders: List[object]) -> List[Dict]:
    process = CrawlerProcess(scrapy_settings)
    crawler_list = []
    for spider in spiders:
        crawler = process.create_crawler(spider)
        crawler_list.append(crawler)
        process.crawl(crawler)
    process.start()

    stats_dic_list = []
    for crawler in crawler_list:
        # stats = crawler.stats   # <class 'scrapy.statscollectors.MemoryStatsCollector'>
        stats = crawler.stats.get_stats()   # <class 'dict'>
        stats_dic_list.append(stats)
    return stats_dic_list

def crawling(board_name, page_num):
    invalid_board_name = True
    if board_name:
        board = f"{board_name.capitalize()}Spider"
        for i in range(len(spiders)):
            if spiders[i].__name__ == board:
                spider_arg = [spiders[i]]
                invalid_board_name = False
                break
    else:
        spider_arg = spiders

    if invalid_board_name and board_name:
        message = "Invalid board name. Request with correct board name to initialize Database."
        result_code = 1
    else:
        scrapy_settings = get_scrapy_settings()
        crawl_spider.page_num = page_num
        proc = Process(
            target=crawling_start, 
            args=(
                scrapy_settings,
                spider_arg,
            )
        )
        proc.start()
        proc.join()
        message = "Success."
        result_code = 0
    return result_code, message