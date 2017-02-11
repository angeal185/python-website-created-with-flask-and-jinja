<section id="section-works" class="section js-scroll-step clearfix">
	<div class="container">
		<div class="row mar-bot40">
			<div class="col-md-offset-3 col-md-6">
				<div class="section-header wow fadeIn" data-wow-delay="1s">
					<h2 class="section-heading animated" data-animation="bounceInUp">{{ headings.portfolio }}</h2>
					<p>{{ lorem.lorem2 }}</p>
				</div>
			</div>
		</div>
		<div class="c-logo-part parallax1"></div>
		<div class="row pad-top40">
			<nav id="filter" class="col-md-12 text-center wow fadeIn" data-wow-delay="1s">
				<ul>{% for filter in filter %}
					<li><a href="#!" class="btn-theme btn-small {{ filter.class }} " data-filter="{{ filter.filter }}">{{ filter.name }}</a></li>{% endfor %}
				</ul>
			</nav>
			<div class="col-md-12">
				<div class="row">
					<div class="portfolio-items parallax1 isotopeWrapper clearfix" id="3">
						{% include "snippets/portfolio.py" %}
					</div>
				</div>
			</div>
		</div>
	</div>
</section>
