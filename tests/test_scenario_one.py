from pages.sbis_contacts import SbisContactsPage


class TestSbisContactsPage:
    def test_pic_sizes(self, browser):
        page = SbisContactsPage(browser)

        page.open()
        page.click_clients_button()
        page.click_anchor_to_pic()

        pic1_height, pic1_width = page.get_pic_size(1)
        pic2_height, pic2_width = page.get_pic_size(2)
        pic3_height, pic3_width = page.get_pic_size(3)
        pic4_height, pic4_width = page.get_pic_size(4)

        assert pic1_width == pic2_width == pic3_width == pic4_width, 'pic width все плохо'
        assert pic1_height == pic2_height == pic3_height == pic4_height, 'pic height все плохо'



