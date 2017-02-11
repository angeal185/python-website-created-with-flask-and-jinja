<div class="gallery">
{% for gallery in gallery %}
<div class="col-lg-4">
	<div class="align-center">
		<div class="testimonial pad-top40 pad-bot40 clearfix wow fadeIn" data-wow-delay="1s">
			<h5>{{lorem.lorem3}}{{ gallery.info }}</h5>
			<br><span class="author">{{lorem.name}}{{ gallery.name }}<a href="mailto:{{ gallery.email }}">{{lorem.email}}{{ gallery.email }}</a></span>
		</div>
	</div>
</div>
<div class="slide slide-{{ gallery.slide }}"><a href="{{ gallery.link }}"><img src="{{ gallery.img }}"></a></div>
{% endfor %}
</div>
