const $keyword = document.querySelector(".keyword");
const $keywords = document.querySelector(".keywords");
const $searchResults = document.querySelector(".search-results");
let idx = -1;
$keyword.addEventListener("keyup", (e) => {
  const { value } = e.target;
  const { key } = e;
  console.log(e.target)
  console.log(key)
  if (key === "Enter") {
    if (idx == -1) {
      fetch(
      `https://jf3iw5iguk.execute-api.ap-northeast-2.amazonaws.com/dev/api/cats/search?q=${value}`
      )
        .then((res) => res.json())
        .then((results) => {
          if (results.data) {
            $searchResults.innerHTML = results.data
              .map((cat) => `<article><img src="${cat.url}" /></article>`)
              .join("");
          }
        });
    }
    else {
      e.target.value = $keywords.childNodes[idx].textContent
      fetch(
        `https://jf3iw5iguk.execute-api.ap-northeast-2.amazonaws.com/dev/api/cats/search?q=${$keywords.childNodes[idx].textContent}`
        )
          .then((res) => res.json())
          .then((results) => {
            if (results.data) {
              $searchResults.innerHTML = results.data
                .map((cat) => `<article><img src="${cat.url}" /></article>`)
                .join("");
            }
          });
      
    }
    $keywords.style.display = 'none'
  }

  if (key == "ArrowUp") {
    if($keywords.childNodes) {
      if (idx > 0) idx --;
      if (idx < $keywords.childNodes.length) {
        $keywords.childNodes[idx+1].classList.remove('active') 
      }
      $keywords.childNodes[idx].classList.add('active')
      
    }
    else {
      idx = -1
    }
  }
  else if(key == 'ArrowDown') {
    if($keywords.childNodes) {
      if (idx < $keywords.childNodes.length-1) idx ++; 
      if (idx > 0) {
        $keywords.childNodes[idx-1].classList.remove('active') 
      } 
      $keywords.childNodes[idx].classList.add('active')
    }
    else {
      idx = -1
    } 
  }

  else if (key == "Escape") {
    idx = -1
    $keywords.style.display = 'none'
  }
});

$keyword.addEventListener("focusout", e => {
  $keywords.style.display = 'none'
})

$keyword.addEventListener("input", (res) => {
  const value = $keyword.value;
  idx = -1
  console.log('value', value)
  if (value) {
    fetch(
      `https://jf3iw5iguk.execute-api.ap-northeast-2.amazonaws.com/dev/api/cats/keywords?q=${value}`
    )
    .then((res) => res.json())
    .then((results) => {
      console.log(results)
      while ($keywords.hasChildNodes()) {
        $keywords.removeChild($keywords.firstChild)
      }
      if (results.length > 0) {
        $keywords.style.display = 'block';
        for (result of results) {
          const litag = document.createElement('li')
          litag.innerHTML = result
          $keywords.appendChild(litag)
        }
      }
      else {
        $keywords.style.display = 'none';
      }
      
    })
  }

  else {
    $keywords.style.display = 'none';
  }
})
