<div class="c-logo-part">
	<div class="container">
		<ul>
{% for clogo in clogo %}<li><a href="{{ clogo.href }}"><img src="{{  meta.staticImg }}{{  clogo.img }}"></a></li>{% endfor %}
		</ul>
	</div>
</div>
