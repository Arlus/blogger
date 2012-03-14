from django import forms
from blogger.blog.models import Post, Photos
from captcha.fields import CaptchaField

class PostAdminForm(forms.ModelForm):
	class Meta:
		model = Post

class CommentForm(forms.Form):
	comment = forms.CharField(widget = forms.Textarea, label = "Comment")
	name = forms.CharField(label = "Your Name")
	Email = forms.EmailField(label = "Your Email(will not be posted)")
	website = forms.URLField(label = "Website(optional)", required = False)
	robot = CaptchaField(label = "Robot test")
	def clean_message(self):
		message = self.cleaned_data['message']
		num = len(message.split())
		if num < 4:
			raise forms.ValidationError("Message too short")
		return message
	
