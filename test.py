import requests
import time

BASE = 'http://127.0.0.1:8080/'

print('_____________________________________________________')
print('Inserting headlines')

data = [
    {
  "source":"The Verge",
 "author": "Dan Seifert",
 "title": "The phone enthusiast\u2019s buying guide",
 "description": "This isn\u2019t your average phone buying guide, this is for the die-hards, the ones who want to make a questionable purchase not because it\u2019s practical or logical, but because it\u2019s a new toy to play with. Whether you fancy folding phones, high-end Android flagshi\u2026",
 "url": "https://www.theverge.com/22451975/phone-buying-guide-enthusiasts-nerds",
 "urlToImage": "https://cdn.vox-cdn.com/thumbor/zftCNpmI1resIJU1xhnE_UjN9Sk=/0x119:6058x3291/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22541475/DSCF5519.jpg",
 "publishedAt": "2021-05-28T13:00:00Z",
 "content": "If you buy something from a Verge link, Vox Media may earn a commission. See our ethics statement.There are plenty of buying guides for figuring out the best phone to buy at a given time, across a wi\u2026 [+10059 chars]"

    },
{
            "source": "The Verge",
            "author": "Cameron Faulkner",
            "title": "Nomad\u2019s Base Station Pro is back down to its lowest price this weekend",
            "description": "Nomad is knocking $100 off the cost of its Base Station Pro Qi wireless charging pad through Saturday, May 29th. Normally $200, you can pick one up for $100. You can also save on Apple USB-C charging products from Daily Steals.",
            "url": "https://www.theverge.com/good-deals/2021/5/28/22456723/nomad-base-station-pro-qi-charger-pad-playstation-gift-card-deal-sale",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/IP3LCdsx3X1sUiYsDlfGBuHwYag=/0x146:2040x1214/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/21813013/cgartenberg_200824_4157_0005.0.jpg",
            "publishedAt": "2021-05-28T12:58:52Z",
            "content": "Recently updated with improved iPhone 12 charging\r\nIf you buy something from a Verge link, Vox Media may earn a commission. See our ethics statement.\r\nThe Base Station Pro can recharge up to three de\u2026 [+4622 chars]"
        },
        {
            "source": "The Verge",
            "author": "Jon Porter",
            "title": "Microsoft warns of \u2018sophisticated\u2019 Russian email attack targeting government agencies",
            "description": "Microsoft has raised the alarm over a \u201csophisticated\u201d ongoing cyberattack from the same Russian-linked hackers behind the SolarWinds hack. Around 3,000 email accounts are believed to have been targeted across 150 organizations.",
            "url": "https://www.theverge.com/2021/5/28/22458202/microsoft-nobelium-hack-usaid-email-phishing-hacking-target-solarwinds",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/nk-drxT0WYuHTTAQw6MhPgi4LK8=/0x146:2040x1214/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/8792137/acastro_170629_1777_0008_v2.jpg",
            "publishedAt": "2021-05-28T12:54:44Z",
            "content": "Targeting around 3,000 email accounts across over 150 organizations\r\nIf you buy something from a Verge link, Vox Media may earn a commission. See our ethics statement.\r\nIllustration by Alex Castro / \u2026 [+2860 chars]"
        },
        {
            "source": "BBC News",
            "author": "BBC News",
            "title": "Fishmongers' Hall: Graduates were unlawfully killed by terrorist",
            "description": "Saskia Jones and Jack Merritt were stabbed by Usman Khan less than a year after he left prison.",
            "url": "http://www.bbc.co.uk/news/uk-england-london-57260509",
            "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/5F74/production/_109963442_composite2.jpg",
            "publishedAt": "2021-05-28T12:52:27.9984395Z",
            "content": "image copyrightMet Police\r\nimage captionSaskia Jones and Jack Merritt were killed by Usman Khan at a conference on offender rehabilitation\r\nFailings by state agencies contributed to the deaths of two\u2026 [+1130 chars]"
        },
        {
            "source":  "BBC News",
            "author": "BBC News",
            "title": "Drones and live-streams: How tech is changing conservation",
            "description": "Around the world, animal conservation has evolved so it's not just humans monitoring wildlife.",
            "url": "http://www.bbc.co.uk/news/newsbeat-57234398",
            "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/1126/production/_118709340_rhino-drone_newsbeat_comp.jpg",
            "publishedAt": "2021-05-28T12:52:23.8744659Z",
            "content": "By Manish PandeyNewsbeat reporter\r\nimage copyrightAFP/Getty/BBC\r\nDrones, satellites and laser sensors. It sounds like the tech of an action-packed spy thriller.\r\nNot things you might typically associ\u2026 [+6002 chars]"
        },
        {
            "source":  "BBC News",
            "author": "BBC News",
            "title": "Russian hackers target aid groups in new cyber-attack, says Microsoft",
            "description": "A fresh wave of cyber-attacks targets government agencies and human rights groups, mostly in the US.",
            "url": "http://www.bbc.co.uk/news/world-us-canada-57280510",
            "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/4CE0/production/_118708691_gettyimages-1229661068-1.jpg",
            "publishedAt": "2021-05-28T12:37:21.9748912Z",
            "content": "image captionMicrosoft said about 3,000 email accounts were targeted\r\nMicrosoft says another wave of Russian cyber-attacks has targeted government agencies and human rights groups in 24 countries, mo\u2026 [+2881 chars]"
        },
        {
            "source":  "BBC News",
            "author": "BBC News",
            "title": "Belarus plane: Russia accuses EU of risking passenger safety",
            "description": "Russia condemns a decision to avoid Belarusian airspace over the arrest of a dissident journalist.",
            "url": "http://www.bbc.co.uk/news/world-europe-57279482",
            "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/87E6/production/_118709743_austrian.jpg",
            "publishedAt": "2021-05-28T11:37:18.7231388Z",
            "content": "image copyrightGetty Images\r\nimage captionAn Austrian Airlines plane (not the one pictured) left Vienna for Moscow on Friday morning\r\nRussia's foreign ministry has condemned the EU's call for Europe-\u2026 [+6936 chars]"
        },
        {
            "source":  "BBC News",
            "author": "BBC News",
            "title": "Nike says it split with Neymar over sexual assault investigation",
            "description": "The sportswear giant and Brazilian footballer give conflicting accounts of why they parted ways.",
            "url": "http://www.bbc.co.uk/news/world-us-canada-57278258",
            "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/FE60/production/_118702156_mediaitem118702154.jpg",
            "publishedAt": "2021-05-28T08:37:28.1041469Z",
            "content": "US sportswear giant Nike says it stopped working with Brazilian footballer Neymar because he \"refused to co-operate in a good faith investigation\" into an allegation of sexual assault against an empl\u2026 [+1563 chars]"
        },
        {
            "source":  "The Verge",
            "author": "Jon Porter",
            "title": "Lenovo\u2019s new 13-inch Android tablet also works as a portable Switch display",
            "description": "Lenovo\u2019s Yoga Pad Pro is a new 13-inch Android tablet that can easily double as an external monitor. It will be available to buy in China for 3,299 yuan (around $517) on May 31st.",
            "url": "https://www.theverge.com/2021/5/28/22458071/lenovo-yoga-pad-pro-android-tablet-external-monitor-hdmi",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/ebb_zcb9Cp12vGFFebq4C3pzZJA=/0x309:1371x1027/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22545437/XEbQB42rd4G9SboycZMTV63zq_0247.jpg",
            "publishedAt": "2021-05-28T08:31:20Z",
            "content": "Thanks to a Micro HDMI port on its grip \r\nA built in Micro HDMI port lets the tablet work as an external monitor. \r\nImage: Lenovo\r\nLenovos Yoga Pad Pro is a new 13-inch Android tablet that can easily\u2026 [+1602 chars]"
        },
        {
            "source":  "BBC News",
            "author": "BBC News",
            "title": "Germany officially recognises colonial-era Namibia genocide",
            "description": "Foreign Minister Heiko Maas asks for forgiveness for atrocities and announces financial support deal.",
            "url": "http://www.bbc.co.uk/news/world-europe-57279008",
            "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/87D2/production/_118707743_gettyimages-1024992770.jpg",
            "publishedAt": "2021-05-28T07:22:23.5054638Z",
            "content": "image copyrightGetty Images\r\nimage captionFriday's announcement follows years of negotiation between the nations\r\nGermany has officially acknowledged that it committed genocide during its colonial-er\u2026 [+3437 chars]"
        },
        {
            "source":  "The Verge",
            "author": "Sam Byford",
            "title": "Sony launches motion-sensing music effects controller on Indiegogo",
            "description": "Sony is selling a new music product called Motion Sonic on Indiegogo. The project was demonstrated at SXSW in 2017.",
            "url": "https://www.theverge.com/2021/5/28/22458023/sony-motion-sonic-launches-music-indiegogo-price-date",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/8BbO8IZU0TZ3urYsCVsGGtJKq5E=/0x86:1200x714/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/22545282/houa3hlugbgte6bjgidn.jpg",
            "publishedAt": "2021-05-28T06:14:48Z",
            "content": "Motion Sonic is finally a real product, almost\r\nIf you buy something from a Verge link, Vox Media may earn a commission. See our ethics statement."
        },
        {
            "source": "BBC News",
            "author": "BBC News",
            "title": "Friends reunion: BTS, Lady Gaga, Justin Bieber censored in China",
            "description": "It is believed that the stars were cut because they are previously deemed to have insulted China.",
            "url": "http://www.bbc.co.uk/news/world-asia-china-57277952",
            "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/BF0E/production/_118701984_tv067487505.jpg",
            "publishedAt": "2021-05-28T04:37:26.8911406Z",
            "content": "image copyrightWarnerMedia\r\nimage captionIn the Friends reunion special, James Corden interviewed the cast in front of the famous fountain from the opening credits\r\nSomething was amiss in China's ver\u2026 [+5074 chars]"
        }


]


