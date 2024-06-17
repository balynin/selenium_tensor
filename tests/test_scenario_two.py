from pages.sbis_contacts import SbisContactsPage
import time
import logging

LOGGER = logging.getLogger(__name__)

class TestSbisContactsPage:
    def test_region_navigation(self, browser):
        page = SbisContactsPage(browser)

        page.open()
        current_url_69reg = page.get_current_url()
        assert current_url_69reg == 'https://sbis.ru/contacts/69-tverskaya-oblast?tab=clients'

        page.click_anchor_to_region()
        time.sleep(3)
        page.select_region(43)
        time.sleep(3)
        current_url_41reg = page.get_current_url()
        assert current_url_41reg == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'

        LOGGER.critical('test pass all fine')


