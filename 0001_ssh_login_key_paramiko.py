
import paramiko

class PdpPerfomance(object):
	"""docstring for ClassName"""
	def __init__(self):
		pass

	def ssh_login(self):

		try:
			cert = paramiko.RSAKey.from_private_key_file("key.pem")
			c = paramiko.SSHClient()
			c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			print "connecting..."
			c.connect( hostname = "10.0.0.0", username = "example", pkey = cert )
			print "connected!!!"
			stdin, stdout, stderr = ssh.exec_command('ls')
			print stdout.readlines()
			c.close()

		except:
			print("Connection Failed!!!")


obj = PdpPerfomance()
obj.ssh_login()
