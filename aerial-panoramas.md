---
layout: default
title: Aerial Panoramas
---

# Panoramas

<p class="lede">Sweeping aerial panoramas from New England to Yellowstone and Yosemite. Click any panorama to view it full-screen.</p>

<div class="pano">
  {% for pano in site.data.panoramas %}
  <figure>
    <img src="{{ '/assets/img/' | append: pano.file | relative_url }}" alt="{{ pano.caption }}" loading="lazy">
    <figcaption><strong>{{ pano.caption }}</strong></figcaption>
  </figure>
  {% endfor %}
</div>
