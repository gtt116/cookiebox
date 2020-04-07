
class CookieBox(object):
    """
    CookieBox manages and persistent cookies by file system.

    Usage example:

    > box = CookieBox()
    > resp = requests.get("http://url", cookies=box.dict())
    > box.update_cookie(resp.cookies)
    > resp1 = requests.get("http://url", cookies=box.dict())
    """

    def __init__(self, path="./cookie.txt"):
        self._path = path
        self._cookies = {}
        self.read()

    def str_to_cookie(self, s):
        cookie = {}
        for line in s.split(";"):
            line = line.strip()
            print line
            k, v = line.split("=", 1)
            cookie[k] = v
        return cookie

    def read(self):
        print("read from %s" % self._path)
        with open(self._path, 'r') as i:
            content = i.read()
        self._cookies = self.str_to_cookie(content)

    def write(self):
        print("write to %s" % self._path)
        with open(self._path, 'w') as o:
            o.write(self.string())

    def dict(self):
        return self._cookies

    def string(self):
        lines = []
        for k, v in self._cookies.iteritems():
            lines.append('%s=%s' % (k, v))

        return '; '.join(lines)

    def update_cookie(self, new_cookies):
        updated = False
        for k, v in new_cookies.iteritems():
            self._cookies[k] = v
            updated = True

        if updated:
            self.write()

    def update(self, k, v):
        self._cookies[k] = v
        self.write()

if __name__ == '__main__':
    box = CookieBox()
    print(box.dict())
    box.update("usenrame", 111)
