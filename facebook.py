class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]


	def add_friend(self,email):
		self.friends_list.append(email)
		print("has added "+email+' as a friend')

	def remove_friend(self,email):
		self.friends_list.remove(email)
		print("has added "+email+' as a friend')

	def add_post(self,text):
		self.posts.append(text)
		print(self.name+' has posted '+text)

	def get_userinfo(self):
		print('name' + self.name + '\nemail' + self.email + '\npassword' + self.password + '\nfriends' + self.friends_list + '\nposts' + self.posts)



user1 = User('adam','tsotzukth1@gmail.com','adam2004')

user2 = User('sarah','sarah@gmail.com', 'sarah2003')


user1.add_friend(user2.email)
user2.add_friend(user1.email)

user1.add_post('thats my text 1')
user2.add_post('that my text 2')

user1.get_userinfo()