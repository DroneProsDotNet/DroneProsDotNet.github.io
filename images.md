---
layout: default
title: Images
---

# Images

<p class="lede">A selection of our aerial stills. Click any photo to view it full-screen.</p>

<div class="gallery">
  {% for photo in site.data.gallery %}
  <figure>
    <img src="{{ '/assets/img/' | append: photo.file | relative_url }}" alt="{{ photo.caption }}" loading="lazy">
    <figcaption>{{ photo.caption }}</figcaption>
  </figure>
  {% endfor %}
</div>
