document.getElementById('toggle_header').onclick = function () {
  const header = document.querySelector('header')
  if (header.classList.contains('red')) {
    header.className = 'green'
  } else {
    header.className = 'red'
  }
}
