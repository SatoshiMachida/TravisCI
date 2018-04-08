class Fuga:

    def __init__(self):
        self.FUJITA_POINT=0
        self.DATESI_POINT=0
        self.KUWABA_POINT=0
    
    def index(self):
        return True
        
    def recommendDrinkGenerator(self):
        print ('あなたの名前を入力してください。')
        input_test_name = raw_input('>>>  ')
        print ('あなたの趣味を入力してください。')
        input_test_hobby = raw_input('>>>  ')
        print ('あなたの口癖を入力してください。')
        input_test_speak = raw_input('>>>  ')

        print ('あなたへのおすすめは' + judge(input_test_name, input_test_hobby, input_test_speak) + 'です。')
        
    def checkName(self, name):
        if name in ['Fujita', 'F', '藤田', 'wotsushi', 'Wotsushi', 'W', 'あれ', 'これ', 'それ', '変な', '神', '太陽神', '中本', 'ムーニー', 'ムーニーマン']:
            self.FUJITA_POINT+=10
        elif name in ['Iwadate', 'I', '岩舘', 'だて', 'date', '伊達市', 'D', 'ヒュゥ', 'シュゥ', 'アァ', '謀略神', '命名神', '第4位', 'マヨネーズLOVE']:
            self.DATESI_POINT+=10
        elif name in ['Kuwabara' ,'K', '桑原', 'KuwabaraK', 'くわ', '煽り魔', 'ヤダヤダヤダヤダ', 'アテン厨', '浦飯交換所', 'ハァア～', 'モンハンプロ']:
            self.KUWABA_POINT+=10

    def checkHobby(self, hobby):
        if hobby in ['水泳', '最適化', 'python', '弁当', '艦これ', '辛いもの', 'ムーニーマン']:
            self.FUJITA_POINT+=7
        elif hobby in ['喫茶店', 'rails', '残業', '散歩', 'SAO', '禁書目録', '超電磁砲']:
            self.DATESI_POINT+=7
        elif hobby in ['モンハン', 'ネトゲ', '卓球', '15時起き', '使わない自動車']:
            self.KUWABA_POINT+=7
        elif hobby in ['パズドラ' ,'ドミニオン']:
            self.FUJITA_POINT+=5
            self.DATESI_POINT+=5
            self.KUWABA_POINT+=5            

    def checkSpeak(self, speak):
        if speak in ['あれ', 'これ', 'それ', '変な', 'スコヴィル値']:
            self.FUJITA_POINT+=4
        elif speak in ['ヒュゥ', 'シュゥ', 'アァ', 'フゥ', 'いいぜ']:
            self.DATESI_POINT+=4
        elif speak in ['ヤダヤダヤダヤダ', 'は？', 'それはないっしょ', 'ハァア～', '聞いてないんだがぁ']:
            self.KUWABA_POINT+=4

    def judge(self, name, hobby, speak):
        self.FUJITA_POINT=0
        self.DATESI_POINT=0
        self.KUWABA_POINT=0
        self.checkName(name)
        self.checkHobby(hobby)
        self.checkSpeak(speak)
        if self.FUJITA_POINT >= 15:
            return '泡盛'
        elif self.DATESI_POINT >= 15:
            return 'coffee'
        elif self.KUWABA_POINT >= 15:
            return 'ビーフカレー'
        else:
            return 'ブッチャー'