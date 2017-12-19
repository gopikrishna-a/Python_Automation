from pexpect import pxssh


class SshLogin(object):
    """docstring for ClassName"""
    def __init__(self):
        self.ip = '10.36.199.7'
        self.port = 22
        self.username = 'kperiyaswamy'
        self.password = 'Lucky@786'

    def ssh_login(self):

        try:
            s = pxssh.pxssh()
            s.login(self.ip, self.username, self.password)
            print("connected!!!")
            s.sendline('pwd')
            s.prompt()
            print s.before
            s.close()
            print("Connection closed!!!")

        except:
            print("Connection Failed!!!")



obj = SshLogin()
obj.ssh_login()
