// Minimal lightbox: click any gallery/pano image to view it full-screen, click again to close.
(function () {
  var box = document.getElementById('lightbox');
  var img = document.getElementById('lightbox-img');
  if (!box || !img) return;
  document.addEventListener('click', function (e) {
    var t = e.target;
    if (t.tagName === 'IMG' && (t.closest('.gallery') || t.closest('.pano'))) {
      img.src = t.src;
      img.alt = t.alt || '';
      box.classList.add('open');
      box.setAttribute('aria-hidden', 'false');
    } else if (box.classList.contains('open')) {
      box.classList.remove('open');
      box.setAttribute('aria-hidden', 'true');
      img.src = '';
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && box.classList.contains('open')) {
      box.classList.remove('open');
      box.setAttribute('aria-hidden', 'true');
      img.src = '';
    }
  });
})();
