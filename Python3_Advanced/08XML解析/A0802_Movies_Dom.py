
from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析打开XML文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element: ",collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print("*****Movie*****")
    if movie.hasAttribute("title"):
        print("Title:",movie.getAttribute("title"))

    type = movie.getElementsByTagName("type")[0]
    print("Type:", type.childNodes[0].data)
    format = movie.getElementsByTagName("format")[0]
    print("Format:", format.childNodes[0].data)
    rating = movie.getElementsByTagName("rating")[0]
    print("Rating:", rating.childNodes[0].data)
    description = movie.getElementsByTagName("description")[0]
    print("Description:", description.childNodes[0].data)
