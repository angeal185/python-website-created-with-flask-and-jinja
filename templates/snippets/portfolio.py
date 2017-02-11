{% for portfolio in portfolio %}
<article class="col-md-4 isotopeItem {{ portfolio.category }} wow fadeIn" data-wow-delay="{{ portfolio.duration}}">
	<div class="portfolio-item"><img src="{{  meta.staticImg }}{{ portfolio.img }}">
		<div class="portfolio-desc align-center">
			<div class="folio-info">
				<h3>{{ lorem.name }}{{ portfolio.name }}</h3><a href="{{  meta.staticImg }}{{ portfolio.img }}" class="fancybox"><i class="fa fa-plus fa-2x"></i></a>
			</div>
		</div>
	</div>
</article>{% endfor %}
