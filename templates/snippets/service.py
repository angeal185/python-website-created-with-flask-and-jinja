{% for service in service %}
<div class="col-lg-4 wow fadeInUp" data-wow-delay="{{ service.delay }}">
	<div class="align-center"><i class="fa fa-{{ service.icon }} fa-5x mar-bot20"></i>
		<h4 class="text-bold">{{ service.info }}</h4>
		<p>{{ lorem.lorem2 }}</p>
	</div>
</div>
{% endfor %}
