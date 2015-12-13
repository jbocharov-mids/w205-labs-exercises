import tweepy

consumer_key = "cb9gP6H7S00JvScNtkLrg1h2Y";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "INwEuKXY12XF2x1aALRMywmeHYECjGbqhz0RZRUKPmz3NCF5L0";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "2992703154-Umvt413O1IQMG70Up8QJYtJu4XikuXO2gvcGajm";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "xxbYD2KCuvQhDNMwhiOHtOX20GzDbqXCMQnsoY1DGhn8J";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



