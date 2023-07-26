function updateButtonURL() {
      const selector = document.getElementById("alfabetico");
      const selectedValue = selector.options[selector.selectedIndex].value;

      // Actualiza la URL del botón dependiendo de la selección en el selector
      const boton = document.getElementById("filtro-boton");
      const url = "{% url 'apps.articulo:articulos' %}?orden=" + selectedValue;
      boton.href = url;
      const selectorc = document.getElementById("categoria");
      const selectedValuec = selectorc.options[selectorc.selectedIndex].value;
      // Actualiza la URL del botón dependiendo de la selección en el selector
      const botonc = document.getElementById("filtro-botonc");
      var url2 = "{% url 'apps.articulo:articulos' %}";
      if (selectedValuec == '1') {
        url2 = "{% url 'apps.articulo:articulos_por_categoria' categorias='1' %}";
      } else if (selectedValuec == '2') {
        url2 = "{% url 'apps.articulo:articulos_por_categoria' categorias='2' %}";
      } else if (selectedValuec == '3') {
        url2 = "{% url 'apps.articulo:articulos_por_categoria' categorias='3' %}";
      } else if (selectedValuec == '4') {
        url2 = "{% url 'apps.articulo:articulos_por_categoria' categorias='4' %}";
      } else if (selectedValuec == '5') {
        url2 = "{% url 'apps.articulo:articulos_por_categoria' categorias='5' %}";
      } else if (selectedValuec == 'None') {
        url2 = "{% url 'apps.articulo:articulos' %}";
      }
      botonc.href = url2;
    }