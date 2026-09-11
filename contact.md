---
layout: default
title: Contact
redirect_from:
  - /about
  - /about/
---

# Contact

<h2 id="who-we-are">Who we are</h2>

We are a team of people from a wide variety of backgrounds that love capturing images and videos from the sky. Our expert pilots, cinematographers and video editors have degrees in Filmmaking, Computer Engineering and Mechanical Engineering. We are passionate about our work and take pride in filling the needs of our clients.

![Team graphic]({{ '/assets/img/about-team-graphic.png' | relative_url }})

## Get in touch

<div class="contact-wrap">
  <div>
    <img src="{{ '/assets/img/contact-wakefield-sunrise.jpg' | relative_url }}" alt="Sunrise over Wakefield Center from above" style="border-radius: 8px;">
    <p style="margin-top: 1rem;">Tell us about your project — real estate, events, commercial work, or something entirely new. We fly where the story is.</p>
    <div class="badges">
      <span class="badge">FAA UAS Part 107 Licensed</span>
      <span class="badge">Fully Insured</span>
    </div>
  </div>
  <div>
    <!--
      CONTACT FORM SETUP (2 minutes, free):
      1. Go to https://formspree.io and create a free account.
      2. Create a form — Formspree gives you an endpoint like https://formspree.io/f/abcd1234
      3. Replace YOUR_FORM_ID below with your endpoint. Done — submissions land in your inbox.
      GitHub Pages can't process forms itself, which is why we use Formspree.
    -->
    <form class="contact" action="https://formspree.io/f/xbgjwzqp" method="POST">
      <label for="name">Name</label>
      <input id="name" type="text" name="name" required autocomplete="name">

      <label for="email">Email</label>
      <input id="email" type="email" name="email" required autocomplete="email">

      <label for="message">Tell us about your project</label>
      <textarea id="message" name="message" required></textarea>

      <button class="btn" type="submit">Send Message</button>
    </form>
  </div>
</div>
