class TokenException(Exception):
    def __init__(self, username, msg=None):
        if msg is None:
            msg = "An error occured gettting the token for {}".format(username)
        super(TokenException, self).__init__(msg)
        self.username = username

class FetchingException(Exception):
    def __init__(self, item, msg=None):
        if msg is None:
            msg = "Failed fetching {}".format(item)
        super(FetchingException, self).__init__(msg)
        self.item = item
