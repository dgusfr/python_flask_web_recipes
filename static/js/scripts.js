const getElement = (selector) => {
  const element = document.querySelector(selector);

  if (element) return element;
  throw Error(
    `Please double check your class names, there is no ${selector} class`
  );
};

const links = getElement(".nav-links");
const navBtnDOM = getElement(".nav-btn");

// Adiciona um listener de eventos ao botão de navegação
navBtnDOM.addEventListener("click", () => {
  // Alterna a classe 'show-links' no elemento 'links'
  links.classList.toggle("show-links");
});

const date = getElement("#date");
const currentYear = new Date().getFullYear();
date.textContent = currentYear;
