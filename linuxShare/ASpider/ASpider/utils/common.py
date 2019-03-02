
import hashlib
def get_md5(url):
    #python2把python3都变成Unicode ，hashlib.md5不接受Unicode 需要加上encode("utf-8")
    #判断用户传过来的url是否是Unicode编码的，str是否是string类型（python3不支持str）
    if isinstance(url,str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == "__main__":
    print(get_md5("http://jobbole.com".encode("utf-8")))