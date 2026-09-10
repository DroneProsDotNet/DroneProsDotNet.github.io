# DronePros.net — GitHub Pages site

A Jekyll site (migrated from Squarespace) ready to deploy on GitHub Pages with the custom domain **www.rediscoveryourworld.com**.

## What's inside

| Path | What it is |
|---|---|
| `index.md` | Homepage (`/`) — hero, aerial reel, feature sections |
| `about.md` | About page (`/about/`) |
| `images.md` | Photo gallery (`/images/`) |
| `aerial-panoramas.md` | Panorama gallery (`/aerial-panoramas/`) |
| `videos.md` | 19 YouTube embeds (`/videos/`) |
| `puckerman.md` | "A Dog's Snow Day" feature (`/puckerman/`) |
| `contact.md` | Contact form (`/contact/`) — needs Formspree, see below |
| `assembly-row.md` | Assembly Row project (`/assembly-row/`) |
| `404.html` | Custom not-found page |
| `_data/gallery.yml`, `_data/panoramas.yml`, `_data/videos.yml` | Edit text, captions & videos here — no HTML needed |
| `assets/img/` | All 40 site images, self-hosted (no more Squarespace CDN) |
| `CNAME` | Custom domain file (`www.rediscoveryourworld.com`) |
| `_config.yml` | Site title, tagline, plugins |

Old `/home` URL redirects to `/` automatically.

## Deploy — step by step

**1. Create the repository**
- On GitHub, create a **public** repository named exactly `<DroneProsDotNet>.github.io` (replace with your GitHub username).
- Push everything in this folder to the `main` branch:
  ```
  cd rediscoveryourworld-site
  git init && git add -A && git commit -m "Migrate from Squarespace"
  git branch -M main
  git remote add origin https://github.com/DroneProsDotNet/DroneProsDotNet.github.io.git
  git push -u origin main
  ```

**2. Turn on GitHub Pages**
- Repo → **Settings → Pages** → Source: **Deploy from a branch** → Branch: `main`, folder `/ (root)` → Save.
- Wait a minute, then visit `https://DroneProsDotNet.github.io` and click through every page.

**3. Add your custom domain (do this BEFORE touching DNS)**
- In **Settings → Pages**, under *Custom domain*, enter `www.rediscoveryourworld.com` → Save.
- This creates the `CNAME` record GitHub needs and blocks anyone else from claiming your domain.

**4. Update DNS at your domain provider**
- Apex `rediscoveryourworld.com` → four `A` records:
  `185.199.108.153` · `185.199.109.153` · `185.199.110.153` · `185.199.111.153`
- `www` → `CNAME` record pointing to `DroneProsDotNet.github.io`
- Leave any `MX` records alone (email keeps working).
- DNS can take up to 24 hours. `rediscoveryourworld.com` will redirect to `www.rediscoveryourworld.com` automatically.

**5. Enforce HTTPS**
- Back in **Settings → Pages**, tick **Enforce HTTPS** once it becomes available (up to 24h after DNS).

**6. Wire up the contact form (2 min, free)**
- GitHub Pages can't process forms, so: sign up at [formspree.io](https://formspree.io), create a form, and paste your endpoint into `contact.md` where it says `YOUR_FORM_ID`.

**7. Cancel Squarespace — last**
- Only after the new site loads correctly on your domain with HTTPS. If your domain is registered through Squarespace, keep the registration (just the DNS changed) or transfer it out first — never let the domain itself lapse.

## Everyday edits

- **Change the site name/tagline:** `_config.yml` (`title`, `tagline`).
- **Edit a gallery or the videos page:** just edit the `_data/*.yml` files — add a line, push, done.
- **Add a photo:** drop it in `assets/img/` and add one line to the matching `_data` file.
- Every push to `main` redeploys automatically.

## Notes

- Branding is "DronePros.net" (matching the original Squarespace site). The custom domain stays `www.rediscoveryourworld.com`. To change the brand later, edit `title:` in `_config.yml`.
- Image files are web-sized (~1600px). Originals remain on the Squarespace CDN until you cancel — download full-res copies now if you want them archived.