try:
   for i in range(len(data)):
       print(data[i])
       response = requests.post(BASE + 'headlines/', json=data[i],verify=False)
       print(response.json())
except:
    print("Connection refused by the server..")
    print("Let me sleep for 5 seconds")
    print("ZZzzzz...")
    time.sleep(5)
    print("Was a nice sleep, now let me continue...")


print('-----------------------------------------------------------------------')
print()
print('-----------------------------------------------------------------------')
print("Inserting allnews")

data = [
{
            "source":  "Mashable",
            "author": "Joseph Green",
            "title": "Understand how to handle data with this online bootcamp",
            "description": "TL;DR: The Complete Big Data and Power BI Bundle is on sale for \u00a328.28 as of May 13, saving you 91% on list price.\n\nIt's clear in today's business landscape that companies live and die by how quickly they respond to trends. But keeping up with market fluctuat\u2026",
            "url": "https://mashable.com/uk/shopping/may-13-big-data-online-course-sale/",
            "urlToImage": "https://mondrian.mashable.com/2021%252F05%252F13%252F45%252F8a14a7e572c1414486ae8fc9429b5d2a.0bc2d.jpg%252F1200x630.jpg?signature=erGSK-gnF2uTFF6JSb2z_LeQfew=",
            "publishedAt": "2021-05-13T04:00:00Z",
            "content": "TL;DR: The Complete Big Data and Power BI Bundle is on sale for \u00a328.28 as of May 13, saving you 91% on list price.\r\nIt's clear in today's business landscape that companies live and die by how quickly\u2026 [+1523 chars]"
        },
        {
            "source": "TechCrunch",
            "author": "Connie Loizos",
            "title": "Eclipse Ventures has $500 million more to digitize old-line industries and bring them up to speed",
            "description": "Two years ago, we talked with Lior Susan, the founder of now six-year-old Eclipse Ventures in Palo Alto, Ca. At the time, the outfit believed that the next big thing wasn\u2019t another social network but instead the remaking of old-line industries through full te\u2026",
            "url": "http://techcrunch.com/2021/04/29/eclipse-ventures-has-500-million-more-to-digitize-old-line-industries-and-bring-them-up-to-speed/",
            "urlToImage": "https://techcrunch.com/wp-content/uploads/2021/04/Screen-Shot-2021-04-29-at-3.24.59-PM.png?w=487",
            "publishedAt": "2021-04-30T06:01:03Z",
            "content": "Two years ago, we talked with Lior Susan, the founder of now six-year-old Eclipse Ventures in Palo Alto, Ca. At the time, the outfit believed that the next big thing wasn\u2019t another social network but\u2026 [+6689 chars]"
        },
        {
            "source":  "TechCrunch",
            "author": "Darrell Etherington",
            "title": "Google Cloud teams up with SpaceX\u2019s Starlink for enterprise connectivity at network\u2019s edge",
            "description": "SpaceX\u2019s bourgeoning Starlink satellite-based broadband internet service just got a big boost from a significant new partner: Google Cloud. Thanks to a new partnership between the two, SpaceX will now be locating Starlink ground stations right within Google\u2019s\u2026",
            "url": "http://techcrunch.com/2021/05/13/google-cloud-teams-up-with-spacexs-starlink-for-enterprise-connectivity-at-networks-edge/",
            "urlToImage": "https://techcrunch.com/wp-content/uploads/2021/03/starlink-satellites-on-orbit.jpg?w=711",
            "publishedAt": "2021-05-13T13:24:58Z",
            "content": "SpaceX\u2019s bourgeoning Starlink satellite-based broadband internet service just got a big boost from a significant new partner: Google Cloud. Thanks to a new partnership between the two, SpaceX will no\u2026 [+1678 chars]"
        },
        {
            "source": "TechCrunch",
            "author": "Ingrid Lunden",
            "title": "Huma, which uses AI and biomarkers to monitor patients and for medical research, raises $130M",
            "description": "While much of the world eagerly watches to see if the vaccination rollout helps curb and eventually stamp out Covid-19, one of the companies that has been helping to manage the spread of the virus is announcing a big round of funding on the heels for strong d\u2026",
            "url": "http://techcrunch.com/2021/05/11/huma-which-uses-ai-and-biomarkers-to-monitor-patients-and-for-medical-research-raises-130m/",
            "urlToImage": "https://techcrunch.com/wp-content/uploads/2021/05/Clinical-portal-seen-by-clinician.jpg?w=533",
            "publishedAt": "2021-05-11T23:29:50Z",
            "content": "While much of the world eagerly watches to see if the vaccination rollout helps curb and eventually stamp out Covid-19, one of the companies that has been helping to manage the spread of the virus is\u2026 [+6009 chars]"
        },
        {
            "source":  "Wired",
            "author": "Maryn McKenna",
            "title": "It\u2019s Already Time to Stop the Next Pandemic. Can a Prize Help?",
            "description": "Covid-19 is still raging, but so are efforts to nip its successor in the bud\u2014thanks to data sharing, political cooperation, or a multimillion-dollar challenge.",
            "url": "https://www.wired.com/story/its-already-time-to-stop-the-next-pandemic-can-a-prize-help/",
            "urlToImage": "https://media.wired.com/photos/609194991a16e5fc13bc0821/191:100/w_1280,c_limit/Science_trinitychallenge_1171036012.jpg",
            "publishedAt": "2021-05-05T11:00:00Z",
            "content": "Its a difficult moment in the global pandemic. As many cases were diagnosed in the past two weeks as in the pandemics first six monthsled by Brazil and India, where more than half of those cases occu\u2026 [+4084 chars]"
        },
        {
            "source": "TechCrunch",
            "author": "Ron Miller",
            "title": "Databricks introduces Delta Sharing, an open source tool for sharing data",
            "description": "Databricks launched its fifth open source project today, a new tool called Delta Sharing designed to be a vendor neutral way to share data with any cloud infrastructure or SaaS product, so long as you have the appropriate connector. It\u2019s part of the broader D\u2026",
            "url": "http://techcrunch.com/2021/05/26/databricks-introduces-delta-sharing-an-open-source-tool-for-sharing-data/",
            "urlToImage": "https://techcrunch.com/wp-content/uploads/2021/05/GettyImages-146423736-1.jpg?w=600",
            "publishedAt": "2021-05-26T15:30:45Z",
            "content": "Databricks launched its fifth open source project today, a new tool called Delta Sharing designed to be a vendor neutral way to share data with any cloud infrastructure or SaaS product, so long as yo\u2026 [+3282 chars]"
        },
        {
            "source": "TechCrunch",
            "author": "Annie Siebert",
            "title": "Healthcare is the next wave of data liberation",
            "description": "Soon, with the emergence of new market leaders, we\u2019ll be able to access our health records as easily as our bank statements.",
            "url": "http://techcrunch.com/2021/04/29/healthcare-is-the-next-wave-of-data-liberation/",
            "urlToImage": "https://techcrunch.com/wp-content/uploads/2021/04/GettyImages-1010720886.jpg?w=521",
            "publishedAt": "2021-04-29T18:43:15Z",
            "content": "Why can we see all our bank, credit card and brokerage data on our phones instantaneously in one app, yet walk into a doctors office blind to our healthcare records, diagnoses and prescriptions? Our \u2026 [+3251 chars]"
        },
        {
            "source": "The Verge",
            "author": "Jon Porter",
            "title": "Go read this report on how law enforcement can extract sensitive data from your car",
            "description": "A new report has shed light on tech that lets law enforcement extract personal data from cars. It reports that US Customs and Border Protection recently purchased iVe \u201cvehicle forensics kits\u201d from data extraction firm MSAB",
            "url": "https://www.theverge.com/2021/5/5/22420674/go-read-this-intercept-report-vehicle-forensics-infotainment-personal-sensitive-data-law-enforcement",
            "urlToImage": "https://cdn.vox-cdn.com/thumbor/nk-drxT0WYuHTTAQw6MhPgi4LK8=/0x146:2040x1214/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/8792137/acastro_170629_1777_0008_v2.jpg",
            "publishedAt": "2021-05-05T11:27:16Z",
            "content": "US Customs and Border Protection recently bought five vehicle forensics kits\r\nIllustration by Alex Castro / The Verge\r\nA new report from The Intercept has shed light on a worrying new technology that\u2026 [+2774 chars]"
        },
        {
            "source": "TechCrunch",
            "author": "Natasha Lomas",
            "title": "The UK\u2019s plan to tackle big tech won\u2019t be one-size fits all",
            "description": "The director of a new unit set up this month inside the UK\u2019s competition watchdog \u2014 with a dedicated focus on tech giants\u2019 impacts on digital markets \u2014 has been giving a hint of how it could operate, once it\u2019s on a statutory footing and imbued with powers to \u2026",
            "url": "http://techcrunch.com/2021/04/27/the-uks-plan-to-tackle-big-tech-wont-be-one-sized-fits-all/",
            "urlToImage": "https://techcrunch.com/wp-content/uploads/2021/04/GettyImages-1016873088.jpg?w=599",
            "publishedAt": "2021-04-27T13:24:09Z",
            "content": "The director of a new unit set up this month inside the UK\u2019s competition watchdog \u2014 with a dedicated focus on tech giants\u2019 impacts on digital markets \u2014 has been giving a hint of how it could operate,\u2026 [+15314 chars]"
        }
]

