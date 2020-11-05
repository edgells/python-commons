from django.core.files.storage import Storage
from django.comf import settings
from fdfs_client.client import Fdfs_client

"""
    django 中自定义文件存储需要定义Storage 子类
"""


class FastDFSStroage(Storage):

    def __init__(self, base_url=None, client_conf=None):
        """
        配置应该在配置文件中导入
        """
        if base_url is None:
            base_url = settings.BASE_URL

        self.base_url = base_url
        if client_conf is None:
            self.client_conf = settings.FASTDFS_CONF

        self.client_conf = client_conf

    def _open(self):
        """
        用来实现打开文件操作
        :return:
        """
        pass

    def _save(self, name, content):
        """
        主要通过fastdfs 保存文件所以只需要重写这个方法
        :return: file_name
        """
        client = Fdfs_client(self.client_conf)
        res = client.upload_by_buffer(content.read())
        if res.get('Status') != "Upload succesd.":
            raise Exception("upload file exception")
        file_name = res.get("Remote file_id")
        return file_name

    def url(self, name):
        return self.base_url + name

    def exists(self, name):
        """
        fastdfs 会自动处理文件重名问题
        :param name:
        :return:
        """
        return False