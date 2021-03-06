<section id="footer" class="section footer">
	<div class="container">
		<div class="row animated opacity mar-bot20 wow fadeIn" data-wow-delay="1s">
			<div class="col-sm-12 align-center">
				<ul class="social-network social-circle">
				{% for footerIcons in footer %}
					<li><a href="{{ footerIcons.href }}" class="{{ footerIcons.class }}" title="{{ footerIcons.title }}"><i class="fa fa-{{ footerIcons.icon }}"></i></a></li>
				{% endfor %}
				</ul>
			</div>
		</div>
		<div class="row align-center copyright wow fadeInUp" data-wow-delay="1s">
			<div class="col-sm-12">
				<p>{{ meta.year }}</p>
				<div class="credits"><span>{{ meta.author }}</span></div>
			</div>
		</div>
	</div>
</section>
