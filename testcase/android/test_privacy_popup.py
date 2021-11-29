import time
from krunner.utils import logger
from krunner.utils import adb
from krunner.conf import get_config_value

from pageobjects.android.privacy_popup import PrivacyPopup
from testcase.krunner import KRunner


class TestPrivacyPopup(KRunner):
    """快手隐私弹窗测试"""

    def setUp(self):
        self.driver.stop_watcher()
        adb.clear_app_data(get_config_value('serialno')[0], get_config_value('pkg_name'))
        time.sleep(5)
        adb.start_schema(get_config_value('serialno')[0], get_config_value('home_scheme'))
        time.sleep(5)

    def test_agree(self):
        """测试同意按钮"""
        logger.info('测试隐私弹窗上的同意按钮')
        time.sleep(10)
        assert PrivacyPopup.agree_button.exist(5)
        PrivacyPopup.agree_button.click()
        time.sleep(2)
        assert not PrivacyPopup.agree_button.exist()

    def test_disagree_and_enter_visitor(self):
        """测试不同意，进入访客模式按钮"""
        logger.info('测试隐私弹窗上的「不同意，并进入访客模式」按钮（9.11.10 版本推全）')
        time.sleep(10)
        assert PrivacyPopup.disagree_button.exist(5)
        PrivacyPopup.disagree_button.click()
        time.sleep(2)
        assert not PrivacyPopup.agree_button.exist()
