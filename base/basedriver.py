class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def scroll(self):
        pagelength = self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight); var '
                                                'pagelength=document.body.scrollTo; return '
                                                'document.body.scrollHeight')
        flag = False
        while not flag:
            lastcount = pagelength
            pagelength = self.driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight); var pagelength=document.body.scrollTo; return '
                'document.body.scrollHeight')
            if lastcount == pagelength:
                flag = True
