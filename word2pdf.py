import util
from win32com import client
import os


def word2pdf_simple(wordPath):
    cwd = os.getcwd()  # the path of the current py script
    print(cwd)
    wordName = wordPath.split("/")[-1]  # ATTENTION: split with `/`
    if wordName.split(".")[-1] not in ('doc', 'docx'):
        print("not supported file type")
        exit()
    word = client.Dispatch("Word.Application")  # open word application
    doc = word.Documents.Open(cwd+"/"+wordPath)
    doc.SaveAs(cwd + "/" + util.DEFAULT_DIR +
               "{}.pdf".format(wordName.split(".")[-2]), 17)  # 17: pdf
    doc.Close()
    word.Quit()


if __name__ == "__main__":
    word2pdf_simple(util.get_target_file_from_argv1())
