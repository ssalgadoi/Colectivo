// document.addEventListener("DOMContentLoaded", () => {
//   //Funcion para obtener el ano actual
//   const getCurrentYear = () => {
//     return new Date().getFullYear();
//   }

//   document.querySelector("#current-year").textContent = getCurrentYear();
// });

document.addEventListener("DOMContentLoaded", () => {
  // Funcion para obtener el ano actual
  const getCurrentYear = () => {
    return new Date().getFullYear();
  }

  // Obtener el elemento por su ID y establecer el tamaño de fuente
  const tituloElement = document.querySelector(".titulo");
  tituloElement.style.fontSize = "24px"; // Cambia el tamaño de fuente a 24px

  // Obtener el elemento por su ID y establecer el año actual
  document.querySelector("#current-year").textContent = getCurrentYear();
});

