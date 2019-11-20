users=[]
posts=[]



class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]

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

#	def create_comment(self,comment_text):
#		self.comment_text=comment_text
#		comment1=Post()
#		self.comments.append(comment1)

	def get_userinfo(self):
		print('name: ' + self.name + ' email: ' + self.email + ' password: ' + self.password + ' friends: ' + str(self.friends_list) + 'posts' + str(self.posts))


class Post():
	def __init__(self,post_text,date):
		self.post_text=post_text
		self.date=date
		self.comments=[]

		def post(self):
			posts.append(post_text)


		def post_date(self):
			print('posted on ' + self.date)

		def edit_comment(self,new_comment):
			self.comment_text=new_comment
			print('your comment has been changed!')

class comment(Post):
	def __init__(self,comment_text):
		self.comment_text=comment_text

	def create_comment(self):
			self.comments.append(comment_text)
			print('your comment is ' + self.comment_text)

	def remove_comment(self):
			self.comments.remove(comment_text)

user1 = User('adam','tsotzukth1@gmail.com','adam2004')

user2 = User('sarah','sarah@gmail.com', 'sarah2003')


user1.add_friend(user2.email)
user2.add_friend(user1.email)

user1.add_post('say hello','30/1')
user2.add_post('that my text 2','4/4')

user1.create_comment('comment')
#user1.get_userinfo()
