import ez_setup
ez_setup.use_setuptools()
from setuptools import setup,find_packages
setup(
	name="send-sinaweibo",
	version = "0.1",
	packages = find_packages(),
	author = "Herry Zhang",
	author_email = "z858570636@gmail.com",
	description = "A package to help you send a sinaweibo",
	url = "https://github.com/zhangyuyan/send-sina-weibo/",
	include_package_data = True,
)
