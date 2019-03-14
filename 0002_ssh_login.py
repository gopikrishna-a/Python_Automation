import paramiko

class RemoteLogin(object):
    """docstring for ClassName"""
    def __init__(self):
        self.ip = '10.0.0.0'
        self.port = 22
        self.username = 'user'
        self.password = 'password'

    def ssh_login(self):

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print("connecting...")
            ssh.connect(self.ip,self.port,self.username,self.password)
            print("connected!!!")
            stdin, stdout, stderr = ssh.exec_command('ls')
            print stdout.readlines()
            ssh.close()
            print("Connection closed!!!")
        except Exception as err:
            print("Connection Failed!!! {}".format(err))


obj = RemoteLogin()
obj.ssh_login()
