# coding:utf-8

import unittest
from fuga import Fuga

class HogeTest(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def test_first(self):
        print('test_first')

    def test_fuga(self):
        fuga = Fuga()
        self.assertTrue(fuga.index())
        self.assertEqual(fuga.judge('伊達市','喫茶店','いいぜ'),'coffee')
        self.assertEqual(fuga.judge('アテン厨','パズドラ','変な'),'ビーフカレー')
        self.assertEqual(fuga.judge('ムーニーマン','15時起き','あれ'),'泡盛')
        self.assertEqual(fuga.judge('チンアナゴ先輩','ドミニオン','聞いてないんだがぁ'),'ブッチャー')

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(HogeTest))
    return suite