users=[]
posts=[]
comments=[]

username='adam'
password='123'

random=0

while random==0:
	try_username=input('whats the username?')
	try_password=input('whats the password?')

	if try_username==username and try_password==password:
		random=1
		print('welcome in!')

	else:
		print('please try again!')

class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		users.append(self)

	def add_friend(self,email):
		self.friends_list.append(email)
		print("has added "+email+' as a friend')

	def remove_friend(self,email):
		self.friends_list.remove(email)
		print("has added "+email+' as a friend')

	def add_post(self,post_text,date):
		self.post_text=post_text
		author=self.name
		post1=Post(date,post_text)
		posts.append(post1)
		print(self.name+' has posted '+post_text)

	def create_comment(self,comment_text):
		self.comment_text=comment_text
		comment1=Comment(self.comment_text)
		comment1.create_comment()

	def get_userinfo(self):
		print('name: ' + self.name + ' email: ' + self.email + ' password: ' + self.password + ' friends: ' + str(self.friends_list) + 'posts' + str(self.posts))


class Post():
	def __init__(self,post_text,date):
		self.post_text=post_text
		self.date=date

		def post(self):
			posts.append(post_text)


		def post_date(self):
			print('posted on ' + self.date)

		def edit_comment(self,new_comment):
			self.comment_text=new_comment
			print('your comment has been changed!')


class Comment(Post):
	def __init__(self,comment_text):
		self.comment_text=comment_text

	def create_comment(self):
		comments.append(self.comment_text)
		print('your comment is ' + self.comment_text)



class Messages(User):
	def __init__(self,message_text):
		self.message_text=message_text

	reciver=input('who do you want to DM?')
	for i in users:
		if reciver==i.name




user1 = User('adam','tsotzukth1@gmail.com','adam2004')

user2 = User('sarah','sarah@gmail.com', 'sarah2003')


user1.add_friend(user2.email)
user2.add_friend(user1.email)

user1.add_post('say hello','30/1')
user2.add_post('that my text 2','4/4')

user1.create_comment('hello')