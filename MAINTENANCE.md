# Updating This Website — Yearly Maintenance Guide

You don't need any special software. Everything is edited right on github.com,
and every change you save rebuilds the site automatically in about a minute.
Nothing else to do — no "publish" button, no re-uploading the whole site.

**The golden rule:** one page = one file. Page text lives in `.md` files at the
top level; photo/video lists live in `_data/*.yml` files; the actual image
files live in `assets/img/`.

## Adding new photos (the most common job)

**1. Prep the photo** (2 minutes, worth doing)
- Phone photos are enormous — shrink them first so the site stays fast.
  Aim for ~1600–2000 pixels wide, saved as JPG. On iPhone: share the photo
  to Files, or use any free "image resize" website.
- Name the file simply: lowercase, dashes instead of spaces, ending in `.jpg`.
  Good: `gallery-sunset-marsh.jpg`. Bad: `IMG_4829 (1).HEIC`.

**2. Upload it**
- In your repo on github.com, open the `assets/img/` folder.
- Click **Add file → Upload files**, drag your photo in, click **Commit changes**.

**3. List it**
- Open `_data/gallery.yml` (for the Images page) or `_data/panoramas.yml`
  (for wide panorama shots on the Panoramas page) and click the pencil icon.
- Add two lines for your photo. Put new favorites at the **top** so they
  appear first:
  ```yaml
  - file: gallery-sunset-marsh.jpg
    caption: Sunset over the marsh
  ```
- Click **Commit changes**. Done — the photo is on the site within a minute.

To *remove* a photo, delete its two lines from the `.yml` file (you can also
delete the image file from `assets/img/`, but leaving it there is harmless).

## Changing wording or descriptions

- **Homepage sections** → `index.md`
- **About text** (now part of the contact page) → `contact.md`
- **Photo captions** → `_data/gallery.yml` / `_data/panoramas.yml`
- **Video titles/descriptions** → `_data/videos.yml`
- **Client logos** → `_data/clients.yml` (logo files go in `assets/img/clients/`)

Just edit the text and commit. Leave anything that looks like
`{{ ... }}` or `{% ... %}` alone — that's the machinery, not the content.

## Adding a video

1. Upload the video to YouTube (unlisted is fine).
2. Copy the 11-character video ID from its URL —
   `youtube.com/watch?v=`**`0anl5ozhZOE`** ← this part.
3. In `_data/videos.yml`, under the category you want, add:
   ```yaml
     - youtube: 0anl5ozhZOE
       title: My New Video
       desc: A sentence about it.
   ```
   (Watch the indentation — two spaces before `- youtube`, four before `title:`.)
4. Commit. It appears on the Videos page within a minute.

## Changing where contact-form emails go

The form is handled by Formspree (free). To point it at a different inbox,
log into formspree.io and change the form's target email there — no website
change needed. If you ever create a brand-new Formspree form, paste its new
ID into `contact.md` where it says `YOUR_FORM_ID`.

## Files to leave alone

- `_config.yml` — site settings (only touch `title:` if the brand name changes)
- `_layouts/`, `assets/css/`, `assets/js/` — design and machinery
- `CNAME` — this is what keeps your domain connected. Don't delete it.

## Checking your work & undoing mistakes

- After any commit, wait ~1 minute, then hard-refresh the page
  (Ctrl/Cmd+Shift+R) or check in an incognito window.
- Made a mistake? Nothing is ever lost: every change is saved in the repo's
  history. On any file's page, click **History**, open the previous version,
  and copy it back — or ask for help and it can be rolled back in seconds.
- The repo itself is your backup. As long as it exists on GitHub, the site
  can always be rebuilt.
