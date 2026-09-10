---
layout: default
title: Videos
---

# Videos

![Aerial view of Wakefield Center]({{ '/assets/img/videos-wakefield-center.jpg' | relative_url }})

{% for section in site.data.videos %}
<section class="video-section">
  <h2>{{ section.category }}</h2>
  <div class="video-grid">
    {% for v in section.items %}
    <div class="video-card">
      <div class="embed">
        <iframe src="https://www.youtube.com/embed/{{ v.youtube }}" title="{{ v.title }}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
      <h3>{{ v.title }}</h3>
      <p>{{ v.desc }}</p>
    </div>
    {% endfor %}
  </div>
</section>
{% endfor %}
