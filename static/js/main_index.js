const triggers = document.querySelectorAll('a');
const highlight = document.createElement('span');
highlight.classList.add('highlight');
document.body.append(highlight);

function highlightLink() {
  const linkCoords = this.getBoundingClientRect();
  const coords = {
    width: `${linkCoords.width}px`,
    height: `${linkCoords.height}px`,
    top: `${linkCoords.top + window.scrollY}px`,
    left: `${linkCoords.left + window.scrollX}px`
  }
  highlight.style.top = 0;
  highlight.style.left = 0;
  highlight.style.width = coords.width;
  highlight.style.height = coords.height;
  highlight.style.transform = `translate(${coords.left}, ${coords.top})`;
}

function unHighlightLink() {
  highlight.style.top = '8em';
  highlight.style.left = '50%';
  highlight.style.width = '100px';
  highlight.style.height = '0';
  highlight.style.transform = 'translate(-50%, 0)';
}

triggers.forEach(a => {
  a.addEventListener('mouseenter', highlightLink);
  a.addEventListener('mouseleave', unHighlightLink);
})