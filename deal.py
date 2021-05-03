"""Convert downloaded documents format to .docx and select
"""
#-*-coding:utf-8-*-
import os
from docx import Document
import win32com.client as wc


class DealDocuments:
    """
    把下载下来的文书转为docx格式，方便后面根据关键字检索
    """


    def __init__(self, text, docx_text):
        self.text = text
        self.docx_text = docx_text

    # python-dox can not deal with .doc, must convert to .docx
    @staticmethod
    def convert_doc_to_docx(filename: str):
        """
        文件由doc转为docx格式
        """
        word = wc.Dispatch('Word.Application')
        # 用相对路径会有问题
        absolute_read_path = 'D:\\Documents\\dealDocs\\text\\' + filename
        absolute_write_path = 'D:\\Documents\\dealDocs\\docx_text\\' + filename + 'x'
        doc = word.Documents.Open(absolute_read_path, False, False, True)
        doc.SaveAs(absolute_write_path, 12)
        doc.Close()
        word.Quit()

    def convert(self):
        """
        批量转换
        """
        for file in os.listdir(self.text):
            self.convert_doc_to_docx(file)

    def deal_content(self, filename: str):
        """
        检索文书中是否同时含有"贵阳银行"和"被告"，若没有则删除
        """
        delete_flag = 1
        file_path = self.docx_text + filename
        doc1 = Document(file_path)
        pl = [paragraph.text for paragraph in doc1.paragraphs]
        for sentence in pl:
            # 含有冒号且不以冒号结尾，且字符串中含有“被告”和“贵阳银行”
            if sentence.endswith("："):
                break
            else:
                if ("：" in sentence) and ("贵阳银行"
                                          in sentence) and ("被告" in sentence):
                    delete_flag = 0
        if delete_flag:
            os.remove(file_path)

    def deal(self):
        """
        批量检索
        """
        for file in os.listdir(self.docx_text):
            self.deal_content(file)

        # FILENAME_LIST = os.listdir('docx_text')
        # for file in FILENAME_LIST:
        #     deal_content(file)


if __name__ == '__main__':
    DEAL_DOCUMENT = DealDocuments('text\\', 'docx_text\\')
    DEAL_DOCUMENT.convert()
    DEAL_DOCUMENT.deal()
