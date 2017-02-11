<form action="" method="post" role="form" class="contactForm">
	<div class="form-group">
		<label for="name">{{ contact.name }}</label>
		<input type="text" name="name" class="form-control" id="name" placeholder="{{ contact.name }}">
	</div>
	<div class="form-group">
		<label for="email">{{ contact.email }}</label>
		<input type="email" class="form-control" name="email" id="email" placeholder="{{ contact.email }}">
	</div>
	<div class="form-group">
		<label for="subject">{{ contact.subject }}</label>
		<input type="text" class="form-control" name="subject" id="subject" placeholder="{{ contact.subject }}">
	</div>
	<div class="form-group">
		<label for="message">{{ contact.message }}</label>
		<textarea class="form-control" name="message" rows="5" placeholder="{{ contact.message }}..."></textarea>
	</div>
	<button type="submit" class="btn btn-theme pull-left">{{ contact.send }}</button>
</form>
