<nav class="Quick-navigation">{% for navigation in navigation %}
	<a href="{{ navigation.link }}" class="Quick-navigation-item {{ navigation.status }}">{{ navigation.name }}</a> 
	{% endfor %}
	<div class="Scroll-progress-indicator visible"></div>
</nav>
