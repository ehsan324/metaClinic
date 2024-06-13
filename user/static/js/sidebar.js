const navBar = document.querySelector("nav")
const toggleNavBtn = document.getElementById("toggle-nav-btn")

toggleNav()

toggleNavBtn.addEventListener("click", (event) => {
  toggleNav()
})

function toggleNav() {
  if (navBar.classList.contains("nav-min")){
    openNav()
  } else {
    closeNav()
  }
}

function openNav() {
  navBar.classList.remove("nav-min") 
  navBar.classList.add("nav-max") 
  document.getElementById("table").style.display = "";
}

function closeNav() {
  document.getElementById("table").style.display = "none";
  navBar.classList.remove("nav-max") 
  navBar.classList.add("nav-min")
  
}

const phone = window.matchMedia("(width <= 480px)")

function media(e) {
  if (e.matches) {
    closeNav()
  } else {
    openNav()
  }
}

phone.addListener(media)




