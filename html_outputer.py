# coding=utf-8
# 网页输出器
class HtmlOutputer(object):
    def __init__(self):
        # 新建一个序列存储数据
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 将收集到的数据输出为html
    def output_html(self):
        fout = open('output', 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<hr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("</hr>")
            fout.write("<hr>")
        fout.write("<td>%s</td>" % data['data'].encode("utf-8"))
        fout.write("</hr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