try:
   for i in range(len(data)):
       print(data[i])
       response = requests.post(BASE + 'allnews/', json=data[i],verify=False)
       print(response.json())
except:
    print("Connection refused by the server..")
    print("Let me sleep for 5 seconds")
    print("ZZzzzz...")
    time.sleep(5)
    print("Was a nice sleep, now let me continue...")


print('-----------------------------------------------------------------------')
print()
print('-----------------------------------------------------------------------')
print('Inserting into sources')

data=[
{
            "id": "cbc-news",
            "name": "CBC News",
            "description": "CBC News is the division of the Canadian Broadcasting Corporation responsible for the news gathering and production of news programs on the corporation's English-language operations, namely CBC Television, CBC Radio, CBC News Network, and CBC.ca.",
            "url": "http://www.cbc.ca/news",
            "category": "general",
            "language": "en",
            "country": "ca"
        },
        {
            "id": "cbs-news",
            "name": "CBS News",
            "description": "CBS News: dedicated to providing the best in journalism under standards it pioneered at the dawn of radio and television and continue in the digital age.",
            "url": "http://www.cbsnews.com",
            "category": "general",
            "language": "en",
            "country": "us"
        },
        {
            "id": "cnn",
            "name": "CNN",
            "description": "View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN",
            "url": "http://us.cnn.com",
            "category": "general",
            "language": "en",
            "country": "us"
        },
        {
            "id": "cnn-es",
            "name": "CNN Spanish",
            "description": "Lee las \u00faltimas noticias e informaci\u00f3n sobre Latinoam\u00e9rica, Estados Unidos, mundo, entretenimiento, pol\u00edtica, salud, tecnolog\u00eda y deportes en CNNEspa\u00f1ol.com.",
            "url": "http://cnnespanol.cnn.com/",
            "category": "general",
            "language": "es",
            "country": "us"
        },
        {
            "id": "crypto-coins-news",
            "name": "Crypto Coins News",
            "description": "Providing breaking cryptocurrency news - focusing on Bitcoin, Ethereum, ICOs, blockchain technology, and smart contracts.",
            "url": "https://www.ccn.com",
            "category": "technology",
            "language": "en",
            "country": "us"
        },
        {
            "id": "der-tagesspiegel",
            "name": "Der Tagesspiegel",
            "description": "Nachrichten, News und neueste Meldungen aus dem Inland und dem Ausland - aktuell pr\u00e4sentiert von tagesspiegel.de.",
            "url": "http://www.tagesspiegel.de",
            "category": "general",
            "language": "de",
            "country": "de"
        },
        {
            "id": "die-zeit",
            "name": "Die Zeit",
            "description": "Aktuelle Nachrichten, Kommentare, Analysen und Hintergrundberichte aus Politik, Wirtschaft, Gesellschaft, Wissen, Kultur und Sport lesen Sie auf ZEIT ONLINE.",
            "url": "http://www.zeit.de/index",
            "category": "business",
            "language": "de",
            "country": "de"
        },
        {
            "id": "el-mundo",
            "name": "El Mundo",
            "description": "Noticias, actualidad, \u00e1lbumes, debates, sociedad, servicios, entretenimiento y \u00faltima hora en Espa\u00f1a y el mundo.",
            "url": "http://www.elmundo.es",
            "category": "general",
            "language": "es",
            "country": "es"
        },
        {
            "id": "engadget",
            "name": "Engadget",
            "description": "Engadget is a web magazine with obsessive daily coverage of everything new in gadgets and consumer electronics.",
            "url": "https://www.engadget.com",
            "category": "technology",
            "language": "en",
            "country": "us"
        },
        {
            "id": "entertainment-weekly",
            "name": "Entertainment Weekly",
            "description": "Online version of the print magazine includes entertainment news, interviews, reviews of music, film, TV and books, and a special area for magazine subscribers.",
            "url": "http://www.ew.com",
            "category": "entertainment",
            "language": "en",
            "country": "us"
        },
        {
            "id": "espn",
            "name": "ESPN",
            "description": "ESPN has up-to-the-minute sports news coverage, scores, highlights and commentary for NFL, MLB, NBA, College Football, NCAA Basketball and more.",
            "url": "http://espn.go.com",
            "category": "sports",
            "language": "en",
            "country": "us"
        },
        {
            "id": "espn-cric-info",
            "name": "ESPN Cric Info",
            "description": "ESPN Cricinfo provides the most comprehensive cricket coverage available including live ball-by-ball commentary, news, unparalleled statistics, quality editorial comment and analysis.",
            "url": "http://www.espncricinfo.com/",
            "category": "sports",
            "language": "en",
            "country": "us"
        },
        {
            "id": "financial-post",
            "name": "Financial Post",
            "description": "Find the latest happenings in the Canadian Financial Sector and stay up to date with changing trends in Business Markets. Read trading and investing advice from professionals.",
            "url": "http://business.financialpost.com",
            "category": "business",
            "language": "en",
            "country": "ca"
        },
        {
            "id": "focus",
            "name": "Focus",
            "description": "Minutenaktuelle Nachrichten und Service-Informationen von Deutschlands modernem Nachrichtenmagazin.",
            "url": "http://www.focus.de",
            "category": "general",
            "language": "de",
            "country": "de"
        },
        {
            "id": "football-italia",
            "name": "Football Italia",
            "description": "Italian football news, analysis, fixtures and results for the latest from Serie A, Serie B and the Azzurri.",
            "url": "http://www.football-italia.net",
            "category": "sports",
            "language": "en",
            "country": "it"
        }
]


try:
   for i in range(len(data)):
       print(data[i])
       response = requests.post(BASE + 'sources/', json=data[i],verify=False)
       print(response.json())
except:
    print("Connection refused by the server..")
    print("Let me sleep for 5 seconds")
    print("ZZzzzz...")
    time.sleep(5)
    print("Was a nice sleep, now let me continue...")


print('-----------------------------------------------------------------------')
print()
print('-----------------------------------------------------------------------')




