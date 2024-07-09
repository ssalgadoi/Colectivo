  // Mostrar el botón cuando el usuario desplaza hacia abajo 20px desde la parte superior del documento
  window.onscroll = function() { scrollFunction() };

  function scrollFunction() {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
          document.getElementById("scrollToTopBtn").style.display = "block";
      } else {
          document.getElementById("scrollToTopBtn").style.display = "none";
      }
  }

  // Cuando el usuario hace clic en el botón, se desplaza hacia arriba
  function scrollToTop() {
      document.body.scrollTop = 0; // Para Safari
      document.documentElement.scrollTop = 0; // Para Chrome, Firefox, IE y Opera
  }
