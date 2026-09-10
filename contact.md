---
layout: default
title: Contact
---

# Contact

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
    <form class="contact" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
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
