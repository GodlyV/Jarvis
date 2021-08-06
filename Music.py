from selenium import webdriver


# TODO: Log into your own chrome account before searching up the song.
class music():
    #Setting up the chromium path

    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\james\.wdm\drivers\chromedriver\win32\92.0.4515.107\chromedriver.exe")
    #play the music
    def play(self,name):
        self.name = name
        self.driver.get(url="https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
        accountLogin = self.driver.find_element_by_xpath('//*[@id="tgnCOd"]')
        accountLogin.click()

        #self.driver.get(url="https://www.youtube.com/results?search_query=" + name)
        #Clicking on the video title to play the video
        #video = self.driver.find_element_by_xpath('//*[@id="title-wrapper"]')
        #video.click()


#testing the music class
bot = music()
bot.play("rick and morty season 1 ep 1")