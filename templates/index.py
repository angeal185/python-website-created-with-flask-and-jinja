{% extends "layout.py" %}
{% block content %}
{% include "includes/featured.py" %}
{% include "includes/services.py" %}
<div class="c-logo-part parallax1"></div>
{% include "includes/reviews.py" %}
{% include "includes/about.py" %}
{% include "snippets/parallax-callout.py" %}
{% include "includes/portfolio.py" %}
{% include "snippets/carousel.py" %}
{% include "includes/contact.py" %} 
{% include "includes/gmap.py" %}    
{% endblock %}
