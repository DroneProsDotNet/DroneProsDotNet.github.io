---
layout: default
title: Home
redirect_from:
  - /home
---

<div class="hero">
  <img src="{{ '/assets/img/home-stormy-sunset.jpg' | relative_url }}" alt="Aerial photo of a stormy sunset over the water">
  <div class="hero-caption">
    <h1>See the world from above</h1>
    <p>Aerial photography &amp; videography for real estate, events, and brands — since 2014.</p>
  </div>
</div>

<section class="block center">
  <h2>Check out our Aerial Reel</h2>
  <div class="embed" style="max-width: 860px; margin: 0 auto;">
    <iframe src="https://www.youtube.com/embed/ztgs4KjEYhU" title="Aerial reel" loading="lazy" allowfullscreen></iframe>
  </div>
</section>

<section class="block">
  <div class="feature">
    <img src="{{ '/assets/img/home-church-flag-lake-sunset.jpg' | relative_url }}" alt="Church, flag and lake at sunset from above">
    <div class="feature-text">
      <h2>Committed to Excellence</h2>
      <p>You can trust that we will be able to capture the perfect moment because we have done it before. We put the same effort and dedication into each of our projects so that you are able to get the absolute best final project.</p>
      <p><a class="btn" href="{{ '/images/' | relative_url }}">Check Out Our Work</a></p>
    </div>
  </div>

  <div class="feature">
    <img src="{{ '/assets/img/home-fog-in-valley.jpg' | relative_url }}" alt="Fog settling in a valley at sunrise">
    <div class="feature-text">
      <h2>Years of Experience</h2>
      <p>We have been providing high quality aerial media solutions for everything from real estate to sports events since 2014. We specialize in creating videos and capturing images from the unique perspective that you are only able to capture from the sky.</p>
      <p><a class="btn btn-ghost" href="{{ '/contact/#who-we-are' | relative_url }}">About Us</a></p>
    </div>
  </div>

  <div class="feature">
    <img src="{{ '/assets/img/home-salem-water-log.jpg' | relative_url }}" alt="Aerial view over the water at Salem">
    <div class="feature-text">
      <h2>Dedication to Safety</h2>
      <p>Safety is our number one priority. We are committed to getting the shot while maintaining the safety of spectators, participants and our shoot location.</p>
      <div class="badges">
        <span class="badge">FAA UAS Part 107 Licensed</span>
        <span class="badge">Fully Insured</span>
      </div>
    </div>
  </div>
</section>

<section class="block center">
  <h2>Clients and Content Partners</h2>
  <div class="logo-grid">
    {% for c in site.data.clients %}
    <div class="logo-cell"><img src="{{ '/assets/img/clients/' | append: c.file | relative_url }}" alt="{{ c.alt }}" loading="lazy"></div>
    {% endfor %}
  </div>
  <p style="margin-top: 1.5rem;"><a class="btn" href="{{ '/contact/' | relative_url }}">Work With Us</a></p>
</section>
