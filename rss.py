from xml.etree import ElementTree
import urllib.request
import datetime


def main():
    print("main")
    with open('./feed.opml', 'rt') as f:
        tree = ElementTree.parse(f)

    nodes = []
    for node in tree.iter('outline'):
        nodes.append(node)

    for node in nodes:
        name = node.attrib.get('text')
        url = node.attrib.get('xmlUrl')
        if name and url:
            print('  %s' % name)
            print('    %s' % url)

            rss_request = urllib.request.urlopen(url)
            rss_data = rss_request.read()
            rss_request.close()

            reddit_root = ElementTree.fromstring(rss_data)
            item = reddit_root.findall('channel/item')
            # print(item)

            reddit_feed = []
            for entry in item:
                pubDate = entry.findtext('pubDate')
                reddit_feed.append([pubDate])
            first_date = reddit_feed[0][0]

            if first_date.find("2018") >= 0 or first_date.find("2019") >= 0:
                print("pass")
            else:
                nodes.remove(node)

        else:
            print(name)

    for node in nodes:
        name = node.attrib.get('text')
        print(name)
        
if __name__ == "__main__":
    main()
