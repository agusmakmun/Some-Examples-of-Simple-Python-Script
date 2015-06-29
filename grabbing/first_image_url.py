from bs4 import BeautifulSoup

data = """
<div>
    <div class="post">
        <a title="Brass-plated door knob" href="http:URL-LINK">
            <img alt="IMAGE ALTERNATE TEXT" src="http://bloggersmart.net/wp-content/uploads/2015/06/7-Kapal-Pesiar-Terbesar-di-Dunia.jpg" />
            <span class="det"><em class="fl">3.87 dollars</em><em class="fr">Housewares</em></span>
            <strong class="vtitle">Brass-plated door knob</strong>
        </a>

        <div class="desc"><p>Brass-plated door knob</p></div>
    </div>
    <div class="post">
        <a title="Brass-plated door knob2" href="http:URL-LINK2">
            <img src="IMAGE SOURCE LINK" alt="IMAGE ALTERNATE TEXT"/>
            <span class="det"><em class="fl">410.25 dollars</em><em class="fr">Housewares</em></span>
            <strong class="vtitle">Brass-plated door knob2</strong>
        </a>

        <div class="desc"><p>Brass-plated door knob2</p></div>
    </div>
</div>
"""

soup = BeautifulSoup(data)
result = []
for post in soup.select('div.post'):
    all_links = soup.findAll('img', src=True)
    first = all_links[0]
    string = str(first)
    split = string.split('"')
    result.append(split[3])

print result[0]

"""RESULT
http://bloggersmart.net/wp-content/uploads/2015/06/7-Kapal-Pesiar-Terbesar-di-Dunia.jpg
"""
