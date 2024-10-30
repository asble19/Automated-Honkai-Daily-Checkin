import requests, json


url = "https://sg-public-api.hoyolab.com/event/mani/sign?lang=en-us"


payload ='{"act_id": "e202110291205111"}'


header = {"Cookie":"mi18nLang=en-us; DEVICEFP_SEED_ID=c33e87c99ba17ab0; DEVICEFP_SEED_TIME=1686882125354; HYV_LOGIN_PLATFORM_OPTIONAL_AGREEMENT={%22content%22:[]}; account_mid_v2=11vfkjx265_hy; account_id_v2=74171044; HYV_LOGIN_PLATFORM_LOAD_TIMEOUT={}; hoyolab_color_scheme=system; _ga_GEYW4HC0FV=GS1.1.1706569873.1.0.1706569873.0.0.0; _ga_PDXBNGQFCP=GS1.1.1706569873.1.1.1706569873.0.0.0; _ga_HR3ZEH2708=GS1.1.1706570054.1.1.1706570077.0.0.0; _ga_RJQB3V8EQN=GS1.1.1706570054.1.1.1706570077.0.0.0; _ga_JTLS2F53NR=GS1.1.1706569760.1.1.1706570255.0.0.0; _ga_GFC5HN79FG=GS1.1.1706569762.1.1.1706570255.0.0.0; DEVICEFP=38d7f1ec88c57; cookie_token_v2=v2_CAQSDGNlMXRidXdiMDB6axokOWQxMWI3OTItMGIzOC00Nzg5LWI0MTAtZmE1YmNiZDkzYjYxIMXi1bYGKOWgktwDMKSFryNCC2hrNGVfZ2xvYmFs.RXHVZgAAAAAB.MEUCIQCsN0aQ34XfPENse0wmGyz8-91LFubsEVflAkM1viwp3QIgRpGXcqEavpvsqmtFmZ5b8Tvyv7s2hzFuvAyVlZ7L0zw; ltmid_v2=11vfkjx265_hy; ltuid_v2=74171044; ltoken_v2=v2_CAISATAg3ZXYtgYorInYPzCkha8jQgphY2NvdW50X29z.3QrWZgAAAAAB.MEUCIQCnLeB-Ev5kuLafuyVQpmYEV2jYek3L4mvONmSAsko9EQIgNCV7d1qpVlCW2MnobGyemkL-7awPpIIcVPVBqSlgA9g; _HYVUUID=cafab12f-8720-4c9d-acfb-7d3192ad81a7; _MHYUUID=e58320d5-bac5-4aa9-a80c-28e4a8f4167c; _gid=GA1.2.1637988997.1730301848; _ga_54PBK3QDF4=GS1.1.1730309696.2.1.1730309768.0.0.0; _ga_T9HTWX7777=GS1.1.1730309696.2.1.1730309768.0.0.0; HYV_LOGIN_PLATFORM_TRACKING_MAP={%22sourceValue%22:%22144%22}; HYV_LOGIN_PLATFORM_LIFECYCLE_ID={%22value%22:%22dedb0636-529d-4147-91c3-32394a3a2bb4%22}; _ga=GA1.1.1683963661.1686882126; _ga_45QSFFBGJT=GS1.1.1730309984.1.1.1730310440.0.0.0; _gat_gtag_UA_200790024_1=1; _ga_HF7DEW0H6V=GS1.1.1730309984.1.1.1730310440.0.0.0",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
"Origin":"https://act.hoyolab.com",
"Referer":"https://act.hoyolab.com/"
}


response_decoded_json = requests.post(url, data=payload, headers=header)
response_json = response_decoded_json.json()
 
print(response_json)