<section id="section-about" class="section js-scroll-step clearfix">
	<div class="container">
		<div class="row mar-bot40">
			<div class="col-md-offset-3 col-md-6">
				<div class="section-header wow fadeIn" data-wow-delay="1s">
					<h2 class="section-heading">{{ headings.team }}</h2>
					<p>{{ lorem.lorem2 }}</p>
				</div>
			</div>
		</div>
		<div class="c-logo-part parallax1"></div>
		<div class="row align-center mar-bot40 pad-top40">
		{% include "snippets/team.py" %} 
		</div>
		<div class="row">
			<div class="col-lg-12">
				<div class="align-center">
					<div class="testimonial pad-top40 pad-bot40 clearfix wow fadeIn" data-wow-delay="1s">
						<h5>{{ lorem.lorem2 }}</h5>
						<br><span class="author">{{ lorem.name }} | </span><a href="mailto:{{ lorem.email }}">{{ lorem.email }}</a></div>
				</div>
			</div>
		</div>
	</div>
</section>
