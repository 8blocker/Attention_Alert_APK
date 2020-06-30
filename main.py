from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import tweepy

key = "1250112852452671490-Y9AgYYo8Kcwq9aGnGF9UVj0niEYf9G"
secret = "KE5bIOUC7qOsOocwe8VOBrZ4gMy7dccPXe1mPFBuq3KSm"
consumer_key = "wiF2RewCTvtJGFB9pFEUnC6uF"
consumer_secret = "qquz5Vw1NMNmoqjzBZDjnnh1qj8e60nvKnSxUoh1mMvgZYK1rF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return Launch()

class Launch(FloatLayout):
    def message_me(self):
        api.send_direct_message(850712539235319808, "I NEED ATTENTION!")

if __name__ == "__main__":
    MyApp().run()