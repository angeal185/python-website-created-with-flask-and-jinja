<!DOCTYPE html>
<html lang="en">
<head>
<title>{{ meta.title  | safe }}</title>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta http-equiv="cache-control" content="no-cache">
<meta http-equiv="content-language" content="en-us">
<meta name="robots" content="index, follow">
<meta name="google" content="nositelinkssearchbox">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="author" content="{{ meta.author }}">
<meta name="description" content="{{ meta.description }}">
<meta name="keywords" content="{{ meta.keywords }}">
<meta property="og:title" content="{{ meta.title }}">
<meta property="og:description" content="{{ meta.description }}">
<meta property="og:site-name" content="{{ meta.title }}">
<meta property="og:url" content="{{ meta.url }}">
<meta property="og:image" content="{{ meta.icon_path }}">
<link rel="shortcut icon" href="{{ meta.iconpath }}">
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
<link href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.css" rel="stylesheet" type="text/css" media="screen">
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" type="text/css">
<link href="https://cdnjs.cloudflare.com/ajax/libs/flickity/2.0.5/flickity.min.css" rel="stylesheet" type="text/css">
<link href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css" rel="stylesheet" type="text/css">
<link href="{{ meta.staticCss }}style.css" rel="stylesheet" type="text/css">
</head>
<body>
<section id="header" class="js-scroll-step"></section>
{% include "includes/nav.py" %}
{% block content %}{% endblock %}
{% include "includes/footer.py" %}
<button class="Scroll-to-top">Scroll To Top</button>
{% include "includes/js-bottom.py" %}
</script>
</body>
</html>
