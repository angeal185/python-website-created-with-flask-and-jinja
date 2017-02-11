{% for team in team %}
<div class="col-md-3">
<div class="team-member wow fadeInUp" data-wow-delay="{{ team.delay }}">
	<figure class="member-photo"><img src="{{ meta.staticImg }}{{ team.img }}"></figure>
	<div class="team-detail">
		<h4>{{ lorem.name }}{{ team.name }}</h4><span>{{ lorem.description }}{{ team.title }}</span>
		<p>{{ lorem.lorem2 }}{{ team.about }}</p>
	</div>
</div>
</div>
{% endfor %}
